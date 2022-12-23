#ifndef DQM_TrackingMonitorSource_StandaloneTrackMonitor_h
#define DQM_TrackingMonitorSource_StandaloneTrackMonitor_h

#include <string>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <fstream>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "DQMServices/Core/interface/DQMStore.h"
#include "DQMServices/Core/interface/MonitorElement.h"
#include "DQMServices/Core/interface/DQMEDAnalyzer.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "DataFormats/JetReco/interface/PFJet.h"

class BeamSpot;
class TrackCollection;
class VertexCollection;
class TrackingRecHit;

class StandaloneTrackMonitor : public DQMEDAnalyzer {
public:
  StandaloneTrackMonitor(const edm::ParameterSet&);
  using MVACollection = std::vector<float>;
  using QualityMaskCollection = std::vector<unsigned char>;

protected:
  void analyze(edm::Event const& iEvent, edm::EventSetup const& iSetup) override;
  //  void endLuminosityBlock(edm::LuminosityBlock const& lumiSeg, edm::EventSetup const& eSetup);// override;
  void processHit(const TrackingRecHit& recHit,
                  edm::EventSetup const& iSetup,
                  const TrackerGeometry& tkGeom,
                  double wfac = 1);
  void processClusters(edm::Event const& iEvent,
                       edm::EventSetup const& iSetup,
                       const TrackerGeometry& tkGeom,
                       double wfac = 1);
  void addClusterToMap(uint32_t detid, const SiStripCluster* cluster);
  void bookHistograms(DQMStore::IBooker&, edm::Run const&, edm::EventSetup const&) override;
  void dqmBeginRun(const edm::Run& iRun, const edm::EventSetup& iSetup) override;
  void endJob();

private:
  edm::ParameterSet parameters_;

  std::string moduleName_;
  std::string folderName_;
  std::ifstream bpixfile_;
  std::vector<unsigned int> runs_;
  std::vector<float> bpix_X_, bpix_Y_, bpix_Z_;
  float bpix_x_ = 0, bpix_y_ = 0, bpix_z_ = 0;

  SiStripClusterInfo siStripClusterInfo_;

  const edm::InputTag trackTag_;
  const edm::InputTag bsTag_;
  const edm::InputTag vertexTag_;
  const edm::InputTag puSummaryTag_;
  const edm::InputTag clusterTag_;
  const edm::InputTag jetsTag_;
  const edm::EDGetTokenT<reco::TrackCollection> trackToken_;
  const edm::EDGetTokenT<reco::BeamSpot> bsToken_;
  const edm::EDGetTokenT<reco::VertexCollection> vertexToken_;
  const edm::EDGetTokenT<std::vector<PileupSummaryInfo> > puSummaryToken_;
  const edm::EDGetTokenT<edmNew::DetSetVector<SiStripCluster> > clusterToken_;
  const edm::EDGetTokenT<std::vector<reco::PFJet> > jetsToken_;
  // track MVA
  const std::string trackQuality_;
  const bool doPUCorrection_;
  const bool doTrackCorrection_;
  const bool isMC_;
  const bool haveAllHistograms_;
  const std::string puScaleFactorFile_;
  const std::string trackScaleFactorFile_;
  const std::vector<std::string> mvaProducers_;
  const edm::InputTag mvaTrackTag_;
  edm::EDGetTokenT<edm::View<reco::Track> > mvaTrackToken_;
  const edm::InputTag tcProducer_;
  const std::string algoName_;

  int nevt = 0;
  int chi2it = 0, chi2itGt = 0, chi2itLt = 0;
  const bool verbose_;
  std::vector<std::tuple<edm::EDGetTokenT<MVACollection>, edm::EDGetTokenT<QualityMaskCollection> > > mvaQualityTokens_;
  std::string histname;
  const edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> geomToken_;
  const edm::ESGetToken<TransientTrackBuilder, TransientTrackRecord> transTrackToken_;
  const TrackerGeometry* tkGeom_ = nullptr;

  MonitorElement* trackEtaH_;
  MonitorElement* trackEtaerrH_;
  //MonitorElement* trackCosThetaH_;
  //MonitorElement* trackThetaerrH_;
  MonitorElement* trackPhiH_;
  MonitorElement* trackPhierrH_;
  MonitorElement* trackPH_;
  MonitorElement* trackPtH_;
  MonitorElement* trackPt_ZoomH_;
  MonitorElement* trackPtUpto2GeVH_;
  MonitorElement* trackPtOver10GeVH_;
  MonitorElement* trackPterrH_;
  MonitorElement* trackqOverpH_;
  MonitorElement* trackqOverperrH_;
  MonitorElement* trackChargeH_;
  MonitorElement* trackChi2H_;
  MonitorElement* tracknDOFH_;
  MonitorElement* trackChi2ProbH_;
  //MonitorElement* trackChi2ProbTestH_;
  //MonitorElement* trackChi2ProbGtCutH_;
  /*  MonitorElement* trackChi2ProbGtLCut1H_;
  MonitorElement* trackChi2ProbGtLCut2H_;
  MonitorElement* trackChi2ProbGtLCut3H_;
  MonitorElement* trackChi2ProbGtLCut4H_;
  MonitorElement* trackChi2ProbZoomedH_;
  MonitorElement* trackChi2Prob_ptGt3H_;
  MonitorElement* trackChi2Prob_ptGt10H_;
  MonitorElement* trackChi2Prob_LHlt8H_;*/
  MonitorElement* trackChi2oNDFH_;
  MonitorElement* trackd0H_;
  MonitorElement* trackChi2bynDOFH_;
  MonitorElement* trackalgoH_;
  MonitorElement* trackorigalgoH_;
  MonitorElement* trackStoppingSourceH_;

  MonitorElement* DistanceOfClosestApproachToPVH_;
  MonitorElement* DistanceOfClosestApproachToPVZoomedH_;
  MonitorElement* DistanceOfClosestApproachToPVVsPhiH_;
  MonitorElement* xPointOfClosestApproachVsZ0wrtPVH_;
  MonitorElement* yPointOfClosestApproachVsZ0wrtPVH_;
  MonitorElement* trackDeltaRwrtClosestTrack_;

  MonitorElement* ip2dToPVH_;
  MonitorElement* iperr2dToPVH_;

  MonitorElement* ip3dToBSH_;
  MonitorElement* iperr3dToBSH_;
  MonitorElement* iperr3dToBSWtH_;
  MonitorElement* iperr2dToBSH_;
  MonitorElement* iperr2dToPVWtH_;

  MonitorElement* ip2dToBSH_;
  MonitorElement* sip2dToBSH_;

  MonitorElement* ip3dToPVH_;
  MonitorElement* iperr3dToPVH_;
  //MonitorElement* iperr3dToPVEta1H_;
  //MonitorElement* iperr3dToPVEta2H_;
  //MonitorElement* iperr3dToPVEta3H_;
  //MonitorElement* iperr3dToPVGtChi2CutH_;
  MonitorElement* iperr3dToPVWtH_;
  MonitorElement* sip3dToPVH_;
  MonitorElement* sip3dToBSH_;
  MonitorElement* sip2dToPVH_;
  //MonitorElement* sip2dToPVEta1H_;
  //MonitorElement* sip2dToPVEta2H_;
  //MonitorElement* sip2dToPVEta3H_;
  //MonitorElement* sip2dToPVGtChi2CutH_;
  MonitorElement* sip2dToPVWtH_;
  MonitorElement* sipDxyToPVH_;
  MonitorElement* sipDzToPVH_;

  MonitorElement* nallHitsH_;
  MonitorElement* ntrackerHitsH_;

  MonitorElement* nvalidTrackerHitsH_;
  MonitorElement* nvalidPixelHitsH_;
  MonitorElement* nvalidPixelBHitsH_;
  MonitorElement* nvalidPixelEHitsH_;
  MonitorElement* nvalidStripHitsH_;
  MonitorElement* nvalidTIBHitsH_;
  MonitorElement* nvalidTOBHitsH_;
  MonitorElement* nvalidTIDHitsH_;
  MonitorElement* nvalidTECHitsH_;

  MonitorElement* nlostTrackerHitsH_;
  MonitorElement* nlostPixelHitsH_;
  MonitorElement* nlostPixelBHitsH_;
  MonitorElement* nlostPixelEHitsH_;
  MonitorElement* nlostStripHitsH_;
  MonitorElement* nlostTIBHitsH_;
  MonitorElement* nlostTOBHitsH_;
  MonitorElement* nlostTIDHitsH_;
  MonitorElement* nlostTECHitsH_;

  MonitorElement* nMissingInnerHitBH_;
  MonitorElement* nMissingInnerHitEH_;
  MonitorElement* nMissingOuterHitBH_;
  MonitorElement* nMissingOuterHitEH_;

  /*  MonitorElement* residualXPBH_;
  MonitorElement* residualXPEH_;
  MonitorElement* residualXTIBH_;
  MonitorElement* residualXTOBH_;
  MonitorElement* residualXTIDH_;
  MonitorElement* residualXTECH_;
  MonitorElement* residualYPBH_;
  MonitorElement* residualYPEH_;
  MonitorElement* residualYTIBH_;
  MonitorElement* residualYTOBH_;
  MonitorElement* residualYTIDH_;
  MonitorElement* residualYTECH_;*/

  MonitorElement* trkLayerwithMeasurementH_;
  MonitorElement* pixelLayerwithMeasurementH_;
  MonitorElement* pixelBLayerwithMeasurementH_;
  MonitorElement* pixelELayerwithMeasurementH_;
  MonitorElement* stripLayerwithMeasurementH_;
  MonitorElement* stripTIBLayerwithMeasurementH_;
  MonitorElement* stripTOBLayerwithMeasurementH_;
  MonitorElement* stripTIDLayerwithMeasurementH_;
  MonitorElement* stripTECLayerwithMeasurementH_;

  MonitorElement* nlostHitsH_;

  MonitorElement* beamSpotXYposH_;
  MonitorElement* beamSpotXYposerrH_;
  MonitorElement* beamSpotZposH_;
  MonitorElement* beamSpotZposerrH_;

  MonitorElement* vertexXposH_;
  MonitorElement* vertexYposH_;
  MonitorElement* vertexZposH_;
  MonitorElement* nVertexH_;
  MonitorElement* nVtxH_;

  MonitorElement* nTracksH_;

  // MC only
  MonitorElement* bunchCrossingH_;
  MonitorElement* nPUH_;
  MonitorElement* trueNIntH_;

  // Exclusive Quantities
  MonitorElement* nLostHitByLayerH_;
  MonitorElement* nLostHitByLayerPixH_;
  MonitorElement* nLostHitByLayerStripH_;
  MonitorElement* nLostHitsVspTH_;
  MonitorElement* nLostHitsVsEtaH_;
  MonitorElement* nLostHitsVsCosThetaH_;
  MonitorElement* nLostHitsVsPhiH_;
  MonitorElement* nLostHitsVsIterationH_;

  MonitorElement* nHitsTIBSVsEtaH_;
  MonitorElement* nHitsTOBSVsEtaH_;
  MonitorElement* nHitsTECSVsEtaH_;
  MonitorElement* nHitsTIDSVsEtaH_;
  MonitorElement* nHitsStripSVsEtaH_;

  MonitorElement* nHitsTIBDVsEtaH_;
  MonitorElement* nHitsTOBDVsEtaH_;
  MonitorElement* nHitsTECDVsEtaH_;
  MonitorElement* nHitsTIDDVsEtaH_;
  MonitorElement* nHitsStripDVsEtaH_;

  MonitorElement* nValidHitsVspTH_;
  MonitorElement* nValidHitsVsnVtxH_;
  MonitorElement* nValidHitsVsEtaH_;
  MonitorElement* nValidHitsVsCosThetaH_;
  MonitorElement* nValidHitsVsPhiH_;

  MonitorElement* nValidHitsPixVsEtaH_;
  MonitorElement* nValidHitsPixBVsEtaH_;
  MonitorElement* nValidHitsPixEVsEtaH_;
  MonitorElement* nValidHitsStripVsEtaH_;
  MonitorElement* nValidHitsTIBVsEtaH_;
  MonitorElement* nValidHitsTOBVsEtaH_;
  MonitorElement* nValidHitsTECVsEtaH_;
  MonitorElement* nValidHitsTIDVsEtaH_;

  MonitorElement* nValidHitsPixVsPhiH_;
  MonitorElement* nValidHitsPixBVsPhiH_;
  MonitorElement* nValidHitsPixEVsPhiH_;
  MonitorElement* nValidHitsStripVsPhiH_;
  MonitorElement* nValidHitsTIBVsPhiH_;
  MonitorElement* nValidHitsTOBVsPhiH_;
  MonitorElement* nValidHitsTECVsPhiH_;
  MonitorElement* nValidHitsTIDVsPhiH_;

  MonitorElement* nLostHitsPixVsEtaH_;
  MonitorElement* nLostHitsPixBVsEtaH_;
  MonitorElement* nLostHitsPixEVsEtaH_;
  MonitorElement* nLostHitsStripVsEtaH_;
  MonitorElement* nLostHitsTIBVsEtaH_;
  MonitorElement* nLostHitsTOBVsEtaH_;
  MonitorElement* nLostHitsTECVsEtaH_;
  MonitorElement* nLostHitsTIDVsEtaH_;

  MonitorElement* nLostHitsPixVsIterationH_;
  MonitorElement* nLostHitsPixBVsIterationH_;
  MonitorElement* nLostHitsPixEVsIterationH_;
  MonitorElement* nLostHitsStripVsIterationH_;
  MonitorElement* nLostHitsTIBVsIterationH_;
  MonitorElement* nLostHitsTOBVsIterationH_;
  MonitorElement* nLostHitsTECVsIterationH_;
  MonitorElement* nLostHitsTIDVsIterationH_;

  MonitorElement* nLostHitsPixVsPhiH_;
  MonitorElement* nLostHitsPixBVsPhiH_;
  MonitorElement* nLostHitsPixEVsPhiH_;
  MonitorElement* nLostHitsStripVsPhiH_;
  MonitorElement* nLostHitsTIBVsPhiH_;
  MonitorElement* nLostHitsTOBVsPhiH_;
  MonitorElement* nLostHitsTECVsPhiH_;
  MonitorElement* nLostHitsTIDVsPhiH_;

  MonitorElement* trackChi2oNDFVsEtaH_;
  MonitorElement* trackChi2oNDFVsPhiH_;
  MonitorElement* trackChi2probVsEtaH_;
  MonitorElement* trackChi2probVsPhiH_;

  /*  MonitorElement* trackChi2probVsPtH_;
  MonitorElement* trackChi2probVsnHitsH_;
  MonitorElement* trackChi2probVsnTrackerHitsH_;
  MonitorElement* trackChi2probVsEta2DH_;
  MonitorElement* trackChi2probVsPhi2DH_;
  MonitorElement* trackChi2probVsPt2DH_;
  MonitorElement* trackChi2probVsnHits2DH_;
  MonitorElement* trackChi2probVsnTrackerHits2DH_;
  MonitorElement* trackChi2probVsnValidHits2DH_;
  MonitorElement* trackChi2probVsnLostHits2DH_;
  MonitorElement* trackChi2probVsnMissingInnerHits2DH_;
  MonitorElement* trackChi2probVsnMissingOuterHits2DH_;

  MonitorElement* trackChi2probVsAlgo2DH_;
  MonitorElement* trackChi2probVsOrigAlgo2DH_;
  MonitorElement* trackChi2probVsStoppingSource2DH_;*/

  MonitorElement* trackIperr3dVsEtaH_;
  //MonitorElement* trackIperr3dVsPtH_;
  MonitorElement* trackIperr3dVsChi2probH_;
  //MonitorElement* trackIperr3dVsnHitsH_;
  //MonitorElement* trackIperr3dVsnValidHitsH_;
  //MonitorElement* trackIperr3dVsnLostHitsH_;

  MonitorElement* trackSip2dVsEtaH_;
  //MonitorElement* trackSip2dVsPtH_;
  //MonitorElement* trackSip2dVsChi2probH_;
  //MonitorElement* trackSip2dVsnHitsH_;
  //MonitorElement* trackSip2dVsnValidHitsH_;
  //MonitorElement* trackSip2dVsnLostHitsH_;

  MonitorElement* trackIperr3dVsEta2DH_;
  //MonitorElement* trackIperr3dVsPt2DH_;
  MonitorElement* trackIperr3dVsChi2prob2DH_;
  //MonitorElement* trackIperr3dVsnHits2DH_;
  //MonitorElement* trackIperr3dVsnValidHits2DH_;
  //MonitorElement* trackIperr3dVsnLostHits2DH_;

  MonitorElement* trackSip2dVsEta2DH_;
  //MonitorElement* trackSip2dVsPt2DH_;
  MonitorElement* trackSip2dVsChi2prob2DH_;
  //MonitorElement* trackSip2dVsnHits2DH_;
  //MonitorElement* trackSip2dVsnValidHits2DH_;
  //MonitorElement* trackSip2dVsnLostHits2DH_;

  MonitorElement* hOnTrkClusChargeThinH_;
  MonitorElement* hOnTrkClusWidthThinH_;
  MonitorElement* hOnTrkClusChargeThickH_;
  MonitorElement* hOnTrkClusWidthThickH_;

  MonitorElement* hOffTrkClusChargeThinH_;
  MonitorElement* hOffTrkClusWidthThinH_;
  MonitorElement* hOffTrkClusChargeThickH_;
  MonitorElement* hOffTrkClusWidthThickH_;

  std::vector<MonitorElement*> trackMVAs;
  std::vector<MonitorElement*> trackMVAsHP;
  std::vector<MonitorElement*> trackMVAsVsPtProfile;
  std::vector<MonitorElement*> trackMVAsHPVsPtProfile;
  std::vector<MonitorElement*> trackMVAsVsEtaProfile;
  std::vector<MonitorElement*> trackMVAsHPVsEtaProfile;

  MonitorElement* nJet_;
  MonitorElement* Jet_pt_;
  MonitorElement* Jet_eta_;
  MonitorElement* Jet_energy_;
  MonitorElement* Jet_chargedMultiplicity_;

  MonitorElement* Zpt_;
  MonitorElement* ZInvMass_;

  unsigned long long m_cacheID_;

  std::vector<int> lumivec1;
  std::vector<int> lumivec2;
  std::vector<float> vpu_;
  std::vector<float> vtrack_;
  std::map<uint32_t, std::set<const SiStripCluster*> > clusterMap_;
};
#endif
