#ifndef _TripletFilter_h_
#define _TripletFilter_h_

#include "DataFormats/GeometryVector/interface/GlobalVector.h"
#include "DataFormats/GeometryVector/interface/LocalVector.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "RecoPixelVertexing/PixelLowPtUtilities/interface/ClusterShapeHitFilter.h"
#include "RecoTracker/Record/interface/CkfComponentsRecord.h"

#include <vector>

namespace edm {
  class EventSetup;
}
class TrackingRecHit;
class ClusterShapeHitFilter;
class TrackerTopology;
class SiPixelClusterShapeCache;

class TripletFilter {
public:
  TripletFilter(const edm::EventSetup& es, edm::ConsumesCollector& iC);
  ~TripletFilter();
  bool checkTrack(const std::vector<const TrackingRecHit*>& recHits,
                  const std::vector<LocalVector>& localDirs,
                  const TrackerTopology* tTopo,
                  const SiPixelClusterShapeCache& clusterShapeCache);
  bool checkTrack(const std::vector<const TrackingRecHit*>& recHits,
                  const std::vector<GlobalVector>& globalDirs,
                  const TrackerTopology* tTopo,
                  const SiPixelClusterShapeCache& clusterShapeCache);

private:
  edm::ESGetToken<ClusterShapeHitFilter, CkfComponentsRecord> clusterShapeToken;
  const ClusterShapeHitFilter* theFilter;
};

#endif
