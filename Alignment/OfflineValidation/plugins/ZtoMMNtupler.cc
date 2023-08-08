#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "TH1F.h"
#include "TH2I.h"
#include "TTree.h"
#include "TLorentzVector.h"

class ZtoMMNtupler : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit ZtoMMNtupler(const edm::ParameterSet&);
  ~ZtoMMNtupler() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void analyze(const edm::Event& event, const edm::EventSetup& setup) override;
  double openingAngle(const reco::Track* track1, const reco::Track* track2);
  std::pair<unsigned int, reco::Vertex> findClosestVertex(const reco::Track* track1,
                                                          const reco::VertexCollection& vertices);
  const bool useReco_;
  const bool doGen_;
  std::vector<double> pTthresholds_;

  // either on or the other!
  //used to select what muon tracks to read from configuration file
  edm::EDGetTokenT<reco::MuonCollection> muonsToken_;
  //used to select what tracks to read from configuration file
  edm::EDGetTokenT<reco::TrackCollection> alcaRecoToken_;

  //used to select what tracks to read from configuration file
  edm::EDGetTokenT<reco::TrackCollection> tracksToken_;

  // for associated genParticles
  edm::EDGetTokenT<edm::View<reco::Candidate>> genParticlesToken_;
  //edm::EDGetTokenT<std::vector<reco::GenParticle>> genParticlesToken_;

  const edm::EDGetTokenT<reco::VertexCollection> vtxToken_;
  const edm::EDGetTokenT<reco::BeamSpot> bsToken_;

  static double constexpr muMass = 0.1056583745;  //!< Muon mass [GeV]

  TTree* tree_;
  float mass_;
  float posTrackDz_;
  float negTrackDz_;
  float posTrackD0_;
  float negTrackD0_;
  float posTrackEta_;
  float negTrackEta_;
  float posTrackPhi_;
  float negTrackPhi_;
  float posTrackPt_;
  float negTrackPt_;

  // for the gen-level info
  float genPosMuonEta_;
  float genNegMuonEta_;
  float genPosMuonPhi_;
  float genNegMuonPhi_;
  float genPosMuonPt_;
  float genNegMuonPt_;

  // control histograms
  TH2I* h_VertexMatrix;
  TH1F* h_cutFlow;
  TH1F* h_DeltaD0;
  TH1F* h_DeltaDz;
  TH1F* h_CosOpeningAngle;
};

ZtoMMNtupler::ZtoMMNtupler(const edm::ParameterSet& iConfig)
    : useReco_(iConfig.getParameter<bool>("useReco")),
      doGen_(iConfig.getParameter<bool>("doGen")),
      pTthresholds_(iConfig.getParameter<std::vector<double>>("pTThresholds")),
      vtxToken_(consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("vertices"))),
      bsToken_(consumes<reco::BeamSpot>(iConfig.getParameter<edm::InputTag>("beamSpot"))),
      mass_{0},
      posTrackDz_{0},
      negTrackDz_{0},
      posTrackD0_{0},
      negTrackD0_{0},
      posTrackEta_{0},
      negTrackEta_{0},
      posTrackPhi_{0},
      negTrackPhi_{0},
      posTrackPt_{0},
      negTrackPt_{0},
      genPosMuonEta_{-99.},
      genNegMuonEta_{-99.},
      genPosMuonPhi_{-99.},
      genNegMuonPhi_{-99.},
      genPosMuonPt_{-99.},
      genNegMuonPt_{-99.} {
  if (useReco_) {
    tracksToken_ = mayConsume<reco::TrackCollection>(iConfig.getParameter<edm::InputTag>("tracks"));
    muonsToken_ = mayConsume<reco::MuonCollection>(iConfig.getParameter<edm::InputTag>("muons"));
  } else {
    alcaRecoToken_ = mayConsume<reco::TrackCollection>(iConfig.getParameter<edm::InputTag>("muonTracks"));
  }

  if (doGen_) {
    genParticlesToken_ = consumes<edm::View<reco::Candidate>>(iConfig.getParameter<edm::InputTag>("genParticles"));
  }

  usesResource(TFileService::kSharedResource);

  // sort the vector of thresholds
  std::sort(pTthresholds_.begin(), pTthresholds_.end(), [](const double& lhs, const double& rhs) { return lhs > rhs; });

  edm::LogInfo("ZtoMMNtupler") << __FUNCTION__;
  for (const auto& thr : pTthresholds_) {
    edm::LogInfo("ZtoMMNtupler") << " Threshold: " << thr << " ";
  }

  edm::Service<TFileService> fs;
  h_cutFlow = fs->make<TH1F>("cutFlow", "cutFlow;cut;remaining events", 9, -0.5, 8.5);
  std::string labels[9] = {"all events",
                           "common vertex",
                           "d0 cut",
                           "p_{T} cut",
                           "#eta cut",
                           "mass window",
                           "#delta d_{0}",
                           "#delta d_{z}",
                           "opening angle"};
  unsigned int count{0};
  for (const auto& label : labels) {
    count++;
    h_cutFlow->GetXaxis()->SetBinLabel(count, label.c_str());
  }

  h_VertexMatrix = fs->make<TH2I>("VertexMatrix",
                                  ";index of closest vertex to #mu_{0};index of closest vertex to #mu_{1}",
                                  100,
                                  0,
                                  100,
                                  100,
                                  0,
                                  100);
  h_DeltaD0 = fs->make<TH1F>("DeltaD0", "#Deltad_{0};#Deltad_{0} [cm];events", 100, -0.5, 0.5);
  h_DeltaDz = fs->make<TH1F>("DeltaDz", "#Deltad_{z};#Deltad_{z} [cm];events", 100, -1, 1);
  h_CosOpeningAngle = fs->make<TH1F>("OpeningAngle", "cos(#gamma(#mu^{+},#mu^{-}));events", 100, -1., 1.);

  tree_ = fs->make<TTree>("tree", "My TTree");
  tree_->Branch("mass", &mass_, "mass/F");
  tree_->Branch("posTrackDz", &posTrackDz_, "posTrackDz/F");
  tree_->Branch("negTrackDz", &negTrackDz_, "negTrackDz/F");
  tree_->Branch("posTrackD0", &posTrackD0_, "posTrackD0/F");
  tree_->Branch("negTrackD0", &negTrackD0_, "negTrackD0/F");
  tree_->Branch("posTrackEta", &posTrackEta_, "posTrackEta/F");
  tree_->Branch("negTrackEta", &negTrackEta_, "negTrackEta/F");
  tree_->Branch("posTrackPhi", &posTrackPhi_, "posTrackPhi/F");
  tree_->Branch("negTrackPhi", &negTrackPhi_, "negTrackPhi/F");
  tree_->Branch("posTrackPt", &posTrackPt_, "posTrackPt/F");
  tree_->Branch("negTrackPt", &negTrackPt_, "negTrackPt/F");

  if (doGen_) {
    tree_->Branch("genPosMuonEta", &genPosMuonEta_, "genPosMuonEta/F");
    tree_->Branch("genNegMuonEta", &genNegMuonEta_, "genNegMuonEta/F");
    tree_->Branch("genPosMuonPhi", &genPosMuonPhi_, "genPosMuonPhi/F");
    tree_->Branch("genNegMuonPhi", &genNegMuonPhi_, "genNegMuonPhi/F");
    tree_->Branch("genPosMuonPt", &genPosMuonPt_, "genPosMuonPt/F");
    tree_->Branch("genNegMuonPt", &genNegMuonPt_, "genNegMuonPt/F");
  }
}

void ZtoMMNtupler::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.ifValue(
          edm::ParameterDescription<bool>("useReco", true, true),
          true >> edm::ParameterDescription<edm::InputTag>("muons", edm::InputTag("muons"), true) or
              false >> edm::ParameterDescription<edm::InputTag>("muonTracks", edm::InputTag("ALCARECOTkAlZMuMu"), true))
      ->setComment("If useReco is true need to specify the muon tracks, otherwise take the ALCARECO Inner tracks");
  desc.add<bool>("doGen", false);
  desc.add<edm::InputTag>("genParticles", edm::InputTag("genParticles"));
  desc.add<edm::InputTag>("tracks", edm::InputTag("generalTracks"));
  desc.add<edm::InputTag>("vertices", edm::InputTag("offlinePrimaryVertices"));
  desc.add<edm::InputTag>("beamSpot", edm::InputTag("offlineBeamSpot"));
  desc.add<std::vector<double>>("pTThresholds", {30., 10.});
  descriptions.addWithDefaultLabel(desc);
}

void ZtoMMNtupler::analyze(const edm::Event& event, const edm::EventSetup& setup) {
  h_cutFlow->Fill(0);

  // the di-muon tracks
  std::vector<const reco::Track*> myTracks;

  // if we have to start from scratch from RECO data-tier
  if (useReco_) {
    // select the good muons
    std::vector<const reco::Muon*> myGoodMuonVector;
    for (const auto& muon : event.get(muonsToken_)) {
      const reco::TrackRef t = muon.innerTrack();
      if (!t.isNull()) {
        if (t->quality(reco::TrackBase::highPurity)) {
          if (t->chi2() / t->ndof() <= 2.5 && t->numberOfValidHits() >= 5 &&
              t->hitPattern().numberOfValidPixelHits() >= 2 && t->quality(reco::TrackBase::highPurity))
            myGoodMuonVector.emplace_back(&muon);
        }
      }
    }

    LogDebug("ZtoMMNtupler") << "myGoodMuonVector size: " << myGoodMuonVector.size() << std::endl;
    std::sort(myGoodMuonVector.begin(), myGoodMuonVector.end(), [](const reco::Muon*& lhs, const reco::Muon*& rhs) {
      return lhs->pt() > rhs->pt();
    });

    // just check the ordering
    for (const auto& muon : myGoodMuonVector) {
      LogDebug("ZtoMMNtupler") << "pT: " << muon->pt() << " ";
    }
    LogDebug("ZtoMMNtupler") << std::endl;

    // reject if there's no Z
    if (myGoodMuonVector.size() < 2)
      return;

    if ((myGoodMuonVector[0]->pt()) < pTthresholds_[0] || (myGoodMuonVector[1]->pt() < pTthresholds_[1]))
      return;

    if (myGoodMuonVector[0]->charge() * myGoodMuonVector[1]->charge() > 0)
      return;

    //const auto& m1 = myGoodMuonVector[1]->p4();
    //const auto& m0 = myGoodMuonVector[0]->p4();
    //const auto& mother = m0 + m1;

    // just copy the top two muons
    std::vector<const reco::Muon*> theZMuonVector;
    theZMuonVector.reserve(2);
    theZMuonVector.emplace_back(myGoodMuonVector[1]);
    theZMuonVector.emplace_back(myGoodMuonVector[0]);

    // do the matching of Z muons with inner tracks
    unsigned int i = 0;
    for (const auto& muon : theZMuonVector) {
      i++;
      float minD = 1000.;
      const reco::Track* theMatch = nullptr;
      for (const auto& track : event.get(tracksToken_)) {
        float D = ::deltaR(muon->eta(), muon->phi(), track.eta(), track.phi());
        if (D < minD) {
          minD = D;
          theMatch = &track;
        }
      }
      LogDebug("ZtoMMNtupler") << "pushing new track: " << i << std::endl;
      myTracks.emplace_back(theMatch);
    }
  } else {
    // we start directly with the pre-selected ALCARECO tracks
    for (const auto& muon : event.get(alcaRecoToken_)) {
      myTracks.emplace_back(&muon);
    }
  }

  const reco::VertexCollection& vertices = event.get(vtxToken_);
  const reco::BeamSpot& beamSpot = event.get(bsToken_);
  math::XYZPoint bs(beamSpot.x0(), beamSpot.y0(), beamSpot.z0());

  //edm::LogPrint("ZtoMMNtupler") << " track size:" << myTracks.size() << " vertex size:" << vertices.size() << std::endl;

  if ((myTracks.size() != 2)) {
    LogTrace("ZtoMMNtupler") << "Found " << myTracks.size() << " muons in the event. Skipping";
    return;
  }

  bool passSameVertex{true};
  bool passD0sigCut{true};
  bool passPtCut{true};
  bool passEtaCut{true};
  bool passMassWindow{true};
  bool passDeltaD0{true};
  bool passDeltaDz{true};
  bool passOpeningAngle{true};
  double d0[2] = {0., 0.};
  double dz[2] = {0., 0.};
  unsigned int vtxIndex[2] = {999, 999};

  unsigned int i = 0;
  for (const auto& track : myTracks) {
    if (track->pt() < 12) {
      passPtCut = false;
      continue;
    }

    if (std::abs(track->eta()) > 2.5) {
      passEtaCut = false;
      continue;
    }

    const auto& closestVertex = this->findClosestVertex(track, vertices);
    vtxIndex[i] = closestVertex.first;
    d0[i] = track->dxy(closestVertex.second.position());
    dz[i] = track->dz(closestVertex.second.position());

    if (d0[i] / track->dxyError() > 4) {
      passD0sigCut = false;
      continue;
    }

    if (track->charge() > 0) {
      posTrackDz_ = dz[i];
      posTrackD0_ = d0[i];
      posTrackEta_ = track->eta();
      posTrackPhi_ = track->phi();
      posTrackPt_ = track->pt();
    } else {
      negTrackDz_ = dz[i];
      negTrackD0_ = d0[i];
      negTrackEta_ = track->eta();
      negTrackPhi_ = track->phi();
      negTrackPt_ = track->pt();
    }
    i++;
  }

  h_VertexMatrix->Fill(vtxIndex[0], vtxIndex[1]);
  // check if the two muons have the same vertex
  passSameVertex = (vtxIndex[0] == vtxIndex[1]);
  if (!passSameVertex)
    return;
  h_cutFlow->Fill(1);

  // checks if both muons pass the IP signficance cut (w.r.t BeamSpot)
  if (!passD0sigCut)
    return;
  h_cutFlow->Fill(2);

  // checks if both muons pass the pT cut
  if (!passPtCut)
    return;
  h_cutFlow->Fill(3);

  // check if both muons pass the eta cut
  if (!passEtaCut)
    return;
  h_cutFlow->Fill(4);

  // compute the invariant mass of the system
  TLorentzVector posTrack, negTrack, mother;
  posTrack.SetPtEtaPhiM(posTrackPt_, posTrackEta_, posTrackPhi_, muMass);  // assume muon mass for tracks
  negTrack.SetPtEtaPhiM(negTrackPt_, negTrackEta_, negTrackPhi_, muMass);
  mother = posTrack + negTrack;
  mass_ = mother.M();

  // checks if invariant mass of the system lies in the fiducial window
  passMassWindow = (mass_ > 70 && mass_ < 110);
  if (!passMassWindow)
    return;
  h_cutFlow->Fill(5);

  // checks if the di-muon system passes the d0 compatibility cut
  passDeltaD0 = (std::abs(d0[0] - d0[1]) < 0.01);
  h_DeltaD0->Fill(d0[0] - d0[1]);
  h_DeltaDz->Fill(dz[0] - dz[1]);
  if (!passDeltaD0)
    return;
  h_cutFlow->Fill(6);

  // checks if the di-muon system passes the z0 compatibility cut
  passDeltaDz = (std::abs(dz[0] - dz[1]) < 0.06);
  if (!passDeltaDz)
    return;
  h_cutFlow->Fill(7);

  // checks if the di-muon system passes the opening angle cut
  double openingAngle = this->openingAngle(myTracks[0], myTracks[1]);
  h_CosOpeningAngle->Fill(openingAngle);
  passOpeningAngle = true;  //(openingAngle > M_PI/4.);

  if (!passOpeningAngle)
    return;
  h_cutFlow->Fill(8);

  if (doGen_) {
    const edm::View<reco::Candidate>* genPartCollection = &event.get(genParticlesToken_);

    // loop on the reconstructed tracks
    for (const auto& track : myTracks) {
      float drmin = 0.1;
      // loop on the gen particles
      for (auto g = genPartCollection->begin(); g != genPartCollection->end(); ++g) {
        if (g->status() != 1)
          continue;

        if (std::abs(g->pdgId()) != 13)
          continue;

        if (g->charge() != track->charge())
          continue;

        float dR = reco::deltaR(*g, *track);
        if (dR < drmin) {
          drmin = dR;

          if (g->charge() > 0) {
            genPosMuonPt_ = g->pt();
            genPosMuonEta_ = g->eta();
            genPosMuonPhi_ = g->phi();
          } else {
            genNegMuonPt_ = g->pt();
            genNegMuonEta_ = g->eta();
            genNegMuonPhi_ = g->phi();
          }
        }
      }
    }
  }

  // if all cuts are passed fill the TTree
  tree_->Fill();
}

double ZtoMMNtupler::openingAngle(const reco::Track* trk1, const reco::Track* trk2) {
  math::XYZVector vec1(trk1->px(), trk1->py(), trk1->pz());
  math::XYZVector vec2(trk2->px(), trk2->py(), trk2->pz());
  return vec1.Dot(vec2) / (vec1.R() * vec2.R());
}

/*
double ZtoMMNtupler::openingAngle(const reco::Track& track1, const reco::Track& track2) {
  double dPhi = std::abs(track1.phi() - track2.phi());
  double dEta = std::abs(track1.eta() - track2.eta());
  double deltaR = reco::deltaR(track1, track2);
  double openingAngle = 2 * std::atan2(std::sqrt(std::sin(dEta / 2) * std::sin(dEta / 2) + std::sinh(dPhi / 2) * std::sinh(dPhi / 2)), std::sqrt(1 - deltaR * deltaR));
  return openingAngle;
}
*/

std::pair<unsigned int, reco::Vertex> ZtoMMNtupler::findClosestVertex(const reco::Track* track,
                                                                      const reco::VertexCollection& vertices) {
  // Initialize variables for minimum distance and closest vertex
  double minDistance = std::numeric_limits<double>::max();
  reco::Vertex closestVertex;

  unsigned int index{0}, theIndex{999};
  // Loop over the primary vertices and calculate the distance to the track
  for (const auto& vertex : vertices) {
    const math::XYZPoint& vertexPosition = vertex.position();

    // Calculate the distance to the track
    const auto& trackMomentum = track->momentum();
    const auto& vertexToPoint = vertexPosition - track->referencePoint();
    double distance = vertexToPoint.Cross(trackMomentum).R() / trackMomentum.R();

    // Check if this is the closest vertex so far
    if (distance < minDistance) {
      minDistance = distance;
      closestVertex = vertex;
      theIndex = index;
    }
    index++;
  }
  return std::make_pair(theIndex, closestVertex);
}

DEFINE_FWK_MODULE(ZtoMMNtupler);
