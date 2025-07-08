// -*- C++ -*-
//
// Package:    Alignment/CommonAlignmentProducer
// Class:      VertexDistanceValueMapProducer
//
/**\class VertexDistanceValueMapProducer VertexDistanceValueMapProducer.cc Alignment/CommonAlignmentProducer/plugins/VertexDistanceValueMapProducer.cc

 Description: creates a value map for each saved vertex with all the distances w.r.t a di-muon fitted vertex

*/
//
// Original Author:  Marco Musich
//         Created:  Mon, 12 Apr 2021 11:59:39 GMT
//
//

// system include files
#include <memory>
#include <vector>

// user include files
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/EDGetToken.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Utilities/interface/StreamID.h"
#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexFitter.h"
#include "RecoVertex/VertexPrimitives/interface/TransientVertex.h"
#include "RecoVertex/VertexTools/interface/VertexDistance3D.h"
#include "RecoVertex/VertexTools/interface/VertexDistanceXY.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"

//
// class declaration
//

class VertexDistanceValueMapProducer : public edm::global::EDProducer<> {
public:
  explicit VertexDistanceValueMapProducer(const edm::ParameterSet&);
  ~VertexDistanceValueMapProducer() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;

  // ----------member data ---------------------------
  // edToken
  const edm::ESGetToken<TransientTrackBuilder, TransientTrackRecord> ttbESToken_;
  const edm::EDGetTokenT<reco::VertexCollection> vertexToken_;
  const edm::EDGetTokenT<reco::TrackCollection> diLeptonToken_;
  
  // putToken
  const edm::EDPutTokenT<edm::ValueMap<float>> distancesPutToken_;
};

//
// constructors and destructor
//
VertexDistanceValueMapProducer::VertexDistanceValueMapProducer(const edm::ParameterSet& iConfig)
  :  ttbESToken_(esConsumes<TransientTrackBuilder, TransientTrackRecord>(edm::ESInputTag("", "TransientTrackBuilder"))),
     vertexToken_(consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("vertices"))),
     diLeptonToken_(consumes<reco::TrackCollection>(iConfig.getParameter<edm::InputTag>("leptonTracks"))),
     distancesPutToken_(produces<edm::ValueMap<float>>()) {}

//
// member functions
//

// ------------ method called to produce the data  ------------
void VertexDistanceValueMapProducer::produce(edm::StreamID streamID,
                                            edm::Event& iEvent,
                                            const edm::EventSetup& iSetup) const {
  using namespace edm;

  //=======================================================
  // Retrieve the muon Tracks information
  //=======================================================

  const auto& leptonTracksHandle = iEvent.getHandle(diLeptonToken_);
  
  if (!leptonTracksHandle.isValid())
    return;
  auto const& leptonTracks = *leptonTracksHandle;

  //=======================================================
  // Retrieve the general Track information
  //=======================================================

  // get collection of reconstructed vertices from event
  const auto& vertexHandle = iEvent.getHandle(vertexToken_);
  if (!vertexHandle.isValid())
    return;
  
  auto const& vertices = *vertexHandle;

  //=======================================================
  // fill the distance vector
  //=======================================================
  
  // fill the transient track collection with the lepton tracks
  const TransientTrackBuilder* theB = &iSetup.getData(ttbESToken_);
  std::vector<reco::TransientTrack> tks;
  for (const auto& track : leptonTracks) {
    reco::TransientTrack trajectory = theB->build(track);
    tks.push_back(trajectory);
  }


  // compute the secondary vertex
  TransientVertex aTransVtx;
  KalmanVertexFitter kalman(true);
  aTransVtx = kalman.vertex(tks);

  // the map cannot be filled straight away, so create an intermediate vector
  std::vector<float> v_dist;

  // find the closest vertex to the secondary vertex in 3D
  VertexDistance3D vertTool3D;
  for (const auto& vtx : vertices) {
    double dist3D = -1.;
    if (!aTransVtx.isValid()) {
      dist3D = vertTool3D.distance(aTransVtx, vtx).value();      
    } 
    v_dist.push_back(dist3D);
  }

  //=======================================================
  // Populate the event with the value map
  //=======================================================

  std::unique_ptr<edm::ValueMap<float>> vm_dist(new edm::ValueMap<float>());
  edm::ValueMap<float>::Filler filler(*vm_dist);
  filler.insert(vertexHandle, v_dist.begin(), v_dist.end());
  filler.fill();
  iEvent.put(distancesPutToken_, std::move(vm_dist));
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void VertexDistanceValueMapProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.setComment("Produces a value map with all the distances of the vertices w.r.t the di-lepton vertex");
  desc.add<edm::InputTag>("leptonTracks", edm::InputTag(""))->setComment("the probe vertex");
  desc.add<edm::InputTag>("vertices", edm::InputTag("vertices"))->setComment("all vertices in the event");
  descriptions.addWithDefaultLabel(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(VertexDistanceValueMapProducer);
