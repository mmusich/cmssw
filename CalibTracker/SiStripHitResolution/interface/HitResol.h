#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/DetId/interface/DetIdCollection.h"
#include "DataFormats/GeometryCommonDetAlgo/interface/MeasurementError.h"
#include "DataFormats/GeometryCommonDetAlgo/interface/MeasurementVector.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"
#include "DataFormats/Scalers/interface/LumiScalers.h"
#include "DataFormats/SiStripCluster/interface/SiStripCluster.h"
#include "DataFormats/SiStripDigi/interface/SiStripRawDigi.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripMatchedRecHit2D.h"
#include "DataFormats/TrackingRecHit/interface/TrackingRecHit.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "RecoLocalTracker/ClusterParameterEstimator/interface/StripClusterParameterEstimator.h"
#include "RecoTracker/Record/interface/CkfComponentsRecord.h"
#include "RecoTracker/SingleTrackPattern/interface/CosmicTrajectoryBuilder.h"
#include "TrackingTools/KalmanUpdators/interface/Chi2MeasurementEstimator.h"
#include "TrackingTools/KalmanUpdators/interface/KFUpdator.h"
#include "TrackingTools/MaterialEffects/interface/PropagatorWithMaterial.h"
#include "TrackingTools/PatternTools/interface/TrajTrackAssociation.h"
#include "TrackingTools/TrackFitters/interface/KFTrajectoryFitter.h"
#include "TrackingTools/TrackFitters/interface/KFTrajectorySmoother.h"
#include "TrackingTools/TrajectoryState/interface/TrajectoryStateTransform.h"
#include "TrackingTools/TransientTrackingRecHit/interface/TransientTrackingRecHitBuilder.h"

#include "TRandom2.h"
#include "TTree.h"
#include "TROOT.h"
#include "TFile.h"
#include "TH1F.h"
#include "TH2F.h"

#include <vector>
#include <iostream>
#include <cstdlib>
#include <cstdio>

class TrackerTopology;

class HitResol : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit HitResol(const edm::ParameterSet& conf);
  double checkConsistency(const StripClusterParameterEstimator::LocalValues& parameters, double xx, double xerr);
  bool isDoubleSided(unsigned int iidd, const TrackerTopology* tTopo) const;
  bool check2DPartner(unsigned int iidd, const std::vector<TrajectoryMeasurement>& traj);
  ~HitResol() override = default;
  unsigned int checkLayer(unsigned int iidd, const TrackerTopology* tTopo);
  void getSimHitRes(const GeomDetUnit* det,
                    const LocalVector& trackdirection,
                    const TrackingRecHit& recHit,
                    float& trackWidth,
                    float* pitch,
                    LocalVector& drift);
  double getSimpleRes(const TrajectoryMeasurement* traj1);
  bool getPairParameters(const MagneticField* magField_,
                         AnalyticalPropagator& propagator,
                         const TrajectoryMeasurement* traj1,
                         const TrajectoryMeasurement* traj2,
                         float& pairPath,
                         float& hitDX,
                         float& trackDX,
                         float& trackDXE,
                         float& trackParamX,
                         float& trackParamY,
                         float& trackParamDXDZ,
                         float& trackParamDYDZ,
                         float& trackParamXE,
                         float& trackParamYE,
                         float& trackParamDXDZE,
                         float& trackParamDYDZE);
  typedef std::vector<Trajectory> TrajectoryCollection;

private:
  void beginJob() override;
  void endJob() override;
  void analyze(const edm::Event& e, const edm::EventSetup& c) override;

  // ----------member data ---------------------------
  const edm::EDGetTokenT<LumiScalersCollection> scalerToken_;
  const edm::EDGetTokenT<edm::DetSetVector<SiStripRawDigi> > commonModeToken_;

  bool addLumi_;
  bool addCommonMode_;
  bool cutOnTracks_;
  unsigned int trackMultiplicityCut_;
  bool useFirstMeas_;
  bool useLastMeas_;
  bool useAllHitsFromTracksWithMissingHits_;
  double MomentumCut_;
  unsigned int UsePairsOnly_;

  const edm::EDGetTokenT<reco::TrackCollection> combinatorialTracks_token_;
  const edm::EDGetTokenT<std::vector<Trajectory> > trajectories_token_;
  const edm::EDGetTokenT<TrajTrackAssociationCollection> trajTrackAsso_token_;
  const edm::EDGetTokenT<std::vector<Trajectory> > tjToken_;
  const edm::EDGetTokenT<reco::TrackCollection> tkToken_;
  const edm::EDGetTokenT<edmNew::DetSetVector<SiStripCluster> > clusters_token_;
  const edm::EDGetTokenT<DetIdCollection> digis_token_;
  const edm::EDGetTokenT<MeasurementTrackerEvent> trackerEvent_token_;

  // ES tokens
  const edm::ESGetToken<TrackerTopology, TrackerTopologyRcd> topoToken_;
  const edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> geomToken_;
  const edm::ESGetToken<StripClusterParameterEstimator, TkStripCPERecord> cpeToken_;
  const edm::ESGetToken<SiStripQuality, SiStripQualityRcd> siStripQualityToken_;
  const edm::ESGetToken<MagneticField, IdealMagneticFieldRecord> magFieldToken_;
  const edm::ESGetToken<MeasurementTracker, CkfComponentsRecord> measurementTkToken_;
  const edm::ESGetToken<Chi2MeasurementEstimatorBase, TrackingComponentsRecord> chi2MeasurementEstimatorToken_;
  const edm::ESGetToken<Propagator, TrackingComponentsRecord> propagatorToken_;

  edm::ParameterSet conf_;

  TTree* reso;
  TTree* treso;

  int events, EventTrackCKF;

  int compSettings;
  unsigned int layers;
  bool DEBUG;
  unsigned int whatlayer;

  double MomentumCut;

  // Tree declarations
  // Hit Resolution Ntuple Content
  float mymom;
  int numHits;
  float ProbTrackChi2;
  unsigned int iidd1;
  float mypitch1;
  unsigned int clusterWidth;
  float expWidth;
  float atEdge;
  float simpleRes;
  unsigned int iidd2;
  unsigned int clusterWidth_2;
  float expWidth_2;
  float atEdge_2;
  float pairPath;
  float hitDX;
  float trackDX;
  float trackDXE;
  float trackParamX;
  float trackParamY;
  float trackParamDXDZ;
  float trackParamDYDZ;
  float trackParamXE;
  float trackParamYE;
  float trackParamDXDZE;
  float trackParamDYDZE;
  unsigned int pairsOnly;
  float track_momentum;
  float track_eta;
  float track_trackChi2;
};

//#endif
