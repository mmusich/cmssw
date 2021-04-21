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

//
// class declaration
//

using reco::TrackCollection;

class DiMuonVertexValidator : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit DiMuonVertexValidator(const edm::ParameterSet&);
  ~DiMuonVertexValidator();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void beginJob() override;
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override;

  // ----------member data ---------------------------

  TH1F* hCosPhi_;
  TH1F* hInvMass_;

  edm::EDGetTokenT<TrackCollection> tracksToken_;  //used to select what tracks to read from configuration file
  edm::EDGetTokenT<reco::MuonCollection> muonsToken_; //used to select what tracks to read from configuration file
  edm::EDGetTokenT<reco::VertexCollection> vertexToken_;  //used to select what vertices to read from configuration file
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
DiMuonVertexValidator::DiMuonVertexValidator(const edm::ParameterSet& iConfig)
  : tracksToken_(consumes<TrackCollection>(iConfig.getParameter<edm::InputTag>("tracks"))),
    muonsToken_(consumes<reco::MuonCollection>(iConfig.getParameter<edm::InputTag>("muons"))),
    vertexToken_(consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("vertices")))
{}

DiMuonVertexValidator::~DiMuonVertexValidator() {}

//
// member functions
//

// ------------ method called for each event  ------------
void DiMuonVertexValidator::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;

  std::vector<const reco::Muon*> myGoodMuonVector;
  for (const auto& muon : iEvent.get(muonsToken_)) {
    const reco::TrackRef t = muon.innerTrack();
    if ( ! t.isNull() ) {
      if(t->quality(reco::TrackBase::highPurity) ) {
        if(t->chi2()/t->ndof() <= 2.5 &&
	   t->numberOfValidHits() >= 5 &&
	   t->hitPattern().numberOfValidPixelHits() >= 2 &&
	   t->quality(reco::TrackBase::highPurity)
	   )  myGoodMuonVector.push_back(&muon);
      }
    }
  }

  //std::cout << "myGoodMuonVector size: " << myGoodMuonVector.size() << std::endl;
  std::sort(myGoodMuonVector.begin(), myGoodMuonVector.end(), [](const reco::Muon*& lhs, const reco::Muon*& rhs) { return lhs->pt() > rhs->pt(); });

  /*
  for(const auto& muon : myGoodMuonVector){
    std::cout << "pT: " << muon->pt() << " ";
  }
  std::cout << std::endl;
  */

  if(myGoodMuonVector.size() < 2) return;
  if( (myGoodMuonVector[0]->pt()) < 30 || (myGoodMuonVector[1]->pt() < 10) ) return;
  if( myGoodMuonVector[0]->charge()*myGoodMuonVector[1]->charge() > 0 ) return;
  
  const auto& m1 = myGoodMuonVector[1]->p4();
  const auto& m0 = myGoodMuonVector[0]->p4();
  const auto& mother = m0+m1;
  
  float invMass = mother.M();
  hInvMass_->Fill(invMass);

  // just copy the top two muons
  std::vector<const reco::Muon*> theZMuonVector;
  theZMuonVector.reserve(2);
  theZMuonVector.push_back(myGoodMuonVector[1]);
  theZMuonVector.push_back(myGoodMuonVector[0]);
  
  // do the matching muons with tracks
  std::vector<const reco::Track*> myTracks;

  // do the muon track matching 
  unsigned int i=0;
  for(const auto& muon : theZMuonVector){
    i++;
    float minD = 1000.;
    const reco::Track* theMatch = nullptr;
    for (const auto& track : iEvent.get(tracksToken_)) {
      // do something with track parameters, e.g, plot the charge.
      float D = ::deltaR(muon->eta(),muon->phi(),track.eta(),track.phi());
      if(D < minD){
	minD = D;
	theMatch = &track;
      }
    }
    //std::cout<< "pushing new track: " << i << std::endl;
    myTracks.push_back(theMatch);
  }

  //std::cout << "selected tracks: " << myTracks.size() << std::endl; 

  edm::ESHandle<TransientTrackBuilder> theB;
  iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder",theB);
  TransientVertex aTransientVertex;
  std::vector<reco::TransientTrack> tks;

  if(myTracks.size()!=2) return;

  const auto& t1 = myTracks[1]->momentum();
  const auto& t0 = myTracks[0]->momentum();
  const auto& ditrack =t1+t0;
  
  math::XYZPoint ZpT(ditrack.x(),ditrack.y(),0);
  
  for(const auto& track : myTracks){
    reco::TransientTrack trajectory = (*theB).build(track);
    tks.push_back(trajectory);
  }

  KalmanVertexFitter kalman(true);
  aTransientVertex = kalman.vertex(tks);
  
  //std::cout << " vertex prob: " << TMath::Prob( aTransientVertex.totalChiSquared(), (int)aTransientVertex.degreesOfFreedom() ) << std::endl;

  // get collection of reconstructed vertices from event
  edm::Handle<reco::VertexCollection> vertexHandle;
  iEvent.getByToken(vertexToken_,vertexHandle);
  
  math::XYZPoint MainVertex(0,0,0);
  reco::Vertex TheMainVertex = vertexHandle.product()->front();
  
  if( vertexHandle.isValid() ) {
    const reco::VertexCollection* vertices = vertexHandle.product();
    if ( (*vertices).at(0).isValid()){
      auto theMainVtx = (*vertices).at(0);
      MainVertex.SetXYZ(theMainVtx.position().x(),theMainVtx.position().y(),theMainVtx.position().z());
    }
  }

  const math::XYZPoint myVertex(aTransientVertex.position().x(),aTransientVertex.position().y(),aTransientVertex.position().z());
  const math::XYZPoint deltaVtx(MainVertex.x()-myVertex.x(),MainVertex.y()-myVertex.y(),0);
 
  static constexpr float cmToum = 10e-4;

  if(TheMainVertex.isValid()){
    VertexDistanceXY vertTool;
    double distance = vertTool.distance(aTransientVertex,TheMainVertex).value();
    double dist_err = vertTool.distance(aTransientVertex,TheMainVertex).error();
    
    //std::cout << "distance: " << distance << "+/-" << dist_err << std::endl;	   

    // cut on the PV - SV distance
    if(distance*cmToum < 50){
      double cosphi = (ZpT.x() * deltaVtx.x() + ZpT.y() * deltaVtx.y()) / (sqrt(ZpT.x() * ZpT.x() + ZpT.y() * ZpT.y()) * sqrt(deltaVtx.x() * deltaVtx.x() + deltaVtx.y() * deltaVtx.y()));

      //std::cout << "cos(phi) = " << cosphi << std::endl;
      hCosPhi_->Fill(cosphi);
    }
  }
}

// ------------ method called once each job just before starting event loop  ------------
void DiMuonVertexValidator::beginJob() {
  edm::Service<TFileService> fs;

  TH1F::SetDefaultSumw2(kTRUE); 
  hCosPhi_ = fs->make<TH1F>("CosPhi",";cos(#phi_{c});N(#mu#mu pairs)",100,-1.,1.);
  hInvMass_ = fs->make<TH1F>("InvMass",";M(#mu#mu) [GeV];N(#mu#mu pairs)",70.,50.,120.);
  
}

// ------------ method called once each job just after ending the event loop  ------------
void DiMuonVertexValidator::endJob() {
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void DiMuonVertexValidator::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
   edm::ParameterSetDescription desc;
   desc.add<edm::InputTag>("tracks",edm::InputTag("generalTracks"));
   desc.add<edm::InputTag>("muons",edm::InputTag("muons"));
   desc.add<edm::InputTag>("vertices",edm::InputTag("offlinePrimaryVertices"));
   descriptions.addWithDefaultLabel(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(DiMuonVertexValidator);
