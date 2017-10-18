// -*- C++ -*-
//
// Package:    CalibTracker/SiStripHitResolution
// Class:      SiStripHitResolution
// 
/**\class CalibTracker/SiStripHitResolution SiStripHitResolution.cc CalibTracker/SiStripHitResolution/plugins/SiStripHitResolution.cc

   Description: <one line class summary>
   Use overlaps in TIF cosmics data to evaluate hit resolution   
*/
//
// Original Authors:  Wolfgang Adam, Keith Ulmer
//          Created:  Thu Oct 11 14:53:32 CEST 2007
// Adapted by:        Nicola De Filippis            
// Updated by:        Marco Musich
//
// $Id: SiStripHitResolution.cc,v 1.18 2010/05/19 15:31:58 speer Exp $
//

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "CommonTools/Statistics/interface/ChiSquaredProbability.h"
#include "FWCore/ParameterSet/interface/FileInPath.h"
#include "CalibTracker/SiStripCommon/interface/SiStripDetInfoFileReader.h"

#include "Geometry/TrackerGeometryBuilder/interface/PixelGeomDetUnit.h"
#include "Geometry/TrackerGeometryBuilder/interface/PixelGeomDetType.h"
#include "Geometry/CommonDetUnit/interface/GeomDetType.h"
#include "Geometry/CommonTopologies/interface/PixelTopology.h"

#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackExtra.h"
#include "DataFormats/TrackReco/interface/TrackExtraFwd.h"
#include "DataFormats/TrackingRecHit/interface/TrackingRecHit.h"
#include "DataFormats/SiStripDetId/interface/StripSubdetector.h"
#include "DataFormats/DetId/interface/DetId.h" 
#include "DataFormats/SiStripDetId/interface/TIBDetId.h"
#include "DataFormats/SiStripDetId/interface/TOBDetId.h"
#include "DataFormats/SiStripDetId/interface/TIDDetId.h"
#include "DataFormats/SiStripDetId/interface/TECDetId.h"
#include "DataFormats/SiPixelDetId/interface/PXBDetId.h"
#include "DataFormats/SiPixelDetId/interface/PXFDetId.h"
#include "Geometry/CommonDetUnit/interface/GeomDet.h"
#include "TrackingTools/PatternTools/interface/Trajectory.h"
#include "TrackingTools/TransientTrackingRecHit/interface/TransientTrackingRecHit.h"
#include "RecoTracker/TransientTrackingRecHit/interface/TSiStripMatchedRecHit.h"
#include "RecoTracker/TransientTrackingRecHit/interface/ProjectedRecHit2D.h"
#include "SimDataFormats/TrackingHit/interface/PSimHit.h"
#include "SimTracker/TrackerHitAssociation/interface/TrackerHitAssociator.h"

#include "TrackingTools/GeomPropagators/interface/AnalyticalPropagator.h"
#include "TrackingTools/AnalyticalJacobians/interface/JacobianLocalToCurvilinear.h"
#include "TrackingTools/AnalyticalJacobians/interface/JacobianCurvilinearToLocal.h"
#include "TrackingTools/AnalyticalJacobians/interface/AnalyticalCurvilinearJacobian.h"
#include "TrackingTools/TrackFitters/interface/TrajectoryStateCombiner.h"
#include "DataFormats/GeometryVector/interface/LocalPoint.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"

#include "RecoLocalTracker/Records/interface/TkStripCPERecord.h"

#include "TFile.h"
#include "TTree.h"
#include "TMath.h"

#include <vector>
#include <utility>

using namespace std;


class SiStripHitResolution : public edm::EDAnalyzer {
public:
  typedef vector<Trajectory> TrajectoryCollection;
  typedef vector<reco::Track> TrackCollection;
  
  explicit SiStripHitResolution(const edm::ParameterSet&);
  ~SiStripHitResolution();

private:
  typedef TransientTrackingRecHit::ConstRecHitPointer ConstRecHitPointer;
  void load(const edm::Event& iEvent, const edm::EventSetup& iSetup);
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;

  void getHitParameters(const TransientTrackingRecHit::ConstRecHitPointer& hit, const LocalVector& trackDirection, unsigned int * detID, unsigned int * clusterWidth, float * expWidth, float * res, bool * atEdge, float *pitch);
  float getSimHitRes(const GeomDetUnit * det, const LocalVector& trackdirection, const TrackingRecHit& recHit, float * trackWidth, float *pitch);
  double getSimpleRes(const TrajectoryMeasurement* traj1);
  bool getPairParameters(const TrajectoryMeasurement* traj1, const TrajectoryMeasurement* traj2, float * pairPath, float * hitDX, float * trackDX, float * trackDXE,
      float * trackParamX, float *trackParamY , float * trackParamDXDZ, float *trackParamDYDZ , float * trackParamXE, float *trackParamYE, float * trackParamDXDZE, float *trackParamDYDZE);
  int layerFromId (const DetId&) const;

  // ----------member data ---------------------------
  edm::ParameterSet config_;
  edm::InputTag trackTag_;
  SiStripDetInfoFileReader* reader;
  const TrackerGeometry* trackerGeometry_;
  const MagneticField* magField_;
  const TrajectoryCollection* trajectoryCollection;
  const vector<reco::Track>*  tracks;
  edm::ESHandle < StripClusterParameterEstimator > stripcpe;
  
  TrackerHitAssociator::Config* helper;
  TrackerHitAssociator* associator;
  AnalyticalPropagator * propagator;
  TrajectoryStateCombiner combiner_;

  edm::EDGetTokenT< edm::DetSetVector<StripDigiSimLink> > stripdigi_token_;
  edm::EDGetTokenT<TrackCollection> tkToken_;
  edm::EDGetTokenT<TrajectoryCollection> tjToken_;
 
  edm::FileInPath FileInPath_;
  TTree* rootTree_;
  bool   genTruth;
  bool   pairsOnly;
  double minMomentum;

  float        momentum;
  int          numHits;
  float        trackChi2;
  unsigned int detID1;
  float        pitch;
  unsigned int clusterW1;
  float        expectedW1;
  float        trueRes;
  bool         atEdge1;
  float        simpleRes;
  unsigned int detID2;
  unsigned int clusterW2;
  float        expectedW2;
  bool         atEdge2;
  float        pairPath;
  float        hitDX;
  float        trackDX;
  float        trackDXE;

  float        trackParamX    ;
  float        trackParamY    ;
  float        trackParamDXDZ ;
  float        trackParamDYDZ ;
  float        trackParamXE   ;
  float        trackParamYE   ;
  float        trackParamDXDZE;
  float        trackParamDYDZE;

  TTree*       rootTrackTree_;
  float        track_momentum;
  float        track_eta;
  float        track_trackChi2;
  float        track_trackChi2_2;

};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

using std::vector;
using std::cout;
using std::endl;
//
// constructors and destructor
//
SiStripHitResolution::SiStripHitResolution(const edm::ParameterSet& iConfig) :
  config_(iConfig),
  trackerGeometry_(0),
  magField_(0),
  associator(0),
  propagator(0),
  FileInPath_("CalibTracker/SiStripCommon/data/SiStripDetInfo.dat"),
  rootTree_(0),
  genTruth(iConfig.getParameter<bool>("genTruth")),
  pairsOnly(iConfig.getParameter<bool>("pairsOnly")),
  minMomentum(iConfig.getParameter<double>("minMomentum"))
{
  tjToken_=consumes<TrajectoryCollection>(iConfig.getParameter<edm::InputTag>("trajectories"));
  tkToken_=consumes<TrackCollection>(iConfig.getParameter<edm::InputTag>("tracks"));
  stripdigi_token_=consumes< edm::DetSetVector<StripDigiSimLink> >(iConfig.getParameter<edm::InputTag>("stripSimLinkSrc"));
  helper= new TrackerHitAssociator::Config(config_,consumesCollector());

  //now do what ever initialization is needed
  trackTag_ = iConfig.getParameter<edm::InputTag>("tracks");
  reader=new SiStripDetInfoFileReader(FileInPath_.fullPath());
 
  edm::Service<TFileService> fs;
  //
  // root output
  //
  rootTree_ = fs->make<TTree>("hits","Hits");
  rootTree_->Branch("momentum"  ,&momentum  ,"momentum/F");
  rootTree_->Branch("numHits"   ,&numHits   ,"numHits/I");
  rootTree_->Branch("trackChi2" ,&trackChi2 ,"trackChi2/F");
  rootTree_->Branch("detID1"    ,&detID1    ,"detID1/i");
  rootTree_->Branch("ptich1"    ,&pitch     ,"pitch1/F");
  rootTree_->Branch("clusterW1" ,&clusterW1 ,"clusterW1/i");
  rootTree_->Branch("expectedW1",&expectedW1,"expectedW1/F");
  if(genTruth)
    rootTree_->Branch("trueRes1"  ,&trueRes ,"trueRes1/F");
  rootTree_->Branch("atEdge1"   ,&atEdge1   ,"atEdge1/O");
  rootTree_->Branch("simpleRes1",&simpleRes ,"simpleRes1/F");
  rootTree_->Branch("detID2"    ,&detID2    ,"detID2/i");
  rootTree_->Branch("clusterW2" ,&clusterW2 ,"clusterW2/i");
  rootTree_->Branch("expectedW2",&expectedW2,"expectedW2/F");
  rootTree_->Branch("atEdge2"   ,&atEdge2   ,"atEdge2/O");
  rootTree_->Branch("pairPath"  ,&pairPath  ,"pairPath/F");
  rootTree_->Branch("hitDX"     ,&hitDX     ,"hitDX/F");
  rootTree_->Branch("trackDX"   ,&trackDX   ,"trackDX/F");
  rootTree_->Branch("trackDXE"  ,&trackDXE  ,"trackDXE/F");

  rootTree_->Branch("trackParamX"    ,&trackParamX      ,"trackParamX/F");
  rootTree_->Branch("trackParamY"    ,&trackParamY      ,"trackParamY/F");
  rootTree_->Branch("trackParamDXDZ" ,&trackParamDXDZ   ,"trackParamDXDZ/F");
  rootTree_->Branch("trackParamDYDZ" ,&trackParamDYDZ   ,"trackParamDYDZ/F");
  rootTree_->Branch("trackParamXE"   ,&trackParamXE     ,"trackParamXE/F");
  rootTree_->Branch("trackParamYE"   ,&trackParamYE     ,"trackParamYE/F");
  rootTree_->Branch("trackParamDXDZE",&trackParamDXDZE  ,"trackParamDXDZE/F");
  rootTree_->Branch("trackParamDYDZE",&trackParamDYDZE  ,"trackParamDYDZE/F");


  rootTrackTree_ = fs->make<TTree>("tracks","Tracks");
  rootTrackTree_->Branch("momentum"  ,&track_momentum  ,"momentum/F");
  rootTrackTree_->Branch("trackChi2" ,&track_trackChi2 ,"trackChi2/F");
  rootTrackTree_->Branch("trackChi2_2" ,&track_trackChi2_2 ,"trackChi2_2/F");
  rootTrackTree_->Branch("eta" ,&track_eta ,"eta/F");
   
}


SiStripHitResolution::~SiStripHitResolution()
{
}

//
// member functions
//

void SiStripHitResolution::load(const edm::Event& iEvent, const edm::EventSetup& iSetup){
  using namespace edm;

  //
  // mag field & search tracker
  //
  edm::ESHandle<MagneticField> magFieldHandle;
  iSetup.get<IdealMagneticFieldRecord>().get(magFieldHandle);
  magField_ = magFieldHandle.product();
  //
  // propagator
  //
  propagator = new AnalyticalPropagator(magField_,anyDirection);

  //CPE
  iSetup.get < TkStripCPERecord > ().get("SimpleStripCPE", stripcpe);
  //

  //
  // geometry
  //
  edm::ESHandle<TrackerGeometry> geometryHandle;
  iSetup.get<TrackerDigiGeometryRecord>().get(geometryHandle);
  trackerGeometry_ = geometryHandle.product();
  //
  // make associator for SimHits
  //
  if(genTruth)
    associator = new TrackerHitAssociator(iEvent, *helper);

  //
  // trajectories (from refit)
  //

  edm::Handle<TrajectoryCollection> trajectoryCollectionHandle;
  iEvent.getByToken(tjToken_,trajectoryCollectionHandle);
  trajectoryCollection = trajectoryCollectionHandle.product();

  edm::Handle<vector<reco::Track>> tracksHandle;
  iEvent.getByToken(tkToken_,tracksHandle);
  tracks = tracksHandle.product();
}

// ------------ method called to for each event  ------------
void
SiStripHitResolution::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  load(iEvent,iSetup);

  for(unsigned int iT = 0; iT < tracks->size(); ++iT){
    track_momentum = tracks->at(iT).pt();
    track_eta = tracks->at(iT).eta();
    track_trackChi2   = ChiSquaredProbability((double)( tracks->at(iT).chi2() ),(double)( tracks->at(iT).ndof() ));
    track_trackChi2_2 = TMath::Prob(tracks->at(iT).chi2(),(int)tracks->at(iT).ndof());
    
    rootTrackTree_->Fill();
  }


  // loop over trajectories from refit
  for ( TrajectoryCollection::const_iterator it=trajectoryCollection->begin();
  it!=trajectoryCollection->end(); ++it ){
    
    vector < TrajectoryMeasurement > tmColl = it->measurements(); // vector of the hits along the fitted track
    for (vector < TrajectoryMeasurement >::const_iterator itTraj = tmColl.begin();
         itTraj != tmColl.end(); itTraj++) {
       if (!itTraj->updatedState().isValid())
          continue;

       //Let's begin with track parameters!
       momentum  = itTraj->updatedState().globalMomentum().perp();
       numHits   = it->foundHits();
       trackChi2 = ChiSquaredProbability((double)( it->chiSquared() ),(double)( it->ndof(false) ));

      if (momentum < minMomentum) continue;

      //Now for the first hit
      TrajectoryStateOnSurface tsos = itTraj->updatedState();
      LocalVector trackDirection = tsos.localDirection();
      const TransientTrackingRecHit::ConstRecHitPointer hit1 = itTraj->recHit();
      if (!hit1->isValid()) continue;
      DetId id1 = hit1->geographicalId();
      if(id1.subdetId() < StripSubdetector::TIB || id1.subdetId() > StripSubdetector::TEC) continue;

      // passing hit1, trackDirection  // computing detID1, cluster width, expected cluster width/track width , trueres., atedge, pitch
      getHitParameters(hit1,trackDirection,&detID1,&clusterW1,&expectedW1,&trueRes,&atEdge1,&pitch); // passing hit1, trackDirection  
      simpleRes = getSimpleRes(&(*itTraj)); // simple resolution by using the track re-fit forward and backward predicted state

      // Now to see if there is a match - pair method - hit in overlapping sensors
      vector < TrajectoryMeasurement >::const_iterator itTraj2 =  tmColl.end(); // last hit along the fitted track

      for (vector<TrajectoryMeasurement>::const_iterator itmCompare = itTraj-1;  // start to compare from the 5th hit
           itmCompare >= tmColl.begin() &&  itmCompare > itTraj - 4;
           --itmCompare){
        const TransientTrackingRecHit::ConstRecHitPointer hit2 = itmCompare->recHit();
        if (!hit2->isValid()) continue;
        DetId id2 = hit2->geographicalId();
	
        //must be from the same detector and layer
        if ( id1.subdetId() != id2.subdetId() || layerFromId(id1) != layerFromId(id2)) break;
        //must both be stereo if one is
        if(SiStripDetId(id1).stereo() != SiStripDetId(id2).stereo() ) continue;
        //A check i dont completely understand but might as well keep there
        if (  SiStripDetId(id1).glued() == id1.rawId() ) edm::LogInfo("SiStripHitResolution") << "BAD GLUED: Have glued layer with id = " << id1.rawId() << " and glued id = " << SiStripDetId(id1).glued() << "  and stereo = " << SiStripDetId(id1).stereo() << endl;
        if (  SiStripDetId(id2).glued() == id2.rawId() ) edm::LogInfo("SiStripHitResolution") << "BAD GLUED: Have glued layer with id = " << id2.rawId() << " and glued id = " << SiStripDetId(id2).glued() << "  and stereo = " << SiStripDetId(id2).stereo() << endl;

        itTraj2 = itmCompare;
        break;
      }

      bool fill = true;

      if(itTraj2 == tmColl.end()){
        detID2          = 0;
        clusterW2       = 0;
        expectedW2      = 0;
        atEdge2         = 0;
        pairPath        = 0;
        hitDX           = 0;
        trackDX         = 0;
        trackDXE        = 0;
        trackParamX     = 0;
        trackParamY     = 0;
        trackParamDXDZ  = 0;
        trackParamDYDZ  = 0;
        trackParamXE    = 0;
        trackParamYE    = 0;
        trackParamDXDZE = 0;
        trackParamDYDZE = 0;
        if(pairsOnly) fill = false;
      } else {
        //dummy vars
        float pitch2     = 0;
        float trueRes2   = 0;

        //We found one....let's fill in the truth info!
        TrajectoryStateOnSurface tsos2 = itTraj2->updatedState();
        LocalVector trackDirection2 = tsos2.localDirection();
        const TransientTrackingRecHit::ConstRecHitPointer hit2 = itTraj2->recHit();
        getHitParameters(hit2,trackDirection2,&detID2,&clusterW2,&expectedW2,&trueRes2,&atEdge2,&pitch2);
        if(pairsOnly && (pitch != pitch2) ) fill = false;

        //Now for the matching ingo
        if(!getPairParameters(&(*itTraj2),&(*itTraj),&pairPath,&hitDX,&trackDX,&trackDXE,
            &trackParamX,&trackParamY, &trackParamDXDZ, &trackParamDYDZ,&trackParamXE,&trackParamYE, &trackParamDXDZE, &trackParamDYDZE) ){
          pairPath   = 0;
          hitDX      = 0;
          trackDX    = 0;
          trackDXE   = 0;
          trackParamX     = 0;
          trackParamY     = 0;
          trackParamDXDZ  = 0;
          trackParamDYDZ  = 0;
          trackParamXE    = 0;
          trackParamYE    = 0;
          trackParamDXDZE = 0;
          trackParamDYDZE = 0;
          if(pairsOnly) fill = false;
        }
      }

      if(fill)
        rootTree_->Fill();
    }
  }
  delete propagator;
}


void SiStripHitResolution::getHitParameters(const TransientTrackingRecHit::ConstRecHitPointer& hit, const LocalVector& trackDirection, unsigned int * detID, unsigned int * clusterWidth, float * expWidth, float * res, bool * atEdge, float * pitch){
  DetId detid = hit->geographicalId();
  unsigned short Nstrips=reader->getNumberOfApvsAndStripLength(detid).first*128;

  (*detID) = detid.rawId();
  (*clusterWidth) = 0;
  (*expWidth) = 0;
  (*res) = 0;
  (*pitch) = 0;

  //Now to see what kind of hit it is!
  const SiStripMatchedRecHit2D *matchedhit =
      dynamic_cast < const SiStripMatchedRecHit2D * >((*hit).hit());

  edm::LogInfo("SiStripHitResolution") << "MatchedRecHit= " << matchedhit<< endl;
  if(matchedhit){
    edm::LogInfo("SiStripHitResolution") << endl << "WHAT THE HELL!" << endl;
    GluedGeomDet *gdet = (GluedGeomDet *) trackerGeometry_->idToDet(matchedhit->geographicalId());

    auto hm = matchedhit->monoHit();
    const SiStripRecHit2D * monoHit = &hm;

    if(monoHit){
      const GeomDetUnit *det = gdet->monoDet();
      GlobalVector gtrkdir = gdet->toGlobal(trackDirection);
      LocalVector tkdir = det->toLocal(gtrkdir);
      (*res) = getSimHitRes(det,tkdir,*monoHit, expWidth,pitch);
      (*clusterWidth) = monoHit->cluster()->amplitudes().size();
      uint16_t firstStrip = monoHit->cluster()->firstStrip();
      uint16_t lastStrip = firstStrip + (monoHit->cluster()->amplitudes()).size() -1;
      (*atEdge) = (firstStrip == 0 || lastStrip == (Nstrips-1) );
    }

    auto s = matchedhit->stereoHit();
    const SiStripRecHit2D *steroHit = &s;

    if(steroHit){
      const GeomDetUnit *det = gdet->stereoDet();
      GlobalVector gtrkdir = gdet->toGlobal(trackDirection);
      LocalVector tkdir = det->toLocal(gtrkdir);
      (*res) = getSimHitRes(det,tkdir,*steroHit, expWidth,pitch);
      (*clusterWidth) = steroHit->cluster()->amplitudes().size();
      uint16_t firstStrip = steroHit->cluster()->firstStrip();
      uint16_t lastStrip = firstStrip + (steroHit->cluster()->amplitudes()).size() -1;
      (*atEdge) = (firstStrip == 0 || lastStrip == (Nstrips-1) );

    }
  }

  const GeomDetUnit *det = (const StripGeomDetUnit *) trackerGeometry_->idToDetUnit(detid);

  const SiStripRecHit1D *hit1d = dynamic_cast < const SiStripRecHit1D * >((*hit).hit());
  edm::LogInfo("SiStripHitResolution") << "Hit1D= " << hit1d<< endl;
  if (hit1d) {
    (*res) = getSimHitRes(det,trackDirection,*hit1d,expWidth,pitch);
    (*clusterWidth) = hit1d->cluster()->amplitudes().size();
    uint16_t firstStrip = hit1d->cluster()->firstStrip();
    uint16_t lastStrip = firstStrip + (hit1d->cluster()->amplitudes()).size() -1;
    (*atEdge) = (firstStrip == 0 || lastStrip == (Nstrips-1) );
  }


  const SiStripRecHit2D *hit2d = dynamic_cast < const SiStripRecHit2D * >((*hit).hit());
  edm::LogInfo("SiStripHitResolution") << "Hit2D= " << hit2d<< endl;
  if (hit2d) {
    (*res) = getSimHitRes(det,trackDirection,*hit2d, expWidth,pitch);
    (*clusterWidth) = hit2d->cluster()->amplitudes().size();
    uint16_t firstStrip = hit2d->cluster()->firstStrip();
    uint16_t lastStrip = firstStrip + (hit2d->cluster()->amplitudes()).size() -1;
    (*atEdge) = (firstStrip == 0 || lastStrip == (Nstrips-1) );
  }

  //  vector<SiStripRecHit2D>::const_iterator detrphi = hit->hit();
  //if (detrphi != hit->hit()->end()) {
  //  SiStripRecHit2DCollection::DetSet rphiHits = *detrphi;
  //  SiStripRecHit2DCollection::DetSet::const_iterator iterrphi = rphiHits.begin(), rechitrphiRangeIteratorEnd = rphiHits.end(); 
  //  for(;iterrphi!=rechitrphiRangeIteratorEnd;++iterrphi){//loop on the rechit
  //SiStripRecHit2D const newrechit=*(hit->hit());
  //std::vector < PSimHit > matched;
  //matched.clear();
  //matched = associator->associateHit(*hit);
  //if(!matched.empty()){
  //  edm::LogInfo("SiStripHitResolution") << "test" << endl;
  //}
  // }
      //}
  //(*res) = getSimHitRes(det,trackDirection, *hit, expWidth,pitch);
  edm::LogInfo("SiStripHitResolution") << "TrueRes is = " << (*res) << endl;

}

float SiStripHitResolution::getSimHitRes(const GeomDetUnit * det, const LocalVector& trackdirection, const TrackingRecHit& recHit, float * trackWidth, float *pitch){

  const StripGeomDetUnit * stripdet = (const StripGeomDetUnit *) (det);
  const StripTopology & topol = (const StripTopology &) stripdet->topology();

  LocalPoint position = recHit.localPosition();
  (*pitch) = topol.localPitch(position);
  MeasurementPoint Mposition = topol.measurementPosition(position);

  float rechitrphiresMF = -1;
  if(genTruth){
    float dist;
    float mindist = 999999;
    PSimHit closest;
    std::vector < PSimHit > matched;
    matched.clear();
    matched = associator->associateHit(recHit);
    edm::LogInfo("SiStripHitResolution") << "RE to Sim hit matched= " << matched.empty() << endl;
    if (!matched.empty()) {

      for (vector < PSimHit >::const_iterator m = matched.begin(); m < matched.end();
          m++) {
        dist = abs(position.x() - (*m).localPosition().x());
        if (dist < mindist) {
          mindist = dist;
          closest = (*m);
        }
        rechitrphiresMF =
            Mposition.x() - (topol.measurementPosition(closest.localPosition())).x();
      }
    }
  }

  float anglealpha = 0;
  if (trackdirection.z() != 0) {
    anglealpha = atan(trackdirection.x() / trackdirection.z()) * TMath::RadToDeg();
  }


  LocalVector drift = stripcpe->driftDirection(stripdet);
  float thickness = stripdet->surface().bounds().thickness();
  float tanalpha = tan(anglealpha * TMath::DegToRad());
  float tanalphaL = drift.x() / drift.z();
  (*trackWidth) = fabs((thickness / (*pitch)) * tanalpha - (thickness / (*pitch)) * tanalphaL);

  return rechitrphiresMF;

}

double SiStripHitResolution::getSimpleRes(const TrajectoryMeasurement* traj1){
  TrajectoryStateOnSurface theCombinedPredictedState;
  
  if ( traj1->backwardPredictedState().isValid() )
    theCombinedPredictedState = TrajectoryStateCombiner().combine( traj1->forwardPredictedState(),
								   traj1->backwardPredictedState());
  else
    theCombinedPredictedState = traj1->forwardPredictedState();
  
  if (!theCombinedPredictedState.isValid()) {
    return -100;
  }
  
  const TransientTrackingRecHit::ConstRecHitPointer firstRecHit = traj1->recHit();
  double recHitX_1 = firstRecHit->localPosition().x();
  return (theCombinedPredictedState.localPosition().x() - recHitX_1);
  
}

//traj1 is the matched trajectory...traj2 is the original
bool SiStripHitResolution::getPairParameters(const TrajectoryMeasurement* traj1, const TrajectoryMeasurement* traj2, float * pairPath, float * hitDX, float * trackDX, float * trackDXE,
    float * trackParamX, float *trackParamY , float * trackParamDXDZ, float *trackParamDYDZ , float * trackParamXE, float *trackParamYE, float * trackParamDXDZE, float *trackParamDYDZE){
  (*pairPath) = 0;
  (*hitDX) = 0;
  (*trackDX) = 0;
  (*trackDXE) = 0;

  (*trackParamX    ) = 0;
  (*trackParamY    ) = 0;
  (*trackParamDXDZ ) = 0;
  (*trackParamDYDZ ) = 0;
  (*trackParamXE   ) = 0;
  (*trackParamYE   ) = 0;
  (*trackParamDXDZE) = 0;
  (*trackParamDYDZE) = 0;


  // backward predicted state at module 1
  TrajectoryStateOnSurface bwdPred1 = traj1->backwardPredictedState();
  if ( !bwdPred1.isValid() )  return false;
  //edm::LogInfo("SiStripHitResolution") << "momentum from backward predicted state = " << bwdPred1.globalMomentum().mag() << endl;
  // forward predicted state at module 2
  TrajectoryStateOnSurface fwdPred2 = traj2->forwardPredictedState();
  //edm::LogInfo("SiStripHitResolution") << "momentum from forward predicted state = " << fwdPred2.globalMomentum().mag() << endl;
  if ( !fwdPred2.isValid() )  return false;
  // extrapolate fwdPred2 to module 1
  TrajectoryStateOnSurface fwdPred2At1 = propagator->propagate(fwdPred2,bwdPred1.surface());
  if ( !fwdPred2At1.isValid() )  return false;
  // combine fwdPred2At1 with bwdPred1 (ref. state, best estimate without hits 1 and 2)
  TrajectoryStateOnSurface comb1 = combiner_.combine(bwdPred1,fwdPred2At1);
  if ( !comb1.isValid() )  return false;

  //
  // propagation of reference parameters to module 2
  //
  std::pair<TrajectoryStateOnSurface,double> tsosWithS =
    propagator->propagateWithPath(comb1,fwdPred2.surface());
  TrajectoryStateOnSurface comb1At2 = tsosWithS.first;
  if ( !comb1At2.isValid() )  return false;
  //distance of propagation from one surface to the next==could cut here
  (*pairPath) = tsosWithS.second;
  if (TMath::Abs((*pairPath)) > 15 ) return false; //cut to remove hit pairs > 15 cm apart

  // local parameters and errors on module 1
  AlgebraicVector5 pars = comb1.localParameters().vector();
  AlgebraicSymMatrix55 errs = comb1.localError().matrix();
  //number 3 is predX
  double predX1 = pars[3];
  //track fitted parameters in local coordinates for position 0
  (*trackParamX    ) = pars[3];
  (*trackParamY    ) = pars[4];
  (*trackParamDXDZ ) = pars[1];
  (*trackParamDYDZ ) = pars[2];
  (*trackParamXE   ) = TMath::Sqrt(errs(3,3));
  (*trackParamYE   ) = TMath::Sqrt(errs(4,4));
  (*trackParamDXDZE) = TMath::Sqrt(errs(1,1));
  (*trackParamDYDZE) = TMath::Sqrt(errs(2,2));

  // local parameters and errors on module 2
  pars = comb1At2.localParameters().vector();
  errs = comb1At2.localError().matrix();
  double predX2 = pars[3];

  //
  // jacobians (local-to-global@1,global 1-2,global-to-local@2)
  //
  JacobianLocalToCurvilinear jacLocToCurv(comb1.surface(),
					  comb1.localParameters(),
					  *magField_);

  AnalyticalCurvilinearJacobian jacCurvToCurv(comb1.globalParameters(),
					      comb1At2.globalPosition(),
					      comb1At2.globalMomentum(),
					      tsosWithS.second);

  JacobianCurvilinearToLocal jacCurvToLoc(comb1At2.surface(),
					  comb1At2.localParameters(),
					  *magField_);

  // combined jacobian local-1-to-local-2
  AlgebraicMatrix55 jacobian = jacLocToCurv.jacobian()*jacCurvToCurv.jacobian()*jacCurvToLoc.jacobian();
  // covariance on module 1
  AlgebraicSymMatrix55 covComb1 = comb1.localError().matrix();
  // variance and correlations for predicted local_x on modules 1 and 2
  double c00 = covComb1(3,3);
  double c10(0.);
  double c11(0.);
  for ( int i=1; i<5; ++i ) {
    c10 += jacobian(3,i)*covComb1(i,3);
    for ( int j=1; j<5; ++j )  c11 += jacobian(3,i)*covComb1(i,j)*jacobian(3,j);
  }
  // choose relative sign in order to minimize error on difference
  double diff = c00 - 2*fabs(c10) + c11;
  diff = diff>0 ? sqrt(diff) : -sqrt(-diff);
  (*trackDXE) = diff;
  double relativeXSign_ = c10>0 ? -1 : 1;

  (*trackDX) = predX1 + relativeXSign_*predX2;

  const TransientTrackingRecHit::ConstRecHitPointer firstRecHit = traj1->recHit();
  const TransientTrackingRecHit::ConstRecHitPointer secondRecHit = traj2->recHit();
  double recHitX_1 = firstRecHit->localPosition().x();
  double recHitX_2 = secondRecHit->localPosition().x();
  //  if (abs(recHitX_1)>5) edm::LogInfo("SiStripHitResolution") << "BAD: Bad hit position: Id = " << firstRecHit->geographicalId().rawId() << endl;
  //  if (abs(recHitX_1)>5) edm::LogInfo("SiStripHitResolution") << "BAD: Bad hit position: Id = " << secondRecHit->geographicalId().rawId() << endl;

  (*hitDX) = recHitX_1 + relativeXSign_*recHitX_2;

  //track parameters in local coordinates at position 0

  return true;
}



int
SiStripHitResolution::layerFromId (const DetId& id) const
{
  if ( id.subdetId()==PixelSubdetector::PixelBarrel ) {
    PXBDetId tobId(id);
    return tobId.layer();
  }
  else if ( id.subdetId()==PixelSubdetector::PixelEndcap ) {
    PXFDetId tobId(id);
    return tobId.disk() + (3*(tobId.side()-1));
  }
  else if ( id.subdetId()==StripSubdetector::TIB ) {
    TIBDetId tibId(id);
    return tibId.layer();
  }
  else if ( id.subdetId()==StripSubdetector::TOB ) {
    TOBDetId tobId(id);
    return tobId.layer();
  }
  else if ( id.subdetId()==StripSubdetector::TEC ) {
    TECDetId tobId(id);
    return tobId.wheel() + (9*(tobId.side()-1));
  }
  else if ( id.subdetId()==StripSubdetector::TID ) {
    TIDDetId tobId(id);
    return tobId.wheel() + (3*(tobId.side()-1));
  }
  return -1;
}

void 
SiStripHitResolution::endJob() {
  if ( rootTree_ ) {
    rootTree_->GetDirectory()->cd();
    rootTree_->Write();
    delete rootTree_;
  }
}

//define this as a plug-in
DEFINE_FWK_MODULE(SiStripHitResolution);
