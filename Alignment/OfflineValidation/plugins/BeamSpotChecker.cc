// -*- C++ -*-
//
// Package:    Alignment/BeamSpotChecker
// Class:      BeamSpotChecker
//
/**\class BeamSpotChecker BeamSpotChecker.cc Alignment/BeamSpotChecker/plugins/BeamSpotChecker.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Marco Musich
//         Created:  Thu, 23 Apr 2020 09:00:45 GMT
//
//

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<>
// This will improve performance in multithreaded jobs.

// ancillary struct to check compatibility
namespace bscheck {

  struct Significance {
    Significance(const double& A, const double& B, const double& ErrA, const double& ErrB)
        : m_A(A), m_B(B), m_ErrA(ErrA), m_ErrB(ErrB) {
      if (m_ErrA == 0 && m_ErrB == 0) {
        edm::LogError("LogicalError") << "Can't calculate significance when both errors are zero!" << std::endl;
      }
    }

    float getSig(bool verbose) {
      if (verbose) {
        edm::LogInfo("BeamSpotChecker") << "A= " << m_A << "+/-" << m_ErrA << "    "
                                        << "B= " << m_B << "+/-" << m_ErrB << " | delta=" << std::abs(m_A - m_B)
                                        << "+/-" << std::sqrt((m_ErrA * m_ErrA) + (m_ErrB * m_ErrB)) << std::endl;
      }
      return std::abs(m_A - m_B) / std::sqrt((m_ErrA * m_ErrA) + (m_ErrB * m_ErrB));
    }

  private:
    double m_A;
    double m_B;
    double m_ErrA;
    double m_ErrB;
  };
}  // namespace bscheck

class BeamSpotChecker : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit BeamSpotChecker(const edm::ParameterSet&);
  ~BeamSpotChecker() override;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void beginJob() override;
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override;
  std::array<float, 6> compareBS(const reco::BeamSpot& BSA, const reco::BeamSpot& BSB);

  // ----------member data ---------------------------

  static constexpr int cmToum = 10000;
  double warningThreshold_;
  double throwingThreshold_;
  bool verbose_;
  edm::EDGetTokenT<reco::BeamSpot> bsFromEventToken_;  // beamSpot from the event
  edm::EDGetTokenT<reco::BeamSpot> bsFromDBToken_;     // beamSpot from the event
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
BeamSpotChecker::BeamSpotChecker(const edm::ParameterSet& iConfig)
    : warningThreshold_(iConfig.getParameter<double>("warningThr")),
      throwingThreshold_(iConfig.getParameter<double>("errorThr")),
      verbose_(iConfig.getUntrackedParameter<bool>("verbose", false)),
      bsFromEventToken_(consumes<reco::BeamSpot>(iConfig.getParameter<edm::InputTag>("bsFromEvent"))),
      bsFromDBToken_(consumes<reco::BeamSpot>(iConfig.getParameter<edm::InputTag>("bsFromDB"))) {
  //now do what ever initialization is needed
  if (warningThreshold_ > throwingThreshold_) {
    throw cms::Exception("ConfigurationError")
        << __PRETTY_FUNCTION__ << "\n Warning threshold (" << warningThreshold_
        << ") cannot be smaller than the throwing threshold (" << throwingThreshold_ << ")" << std::endl;
  }
}

BeamSpotChecker::~BeamSpotChecker() {
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
}

//
// member functions
//

// ------------ method called for each event  ------------
void BeamSpotChecker::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;
  reco::BeamSpot spotEvent, spotDB;

  edm::Handle<reco::BeamSpot> beamSpotFromEventHandle;
  iEvent.getByToken(bsFromEventToken_, beamSpotFromEventHandle);
  spotEvent = *beamSpotFromEventHandle;

  double evt_BSx0_ = spotEvent.x0();
  double evt_BSy0_ = spotEvent.y0();
  double evt_BSz0_ = spotEvent.z0();
  double evt_Beamsigmaz_ = spotEvent.sigmaZ();
  double evt_BeamWidthX_ = spotEvent.BeamWidthX();
  double evt_BeamWidthY_ = spotEvent.BeamWidthY();

  edm::Handle<reco::BeamSpot> beamSpotFromDBHandle;
  iEvent.getByToken(bsFromDBToken_, beamSpotFromDBHandle);
  spotDB = *beamSpotFromDBHandle;

  double db_BSx0_ = spotDB.x0();
  double db_BSy0_ = spotDB.y0();
  double db_BSz0_ = spotDB.z0();
  double db_Beamsigmaz_ = spotDB.sigmaZ();
  double db_BeamWidthX_ = spotDB.BeamWidthX();
  double db_BeamWidthY_ = spotDB.BeamWidthY();

  double deltaX0 = evt_BSx0_ - db_BSx0_;
  double deltaY0 = evt_BSy0_ - db_BSy0_;
  double deltaZ0 = evt_BSz0_ - db_BSz0_;
  double deltaSigmaX = evt_BeamWidthX_ - db_BeamWidthX_;
  double deltaSigmaY = evt_BeamWidthY_ - db_BeamWidthY_;
  double deltaSigmaZ = evt_Beamsigmaz_ - db_Beamsigmaz_;

  if (verbose_) {
    edm::LogVerbatim("BeamSpotChecker") << "BS from Event: \n" << spotEvent << std::endl;
    edm::LogVerbatim("BeamSpotChecker") << "BS from DB: \n" << spotDB << std::endl;
  }

  auto significances = compareBS(spotDB, spotEvent);
  std::vector<std::string> labels = {"x0", "y0", "z0", "sigmaX", "sigmaY", "sigmaZ"};

  std::string msg = " |delta X0|=" + std::to_string(std::abs(deltaX0) * cmToum) +
                    " um |delta Y0|=" + std::to_string(std::abs(deltaY0) * cmToum) +
                    " um |delta Z0|=" + std::to_string(std::abs(deltaZ0) * cmToum) +
                    " um |delta sigmaX|=" + std::to_string(std::abs(deltaSigmaX) * cmToum) +
                    " um |delta sigmaY|=" + std::to_string(std::abs(deltaSigmaY) * cmToum) +
                    " um |delta sigmaZ|=" + std::to_string(std::abs(deltaSigmaZ)) + "cm";

  //unsigned int i=0;
  //for(const auto& sig: significances){
  for (unsigned int i = 0; i < 3; i++) {
    auto sig = significances.at(i);
    if (sig > throwingThreshold_) {
      edm::LogError("BeamSpotChecker") << msg.c_str() << std::endl;
      throw cms::Exception("BeamSpotChecker")
          << "[" << __PRETTY_FUNCTION__ << "] \n DB-Event BeamSpot " << labels.at(i) << " distance sigificance " << sig
          << ", exceeds the threshold of " << throwingThreshold_ << "!" << std::endl;
    } else if (sig > warningThreshold_) {
      edm::LogWarning("BeamSpotChecker") << msg.c_str() << std::endl;
      edm::LogWarning("BeamSpotChecker") << "[" << __PRETTY_FUNCTION__ << "]  \n  DB-Event BeamSpot " << labels.at(i)
                                         << " distance significance " << sig << ", exceeds the threshold of "
                                         << warningThreshold_ << "!" << std::endl;
    }
    //i++;
  }
}

std::array<float, 6> BeamSpotChecker::compareBS(const reco::BeamSpot& BSA, const reco::BeamSpot& BSB) {
  auto xS = bscheck::Significance(BSA.x0(), BSB.x0(), BSA.x0Error(), BSB.x0Error());
  auto yS = bscheck::Significance(BSA.y0(), BSB.y0(), BSA.y0Error(), BSB.y0Error());
  auto zS = bscheck::Significance(BSA.z0(), BSB.z0(), BSA.z0Error(), BSB.z0Error());
  auto xWS = bscheck::Significance(BSA.BeamWidthX(), BSB.BeamWidthX(), BSA.BeamWidthXError(), BSB.BeamWidthXError());
  auto yWS = bscheck::Significance(BSA.BeamWidthY(), BSB.BeamWidthY(), BSA.BeamWidthYError(), BSB.BeamWidthYError());
  auto zWS = bscheck::Significance(BSA.sigmaZ(), BSB.sigmaZ(), BSA.sigmaZ0Error(), BSB.sigmaZ0Error());

  std::array<float, 6> ret = {
      {xS.getSig(false), yS.getSig(false), zS.getSig(false), xWS.getSig(false), yWS.getSig(false), zWS.getSig(false)}};
  return ret;
}

// ------------ method called once each job just before starting event loop  ------------
void BeamSpotChecker::beginJob() {}

// ------------ method called once each job just after ending the event loop  ------------
void BeamSpotChecker::endJob() {}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void BeamSpotChecker::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);

  //Specify that only 'tracks' is allowed
  //To use, remove the default given above and uncomment below
  //ParameterSetDescription desc;
  //desc.addUntracked<edm::InputTag>("tracks","ctfWithMaterialTracks");
  //descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(BeamSpotChecker);
