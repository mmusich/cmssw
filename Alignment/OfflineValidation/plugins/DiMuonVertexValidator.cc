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
#include <utility>
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
// Ancillary class for plotting
//
class PlotsVsDiMuKinematics {
public:
  PlotsVsDiMuKinematics(const std::string& name, const std::string& tt, const std::string& ytt)
      : m_name(name), m_title(tt), m_ytitle(ytt), m_isBooked(false) {}

  ~PlotsVsDiMuKinematics() {}

  void bookPlots(TFileDirectory& fs, const float valmin, const float valmax, const int nxbins, const int nybins) {
    static constexpr float maxMuEta = 2.4;
    static constexpr float maxMuMuEta = 3.5;
    TH1F::SetDefaultSumw2(kTRUE);

    // clang-format off
    h2_vs_Z_eta = fs.make<TH2F>(fmt::sprintf("%sVsMuMuPhi", m_name).c_str(),
                                fmt::sprintf("%s vs #mu#mu pair #eta;#mu^{+}#mu^{-} #eta;%s", m_title, m_ytitle).c_str(),
                                nxbins, -maxMuMuEta, maxMuMuEta,
                                nybins, valmin, valmax);

    h2_vs_Z_phi = fs.make<TH2F>(fmt::sprintf("%sVsMuMuEta", m_name).c_str(),
				fmt::sprintf("%s vs #mu#mu pair #phi;#mu^{+}#mu^{-} #phi [rad];%s", m_title, m_ytitle).c_str(),
				nxbins, -M_PI, M_PI,
				nybins, valmin, valmax);

    h2_vs_muplus_eta = fs.make<TH2F>(fmt::sprintf("%sVsMuPlusEta", m_name).c_str(),
                                     fmt::sprintf("%s vs #mu^{+} #eta;#mu^{+} #eta;%s", m_title, m_ytitle).c_str(),
                                     nxbins, -maxMuEta, maxMuEta,
                                     nybins, valmin, valmax);

    h2_vs_muplus_phi = fs.make<TH2F>(fmt::sprintf("%sVsMuPlusPhi", m_name).c_str(),
                                     fmt::sprintf("%s vs #mu^{+} #phi;#mu^{+} #phi [rad];%s", m_title, m_ytitle).c_str(),
                                     nxbins, -M_PI, M_PI,
                                     nybins, valmin, valmax);

    h2_vs_muminus_eta = fs.make<TH2F>(fmt::sprintf("%sVsMuMinusEta", m_name).c_str(),
                                      fmt::sprintf("%s vs #mu^{-} #eta;#mu^{-} #eta;%s", m_title, m_ytitle).c_str(),
                                      nxbins, -maxMuEta, maxMuEta,
                                      nybins, valmin, valmax);

    h2_vs_muminus_phi = fs.make<TH2F>(fmt::sprintf("%sVsMuMinusPhi", m_name).c_str(),
                                      fmt::sprintf("%s vs #mu^{-} #phi;#mu^{-} #phi [rad];%s", m_title, m_ytitle).c_str(),
                                      nxbins, -M_PI, M_PI,
                                      nybins, valmin, valmax);
    // clang-format on

    // flip the is booked bit
    m_isBooked = true;
  }

  void fillPlots(const float val, const std::pair<TLorentzVector, TLorentzVector>& momenta) {
    if (!m_isBooked)
      return;

    h2_vs_Z_eta->Fill((momenta.first + momenta.second).Eta(), val);
    h2_vs_Z_phi->Fill((momenta.first + momenta.second).Phi(), val);
    h2_vs_muplus_eta->Fill((momenta.first).Eta(), val);
    h2_vs_muplus_phi->Fill((momenta.first).Phi(), val);
    h2_vs_muminus_eta->Fill((momenta.second).Eta(), val);
    h2_vs_muminus_phi->Fill((momenta.second).Phi(), val);
  }

private:
  const std::string m_name;
  const std::string m_title;
  const std::string m_ytitle;

  bool m_isBooked;

  TH2F* h2_vs_Z_phi;
  TH2F* h2_vs_Z_eta;
  TH2F* h2_vs_muplus_eta;
  TH2F* h2_vs_muplus_phi;
  TH2F* h2_vs_muminus_eta;
  TH2F* h2_vs_muminus_phi;
};

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

  // control plots

  TH1F* hSVProb_;

  TH1F* hSVDist_;
  TH1F* hSVDistSig_;
  TH1F* hSVDist3D_;
  TH1F* hSVDist3DSig_;

  TH1F* hCosPhi_;
  TH1F* hCosPhi3D_;
  TH1F* hCosPhiInv_;
  TH1F* hCosPhiInv3D_;

  TH1F* hInvMass_;
  TH1F* hTrackInvMass_;

  // 2D maps

  PlotsVsDiMuKinematics CosPhiPlots = PlotsVsDiMuKinematics("CosPhi", "cos(#phi_{xy})", "cos(#phi_{xy})");
  PlotsVsDiMuKinematics CosPhi3DPlots = PlotsVsDiMuKinematics("CosPhi3D", "cos(#phi_{3D})", "cos(#phi_{3D})");
  PlotsVsDiMuKinematics VtxProbPlots =
      PlotsVsDiMuKinematics("VtxProb", "Secondary Vertex Probability", "Prob(#chi^{2}_{SV})");
  PlotsVsDiMuKinematics VtxDistPlots =
      PlotsVsDiMuKinematics("VtxDist", "Secondary Vertex Distance", "dist(PV,ZV) [#mum]");
  PlotsVsDiMuKinematics VtxDist3DPlots =
      PlotsVsDiMuKinematics("VtxDist3D", "Secondary Vertex 3D Distance", "dist_{3D}(PV,ZV) [#mum]");
  PlotsVsDiMuKinematics VtxDistSigPlots =
      PlotsVsDiMuKinematics("SVDistSig", "Secondary Vertex Distance Significance", "dist_{xy}/#sigma_{xy}(PV,ZV)");
  PlotsVsDiMuKinematics VtxDist3DSigPlots = PlotsVsDiMuKinematics(
      "SVDist3DSig", "Secondary Vertex 3D Distance Significance vs", "dist_{3D}/#sigma_{3D}(PV,ZV)");
  PlotsVsDiMuKinematics ZMassPlots = PlotsVsDiMuKinematics("DiMuMass", "Di-muon invariant mass", "M(#mu#mu) [GeV]");

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

  // fill the z->mm mass plots
  ZMassPlots.fillPlots(track_invMass, std::make_pair(p4_tplus, p4_tminus));

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

  // fill the VtxProb plots
  VtxProbPlots.fillPlots(SVProb, std::make_pair(p4_tplus, p4_tminus));

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

    // fill the VtxDist plots
    VtxDistPlots.fillPlots(distance * cmToum, std::make_pair(p4_tplus, p4_tminus));

    // fill the VtxDisSig plots
    VtxDistSigPlots.fillPlots(distance / dist_err, std::make_pair(p4_tplus, p4_tminus));

    // Z Vertex distance in 3D

    VertexDistance3D vertTool3D;
    double distance3D = vertTool3D.distance(aTransientVertex, TheMainVertex).value();
    double dist3D_err = vertTool3D.distance(aTransientVertex, TheMainVertex).error();

    hSVDist3D_->Fill(distance3D * cmToum);
    hSVDist3DSig_->Fill(distance3D / dist3D_err);

    // fill the VtxDist3D plots
    VtxDist3DPlots.fillPlots(distance3D * cmToum, std::make_pair(p4_tplus, p4_tminus));

    // fill the VtxDisSig plots
    VtxDist3DSigPlots.fillPlots(distance3D / dist3D_err, std::make_pair(p4_tplus, p4_tminus));

    LogDebug("DiMuonVertexValidator") << "distance: " << distance << "+/-" << dist_err << std::endl;
    // cut on the PV - SV distance
    if (distance * cmToum < 50) {
      double cosphi = (ZpT.x() * deltaVtx.x() + ZpT.y() * deltaVtx.y()) /
                      (sqrt(ZpT.x() * ZpT.x() + ZpT.y() * ZpT.y()) *
                       sqrt(deltaVtx.x() * deltaVtx.x() + deltaVtx.y() * deltaVtx.y()));

      double cosphi3D = (Zp.x() * deltaVtx.x() + Zp.y() * deltaVtx.y() + Zp.z() * deltaVtx.z()) /
                        (sqrt(Zp.x() * Zp.x() + Zp.y() * Zp.y() + Zp.z() * Zp.z()) *
                         sqrt(deltaVtx.x() * deltaVtx.x() + deltaVtx.y() * deltaVtx.y() + deltaVtx.z() * deltaVtx.z()));

      LogDebug("DiMuonVertexValidator") << "cos(phi) = " << cosphi << std::endl;

      hCosPhi_->Fill(cosphi);
      hCosPhi3D_->Fill(cosphi3D);

      // fill the cosphi plots
      CosPhiPlots.fillPlots(cosphi, std::make_pair(p4_tplus, p4_tminus));

      // fill the VtxDisSig plots
      CosPhi3DPlots.fillPlots(cosphi3D, std::make_pair(p4_tplus, p4_tminus));
    }
  }
}

// ------------ method called once each job just before starting event loop  ------------
void DiMuonVertexValidator::beginJob() {
  edm::Service<TFileService> fs;

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
  // clang-format on

  // 2D Maps

  TFileDirectory DirCosPhi = fs->mkdir("CosPhiPlots");
  CosPhiPlots.bookPlots(DirCosPhi, -1., 1., 50, 50);

  TFileDirectory dirCosPhi3D = fs->mkdir("CosPhi3DPlots");
  CosPhi3DPlots.bookPlots(dirCosPhi3D, -1., 1., 50, 50);

  TFileDirectory dirVtxProb = fs->mkdir("VtxProbPlots");
  VtxProbPlots.bookPlots(dirVtxProb, 0., 1., 50, 50);

  TFileDirectory dirVtxDist = fs->mkdir("VtxDistPlots");
  VtxDistPlots.bookPlots(dirVtxDist, 0., 300., 50, 100);

  TFileDirectory dirVtxDist3D = fs->mkdir("VtxDist3DPlots");
  VtxDist3DPlots.bookPlots(dirVtxDist3D, 0., 500., 50, 250);

  TFileDirectory dirVtxDistSig = fs->mkdir("VtxDistSigPlots");
  VtxDistSigPlots.bookPlots(dirVtxDistSig, 0., 5., 50, 100);

  TFileDirectory dirVtxDist3DSig = fs->mkdir("VtxDist3DSigPlots");
  VtxDist3DSigPlots.bookPlots(dirVtxDist3DSig, 0., 5., 50, 100);

  TFileDirectory dirInvariantMass = fs->mkdir("InvariantMassPlots");
  ZMassPlots.bookPlots(dirInvariantMass, 70., 120., 50, 50);
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
