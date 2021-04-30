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

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
// muons
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "TLorentzVector.h"

#include "RecoVertex/VertexPrimitives/interface/TransientVertex.h"
#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexFitter.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"

#include "RecoVertex/VertexTools/interface/VertexDistanceXY.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

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
  TH1F* hCosPhi_;
  TH1F* hCosPhi3D_;
  TH2F* hCosPhi3DVsZEta_;
  TH2F* hCosPhi3DVsZPhi_;
  TH2F* hCosPhi3DVsMuPlusEta_;
  TH2F* hCosPhi3DVsMuPlusPhi_;
  TH2F* hCosPhi3DVsMuMinusEta_;
  TH2F* hCosPhi3DVsMuMinusPhi_;
  TH1F* hCosPhiInv_;
  TH1F* hCosPhiInv3D_;
  TH1F* hInvMass_;

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
      vertexToken_(consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("vertices"))) {}

DiMuonVertexValidator::~DiMuonVertexValidator() {}

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
    VertexDistanceXY vertTool;
    double distance = vertTool.distance(aTransientVertex, TheMainVertex).value();
    double dist_err = vertTool.distance(aTransientVertex, TheMainVertex).error();

    hSVDist_->Fill(distance * cmToum);
    hSVDistSig_->Fill(distance / dist_err);
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

  // clang-format off
  TH1F::SetDefaultSumw2(kTRUE);
  hSVProb_ = fs->make<TH1F>("VtxProb", ";ZV vertex probability;N(#mu#mu pairs)", 100, 0., 1.);
  hSVDist_ = fs->make<TH1F>("VtxDist", ";PV-ZV X-Y distance [#mum];N(#mu#mu pairs)", 100, 0., 300.);
  hSVDistSig_ = fs->make<TH1F>("VtxDistSig", ";PV-ZV X-Y distance signficance;N(#mu#mu pairs)", 100, 0., 5.);
  hCosPhi_ = fs->make<TH1F>("CosPhi", ";cos(#phi_{xy});N(#mu#mu pairs)", 50, -1., 1.);
  hCosPhi3D_ = fs->make<TH1F>("CosPhi3D", ";cos(#phi_{3D});N(#mu#mu pairs)", 50, -1., 1.);
  hCosPhi3DVsZEta_ = fs->make<TH2F>("CosPhi3DvsZEta", "cos(#phi_{3D}) vs #mu#mu #eta;#mu#mu pair #eta;cos(#phi_{3D})", 50, -3.5, 3.5, 50, -1., 1.);
  hCosPhi3DVsZPhi_ = fs->make<TH2F>("CosPhi3DvsZPhi", "cos(#phi_{3D}) vs #mu#mu #phi;#mu#mu pair #phi;cos(#phi_{3D})", 50, -M_PI, M_PI, 50, -1., 1.);
  hCosPhi3DVsMuPlusEta_  = fs->make<TH2F>("CosPhi3DvsMuPlusEta", "cos(#phi_{3D}) vs #mu^{+} #eta;#mu^{+} #eta;cos(#phi_{3D})", 50, -3.0, 3.0, 50, -1., 1.);
  hCosPhi3DVsMuPlusPhi_  = fs->make<TH2F>("CosPhi3DvsMuPlusPhi", "cos(#phi_{3D}) vs #mu^{+} #phi;#mu^{+} #phi;cos(#phi_{3D})", 50, -M_PI, M_PI, 50, -1., 1.);
  hCosPhi3DVsMuMinusEta_ = fs->make<TH2F>("CosPhi3DvsMuMinusEta","cos(#phi_{3D}) vs #mu^{-} #eta;#mu^{-} #eta;cos(#phi_{3D})", 50, -3.0, 3.0, 50, -1., 1.);
  hCosPhi3DVsMuMinusPhi_ = fs->make<TH2F>("CosPhi3DvMuMinusPhi", "cos(#phi_{3D}) vs #mu^{-} #phi;#mu^{-} #phi;cos(#phi_{3D})", 50, -M_PI, M_PI, 50, -1., 1.);
  hCosPhiInv_ = fs->make<TH1F>("CosPhiInv", ";inverted cos(#phi_{xy});N(#mu#mu pairs)", 50, -1., 1.);
  hCosPhiInv3D_ = fs->make<TH1F>("CosPhiInv3D", ";inverted cos(#phi_{3D});N(#mu#mu pairs)", 50, -1., 1.);
  hInvMass_ = fs->make<TH1F>("InvMass", ";M(#mu#mu) [GeV];N(#mu#mu pairs)", 70., 50., 120.);
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
