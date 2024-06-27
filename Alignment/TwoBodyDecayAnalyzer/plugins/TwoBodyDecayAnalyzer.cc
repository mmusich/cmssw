// -*- C++ -*-
//
// Package:    Alignment/TwoBodyDecayAnalyzer
// Class:      TwoBodyDecayAnalyzer
//
/**\class TwoBodyDecayAnalyzer TwoBodyDecayAnalyzer.cc Alignment/TwoBodyDecayAnalyzer/plugins/TwoBodyDecayAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Marco Musich
//         Created:  Thu, 27 Jun 2024 10:15:04 GMT
//
//

// system include files
#include <cmath>
#include <iostream>
#include <memory>
#include <string>
#include <utility>
#include <vector>

// user include files
#include "Alignment/OfflineValidation/interface/SmartSelectionMonitor.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexFitter.h"
#include "RecoVertex/VertexPrimitives/interface/ConvertToFromReco.h"
#include "TrackingTools/GeomPropagators/interface/AnalyticalImpactPointExtrapolator.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TrackingTools/TrajectoryState/interface/TrajectoryStateOnSurface.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"

// ROOT user includes
#include "TLorentzVector.h"
#include "TTree.h"
#include "TH1F.h"
#include "TMath.h"

using reco::TrackCollection;

class TwoBodyDecayAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit TwoBodyDecayAnalyzer(const edm::ParameterSet&);
  ~TwoBodyDecayAnalyzer() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void beginJob() override;
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override;

  const edm::ESGetToken<TransientTrackBuilder, TransientTrackRecord> ttkbuilderToken_;
  const edm::EDGetTokenT<reco::TrackCollection> alcareco_trackCollToken_;
  const edm::EDGetTokenT<reco::TrackCollection> refit1_trackCollToken_;
  const edm::EDGetTokenT<reco::TrackCollection> ctf_trackCollToken_;
  const edm::EDGetTokenT<reco::TrackCollection> final_trackCollToken_;

  void analyzeTrackCollection(std::string strTrackType,
                              const TransientTrackBuilder& theTTBuilder,
                              edm::Handle<reco::TrackCollection>& hTrackColl,
                              bool verbose = false);
  reco::Vertex fitDimuonVertex(const TransientTrackBuilder& theTTBuilder,
                               edm::Handle<reco::TrackCollection>& hTrackColl,
                               bool& fitOk);

  SmartSelectionMonitor mon;
};

//
// constructors and destructor
//
TwoBodyDecayAnalyzer::TwoBodyDecayAnalyzer(const edm::ParameterSet& iConfig)
    : ttkbuilderToken_(esConsumes(edm::ESInputTag("", "TransientTrackBuilder"))),
      alcareco_trackCollToken_(consumes<reco::TrackCollection>(iConfig.getParameter<edm::InputTag>("alcarecotracks"))),
      refit1_trackCollToken_(consumes<reco::TrackCollection>(iConfig.getParameter<edm::InputTag>("refit1tracks"))),
      ctf_trackCollToken_(consumes<reco::TrackCollection>(iConfig.getParameter<edm::InputTag>("refit2tracks"))),
      final_trackCollToken_(consumes<reco::TrackCollection>(iConfig.getParameter<edm::InputTag>("finaltracks"))) {
  usesResource(TFileService::kSharedResource);

  edm::Service<TFileService> fs;
}

//
// member functions
//

// ------------ method called for each event  ------------
void TwoBodyDecayAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;

  using namespace edm;
  using namespace reco;
  using reco::TrackCollection;

  edm::Handle<reco::TrackCollection> alcarecotracks;
  iEvent.getByToken(alcareco_trackCollToken_, alcarecotracks);
  edm::Handle<reco::TrackCollection> refit1tracks;
  iEvent.getByToken(refit1_trackCollToken_, refit1tracks);
  edm::Handle<reco::TrackCollection> ctftracks;
  iEvent.getByToken(ctf_trackCollToken_, ctftracks);
  edm::Handle<reco::TrackCollection> finaltracks;
  iEvent.getByToken(final_trackCollToken_, finaltracks);

  const auto& theTTBuilder = iSetup.getData(ttkbuilderToken_);

  analyzeTrackCollection("alcareco", theTTBuilder, alcarecotracks);
  analyzeTrackCollection("refit1", theTTBuilder, refit1tracks);
  analyzeTrackCollection("refit2", theTTBuilder, ctftracks);
  analyzeTrackCollection("final", theTTBuilder, finaltracks);
}

void TwoBodyDecayAnalyzer::analyzeTrackCollection(std::string strTrackType,
                                                  const TransientTrackBuilder& theTTBuilder,
                                                  edm::Handle<reco::TrackCollection>& hTrackColl,
                                                  bool verbose) {
  if (verbose)
    std::cout << "Starting to process the track collection for " << strTrackType << std::endl;

  using namespace edm;
  using namespace reco;
  using reco::TrackCollection;

  if (!hTrackColl.isValid()) {
    if (verbose)
      std::cout << "Track collection is invalid." << std::endl;
    return;
  }
  if (hTrackColl->size() < 2) {
    if (verbose)
      std::cout << "Track collection size<2." << std::endl;
    return;
  }

  unsigned int itrk = 0;
  unsigned int j = 0;
  int totalcharge = 0;
  bool isValidPair = true;
  bool ZVtxOk = false;
  TLorentzVector trackMom[2];
  TLorentzVector trackMomAfterZVtxFit[2];
  TVector3 trackVtx[2];

  for (unsigned int jtrk = 0; jtrk < 2; jtrk++) {
    trackMom[jtrk].SetXYZT(0, 0, 0, 0);
    trackVtx[jtrk].SetXYZ(0, 0, 0);
  }
  for (reco::TrackCollection::const_iterator track = hTrackColl->begin(); track != hTrackColl->end(); ++track) {
    int charge = track->charge();
    totalcharge += charge;
    if (j == 0) {
      itrk = (charge > 0 ? 1 : 0);
    } else
      itrk = 1 - itrk;
    trackMom[itrk].SetPtEtaPhiM(track->pt(), track->eta(), track->phi(), 0.105);
    trackVtx[itrk].SetXYZ(track->vx(), track->vy(), track->vz());
    j++;
    if (j == 2)
      break;
  }

  isValidPair = (totalcharge == 0 && trackMom[0].P() != 0. && trackMom[1].P() != 0.);
  if (verbose && !isValidPair)
    std::cout << "Track collection does not contain a valid std::pair." << std::endl;
  mon.fillHisto("present", strTrackType, (isValidPair ? (short)1 : (short)0), 1.);
  if (isValidPair) {
    TLorentzVector ZMom = trackMom[0] + trackMom[1];
    mon.fillHisto("ZPt", strTrackType, (float)ZMom.Pt(), 1.);
    mon.fillHisto("ZPz", strTrackType, (float)ZMom.Pz(), 1.);
    mon.fillHisto("ZPhi", strTrackType, (float)ZMom.Phi(), 1.);
    mon.fillHisto("ZMass", strTrackType, (float)ZMom.M(), 1.);

    reco::Vertex ZVtx = fitDimuonVertex(theTTBuilder, hTrackColl, ZVtxOk);
    if (ZVtxOk) {
      mon.fillHisto("ZVertex_x", strTrackType, (float)ZVtx.x(), 1.);
      mon.fillHisto("ZVertex_y", strTrackType, (float)ZVtx.y(), 1.);
      mon.fillHisto("ZVertex_z", strTrackType, (float)ZVtx.z(), 1.);
      mon.fillHisto("ZVertex_NormChi2", strTrackType, (float)ZVtx.normalizedChi2(), 1.);

      // Recalculate track momenta with this vertex as reference
      j = 0;
      for (reco::TrackCollection::const_iterator track = hTrackColl->begin(); track != hTrackColl->end(); ++track) {
        TransientTrack t_track = theTTBuilder.build(&(*track));
        AnalyticalImpactPointExtrapolator extrapolator(t_track.field());
        TrajectoryStateOnSurface closestIn3DSpaceState =
            extrapolator.extrapolate(t_track.impactPointState(), RecoVertex::convertPos(ZVtx.position()));
        GlobalVector mom = closestIn3DSpaceState.globalMomentum();
        int charge = track->charge();
        totalcharge += charge;
        if (j == 0) {
          itrk = (charge > 0 ? 1 : 0);
        } else
          itrk = 1 - itrk;
        trackMomAfterZVtxFit[itrk].SetXYZT(mom.x(), mom.y(), mom.z(), sqrt(pow(0.105, 2) + pow(mom.mag(), 2)));
        j++;
        if (j == 2)
          break;
      }
      if (totalcharge != 0)
        std::cerr
            << "TwoBodyDecayAnalyzer::analyzeTrackCollection: Something went wrong! The total charge is no longer 0!"
            << std::endl;
      for (unsigned int jtrk = 0; jtrk < 2; jtrk++) {
        std::string strMuCore = (jtrk == 0 ? "MuMinus" : "MuPlus");
        mon.fillHisto("Pt_AfterZVtxFit", strTrackType + "_" + strMuCore, (float)trackMomAfterZVtxFit[jtrk].Pt(), 1.);
        mon.fillHisto("Pz_AfterZVtxFit", strTrackType + "_" + strMuCore, (float)trackMomAfterZVtxFit[jtrk].Pz(), 1.);
        mon.fillHisto("Phi_AfterZVtxFit", strTrackType + "_" + strMuCore, (float)trackMomAfterZVtxFit[jtrk].Phi(), 1.);
      }
      TLorentzVector ZMom_AfterZVtxFit = trackMomAfterZVtxFit[0] + trackMomAfterZVtxFit[1];
      mon.fillHisto("ZPt_AfterZVtxFit", strTrackType, (float)ZMom_AfterZVtxFit.Pt(), 1.);
      mon.fillHisto("ZPz_AfterZVtxFit", strTrackType, (float)ZMom_AfterZVtxFit.Pz(), 1.);
      mon.fillHisto("ZPhi_AfterZVtxFit", strTrackType, (float)ZMom_AfterZVtxFit.Phi(), 1.);
      mon.fillHisto("ZMass_AfterZVtxFit", strTrackType, (float)ZMom_AfterZVtxFit.M(), 1.);
    } else
      std::cerr << "TwoBodyDecayAnalyzer::analyzeTrackCollection: Z vertex fit failed for track collection "
                << strTrackType << std::endl;
  }
  for (unsigned int jtrk = 0; jtrk < 2; jtrk++) {
    std::string strMuCore = (jtrk == 0 ? "MuMinus" : "MuPlus");
    mon.fillHisto("Pt", strTrackType + "_" + strMuCore, (float)trackMom[jtrk].Pt(), 1.);
    mon.fillHisto("Pz", strTrackType + "_" + strMuCore, (float)trackMom[jtrk].Pz(), 1.);
    mon.fillHisto("Phi", strTrackType + "_" + strMuCore, (float)trackMom[jtrk].Phi(), 1.);
    mon.fillHisto("Vertex_x", strTrackType + "_" + strMuCore, (float)trackVtx[jtrk].X(), 1.);
    mon.fillHisto("Vertex_y", strTrackType + "_" + strMuCore, (float)trackVtx[jtrk].Y(), 1.);
    mon.fillHisto("Vertex_z", strTrackType + "_" + strMuCore, (float)trackVtx[jtrk].Z(), 1.);
  }
}

reco::Vertex TwoBodyDecayAnalyzer::fitDimuonVertex(const TransientTrackBuilder& theTTBuilder,
                                                   edm::Handle<reco::TrackCollection>& hTrackColl,
                                                   bool& fitOk) {
  using namespace edm;
  using namespace reco;

  std::vector<TransientTrack> t_tks;
  for (TrackCollection::const_iterator track = hTrackColl->begin(); track != hTrackColl->end(); ++track) {
    TransientTrack tt = theTTBuilder.build(&(*track));
    t_tks.push_back(tt);
  }

  // Kalman vertex fit without constraint
  KalmanVertexFitter vtxFitter;
  TransientVertex stdVertex = vtxFitter.vertex(t_tks);
  fitOk = stdVertex.isValid();
  if (fitOk) {
    reco::Vertex stdRecoVertex(Vertex::Point(stdVertex.position()),
                               stdVertex.positionError().matrix(),
                               stdVertex.totalChiSquared(),
                               stdVertex.degreesOfFreedom(),
                               0);
    return stdRecoVertex;
  } else {
    reco::Vertex stdRecoVertex;
    return stdRecoVertex;
  }
}

void TwoBodyDecayAnalyzer::beginJob() {
  // Booking calls for histogram filling
  mon.addHistogram(new TH1F("present", ";IsValidPair;Events", 2, 0, 2));
  mon.addHistogram(new TH1F("ZPt", ";Z boson p_{T} [GeV];Events", 100, 0., 200.));
  mon.addHistogram(new TH1F("ZPz", ";Z boson p_{z} [GeV];Events", 100, -300., 300.));
  mon.addHistogram(new TH1F("ZPhi", ";Z boson #phi;Events", 64, -3.2, 3.2));
  mon.addHistogram(new TH1F("ZMass", ";Z boson mass [GeV];Events", 100, 70., 110.));
  mon.addHistogram(new TH1F("ZVertex_x", ";Z vertex x [cm];Events", 100, -0.5, 0.5));
  mon.addHistogram(new TH1F("ZVertex_y", ";Z vertex y [cm];Events", 100, -0.5, 0.5));
  mon.addHistogram(new TH1F("ZVertex_z", ";Z vertex z [cm];Events", 100, -20., 20.));
  mon.addHistogram(new TH1F("ZVertex_NormChi2", ";Z vertex #chi^{2}/ndf;Events", 100, 0., 10.));

  // For "AfterZVtxFit" histograms
  mon.addHistogram(new TH1F("Pt_AfterZVtxFit", ";Track p_{T} after Z vertex fit [GeV];Events", 100, 0., 200.));
  mon.addHistogram(new TH1F("Pz_AfterZVtxFit", ";Track p_{z} after Z vertex fit [GeV];Events", 100, -300., 300.));
  mon.addHistogram(new TH1F("Phi_AfterZVtxFit", ";Track #phi after Z vertex fit;Events", 64, -3.2, 3.2));
  mon.addHistogram(new TH1F("ZPt_AfterZVtxFit", ";Z boson p_{T} after fit [GeV];Events", 100, 0., 200.));
  mon.addHistogram(new TH1F("ZPz_AfterZVtxFit", ";Z boson p_{z} after fit [GeV];Events", 100, -300., 300.));
  mon.addHistogram(new TH1F("ZPhi_AfterZVtxFit", ";Z boson #phi after fit;Events", 64, -3.2, 3.2));
  mon.addHistogram(new TH1F("ZMass_AfterZVtxFit", ";Z boson mass after fit [GeV];Events", 100, 70., 110.));

  // For standard track histograms
  mon.addHistogram(new TH1F("Pt", ";Track p_{T} [GeV];Events", 100, 0., 200.));
  mon.addHistogram(new TH1F("Pz", ";Track p_{z} [GeV];Events", 100, -300., 300.));
  mon.addHistogram(new TH1F("Phi", ";Track #phi;Events", 64, -3.2, 3.2));
  mon.addHistogram(new TH1F("Vertex_x", ";Track vertex x [cm];Events", 100, -0.5, 0.5));
  mon.addHistogram(new TH1F("Vertex_y", ";Track vertex y [cm];Events", 100, -0.5, 0.5));
  mon.addHistogram(new TH1F("Vertex_z", ";Track vertex z [cm];Events", 100, -20., 20.));

  // booked but unused
  mon.addHistogram(new TH1F("nvtx", ";Vertices;Events", 50, 0, 50));
  mon.addHistogram(new TH1F("dxy", ";d_{xy};tracks", 100, -100, 100));
  mon.addHistogram(new TH1F("dz", ";d_{z};tracks", 100, -100, 100));
  mon.addHistogram(new TH1F("dxyerr", ";d_{xy} error;tracks", 100, 0., 200));
  mon.addHistogram(new TH1F("dzerr", ";d_{z} error;tracks", 100, 0., 200));
  mon.addHistogram(new TProfile("dxyErrVsPt", ";track p_{T};d_{xy} error", 100, 0., 200, 0., 100.));
  mon.addHistogram(new TProfile("dzErrVsPt", ";track p_{T};d_{z} error", 100, 0., 200, 0., 100.));
  mon.addHistogram(new TProfile("dxyErrVsPhi", ";track #varphi;d_{xy} error", 100, -M_PI, M_PI, 0., 100.));
  mon.addHistogram(new TProfile("dzErrVsPhi", ";track #varphi;d_{z} error", 100, -M_PI, M_PI, 0., 100.));
  mon.addHistogram(new TProfile("dxyErrVsEta", ";track #eta;d_{xy} error", 100, -2.5, 2.5, 0., 100.));
  mon.addHistogram(new TProfile("dzErrVsEta", ";track #eta;d_{z} error", 100, -2.5, 2.5, 0., 100.));
}

// ------------ method called once each job just after ending the event loop  ------------
void TwoBodyDecayAnalyzer::endJob() { mon.Write(); }

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void TwoBodyDecayAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<edm::InputTag>("alcarecotracks", edm::InputTag("ALCARECOTkAlZMuMu"));
  desc.add<edm::InputTag>("refit1tracks", edm::InputTag("FirstTrackRefitter"));
  desc.add<edm::InputTag>("refit2tracks", edm::InputTag("HitFilteredTracksTrackFitter"));
  desc.add<edm::InputTag>("finaltracks", edm::InputTag("FinalTrackRefitter"));
  descriptions.addWithDefaultLabel(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TwoBodyDecayAnalyzer);
