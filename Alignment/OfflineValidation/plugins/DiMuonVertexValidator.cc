// -*- C++ -*-
//
// Package:    Alignment/OfflineValidaiton
// Class:      DiMuonVertexValidator
//
/**\class DiMuonVertexValidator DiMuonVertexValidator.cc Alignment/DiMuonVertexValidator/plugins/DiMuonVertexValidator.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Marco Musich
//         Created:  Wed, 21 Apr 2021 09:06:25 GMT
//
//

// system include files
#include <memory>
#include <fmt/printf.h>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

// muons
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"

// utils
#include "DataFormats/Math/interface/deltaR.h"
#include "TLorentzVector.h"

// tracks
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "RecoVertex/VertexPrimitives/interface/TransientVertex.h"
#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexFitter.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"

// vertices
#include "RecoVertex/VertexTools/interface/VertexDistanceXY.h"
#include "RecoVertex/VertexTools/interface/VertexDistance3D.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

// ROOT
#include "TH1F.h"
#include "TH2F.h"

//#define LogDebug(X) std::cout << X <<

//
// class declaration
//

class DiMuonVertexValidator : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit DiMuonVertexValidator(const edm::ParameterSet&);
  ~DiMuonVertexValidator() override;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void beginJob() override;
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override;

  // ----------member data ---------------------------

  TH1F* hSVProb_;

  TH1F* hSVDist_;
  TH1F* hSVDistSig_;
  TH1F* hSVDist3D_;
  TH1F* hSVDist3DSig_;

  TH1F* hCosPhi_;
  TH1F* hCosPhi3D_;
  TH1F* hCosPhiInv_;
  TH1F* hCosPhiInv3D_;

  TH2F* hCosPhi3DVsZEta_;
  TH2F* hCosPhi3DVsZPhi_;

  TH2F* hCosPhiVsMuPlusEta_;
  TH2F* hCosPhiVsMuPlusPhi_;
  TH2F* hCosPhiVsMuMinusEta_;
  TH2F* hCosPhiVsMuMinusPhi_;

  TH2F* hCosPhi3DVsMuPlusEta_;
  TH2F* hCosPhi3DVsMuPlusPhi_;
  TH2F* hCosPhi3DVsMuMinusEta_;
  TH2F* hCosPhi3DVsMuMinusPhi_;

  TH2F* hVtxProbVsMuPlusEta_;
  TH2F* hVtxProbVsMuPlusPhi_;
  TH2F* hVtxProbVsMuMinusEta_;
  TH2F* hVtxProbVsMuMinusPhi_;

  TH2F* hVtxDistVsMuPlusEta_;
  TH2F* hVtxDistVsMuPlusPhi_;
  TH2F* hVtxDistVsMuMinusEta_;
  TH2F* hVtxDistVsMuMinusPhi_;

  TH2F* hVtxDist3DVsMuPlusEta_;
  TH2F* hVtxDist3DVsMuPlusPhi_;
  TH2F* hVtxDist3DVsMuMinusEta_;
  TH2F* hVtxDist3DVsMuMinusPhi_;

  TH2F* hSVDistSigVsMuPlusEta_;
  TH2F* hSVDistSigVsMuPlusPhi_;
  TH2F* hSVDistSigVsMuMinusEta_;
  TH2F* hSVDistSigVsMuMinusPhi_;

  TH2F* hSVDist3DSigVsMuPlusEta_;
  TH2F* hSVDist3DSigVsMuPlusPhi_;
  TH2F* hSVDist3DSigVsMuMinusEta_;
  TH2F* hSVDist3DSigVsMuMinusPhi_;

  TH1F* hInvMass_;
  TH1F* hTrackInvMass_;

  const edm::ESGetToken<TransientTrackBuilder, TransientTrackRecord> ttbESToken_;

  edm::EDGetTokenT<reco::TrackCollection> tracksToken_;   //used to select what tracks to read from configuration file
  edm::EDGetTokenT<reco::MuonCollection> muonsToken_;     //used to select what tracks to read from configuration file
  edm::EDGetTokenT<reco::VertexCollection> vertexToken_;  //used to select what vertices to read from configuration file
};

//
// constants, enums and typedefs
//

static constexpr float cmToum = 10e4;

//
// static data member definitions
//

//
// constructors and destructor
//
DiMuonVertexValidator::DiMuonVertexValidator(const edm::ParameterSet& iConfig)
    : ttbESToken_(esConsumes(edm::ESInputTag("", "TransientTrackBuilder"))),
      tracksToken_(consumes<reco::TrackCollection>(iConfig.getParameter<edm::InputTag>("tracks"))),
      muonsToken_(consumes<reco::MuonCollection>(iConfig.getParameter<edm::InputTag>("muons"))),
      vertexToken_(consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("vertices"))) {
  usesResource(TFileService::kSharedResource);
}

DiMuonVertexValidator::~DiMuonVertexValidator() = default;

//
// member functions
//

// ------------ method called for each event  ------------
void DiMuonVertexValidator::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;

  // select the good muons
  std::vector<const reco::Muon*> myGoodMuonVector;
  for (const auto& muon : iEvent.get(muonsToken_)) {
    const reco::TrackRef t = muon.innerTrack();
    if (!t.isNull()) {
      if (t->quality(reco::TrackBase::highPurity)) {
        if (t->chi2() / t->ndof() <= 2.5 && t->numberOfValidHits() >= 5 &&
            t->hitPattern().numberOfValidPixelHits() >= 2 && t->quality(reco::TrackBase::highPurity))
          myGoodMuonVector.emplace_back(&muon);
      }
    }
  }

  LogDebug("DiMuonVertexValidator") << "myGoodMuonVector size: " << myGoodMuonVector.size() << std::endl;
  std::sort(myGoodMuonVector.begin(), myGoodMuonVector.end(), [](const reco::Muon*& lhs, const reco::Muon*& rhs) {
    return lhs->pt() > rhs->pt();
  });

  // just check the ordering
  for (const auto& muon : myGoodMuonVector) {
    LogDebug("DiMuonVertexValidator") << "pT: " << muon->pt() << " ";
  }
  LogDebug("DiMuonVertexValidator") << std::endl;

  // reject if there's no Z

  if (myGoodMuonVector.size() < 2)
    return;
  if ((myGoodMuonVector[0]->pt()) < 30 || (myGoodMuonVector[1]->pt() < 10))
    return;
  if (myGoodMuonVector[0]->charge() * myGoodMuonVector[1]->charge() > 0)
    return;

  const auto& m1 = myGoodMuonVector[1]->p4();
  const auto& m0 = myGoodMuonVector[0]->p4();
  const auto& mother = m0 + m1;

  float invMass = mother.M();
  hInvMass_->Fill(invMass);

  // just copy the top two muons
  std::vector<const reco::Muon*> theZMuonVector;
  theZMuonVector.reserve(2);
  theZMuonVector.emplace_back(myGoodMuonVector[1]);
  theZMuonVector.emplace_back(myGoodMuonVector[0]);

  // do the matching of Z muons with inner tracks
  std::vector<const reco::Track*> myTracks;

  unsigned int i = 0;
  for (const auto& muon : theZMuonVector) {
    i++;
    float minD = 1000.;
    const reco::Track* theMatch = nullptr;
    for (const auto& track : iEvent.get(tracksToken_)) {
      float D = ::deltaR(muon->eta(), muon->phi(), track.eta(), track.phi());
      if (D < minD) {
        minD = D;
        theMatch = &track;
      }
    }
    LogDebug("DiMuonVertexValidator") << "pushing new track: " << i << std::endl;
    myTracks.emplace_back(theMatch);
  }

  LogDebug("DiMuonVertexValidator") << "selected tracks: " << myTracks.size() << std::endl;

  const TransientTrackBuilder* theB = &iSetup.getData(ttbESToken_);
  TransientVertex aTransientVertex;
  std::vector<reco::TransientTrack> tks;

  if (myTracks.size() != 2)
    return;

  const auto& t1 = myTracks[1]->momentum();
  const auto& t0 = myTracks[0]->momentum();
  const auto& ditrack = t1 + t0;

  const auto& tplus = myTracks[0]->charge() > 0 ? myTracks[0] : myTracks[1];
  const auto& tminus = myTracks[0]->charge() < 0 ? myTracks[0] : myTracks[1];

  static constexpr float mumass = 0.105658367;  //mu mass  (GeV/c^2)

  TLorentzVector p4_tplus(tplus->px(), tplus->py(), tplus->pz(), sqrt((tplus->p() * tplus->p()) + (mumass * mumass)));
  TLorentzVector p4_tminus(
      tminus->px(), tminus->py(), tminus->pz(), sqrt((tminus->p() * tminus->p()) + (mumass * mumass)));

  const auto& Zp4 = p4_tplus + p4_tminus;
  float track_invMass = Zp4.M();
  hTrackInvMass_->Fill(track_invMass);

  math::XYZPoint ZpT(ditrack.x(), ditrack.y(), 0);
  math::XYZPoint Zp(ditrack.x(), ditrack.y(), ditrack.z());

  for (const auto& track : myTracks) {
    reco::TransientTrack trajectory = theB->build(track);
    tks.push_back(trajectory);
  }

  KalmanVertexFitter kalman(true);
  aTransientVertex = kalman.vertex(tks);

  double SVProb = TMath::Prob(aTransientVertex.totalChiSquared(), (int)aTransientVertex.degreesOfFreedom());

  LogDebug("DiMuonVertexValidator") << " vertex prob: " << SVProb << std::endl;

  hSVProb_->Fill(SVProb);

  if (!aTransientVertex.isValid())
    return;

  hVtxProbVsMuPlusEta_->Fill(tplus->eta(), SVProb);
  hVtxProbVsMuPlusPhi_->Fill(tplus->phi(), SVProb);
  hVtxProbVsMuMinusEta_->Fill(tminus->eta(), SVProb);
  hVtxProbVsMuMinusPhi_->Fill(tminus->phi(), SVProb);

  // get collection of reconstructed vertices from event
  edm::Handle<reco::VertexCollection> vertexHandle = iEvent.getHandle(vertexToken_);

  math::XYZPoint MainVertex(0, 0, 0);
  reco::Vertex TheMainVertex = vertexHandle.product()->front();

  if (vertexHandle.isValid()) {
    const reco::VertexCollection* vertices = vertexHandle.product();
    if ((*vertices).at(0).isValid()) {
      auto theMainVtx = (*vertices).at(0);
      MainVertex.SetXYZ(theMainVtx.position().x(), theMainVtx.position().y(), theMainVtx.position().z());
    }
  }

  const math::XYZPoint myVertex(
      aTransientVertex.position().x(), aTransientVertex.position().y(), aTransientVertex.position().z());
  const math::XYZPoint deltaVtx(
      MainVertex.x() - myVertex.x(), MainVertex.y() - myVertex.y(), MainVertex.z() - myVertex.z());

  if (TheMainVertex.isValid()) {
    // Z Vertex distance in the xy plane

    VertexDistanceXY vertTool;
    double distance = vertTool.distance(aTransientVertex, TheMainVertex).value();
    double dist_err = vertTool.distance(aTransientVertex, TheMainVertex).error();

    hSVDist_->Fill(distance * cmToum);
    hSVDistSig_->Fill(distance / dist_err);

    hVtxDistVsMuPlusEta_->Fill(tplus->eta(), distance * cmToum);
    hVtxDistVsMuPlusPhi_->Fill(tplus->phi(), distance * cmToum);
    hVtxDistVsMuMinusEta_->Fill(tminus->eta(), distance * cmToum);
    hVtxDistVsMuMinusPhi_->Fill(tminus->phi(), distance * cmToum);

    hSVDistSigVsMuPlusEta_->Fill(tplus->eta(), distance / dist_err);
    hSVDistSigVsMuPlusPhi_->Fill(tplus->phi(), distance / dist_err);
    hSVDistSigVsMuMinusEta_->Fill(tminus->eta(), distance / dist_err);
    hSVDistSigVsMuMinusPhi_->Fill(tminus->phi(), distance / dist_err);

    // Z Vertex distance in 3D

    VertexDistance3D vertTool3D;
    double distance3D = vertTool3D.distance(aTransientVertex, TheMainVertex).value();
    double dist3D_err = vertTool3D.distance(aTransientVertex, TheMainVertex).error();

    hSVDist3D_->Fill(distance3D * cmToum);
    hSVDist3DSig_->Fill(distance3D / dist3D_err);

    hVtxDist3DVsMuPlusEta_->Fill(tplus->eta(), distance3D * cmToum);
    hVtxDist3DVsMuPlusPhi_->Fill(tplus->phi(), distance3D * cmToum);
    hVtxDist3DVsMuMinusEta_->Fill(tminus->eta(), distance3D * cmToum);
    hVtxDist3DVsMuMinusPhi_->Fill(tminus->phi(), distance3D * cmToum);

    hSVDist3DSigVsMuPlusEta_->Fill(tplus->eta(), distance3D / dist3D_err);
    hSVDist3DSigVsMuPlusPhi_->Fill(tplus->phi(), distance3D / dist3D_err);
    hSVDist3DSigVsMuMinusEta_->Fill(tminus->eta(), distance3D / dist3D_err);
    hSVDist3DSigVsMuMinusPhi_->Fill(tminus->phi(), distance3D / dist3D_err);

    LogDebug("DiMuonVertexValidator") << "distance: " << distance << "+/-" << dist_err << std::endl;
    // cut on the PV - SV distance
    if (distance * cmToum < 50) {
      double cosphi = (ZpT.x() * deltaVtx.x() + ZpT.y() * deltaVtx.y()) /
                      (sqrt(ZpT.x() * ZpT.x() + ZpT.y() * ZpT.y()) *
                       sqrt(deltaVtx.x() * deltaVtx.x() + deltaVtx.y() * deltaVtx.y()));

      double cosphi3D = (Zp.x() * deltaVtx.x() + Zp.y() * deltaVtx.y() + Zp.z() * deltaVtx.z()) /
                        (sqrt(Zp.x() * Zp.x() + Zp.y() * Zp.y() + Zp.z() * Zp.z()) *
                         sqrt(deltaVtx.x() * deltaVtx.x() + deltaVtx.y() * deltaVtx.y() + deltaVtx.z() * deltaVtx.z()));

      hCosPhi3DVsZEta_->Fill(mother.eta(), cosphi3D);
      hCosPhi3DVsZPhi_->Fill(mother.phi(), cosphi3D);

      hCosPhiVsMuPlusEta_->Fill(tplus->eta(), cosphi);
      hCosPhiVsMuPlusPhi_->Fill(tplus->phi(), cosphi);
      hCosPhiVsMuMinusEta_->Fill(tminus->eta(), cosphi);
      hCosPhiVsMuMinusPhi_->Fill(tminus->phi(), cosphi);

      hCosPhi3DVsMuPlusEta_->Fill(tplus->eta(), cosphi3D);
      hCosPhi3DVsMuPlusPhi_->Fill(tplus->phi(), cosphi3D);
      hCosPhi3DVsMuMinusEta_->Fill(tminus->eta(), cosphi3D);
      hCosPhi3DVsMuMinusPhi_->Fill(tminus->phi(), cosphi3D);

      LogDebug("DiMuonVertexValidator") << "cos(phi) = " << cosphi << std::endl;
      hCosPhi_->Fill(cosphi);
      hCosPhi3D_->Fill(cosphi3D);
    }
  }
}

// ------------ method called once each job just before starting event loop  ------------
void DiMuonVertexValidator::beginJob() {
  edm::Service<TFileService> fs;

  static constexpr float maxMuEta = 2.4;

  // clang-format off
  TH1F::SetDefaultSumw2(kTRUE);
  hSVProb_ = fs->make<TH1F>("VtxProb", ";ZV vertex probability;N(#mu#mu pairs)", 100, 0., 1.);

  hSVDist_ = fs->make<TH1F>("VtxDist", ";PV-ZV xy distance [#mum];N(#mu#mu pairs)", 100, 0., 300.);
  hSVDistSig_ = fs->make<TH1F>("VtxDistSig", ";PV-ZV xy distance signficance;N(#mu#mu pairs)", 100, 0., 5.);

  hSVDist3D_ = fs->make<TH1F>("VtxDist3D", ";PV-ZV 3D distance [#mum];N(#mu#mu pairs)", 100, 0., 300.);
  hSVDist3DSig_ = fs->make<TH1F>("VtxDist3DSig", ";PV-ZV 3D distance signficance;N(#mu#mu pairs)", 100, 0., 5.);

  hInvMass_ = fs->make<TH1F>("InvMass", ";M(#mu#mu) [GeV];N(#mu#mu pairs)", 70., 50., 120.);
  hTrackInvMass_ = fs->make<TH1F>("TkTkInvMass", ";M(tk,tk) [GeV];N(tk tk pairs)", 70., 50., 120.);

  hCosPhi_ = fs->make<TH1F>("CosPhi", ";cos(#phi_{xy});N(#mu#mu pairs)", 50, -1., 1.);
  hCosPhi3D_ = fs->make<TH1F>("CosPhi3D", ";cos(#phi_{3D});N(#mu#mu pairs)", 50, -1., 1.);

  hCosPhiInv_ = fs->make<TH1F>("CosPhiInv", ";inverted cos(#phi_{xy});N(#mu#mu pairs)", 50, -1., 1.);
  hCosPhiInv3D_ = fs->make<TH1F>("CosPhiInv3D", ";inverted cos(#phi_{3D});N(#mu#mu pairs)", 50, -1., 1.);

  // 2D Maps

  hCosPhi3DVsZEta_ = fs->make<TH2F>("CosPhi3DvsZEta", "cos(#phi_{3D}) vs #mu#mu #eta;#mu#mu pair #eta;cos(#phi_{3D})", 50, -3.5, 3.5, 50, -1., 1.);
  hCosPhi3DVsZPhi_ = fs->make<TH2F>("CosPhi3DvsZPhi", "cos(#phi_{3D}) vs #mu#mu #phi;#mu#mu pair #phi;cos(#phi_{3D})", 50, -M_PI, M_PI, 50, -1., 1.);

  std::string tt  = "cos(#phi_{xy}) vs";
  std::string ytt = "cos(#phi_{xy})";

  hCosPhiVsMuPlusEta_  = fs->make<TH2F>("CosPhivsMuPlusEta",  fmt::sprintf("%s #mu^{+} #eta;#mu^{+} #eta;%s",tt,ytt).c_str(), 50, -maxMuEta, maxMuEta, 50, -1., 1.);
  hCosPhiVsMuPlusPhi_  = fs->make<TH2F>("CosPhivsMuPlusPhi",  fmt::sprintf("%s #mu^{+} #phi;#mu^{+} #phi;%s",tt,ytt).c_str(), 50, -M_PI, M_PI, 50, -1., 1.);
  hCosPhiVsMuMinusEta_ = fs->make<TH2F>("CosPhivsMuMinusEta", fmt::sprintf("%s #mu^{-} #eta;#mu^{-} #eta;%s",tt,ytt).c_str(), 50, -maxMuEta, maxMuEta, 50, -1., 1.);
  hCosPhiVsMuMinusPhi_ = fs->make<TH2F>("CosPhivMuMinusPhi",  fmt::sprintf("%s #mu^{-} #phi;#mu^{-} #phi;%s",tt,ytt).c_str(), 50, -M_PI, M_PI, 50, -1., 1.);

  tt  = "cos(#phi_{3D}) vs";
  ytt = "cos(#phi_{3D})";

  hCosPhi3DVsMuPlusEta_  = fs->make<TH2F>("CosPhi3DvsMuPlusEta", fmt::sprintf("%s #mu^{+} #eta;#mu^{+} #eta;%s",tt,ytt).c_str(), 50, -maxMuEta, maxMuEta, 50, -1., 1.);
  hCosPhi3DVsMuPlusPhi_  = fs->make<TH2F>("CosPhi3DvsMuPlusPhi", fmt::sprintf("%s #mu^{+} #phi;#mu^{+} #phi;%s",tt,ytt).c_str(), 50, -M_PI, M_PI, 50, -1., 1.);
  hCosPhi3DVsMuMinusEta_ = fs->make<TH2F>("CosPhi3DvsMuMinusEta",fmt::sprintf("%s #mu^{-} #eta;#mu^{-} #eta;%s",tt,ytt).c_str(), 50, -maxMuEta, maxMuEta, 50, -1., 1.);
  hCosPhi3DVsMuMinusPhi_ = fs->make<TH2F>("CosPhi3DvMuMinusPhi", fmt::sprintf("%s #mu^{-} #phi;#mu^{-} #phi;%s",tt,ytt).c_str(), 50, -M_PI, M_PI, 50, -1., 1.);

  tt  = "Secondary Vertex Probability vs";
  ytt = "Prob(#chi^{2}_{ZV})";

  hVtxProbVsMuPlusEta_  = fs->make<TH2F>("VtxProbvsMuPlusEta", fmt::sprintf("%s #mu^{+} #eta;#mu^{+} #eta;%s",tt,ytt).c_str(), 50, -maxMuEta, maxMuEta, 50, 0.,1.);
  hVtxProbVsMuPlusPhi_  = fs->make<TH2F>("VtxProbvsMuPlusPhi", fmt::sprintf("%s #mu^{+} #phi;#mu^{+} #phi;%s",tt,ytt).c_str(), 50, -M_PI, M_PI, 50, 0.,1.);
  hVtxProbVsMuMinusEta_ = fs->make<TH2F>("VtxProbvsMuMinusEta",fmt::sprintf("%s #mu^{-} #eta;#mu^{-} #eta;%s",tt,ytt).c_str(), 50, -maxMuEta, maxMuEta, 50, 0.,1.);
  hVtxProbVsMuMinusPhi_ = fs->make<TH2F>("VtxProbvMuMinusPhi", fmt::sprintf("%s #mu^{-} #phi;#mu^{-} #phi;%s",tt,ytt).c_str(), 50, -M_PI, M_PI, 50, 0.,1.);

  tt  = "Secondary Vertex Distance vs";
  ytt = "dist(PV,ZV) [#mum]";

  hVtxDistVsMuPlusEta_  = fs->make<TH2F>("VtxDistvsMuPlusEta", fmt::sprintf("%s #mu^{+} #eta;#mu^{+} #eta;%s",tt,ytt).c_str(), 50, -maxMuEta, maxMuEta, 100,0.,300.);
  hVtxDistVsMuPlusPhi_  = fs->make<TH2F>("VtxDistvsMuPlusPhi", fmt::sprintf("%s #mu^{+} #phi;#mu^{+} #phi;%s",tt,ytt).c_str(), 50, -M_PI, M_PI, 100,0.,300.);
  hVtxDistVsMuMinusEta_ = fs->make<TH2F>("VtxDistvsMuMinusEta",fmt::sprintf("%s #mu^{-} #eta;#mu^{-} #eta;%s",tt,ytt).c_str(), 50, -maxMuEta, maxMuEta, 100,0.,300.);
  hVtxDistVsMuMinusPhi_ = fs->make<TH2F>("VtxDistvMuMinusPhi", fmt::sprintf("%s #mu^{-} #phi;#mu^{-} #phi;%s",tt,ytt).c_str(), 50, -M_PI, M_PI, 100,0.,300.);

  tt  = "Secondary Vertex 3D Distance vs";
  ytt = "dist_{3D}(PV,ZV) [#mum]";

  hVtxDist3DVsMuPlusEta_  = fs->make<TH2F>("VtxDist3DvsMuPlusEta", fmt::sprintf("%s #mu^{+} #eta;#mu^{+} #eta;%s",tt,ytt).c_str(), 50, -maxMuEta, maxMuEta, 250,0.,500.);
  hVtxDist3DVsMuPlusPhi_  = fs->make<TH2F>("VtxDist3DvsMuPlusPhi", fmt::sprintf("%s #mu^{+} #phi;#mu^{+} #phi;%s",tt,ytt).c_str(), 50, -M_PI, M_PI, 100,0.,500.);
  hVtxDist3DVsMuMinusEta_ = fs->make<TH2F>("VtxDist3DvsMuMinusEta",fmt::sprintf("%s #mu^{-} #eta;#mu^{-} #eta;%s",tt,ytt).c_str(), 50, -maxMuEta, maxMuEta, 250,0.,500.);
  hVtxDist3DVsMuMinusPhi_ = fs->make<TH2F>("VtxDist3DvMuMinusPhi", fmt::sprintf("%s #mu^{-} #phi;#mu^{-} #phi;%s",tt,ytt).c_str(), 50, -M_PI, M_PI, 250,0.,500.);

  tt  = "Secondary Vertex Distance Significance vs";
  ytt = "dist_{xy}/#sigma_{xy}(PV,ZV)";

  hSVDistSigVsMuPlusEta_  = fs->make<TH2F>("SVDistSigvsMuPlusEta", fmt::sprintf("%s vs #mu^{+} #eta;#mu^{+} #eta;%s",tt,ytt).c_str(), 50, -maxMuEta, maxMuEta, 100, 0., 5.);
  hSVDistSigVsMuPlusPhi_  = fs->make<TH2F>("SVDistSigvsMuPlusPhi", fmt::sprintf("%s vs #mu^{+} #phi;#mu^{+} #phi;%s",tt,ytt).c_str(), 50, -M_PI, M_PI, 100, 0., 5.);
  hSVDistSigVsMuMinusEta_ = fs->make<TH2F>("SVDistSigvsMuMinusEta",fmt::sprintf("%s vs #mu^{-} #eta;#mu^{-} #eta;%s",tt,ytt).c_str(), 50, -maxMuEta, maxMuEta, 100, 0., 5.);
  hSVDistSigVsMuMinusPhi_ = fs->make<TH2F>("SVDistSigvMuMinusPhi", fmt::sprintf("%s vs #mu^{-} #phi;#mu^{-} #phi;%s",tt,ytt).c_str(), 50, -M_PI, M_PI, 100, 0., 5.);

  tt  = "Secondary Vertex 3D Distance Significance vs";
  ytt = "dist_{3D}/#sigma_{3D}(PV,ZV)";

  hSVDist3DSigVsMuPlusEta_  = fs->make<TH2F>("SVDist3DSigvsMuPlusEta", fmt::sprintf("%s vs #mu^{+} #eta;#mu^{+} #eta;%s",tt,ytt).c_str(), 50, -maxMuEta, maxMuEta, 100, 0., 5.);
  hSVDist3DSigVsMuPlusPhi_  = fs->make<TH2F>("SVDist3DSigvsMuPlusPhi", fmt::sprintf("%s vs #mu^{+} #phi;#mu^{+} #phi;%s",tt,ytt).c_str(), 50, -M_PI, M_PI, 100, 0., 5.);
  hSVDist3DSigVsMuMinusEta_ = fs->make<TH2F>("SVDist3DSigvsMuMinusEta",fmt::sprintf("%s vs #mu^{-} #eta;#mu^{-} #eta;%s",tt,ytt).c_str(), 50, -maxMuEta, maxMuEta, 100, 0., 5.);
  hSVDist3DSigVsMuMinusPhi_ = fs->make<TH2F>("SVDist3DSigvMuMinusPhi", fmt::sprintf("%s vs #mu^{-} #phi;#mu^{-} #phi;%s",tt,ytt).c_str(), 50, -M_PI, M_PI, 100, 0., 5.);
  // clang-format on
}

// ------------ method called once each job just after ending the event loop  ------------
void DiMuonVertexValidator::endJob() {
  TH1F::SetDefaultSumw2(kTRUE);
  const unsigned int nBinsX = hCosPhi_->GetNbinsX();
  for (unsigned int i = 1; i <= nBinsX; i++) {
    //float binContent = hCosPhi_->GetBinContent(i);
    float invertedBinContent = hCosPhi_->GetBinContent(nBinsX + 1 - i);
    float invertedBinError = hCosPhi_->GetBinError(nBinsX + 1 - i);
    hCosPhiInv_->SetBinContent(i, invertedBinContent);
    hCosPhiInv_->SetBinError(i, invertedBinError);

    //float binContent3D = hCosPhi3D_->GetBinContent(i);
    float invertedBinContent3D = hCosPhi3D_->GetBinContent(nBinsX + 1 - i);
    float invertedBinError3D = hCosPhi3D_->GetBinError(nBinsX + 1 - i);
    hCosPhiInv3D_->SetBinContent(i, invertedBinContent3D);
    hCosPhiInv3D_->SetBinError(i, invertedBinError3D);
  }
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void DiMuonVertexValidator::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<edm::InputTag>("tracks", edm::InputTag("generalTracks"));
  desc.add<edm::InputTag>("muons", edm::InputTag("muons"));
  desc.add<edm::InputTag>("vertices", edm::InputTag("offlinePrimaryVertices"));
  descriptions.addWithDefaultLabel(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(DiMuonVertexValidator);
