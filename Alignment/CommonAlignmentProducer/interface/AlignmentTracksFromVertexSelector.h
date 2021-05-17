#ifndef Alignment_CommonAlignmentAlgorithm_AlignmentTrackFromVertexSelector_h
#define Alignment_CommonAlignmentAlgorithm_AlignmentTrackFromVertexSelector_h

#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "FWCore/Utilities/interface/EDGetToken.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include <vector>

namespace edm {
  class Event;
  class ParameterSet;
}  // namespace edm

class TrackingRecHit;

class AlignmentTrackFromVertexSelector {
public:
  typedef std::vector<const reco::Track*> Tracks;

  /// constructor
  AlignmentTrackFromVertexSelector(const edm::ParameterSet& cfg, edm::ConsumesCollector& iC);

  /// destructor
  ~AlignmentTrackFromVertexSelector();

  /// select tracks
  Tracks select(const edm::Handle<reco::TrackCollection>& tc, const edm::Event& evt) const;

private:
  edm::EDGetTokenT<reco::VertexCollection> vertexToken_;
  unsigned int vertexIndex_;
};

#endif
