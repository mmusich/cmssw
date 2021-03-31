// -*- C++ -*-
//
// Package:    Calibration/TkAlCaRecoProducers
// Class:      NearbyPixelClusterProducer
//
/**\class NearbyPixelClusterProducer NearbyPixelClusterProducer.cc Calibration/TkAlCaRecoProducers/plugins/NearbyPixelClusterProducer.cc

 Description: Class to produce the collection of SiPixelClusters closest, hit by hit, to the trajectory measurements of a given track

 Implementation: Implementation is heavily endebted to https://github.com/jkarancs/PhaseIPixelNtuplizer/blob/master/plugins/PhaseIPixelNtuplizer.h

*/
//
// Original Author:  Marco Musich
//         Created:  Mon, 29 Mar 2021 12:29:30 GMT
//
//

// system include files
#include <memory>

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

//
// class declaration
//

class NearbyPixelClusterProducer : public edm::stream::EDProducer<> {
public:
  explicit NearbyPixelClusterProducer(const edm::ParameterSet&);
  ~NearbyPixelClusterProducer() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void produce(edm::Event&, const edm::EventSetup&) override;
  TrajectoryStateOnSurface getTrajectoryStateOnSurface(const TrajectoryMeasurement& measurement);
  bool detidIsOnPixel(const DetId& detid);

  // ----------member data ---------------------------

  const edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> geomEsToken_;
  const edm::ESGetToken<PixelClusterParameterEstimator, TkPixelCPERecord> pixelCPEEsToken_;

  edm::EDGetTokenT<edmNew::DetSetVector<SiPixelCluster>> clustersToken_;
  edm::EDGetTokenT<TrajTrackAssociationCollection> trajTrackCollectionToken_;

  edm::EDPutTokenT<SiPixelClusterCollectionNew> clusterPutToken_;
};

//
// constructors and destructor
//
NearbyPixelClusterProducer::NearbyPixelClusterProducer(const edm::ParameterSet& iConfig)
    : geomEsToken_(esConsumes()),
      pixelCPEEsToken_(esConsumes(edm::ESInputTag("", "PixelCPEGeneric"))),
      clustersToken_(
          consumes<edmNew::DetSetVector<SiPixelCluster>>(iConfig.getParameter<edm::InputTag>("clusterCollection"))),
      trajTrackCollectionToken_(
          consumes<TrajTrackAssociationCollection>(iConfig.getParameter<edm::InputTag>("trajectoryInput"))),
      clusterPutToken_(produces<SiPixelClusterCollectionNew>()) {}

//
// member functions
//

// ------------ method called to produce the data  ------------
void NearbyPixelClusterProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;

  auto outputClusters = std::make_unique<SiPixelClusterCollectionNew>();

  // get the Tracker geometry from event setup
  const TrackerGeometry* trackerGeometry_ = &iSetup.getData(geomEsToken_);

  // get the Pixel CPE from event setup
  const PixelClusterParameterEstimator* pixelClusterParameterEstimator_ = &iSetup.getData(pixelCPEEsToken_);

  // Get cluster collection
  edm::Handle<edmNew::DetSetVector<SiPixelCluster>> clusterCollectionHandle;
  iEvent.getByToken(clustersToken_, clusterCollectionHandle);

  // Get Traj-Track Collection
  edm::Handle<TrajTrackAssociationCollection> trajTrackCollectionHandle;
  iEvent.getByToken(trajTrackCollectionToken_, trajTrackCollectionHandle);
  if (!trajTrackCollectionHandle.isValid())
    return;

  //std::cout << (*trajTrackCollectionHandle).size() << std::endl;

  std::vector<uint32_t> treatedIDs;

  for (const auto& pair : *trajTrackCollectionHandle) {
    const edm::Ref<std::vector<Trajectory>> traj = pair.key;
    const reco::TrackRef track = pair.val;

    for (const TrajectoryMeasurement& measurement : traj->measurements()) {
      //Check if the measurement infos can be read
      if (!measurement.updatedState().isValid())
        return;

      const TransientTrackingRecHit::ConstRecHitPointer& recHit = measurement.recHit();

      // Only looking for pixel hits
      DetId r_rawId = recHit->geographicalId();

      if (!this->detidIsOnPixel(r_rawId))
        continue;

      if (std::find(treatedIDs.begin(), treatedIDs.end(), r_rawId.rawId()) != treatedIDs.end()) {
        continue;
      } else {
        treatedIDs.push_back(r_rawId.rawId());
      }

      // Skipping hits with undeterminable positions
      TrajectoryStateOnSurface trajStateOnSurface = this->getTrajectoryStateOnSurface(measurement);

      if (!(trajStateOnSurface.isValid()))
        continue;

      // Position measurements
      // Looking for valid and missing hits
      LocalPoint localPosition = trajStateOnSurface.localPosition();

      const auto& traj_lx = localPosition.x();
      const auto& traj_ly = localPosition.y();

      const edmNew::DetSetVector<SiPixelCluster>& clusterCollection = *clusterCollectionHandle;
      edmNew::DetSetVector<SiPixelCluster>::const_iterator itClusterSet = clusterCollection.begin();

      float minD = 10000.;

      for (; itClusterSet != clusterCollection.end(); itClusterSet++) {
        DetId detId(itClusterSet->id());
        if (detId.rawId() != r_rawId)
          continue;

        unsigned int subDetId = detId.subdetId();
        if (subDetId != PixelSubdetector::PixelBarrel && subDetId != PixelSubdetector::PixelEndcap) {
          edm::LogError("NearByPixelClusterProducer")
              << "ERROR: not a pixel cluster!!!" << std::endl;  // should not happen
          continue;
        }

        const PixelGeomDetUnit* pixdet = (const PixelGeomDetUnit*)trackerGeometry_->idToDetUnit(detId);
        edmNew::DetSet<SiPixelCluster>::const_iterator itCluster = itClusterSet->begin();

        edmNew::DetSetVector<SiPixelCluster>::FastFiller spc(*outputClusters, detId.rawId());

        edmNew::DetSet<SiPixelCluster>::const_iterator closest = nullptr;

        for (; itCluster != itClusterSet->end(); ++itCluster) {
          LocalPoint lp(itCluster->x(), itCluster->y(), 0.);
          PixelClusterParameterEstimator::ReturnType params =
              pixelClusterParameterEstimator_->getParameters(*itCluster, *pixdet);
          lp = std::get<0>(params);

          float D = sqrt((lp.x() - traj_lx) * (lp.x() - traj_lx) + (lp.y() - traj_ly) * (lp.y() - traj_ly));
          if (D < minD) {
            closest = itCluster;
            minD = D;
            //std::cout << "rawID: " << detId.rawId() <<"( " << traj_lx << "," << traj_ly  << " ) minD: "<< minD << std::endl;
          }
        }  // loop on cluster sets

        if (closest) {
          spc.push_back(*closest);
        }

        if (spc.empty())
          spc.abort();

      }  // loop on all clusters
    }    // loop on trajectory measurements
  }      // loop on trajectories

  iEvent.put(clusterPutToken_, std::move(outputClusters));
}

/*--------------------------------------------------------------------*/
bool NearbyPixelClusterProducer::detidIsOnPixel(const DetId& detid)
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
TrajectoryStateOnSurface NearbyPixelClusterProducer::getTrajectoryStateOnSurface(
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

  edm::LogError("NearbyPixelClusterProducer") << "Error saving traj. measurement data."
                                              << " Trajectory state on surface cannot be determined." << std::endl;

  return TrajectoryStateOnSurface();
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void NearbyPixelClusterProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.setComment(
      "Produces the collection of SiPixelClusters closest, hit by hit, to the trajectory measurements of a given "
      "track");
  desc.add<edm::InputTag>("clusterCollection", edm::InputTag("siPixelClusters"));
  desc.add<edm::InputTag>("trajectoryInput", edm::InputTag("myRefitter"));
  descriptions.addWithDefaultLabel(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(NearbyPixelClusterProducer);
