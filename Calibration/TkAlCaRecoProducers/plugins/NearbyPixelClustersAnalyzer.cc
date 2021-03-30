// -*- C++ -*-
//
// Package:    Calibration/TkAlCaRecoProducers
// Class:      NearbyPixelClustersAnalyzer
//
/**\class NearbyPixelClustersAnalyzer NearbyPixelClustersAnalyzer.cc Calibration/TkAlCaRecoProducers/plugins/NearbyPixelClustersAnalyzer.cc

 Description: Analysis of the closebyPixelClusters collections
*/
//
// Original Author:  Marco Musich
//         Created:  Tue, 30 Mar 2021 09:22:07 GMT
//
//

// system include files
#include <memory>

// user include files
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
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
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
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

class NearbyPixelClustersAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit NearbyPixelClustersAnalyzer(const edm::ParameterSet&);
  ~NearbyPixelClustersAnalyzer() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void beginJob() override;
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override;

  void countClusters(const edm::Handle<edmNew::DetSetVector<SiPixelCluster>>& handle,
                     //const TrackerGeometry* tkGeom_,
                     unsigned int& nClusGlobal);

  bool detidIsOnPixel(const DetId& detid);
  TrajectoryStateOnSurface getTrajectoryStateOnSurface(const TrajectoryMeasurement& measurement);
  std::pair<float, float> findClosestCluster(const edm::Handle<edmNew::DetSetVector<SiPixelCluster>>& handle,
                                             const PixelClusterParameterEstimator* pixelCPE_,
                                             const TrackerGeometry* trackerGeometry_,
                                             uint32_t rawId,
                                             float traj_lx,
                                             float traj_ly);

  // ----------member data ---------------------------
  const edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> geomEsToken_;
  const edm::ESGetToken<PixelClusterParameterEstimator, TkPixelCPERecord> pixelCPEEsToken_;

  edm::EDGetTokenT<edmNew::DetSetVector<SiPixelCluster>> clustersToken_;
  edm::EDGetTokenT<edmNew::DetSetVector<SiPixelCluster>> nearByClustersToken_;
  edm::EDGetTokenT<TrajTrackAssociationCollection> trajTrackCollectionToken_;

  edm::Service<TFileService> fs;

  TH1I* h_nALCARECOClusters;
  TH1I* h_nCloseByClusters;
  TH1F* h_distClosestValid;
  TH1F* h_distClosestMissing;
  TH1F* h_distClosestInactive;
};

//
// constructors and destructor
//
NearbyPixelClustersAnalyzer::NearbyPixelClustersAnalyzer(const edm::ParameterSet& iConfig)
    : geomEsToken_(esConsumes()),
      pixelCPEEsToken_(esConsumes(edm::ESInputTag("", "PixelCPEGeneric"))),
      clustersToken_(
          consumes<edmNew::DetSetVector<SiPixelCluster>>(iConfig.getParameter<edm::InputTag>("clusterCollection"))),
      nearByClustersToken_(consumes<edmNew::DetSetVector<SiPixelCluster>>(
          iConfig.getParameter<edm::InputTag>("nearByClusterCollection"))),
      trajTrackCollectionToken_(
          consumes<TrajTrackAssociationCollection>(iConfig.getParameter<edm::InputTag>("trajectoryInput"))) {
  usesResource(TFileService::kSharedResource);
}

//
// member functions
//

// ------------ method called for each event  ------------
void NearbyPixelClustersAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;

  // get the Tracker geometry from event setup
  const TrackerGeometry* trackerGeometry_ = &iSetup.getData(geomEsToken_);

  // get the Pixel CPE from event setup
  const PixelClusterParameterEstimator* pixelCPE_ = &iSetup.getData(pixelCPEEsToken_);

  // Get cluster collection
  edm::Handle<edmNew::DetSetVector<SiPixelCluster>> clusterCollectionHandle;
  iEvent.getByToken(clustersToken_, clusterCollectionHandle);

  unsigned int nClusGlobal = 0;
  countClusters(clusterCollectionHandle, nClusGlobal);

  h_nALCARECOClusters->Fill(nClusGlobal);
  std::cout << "total ALCARECO clusters: " << nClusGlobal << std::endl;

  // Get nearby cluster collection
  edm::Handle<edmNew::DetSetVector<SiPixelCluster>> nearByClusterCollectionHandle;
  iEvent.getByToken(nearByClustersToken_, /*trackerGeometry_,*/ nearByClusterCollectionHandle);

  unsigned int nNearByClusGlobal = 0;
  countClusters(nearByClusterCollectionHandle, /*trackerGeometry_,*/ nNearByClusGlobal);

  h_nCloseByClusters->Fill(nNearByClusGlobal);
  std::cout << "total close-by clusters: " << nNearByClusGlobal << std::endl;

  // Get Traj-Track Collection
  edm::Handle<TrajTrackAssociationCollection> trajTrackCollectionHandle;
  iEvent.getByToken(trajTrackCollectionToken_, trajTrackCollectionHandle);

  if (!trajTrackCollectionHandle.isValid())
    return;

  for (const auto& pair : *trajTrackCollectionHandle) {
    const edm::Ref<std::vector<Trajectory>> traj = pair.key;
    const reco::TrackRef track = pair.val;

    for (const TrajectoryMeasurement& measurement : traj->measurements()) {
      if (!measurement.updatedState().isValid())
        return;

      const TransientTrackingRecHit::ConstRecHitPointer& recHit = measurement.recHit();

      // Only looking for pixel hits
      DetId r_rawId = recHit->geographicalId();

      if (!this->detidIsOnPixel(r_rawId))
        continue;

      // Skipping hits with undeterminable positions
      TrajectoryStateOnSurface trajStateOnSurface = this->getTrajectoryStateOnSurface(measurement);

      if (!(trajStateOnSurface.isValid()))
        continue;

      // Position measurements
      // Looking for valid and missing hits
      LocalPoint localPosition = trajStateOnSurface.localPosition();

      const auto& traj_lx = localPosition.x();
      const auto& traj_ly = localPosition.y();

      const auto loc = this->findClosestCluster(
          nearByClusterCollectionHandle, pixelCPE_, trackerGeometry_, r_rawId.rawId(), traj_lx, traj_ly);

      float dist = (loc.first != -999.) ? std::sqrt(loc.first * loc.first + loc.second * loc.second) : -0.1;

      if (recHit->getType() == TrackingRecHit::valid) {
        std::cout << "RawID:" << r_rawId.rawId() << " (valid hit), distance: " << dist << std::endl;
        h_distClosestValid->Fill(dist);
      }

      if (recHit->getType() == TrackingRecHit::missing) {
        std::cout << "RawID:" << r_rawId.rawId() << " (missing hit), distance: " << dist << std::endl;
        h_distClosestMissing->Fill(dist);
      }

      if (recHit->getType() == TrackingRecHit::inactive) {
        std::cout << "RawID:" << r_rawId.rawId() << " (inactive hit), distance: " << dist << std::endl;
        h_distClosestInactive->Fill(dist);
      }
    }
  }
}

// ------------ method called once each job just before starting event loop  ------------
void NearbyPixelClustersAnalyzer::beginJob() {
  TFileDirectory ClusterCounts = fs->mkdir("ClusterCounts");
  h_nALCARECOClusters = ClusterCounts.make<TH1I>(
      "h_nALCARECOClusters", "Number of Pixel clusters per event (ALCARECO) ;N_{clusters};events", 20, 0, 20);
  h_nCloseByClusters = ClusterCounts.make<TH1I>(
      "h_nCloseByClusters", "Number of Pixel clusters per event (close-by) ;N_{clusters};events", 20, 0, 20);

  TFileDirectory Distances = fs->mkdir("TrajDistance");
  h_distClosestValid = Distances.make<TH1F>(
      "h_distClosestValid",
      "Distance of Closest cluster to trajectory (valid);distance (cm); valid trajectory measurements",
      110,
      -0.105,
      0.995);
  h_distClosestMissing = Distances.make<TH1F>(
      "h_distClosestMissing",
      "Distance of Closest cluster to trajectory (missing);distance (cm);missing trajectory measurements",
      110,
      -0.105,
      0.995);
  h_distClosestInactive = Distances.make<TH1F>(
      "h_distClosestInactive",
      "Distance of Closest cluster to trajectory (inactive);distance (cm);inactive trajectory measurements",
      110,
      -0.105,
      0.995);
}

// ------------ method called once each job just after ending the event loop  ------------
void NearbyPixelClustersAnalyzer::endJob() {
  // please remove this method if not needed
}

/*--------------------------------------------------------------------*/
bool NearbyPixelClustersAnalyzer::detidIsOnPixel(const DetId& detid)
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
TrajectoryStateOnSurface NearbyPixelClustersAnalyzer::getTrajectoryStateOnSurface(
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

/*--------------------------------------------------------------------*/
void NearbyPixelClustersAnalyzer::countClusters(const edm::Handle<edmNew::DetSetVector<SiPixelCluster>>& handle,
                                                //const TrackerGeometry* tkGeom_,
                                                unsigned int& nClusGlobal)
/*--------------------------------------------------------------------*/
{
  for (const auto& DSVItr : *handle) {
    uint32_t rawid(DSVItr.detId());
    DetId detId(rawid);
    //std::cout << "DetId: "<< detId.rawId() << " size: " <<  DSVItr.size() << std::endl;
    nClusGlobal += DSVItr.size();
  }
}

/*--------------------------------------------------------------------*/
std::pair<float, float> NearbyPixelClustersAnalyzer::findClosestCluster(
    const edm::Handle<edmNew::DetSetVector<SiPixelCluster>>& handle,
    const PixelClusterParameterEstimator* pixelCPE_,
    const TrackerGeometry* trackerGeometry_,
    uint32_t rawId,
    float traj_lx,
    float traj_ly)
/*--------------------------------------------------------------------*/
{
  const edmNew::DetSetVector<SiPixelCluster>& clusterCollection = *handle;
  edmNew::DetSetVector<SiPixelCluster>::const_iterator itClusterSet = clusterCollection.begin();

  float minD = 10000.;

  auto loc = std::make_pair(-999., -999.);

  for (; itClusterSet != clusterCollection.end(); itClusterSet++) {
    DetId detId(itClusterSet->id());
    if (detId.rawId() != rawId)
      continue;

    unsigned int subDetId = detId.subdetId();
    if (subDetId != PixelSubdetector::PixelBarrel && subDetId != PixelSubdetector::PixelEndcap) {
      edm::LogError("NearByPixelClustersAnalyzer")
          << "ERROR: not a pixel cluster!!!" << std::endl;  // should not happen
      continue;
    }

    const PixelGeomDetUnit* pixdet = (const PixelGeomDetUnit*)trackerGeometry_->idToDetUnit(detId);
    edmNew::DetSet<SiPixelCluster>::const_iterator itCluster = itClusterSet->begin();
    for (; itCluster != itClusterSet->end(); ++itCluster) {
      LocalPoint lp(itCluster->x(), itCluster->y(), 0.);
      PixelClusterParameterEstimator::ReturnType params = pixelCPE_->getParameters(*itCluster, *pixdet);
      lp = std::get<0>(params);

      float D = sqrt((lp.x() - traj_lx) * (lp.x() - traj_lx) + (lp.y() - traj_ly) * (lp.y() - traj_ly));
      if (D < minD) {
        minD = D;
        loc.first = (lp.x() - traj_lx);
        loc.second = (lp.y() - traj_ly);
      }
    }  // loop on cluster sets
  }
  return loc;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void NearbyPixelClustersAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.setComment("Analysis of the closebyPixelClusters collections");
  desc.add<edm::InputTag>("clusterCollection", edm::InputTag("ALCARECOSiPixelCalSingleMuonTight"));
  desc.add<edm::InputTag>("nearByClusterCollection", edm::InputTag("closebyPixelClusters"));
  desc.add<edm::InputTag>("trajectoryInput", edm::InputTag("refittedTracks"));
  descriptions.addWithDefaultLabel(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(NearbyPixelClustersAnalyzer);
