// -*- C++ -*-
//
// Package:    TrackPropagation/trackanalysis
// Class:      trackanalysis
//
/**\class trackanalysis trackanalysis.cc TrackPropagation/trackanalysis/plugins/trackanalysis.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Marco Musich
//         Created:  Tue, 20 Dec 2022 13:06:50 GMT
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
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
//
// class declaration
//

using reco::TrackCollection;

class trackanalysis : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit trackanalysis(const edm::ParameterSet&);
  ~trackanalysis() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void analyze(const edm::Event&, const edm::EventSetup&) override;

  // ----------member data ---------------------------
  edm::EDGetTokenT<TrackCollection> tracksToken_;  //used to select what tracks to read from configuration file
};

//
// constructors and destructor
//
trackanalysis::trackanalysis(const edm::ParameterSet& iConfig)
    : tracksToken_(consumes<TrackCollection>(iConfig.getUntrackedParameter<edm::InputTag>("tracks"))) {}

//
// member functions
//

// ------------ method called for each event  ------------
void trackanalysis::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;

  edm::LogPrint("trackanalysis") << "BEGIN TRACK ANALYSIS REPORT" << std::endl;
  for (const auto& track : iEvent.get(tracksToken_)) {
    edm::LogPrint("trackanalysis") << "track chi2: " << track.normalizedChi2() << std::endl;
    edm::LogPrint("trackanalysis") << "track pT: " << track.pt() << std::endl;
  }
  edm::LogPrint("trackanalysis") << "END TRACK ANALYSIS REPORT" << std::endl;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void trackanalysis::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.addUntracked<edm::InputTag>("tracks",edm::InputTag("ctfWithMaterialTracks"));
  descriptions.addWithDefaultLabel(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(trackanalysis);
