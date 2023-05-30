// -*- C++ -*-
//
// Package:    CalibTracker/SiStripLorentzAnglePCLHarvester
// Class:      SiStripLorentzAnglePCLHarvester
//
/**\class SiStripLorentzAnglePCLHarvester SiStripLorentzAnglePCLHarvester.cc CalibTracker/SiStripLorentzAngle/plugins/SiStripLorentzAnglePCLHarvester.cc
 Description: reads the intermediate ALCAPROMPT DQMIO-like dataset and performs the fitting of the SiStrip Lorentz Angle in the Prompt Calibration Loop
*/
//
// Original Author:  mmusich
//         Created:  Sat, 29 May 2021 14:46:19 GMT
//
//

// system includes
#include <fmt/format.h>
#include <fmt/printf.h>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

// user includes
#include "CalibTracker/SiStripLorentzAngle/interface/SiStripLorentzAngleCalibrationStruct.h"
#include "CondCore/DBOutputService/interface/PoolDBOutputService.h"
#include "CondFormats/DataRecord/interface/SiStripLorentzAngleRcd.h"
#include "CondFormats/SiStripObjects/interface/SiStripLorentzAngle.h"
#include "DQMServices/Core/interface/DQMEDHarvester.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"
#include "Geometry/Records/interface/IdealGeometryRecord.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"

// for ROOT fits
#include "TFitResult.h"
#include "TF1.h"

namespace siStripLACalibration {
  double fitFunction(double* x, double* par) {
    double a = par[0];
    double thetaL = par[1];
    double b = par[2];

    double tanThetaL = std::tan(thetaL);
    double value = a * std::abs(std::tan(x[0]) - tanThetaL) + b;

    //TF1::RejectPoint();  // Reject points outside the fit range
    return value;
  }
}  // namespace siStripLACalibration

//------------------------------------------------------------------------------
class SiStripLorentzAnglePCLHarvester : public DQMEDHarvester {
public:
  SiStripLorentzAnglePCLHarvester(const edm::ParameterSet&);
  ~SiStripLorentzAnglePCLHarvester() override = default;
  void beginRun(const edm::Run&, const edm::EventSetup&) override;

  static void fillDescriptions(edm::ConfigurationDescriptions&);

private:
  void dqmEndJob(DQMStore::IBooker&, DQMStore::IGetter&) override;
  void endRun(const edm::Run&, const edm::EventSetup&) override;
  std::string getFolder(const std::string& histoName);

  // es tokens
  const edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> geomEsToken_;
  const edm::ESGetToken<TrackerTopology, TrackerTopologyRcd> topoEsTokenBR_, topoEsTokenER_;
  const edm::ESGetToken<SiStripLorentzAngle, SiStripLorentzAngleRcd> siStripLAEsToken_;
  const edm::ESGetToken<MagneticField, IdealMagneticFieldRecord> magneticFieldToken_;

  // member data
  SiStripLorentzAngleCalibrationHistograms iHists_;

  const std::string dqmDir_;
  const std::vector<double> fitRange_;
  const std::string recordName_;
  float theMagField_{0.f};

  static constexpr float teslaToInverseGeV_ = 2.99792458e-3f;
  std::pair<double, double> theFitRange_{5., 280.};

  SiStripLorentzAngleCalibrationHistograms hists_;
  const SiStripLorentzAngle* currentLorentzAngle_;
  std::unique_ptr<TrackerTopology> theTrackerTopology_;
};

//------------------------------------------------------------------------------
SiStripLorentzAnglePCLHarvester::SiStripLorentzAnglePCLHarvester(const edm::ParameterSet& iConfig)
    : geomEsToken_(esConsumes<edm::Transition::BeginRun>()),
      topoEsTokenBR_(esConsumes<edm::Transition::BeginRun>()),
      topoEsTokenER_(esConsumes<edm::Transition::EndRun>()),
      siStripLAEsToken_(esConsumes<edm::Transition::BeginRun>(edm::ESInputTag("", "deconvolution"))),
      magneticFieldToken_(esConsumes<edm::Transition::BeginRun>()),
      dqmDir_(iConfig.getParameter<std::string>("dqmDir")),
      fitRange_(iConfig.getParameter<std::vector<double>>("fitRange")),
      recordName_(iConfig.getParameter<std::string>("record")) {
  // initialize the fit range
  if (fitRange_.size() == 2) {
    theFitRange_.first = fitRange_[0];
    theFitRange_.second = fitRange_[1];
  } else {
    throw cms::Exception("SiStripLorentzAnglePCLHarvester") << "Too many fit range parameters specified";
  }

  // first ensure DB output service is available
  edm::Service<cond::service::PoolDBOutputService> poolDbService;
  if (!poolDbService.isAvailable())
    throw cms::Exception("SiStripLorentzAnglePCLHarvester") << "PoolDBService required";
}

//------------------------------------------------------------------------------
void SiStripLorentzAnglePCLHarvester::beginRun(const edm::Run& iRun, const edm::EventSetup& iSetup) {
  // geometry
  const TrackerGeometry* geom = &iSetup.getData(geomEsToken_);
  const TrackerTopology* tTopo = &iSetup.getData(topoEsTokenBR_);

  const MagneticField* magField = &iSetup.getData(magneticFieldToken_);
  currentLorentzAngle_ = &iSetup.getData(siStripLAEsToken_);

  // B-field value
  // inverseBzAtOriginInGeV() returns the inverse of field z component for this map in GeV
  // for the conversion please consult https://github.com/cms-sw/cmssw/blob/master/MagneticField/Engine/src/MagneticField.cc#L17
  // theInverseBzAtOriginInGeV = 1.f / (at0z * 2.99792458e-3f);
  // ==> at0z = 1.f / (theInverseBzAtOriginInGeV * 2.99792458e-3f)

  theMagField_ = 1.f / (magField->inverseBzAtOriginInGeV() * teslaToInverseGeV_);
}

//------------------------------------------------------------------------------
void SiStripLorentzAnglePCLHarvester::endRun(edm::Run const& run, edm::EventSetup const& isetup) {
  if (!theTrackerTopology_) {
    theTrackerTopology_ = std::make_unique<TrackerTopology>(isetup.getData(topoEsTokenER_));
  }
}

//------------------------------------------------------------------------------
void SiStripLorentzAnglePCLHarvester::dqmEndJob(DQMStore::IBooker& iBooker, DQMStore::IGetter& iGetter) {
  // go in the right directory
  iGetter.cd();
  iGetter.setCurrentFolder(dqmDir_);

  // fill in the module types
  iHists_.nlayers_["TIB"] = 4;
  iHists_.nlayers_["TOB"] = 6;
  iHists_.modtypes_.push_back("s");
  iHists_.modtypes_.push_back("a");

  std::vector<std::string> MEtoHarvest = {"tanthcosphtrk_nstrip",
                                          "thetatrk_nstrip",
                                          "tanthcosphtrk_var2",
                                          "tanthcosphtrk_var3",
                                          "thcosphtrk_var2",
                                          "thcosphtrk_var3"};

  // prepare the histograms to be harvested
  for (auto& layers : iHists_.nlayers_) {
    std::string subdet = layers.first;
    for (int l = 1; l <= layers.second; ++l) {
      for (auto& t : iHists_.modtypes_) {
        // do not fill stereo where there aren't
        if (l > 2 && t == "s")
          continue;
        std::string locationtype = Form("%s_L%d%s", subdet.c_str(), l, t.c_str());

        /*
	iHists_.h2_[Form("%s_tanthcosphtrk_nstrip", locationtype.c_str())] = iGetter.get(Form("%s_tanthcosphtrk_nstrip", locationtype.c_str()));
        iHists_.h2_[Form("%s_thetatrk_nstrip", locationtype.c_str())] = iGetter.get(Form("%s_thetatrk_nstrip", locationtype.c_str()));
        iHists_.h2_[Form("%s_tanthcosphtrk_var2", locationtype.c_str())] = iGetter.get(Form("%s_tanthcosphtrk_var2", locationtype.c_str()));
        iHists_.h2_[Form("%s_tanthcosphtrk_var3", locationtype.c_str())] = iGetter.get(Form("%s_tanthcosphtrk_var3", locationtype.c_str()));
        iHists_.h2_[Form("%s_thcosphtrk_var2", locationtype.c_str())] = iGetter.get(Form("%s_thcosphtrk_var2", locationtype.c_str()));
        iHists_.h2_[Form("%s_thcosphtrk_var3", locationtype.c_str())] = iGetter.get(Form("%s_thcosphtrk_var3", locationtype.c_str()));
	*/

        for (const auto& toHarvest : MEtoHarvest) {
          const char* address =
              Form("%s/%s/L%d/%s_%s", dqmDir_.c_str(), subdet.c_str(), l, locationtype.c_str(), toHarvest.c_str());
          //std::cout << "harvesting at: " << address << std::endl;

          iHists_.h2_[Form("%s_%s", locationtype.c_str(), toHarvest.c_str())] = iGetter.get(address);
          if (iHists_.h2_[Form("%s_%s", locationtype.c_str(), toHarvest.c_str())] == nullptr) {
            std::cout << "could not retrieve: " << Form("%s_%s", locationtype.c_str(), toHarvest.c_str()) << std::endl;
          }
        }
      }
    }
  }

  // prepare the profiles
  for (const auto& ME : iHists_.h2_) {
    //std::cout << "profiling " << ME.first << std::endl;  //" which is of kind" << ME.second->kind() << std::endl;
    TProfile* hp = (TProfile*)ME.second->getTH2F()->ProfileX();
    this->getFolder(ME.first);
    iBooker.setCurrentFolder(dqmDir_ + "/" + getFolder(ME.first));
    iHists_.p_[hp->GetName()] = iBooker.bookProfile(hp->GetName(), hp);
    delete hp;
  }

  // do the fits
  for (const auto& prof : iHists_.p_) {
    //fit only this type of profile
    if ((prof.first).find("thetatrk_nstrip") != std::string::npos) {
      // Create the TF1 function
      TF1* fitFunc = new TF1(
          "fitFunc", siStripLACalibration ::fitFunction, prof.second->getAxisMin(1), prof.second->getAxisMax(1), 3);
      //fitFunc->SetParameters(5.-2, -7.e-2, 8.e-2);

      // Fit the function to the data
      prof.second->getTProfile()->Fit(fitFunc, "F");  // "F" option performs a least-squares fit

      // Get the fit results
      Double_t a_fit = fitFunc->GetParameter(0);
      Double_t thetaL_fit = fitFunc->GetParameter(1);
      Double_t b_fit = fitFunc->GetParameter(2);
      std::cout << prof.first << " fit result: a=" << a_fit << " theta_L=" << thetaL_fit << " b=" << b_fit << std::endl;
    }
  }
}

//------------------------------------------------------------------------------
std::string SiStripLorentzAnglePCLHarvester::getFolder(const std::string& histoName) {
  std::vector<std::string> tokens;

  // Create a string stream from the input string
  std::istringstream iss(histoName);

  std::string token;
  while (std::getline(iss, token, '_')) {
    // Add each token to the vector
    tokens.push_back(token);
  }

  std::string output = tokens[0] + "/" + tokens[1];
  output.pop_back();

  return output;
}

//------------------------------------------------------------------------------
void SiStripLorentzAnglePCLHarvester::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.setComment("Harvester module of the SiStrip Lorentz Angle PCL monitoring workflow");
  desc.add<std::string>("dqmDir", "AlCaReco/SiStripLorentzAngle")->setComment("the directory of PCL Worker output");
  desc.add<std::vector<double>>("fitRange", {5., 280.})->setComment("range of depths to perform the LA fit");
  desc.add<std::string>("record", "SiStripLorentzAngleRcd")->setComment("target DB record");
  descriptions.addWithDefaultLabel(desc);
}

DEFINE_FWK_MODULE(SiStripLorentzAnglePCLHarvester);
