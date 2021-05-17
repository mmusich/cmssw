#include "Alignment/CommonAlignmentProducer/interface/AlignmentTracksFromVertexSelector.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/TrackReco/interface/Track.h"

// constructor ----------------------------------------------------------------
AlignmentTrackFromVertexSelector::AlignmentTrackFromVertexSelector(const edm::ParameterSet& cfg,
                                                                   edm::ConsumesCollector& iC)
    : vertexToken_(iC.consumes<reco::VertexCollection>(cfg.getParameter<edm::InputTag>("vertices"))),
      vertexIndex_(cfg.getParameter<unsigned int>("vertexIndex")) {}

// destructor -----------------------------------------------------------------
AlignmentTrackFromVertexSelector::~AlignmentTrackFromVertexSelector() {}

// do selection ---------------------------------------------------------------
AlignmentTrackFromVertexSelector::Tracks AlignmentTrackFromVertexSelector::select(
    const edm::Handle<reco::TrackCollection>& tc, const edm::Event& evt) const {
  Tracks result;

  std::vector<unsigned int> thePVkeys;

  // get collection of reconstructed vertices from event
  edm::Handle<reco::VertexCollection> vertexHandle = evt.getHandle(vertexToken_);

  // fill the vector of keys
  if (vertexHandle.isValid()) {
    const reco::VertexCollection* vertices = vertexHandle.product();
    if ((*vertices).at(vertexIndex_).isValid()) {
      const reco::Vertex* theVtx = &(vertices->at(vertexIndex_));
      for (auto tv = theVtx->tracks_begin(); tv != theVtx->tracks_end(); tv++) {
        if (tv->isNonnull()) {
          const reco::TrackRef trackRef = tv->castTo<reco::TrackRef>();
          thePVkeys.push_back(trackRef.key());
        }
      }
    }
  }

  std::sort(thePVkeys.begin(), thePVkeys.end());

  LogDebug("AlignmentTrackFromVertexSelector")
      << "after collecting the PV keys: thePVkeys.size()" << thePVkeys.size() << std::endl;
  for (const auto& key : thePVkeys) {
    LogDebug("AlignmentTrackFromVertexSelector") << key << ", ";
  }
  LogDebug("AlignmentTrackFromVertexSelector") << std::endl;

  if (tc.isValid()) {
    int indx(0);
    // put the track in the collection is it was used for the vertex
    for (reco::TrackCollection::const_iterator tk = tc->begin(); tk != tc->end(); ++tk, ++indx) {
      reco::TrackRef trackRef = reco::TrackRef(tc, indx);
      if (std::find(thePVkeys.begin(), thePVkeys.end(), trackRef.key()) != thePVkeys.end()) {
        LogDebug("AlignmentTrackFromVertexSelector") << "track index: " << indx << "filling result vector" << std::endl;
        result.push_back(&(*tk));
      }  // if a valid key is found
    }    // end loop over tracks
  }      // if the handle is valid
  return result;
}
