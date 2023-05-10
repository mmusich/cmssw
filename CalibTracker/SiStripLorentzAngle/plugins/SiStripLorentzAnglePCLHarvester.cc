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

  // es tokens
  const edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> geomEsToken_;
  const edm::ESGetToken<TrackerTopology, TrackerTopologyRcd> topoEsTokenBR_, topoEsTokenER_;
  const edm::ESGetToken<SiStripLorentzAngle, SiStripLorentzAngleRcd> siStripLAEsToken_;
  const edm::ESGetToken<MagneticField, IdealMagneticFieldRecord> magneticFieldToken_;

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
