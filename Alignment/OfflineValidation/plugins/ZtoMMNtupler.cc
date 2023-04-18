#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "TTree.h"
#include "TLorentzVector.h"

class ZtoMMNtupler : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit ZtoMMNtupler(const edm::ParameterSet&);
  ~ZtoMMNtupler() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void analyze(const edm::Event& event, const edm::EventSetup& setup) override;

  const edm::EDGetTokenT<reco::TrackCollection> trackToken_;

  static double constexpr muMass = 0.1056583745;  //!< Muon mass [GeV]

  TTree* tree_;
  float mass_;
  float posTrackEta_;
  float negTrackEta_;
  float posTrackPhi_;
  float negTrackPhi_;
  float posTrackPt_;
  float negTrackPt_;
};

ZtoMMNtupler::ZtoMMNtupler(const edm::ParameterSet& iConfig)
    : trackToken_(consumes<reco::TrackCollection>(iConfig.getParameter<edm::InputTag>("tracks"))),
      mass_{0},
      posTrackEta_{0},
      negTrackEta_{0},
      posTrackPhi_{0},
      negTrackPhi_{0},
      posTrackPt_{0},
      negTrackPt_{0} {
  usesResource(TFileService::kSharedResource);

  edm::Service<TFileService> fs;
  tree_ = fs->make<TTree>("tree", "My TTree");
  tree_->Branch("mass", &mass_, "mass/F");
  tree_->Branch("posTrackEta", &posTrackEta_, "posTrackEta/F");
  tree_->Branch("negTrackEta", &negTrackEta_, "negTrackEta/F");
  tree_->Branch("posTrackPhi", &posTrackPhi_, "posTrackPhi/F");
  tree_->Branch("negTrackPhi", &negTrackPhi_, "negTrackPhi/F");
  tree_->Branch("posTrackPt", &posTrackPt_, "posTrackPt/F");
  tree_->Branch("negTrackPt", &negTrackPt_, "negTrackPt/F");
}

void ZtoMMNtupler::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<edm::InputTag>("tracks", edm::InputTag("ALCARECOTkAlZMuMu"));
  descriptions.addWithDefaultLabel(desc);
}

void ZtoMMNtupler::analyze(const edm::Event& event, const edm::EventSetup& setup) {
  edm::Handle<reco::TrackCollection> tracks;
  event.getByToken(trackToken_, tracks);

  if (((*tracks).size() != 2)) {
    edm::LogError("ZtoMMNtupler") << "found more than two muons";
    return;
  }

  for (const auto& track : *tracks) {
    if (track.charge() > 0) {
      posTrackEta_ = track.eta();
      posTrackPhi_ = track.phi();
      posTrackPt_ = track.pt();
    } else {
      negTrackEta_ = track.eta();
      negTrackPhi_ = track.phi();
      negTrackPt_ = track.pt();
    }
  }

  TLorentzVector posTrack, negTrack, mother;
  posTrack.SetPtEtaPhiM(posTrackPt_, posTrackEta_, posTrackPhi_, muMass);  // assume muon mass for tracks
  negTrack.SetPtEtaPhiM(negTrackPt_, negTrackEta_, negTrackPhi_, muMass);
  mother = posTrack + negTrack;
  mass_ = mother.M();
  tree_->Fill();
}

DEFINE_FWK_MODULE(ZtoMMNtupler);
