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
        const reco::TrackRef trackRef = tv->castTo<reco::TrackRef>();
        thePVkeys.push_back(trackRef.key());
      }
    }
  }

  if (tc.isValid()) {
    // put the track in the collection is it was used for the vertex
    reco::TrackCollection tracks = *(tc.product());
    size_t itk = 0;
    for (; itk < tracks.size(); ++itk) {
      const reco::TrackRef trackRef(tc, itk);
      if (std::find(thePVkeys.begin(), thePVkeys.end(), trackRef.key()) == thePVkeys.end()) {
        result.push_back(&tracks.at(itk));
      }
    }  // end loop over tracks
  }

  return result;
}
