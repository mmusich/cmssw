#ifndef SimTracker_VertexAssociation_calculateVertexSharedTracks_h
#define SimTracker_VertexAssociation_calculateVertexSharedTracks_h

#include "SimDataFormats/Associations/interface/TrackAssociation.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "SimDataFormats/TrackingAnalysis/interface/TrackingVertex.h"

struct NumFrac {
  NumFrac(unsigned int n, double f) : num(n), frac(f) {}
  unsigned int num;
  double frac;
};

NumFrac calculateVertexSharedTracks(const reco::Vertex &recoV,
                                    const TrackingVertex &simV,
                                    const reco::RecoToSimCollection &trackRecoToSimAssociation,
                                    const bool weightPtSum2);

NumFrac calculateVertexSharedTracks(const TrackingVertex &simV,
                                    const reco::Vertex &recoV,
                                    const reco::SimToRecoCollection &trackSimToRecoAssociation,
                                    const bool weightPtSum2);

#endif
