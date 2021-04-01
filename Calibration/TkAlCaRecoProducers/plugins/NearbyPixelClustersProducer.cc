// -*- C++ -*-
//
// Package:    Calibration/TkAlCaRecoProducers
// Class:      NearbyPixelClustersProducer
//
/**\class NearbyPixelClustersProducer NearbyPixelClustersProducer.cc Calibration/TkAlCaRecoProducers/plugins/NearbyPixelClustersProducer.cc

 Description: Class to produce the collection of SiPixelClusters closest, hit by hit, to the trajectory measurements of a given track

 Implementation: 
     Implementation of this class is heavily endebted to https://github.com/jkarancs/PhaseIPixelNtuplizer/blob/master/plugins/PhaseIPixelNtuplizer.h

*/
//
// Original Author:  Marco Musich
//         Created:  Mon, 29 Mar 2021 12:29:30 GMT
//
//

// system include files
#include <memory>
#include <map>

// user include files
#include "DataFormats/Common/interface/DetSetVector.h"
#include "DataFormats/Common/interface/DetSetVectorNew.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/SiPixelCluster/interface/SiPixelCluster.h"
#include "DataFormats/SiPixelDetId/interface/PixelSubdetector.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackerCommon/interface/PixelBarrelName.h"
#include "DataFormats/TrackerCommon/interface/PixelEndcapName.h"
#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"
#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHit.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/StreamID.h"
#include "Geometry/CommonDetUnit/interface/PixelGeomDetUnit.h"
#include "Geometry/CommonTopologies/interface/PixelTopology.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/TrackerNumberingBuilder/interface/GeometricDet.h"
#include "RecoLocalTracker/ClusterParameterEstimator/interface/PixelClusterParameterEstimator.h"
#include "RecoLocalTracker/Records/interface/TkPixelCPERecord.h"
#include "RecoTracker/MeasurementDet/interface/MeasurementTracker.h"
#include "RecoTracker/MeasurementDet/interface/MeasurementTrackerEvent.h"
#include "RecoTracker/Record/interface/CkfComponentsRecord.h"
#include "TrackingTools/GeomPropagators/interface/Propagator.h"
#include "TrackingTools/KalmanUpdators/interface/Chi2MeasurementEstimator.h"
#include "TrackingTools/KalmanUpdators/interface/Chi2MeasurementEstimatorBase.h"
#include "TrackingTools/MeasurementDet/interface/LayerMeasurements.h"
#include "TrackingTools/PatternTools/interface/TrajTrackAssociation.h"
#include "TrackingTools/Records/interface/TrackingComponentsRecord.h"
#include "TrackingTools/TrackFitters/interface/TrajectoryStateCombiner.h"
#include "TrackingTools/TrajectoryState/interface/FreeTrajectoryState.h"
#include "TrackingTools/TrajectoryState/interface/TrajectoryStateOnSurface.h"
#include "TrackingTools/TransientTrackingRecHit/interface/TransientTrackingRecHit.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelQuality.h"
#include "CondFormats/DataRecord/interface/SiPixelQualityFromDbRcd.h"

using trajCrossings_t = std::map<uint32_t, std::vector<LocalPoint>>;

//
// class declaration
//

class NearbyPixelClustersProducer : public edm::stream::EDProducer<> {
public:
  explicit NearbyPixelClustersProducer(const edm::ParameterSet&);
  ~NearbyPixelClustersProducer() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void produce(edm::Event&, const edm::EventSetup&) override;
  const trajCrossings_t findAllTrajectoriesCrossings(
      const edm::Handle<TrajTrackAssociationCollection>& trajTrackCollectionHandle);

  const std::vector<edmNew::DetSet<SiPixelCluster>::const_iterator> findAllNearbyClusters(
      const edmNew::DetSetVector<SiPixelCluster>::const_iterator& clusterSet,
      const uint32_t rawId,
      const std::vector<LocalPoint>& vLocalPos);

  TrajectoryStateOnSurface getTrajectoryStateOnSurface(const TrajectoryMeasurement& measurement);
  bool detidIsOnPixel(const DetId& detid);

  // ----------member data ---------------------------

  const bool dumpWholeDetId_;

  const edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> geomEsToken_;
  const edm::ESGetToken<PixelClusterParameterEstimator, TkPixelCPERecord> pixelCPEEsToken_;
  const edm::ESGetToken<SiPixelQuality, SiPixelQualityFromDbRcd> badModuleToken_;

  edm::EDGetTokenT<edmNew::DetSetVector<SiPixelCluster>> clustersToken_;
  edm::EDGetTokenT<TrajTrackAssociationCollection> trajTrackCollectionToken_;

  edm::EDPutTokenT<SiPixelClusterCollectionNew> clusterPutToken_;

  const TrackerGeometry* trackerGeometry_;
  const PixelClusterParameterEstimator* pixelCPE_;
};

//
// constructors and destructor
//
NearbyPixelClustersProducer::NearbyPixelClustersProducer(const edm::ParameterSet& iConfig)
    : dumpWholeDetId_(iConfig.getParameter<bool>("dumpWholeDetIds")),
      geomEsToken_(esConsumes()),
      pixelCPEEsToken_(esConsumes(edm::ESInputTag("", "PixelCPEGeneric"))),
      badModuleToken_(esConsumes()),
      clustersToken_(
          consumes<edmNew::DetSetVector<SiPixelCluster>>(iConfig.getParameter<edm::InputTag>("clusterCollection"))),
      trajTrackCollectionToken_(
          consumes<TrajTrackAssociationCollection>(iConfig.getParameter<edm::InputTag>("trajectoryInput"))),
      clusterPutToken_(produces<SiPixelClusterCollectionNew>()) {}

//
// member functions
//

// ------------ method called to produce the data  ------------
void NearbyPixelClustersProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;

  auto outputClusters = std::make_unique<SiPixelClusterCollectionNew>();

  // get the Tracker geometry from event setup
  trackerGeometry_ = &iSetup.getData(geomEsToken_);

  // get the Pixel CPE from event setup
  pixelCPE_ = &iSetup.getData(pixelCPEEsToken_);

  const auto& SiPixelBadModule_ = &iSetup.getData(badModuleToken_);

  // get cluster collection
  edm::Handle<edmNew::DetSetVector<SiPixelCluster>> clusterCollectionHandle;
  iEvent.getByToken(clustersToken_, clusterCollectionHandle);
  const edmNew::DetSetVector<SiPixelCluster>& clusterCollection = *clusterCollectionHandle;

  // get Traj-Track Collection
  edm::Handle<TrajTrackAssociationCollection> trajTrackCollectionHandle;
  iEvent.getByToken(trajTrackCollectionToken_, trajTrackCollectionHandle);
  if (!trajTrackCollectionHandle.isValid())
    return;

  // find all trajectory crossings in the event
  const auto& allCrossings = this->findAllTrajectoriesCrossings(trajTrackCollectionHandle);

  LogDebug("NearbyPixelClustersProducer") << allCrossings.size() << std::endl;

  // now find all nearby clusters
  for (const auto& [id, vLocalPos] : allCrossings) {
    // if the module is bad continue
    if (SiPixelBadModule_->IsModuleBad(id))
      continue;

    // prepare the filler
    edmNew::DetSetVector<SiPixelCluster>::FastFiller spc(*outputClusters, id);

    // retrieve the clusters of the right detId
    const auto& clustersOnDet = clusterCollection.find(id);

    // if the cluster DetSet is not valid, move on
    if (!(*clustersOnDet).isValid())
      continue;

    // find all the clusters to put into the event
    const auto& clustersToPut = this->findAllNearbyClusters(clustersOnDet, id, vLocalPos);

    for (const auto& cluster : clustersToPut) {
      spc.push_back(*cluster);
    }

    if (spc.empty())
      spc.abort();

  }  // loop on trajectory crossings

  iEvent.put(clusterPutToken_, std::move(outputClusters));
}

/*--------------------------------------------------------------------*/
const trajCrossings_t NearbyPixelClustersProducer::findAllTrajectoriesCrossings(
    const edm::Handle<TrajTrackAssociationCollection>& trajTrackCollectionHandle)
/*--------------------------------------------------------------------*/
{
  trajCrossings_t crossings;  // = {0xFFFFF,{}};

  std::vector<uint32_t> treatedIds;

  for (const auto& pair : *trajTrackCollectionHandle) {
    const edm::Ref<std::vector<Trajectory>> traj = pair.key;

    for (const TrajectoryMeasurement& measurement : traj->measurements()) {
      //Check if the measurement infos can be read
      if (!measurement.updatedState().isValid())
        continue;

      const TransientTrackingRecHit::ConstRecHitPointer& recHit = measurement.recHit();

      // Only looking for pixel hits
      DetId recHitDetid = recHit->geographicalId();
      const auto& rawId = recHitDetid.rawId();

      if (!this->detidIsOnPixel(recHitDetid))
        continue;

      // Skipping hits with undeterminable positions
      TrajectoryStateOnSurface trajStateOnSurface = this->getTrajectoryStateOnSurface(measurement);

      if (!(trajStateOnSurface.isValid()))
        continue;

      // Position measurements
      // Looking for valid and missing hits
      LocalPoint localPosition = trajStateOnSurface.localPosition();

      if (std::find(treatedIds.begin(), treatedIds.end(), rawId) != treatedIds.end()) {
        crossings.at(rawId).push_back(localPosition);
      } else {
        crossings.insert(std::pair<uint32_t, std::vector<LocalPoint>>(rawId, {localPosition}));
        treatedIds.push_back(rawId);
      }
    }  // loop on measurements in trajectory
  }    // loop on trajectories

  return crossings;
}

/*--------------------------------------------------------------------*/
const std::vector<edmNew::DetSet<SiPixelCluster>::const_iterator> NearbyPixelClustersProducer::findAllNearbyClusters(
    const edmNew::DetSetVector<SiPixelCluster>::const_iterator& clusterSet,
    const uint32_t rawId,
    const std::vector<LocalPoint>& vLocalPos)
/*--------------------------------------------------------------------*/
{
  std::vector<edmNew::DetSet<SiPixelCluster>::const_iterator> outputClusters;

  static constexpr unsigned int k_maxClustersInDet = 1024;

  // something funny is going on here ...
  if ((*clusterSet).size() > k_maxClustersInDet) {
    edm::LogWarning("NearbyPixelClustersProducer")
        << __func__ << "() number of clusters in det " << rawId /*(*clusterSet).id()*/ << " is " << (*clusterSet).size()
        << ", which is larger than maximum (1024).\n Something funny with the data is going on!" << std::endl;
    return outputClusters;
  }

  const PixelGeomDetUnit* pixdet = (const PixelGeomDetUnit*)trackerGeometry_->idToDetUnit(rawId);
  edmNew::DetSet<SiPixelCluster>::const_iterator itCluster = clusterSet->begin();

  // just copy straight the whole set of clusters in the detid
  if (dumpWholeDetId_) {
    for (; itCluster != clusterSet->end(); ++itCluster) {
      outputClusters.push_back(itCluster);
    }
    return outputClusters;
  }

  int count = 0;
  for (const auto& localPos : vLocalPos) {
    count++;
    //trajectory crossing local coordinates
    const auto& traj_lx = localPos.x();
    const auto& traj_ly = localPos.y();

    float minD = 10000.;
    edmNew::DetSet<SiPixelCluster>::const_iterator closest = nullptr;

    //std::cout<< rawId << " count: " << count << " n. clusters: " << (*clusterSet).size() << std::endl;
    LogDebug("NearbyPixelClustersProducer")
        << __func__ << rawId << " count: " << count << " n. clusters: " << (*clusterSet).size() << std::endl;

    for (; itCluster != clusterSet->end(); ++itCluster) {
      LocalPoint lp(itCluster->x(), itCluster->y(), 0.);
      const auto& params = pixelCPE_->getParameters(*itCluster, *pixdet);
      lp = std::get<0>(params);

      float D = sqrt((lp.x() - traj_lx) * (lp.x() - traj_lx) + (lp.y() - traj_ly) * (lp.y() - traj_ly));
      if (D < minD) {
        closest = itCluster;
        minD = D;
      }
    }  // loop on cluster sets

    if (closest) {
      outputClusters.push_back(closest);
    }
  }  // loop on the trajectory crossings

  return outputClusters;
}

/*--------------------------------------------------------------------*/
bool NearbyPixelClustersProducer::detidIsOnPixel(const DetId& detid)
/*--------------------------------------------------------------------*/
{
  if (detid.det() != DetId::Tracker)
    return false;
  if (detid.subdetId() == PixelSubdetector::PixelBarrel)
    return true;
  if (detid.subdetId() == PixelSubdetector::PixelEndcap)
    return true;
  return false;
}

/*--------------------------------------------------------------------*/
TrajectoryStateOnSurface NearbyPixelClustersProducer::getTrajectoryStateOnSurface(
    const TrajectoryMeasurement& measurement)
/*--------------------------------------------------------------------*/
{
  static TrajectoryStateCombiner trajStateCombiner;

  const auto& forwardPredictedState = measurement.forwardPredictedState();
  const auto& backwardPredictedState = measurement.backwardPredictedState();

  if (forwardPredictedState.isValid() && backwardPredictedState.isValid())
    return trajStateCombiner(forwardPredictedState, backwardPredictedState);

  else if (backwardPredictedState.isValid())
    return backwardPredictedState;

  else if (forwardPredictedState.isValid())
    return forwardPredictedState;

  edm::LogError("NearbyPixelClustersProducer") << "Error saving traj. measurement data."
                                               << " Trajectory state on surface cannot be determined." << std::endl;

  return TrajectoryStateOnSurface();
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void NearbyPixelClustersProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.setComment(
      "Produces the collection of SiPixelClusters closest, hit by hit, to the trajectory measurements of a given "
      "track");
  desc.add<bool>("dumpWholeDetIds", false);
  desc.add<edm::InputTag>("clusterCollection", edm::InputTag("siPixelClusters"));
  desc.add<edm::InputTag>("trajectoryInput", edm::InputTag("myRefitter"));
  descriptions.addWithDefaultLabel(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(NearbyPixelClustersProducer);
