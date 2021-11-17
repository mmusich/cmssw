// -*- C++ -*-
//
// Package:    SiPixelTrackProbQXYProducer 
// Class:      SiPixelTrackProbQXYProducer 
// 
/**\class SiPixelTrackProbQXYProducer  SiPixelTrackProbQXYProducer.cc RecoTracker/DeDx/plugins/SiPixelTrackProbQXYProducer.cc

 Description: SiPixel Charge and shape probabilities combined for tracks

*/
//
// Original Author:  Tamas Almos Vami 
//         Created:  Mon Nov 17 14:09:02 CEST 2021
//


// system include files
#include <memory>
#include <cmath>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/TrackerGeometryBuilder/interface/StripGeomDetUnit.h"
#include "Geometry/TrackerGeometryBuilder/interface/PixelGeomDetUnit.h"

#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "TrackingTools/PatternTools/interface/TrajTrackAssociation.h"
#include "TrackingTools/TransientTrackingRecHit/interface/TransientTrackingRecHit.h"
#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHit.h"
//
// class declaration
//

class SiPixelTrackProbQXYProducer : public edm::stream::EDProducer<> {
public:
  explicit SiPixelTrackProbQXYProducer(const edm::ParameterSet&);
  ~SiPixelTrackProbQXYProducer() override;

private:
  void produce(edm::Event&, const edm::EventSetup&) override;
  int factorial(int);

  // ----------member data ---------------------------
  edm::EDGetTokenT<reco::TrackCollection>  trackToken_;
  edm::ESHandle<TrackerGeometry> tkGeom;
};

using namespace reco;
using namespace std;
using namespace edm;

SiPixelTrackProbQXYProducer::SiPixelTrackProbQXYProducer(const edm::ParameterSet& iConfig) {
   //produces<reco::DeDxHitInfoCollection >();
   //produces<reco::DeDxHitInfoAss >();
   produces<edm::ValueMap<int> >("prescale");

   trackToken_ = consumes<reco::TrackCollection>(iConfig.getParameter<edm::InputTag>("tracks"));

   //if(!usePixel && !useStrip)
  // edm::LogError("DeDxHitsProducer") << "No Pixel Hits NOR Strip Hits will be saved.  Running this module is useless";
}


SiPixelTrackProbQXYProducer::~SiPixelTrackProbQXYProducer(){}

void SiPixelTrackProbQXYProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{  
  edm::Handle<reco::TrackCollection> trackCollectionHandle;
  iEvent.getByToken(trackToken_,trackCollectionHandle);
  const TrackCollection& trackCollection(*trackCollectionHandle.product());
  float probQonTrack = 0.0;
  float probXYonTrack = 0.0;
  // creates the output collection
  //auto resultdedxHitColl = std::make_unique<reco::DeDxHitInfoCollection>();

  std::vector<int> indices; std::vector<int> prescales;
  //uint64_t state[2] = { iEvent.id().event(), iEvent.id().luminosityBlock() };
  
  for(unsigned int j=0;j<trackCollection.size();j++){            
     const reco::Track& track = trackCollection[j];

//     reco::DeDxHitInfo hitDeDxInfo;

     int numRecHits = 0;
     float probQonTrackWMulti = 1;
     float probXYonTrackWMulti = 1;
     //auto const & trajParams = track.extra()->trajParams();
     auto hb = track.recHitsBegin();
     for(unsigned int h=0;h<track.recHitsSize();h++){
        auto recHit = *(hb+h);
        //if (!trackerHitRTTI::isFromDet(*recHit) ) continue;
        const SiPixelRecHit* pixhit = dynamic_cast<const SiPixelRecHit*>(recHit);
        if (pixhit->geographicalId().det() != DetId::Tracker) continue;
        if (pixhit == nullptr) continue;
        if (!pixhit->isValid()) continue;
        float probQ         = pixhit->probabilityQ();
        float probXY        = pixhit->probabilityXY();
        numRecHits++;
        probQonTrackWMulti *= probQ;
        probXYonTrackWMulti *= probXY;
     } // end looping on the rechits
     float logprobQonTrackWMulti = log(probQonTrackWMulti);
     float logprobXYonTrackWMulti = log(probXYonTrackWMulti);
     std::cout << "numRecHits: " << numRecHits << std::endl;
     float probQonTrackTerm = 0;
     float probXYonTrackTerm = 0;
     for(int iTkRh = 0; iTkRh < numRecHits; ++iTkRh) {
        probQonTrackTerm += ((pow(-logprobQonTrackWMulti,iTkRh))/(factorial(iTkRh)));
        probXYonTrackTerm += ((pow(-logprobXYonTrackWMulti,iTkRh))/(factorial(iTkRh)));
        cout << "For cluster " << iTkRh << " the probQonTrackTerm is " << probQonTrackTerm << " the probXYonTrackTerm is " << probXYonTrackTerm <<  endl;
     }
            
     probQonTrack = probQonTrackWMulti*probQonTrackTerm;
     probXYonTrack = probXYonTrackWMulti*probXYonTrackTerm;
     std::cout << "For this track probQonTrack is " << probQonTrack << " and probXYonTrack is  " << probXYonTrack << endl;
     //break;
     //indices.push_back(resultdedxHitColl->size());
     //resultdedxHitColl->push_back(hitDeDxInfo);
  }
 

  //edm::OrphanHandle<reco::DeDxHitInfoCollection> dedxHitCollHandle = iEvent.put(std::move(resultdedxHitColl));

  //create map passing the handle to the matched collection
  //auto dedxMatch = std::make_unique<reco::DeDxHitInfoAss>(dedxHitCollHandle);
  //reco::DeDxHitInfoAss::Filler filler(*dedxMatch);  
  //filler.insert(trackCollectionHandle, indices.begin(), indices.end()); 
  //filler.fill();
  //iEvent.put(std::move(dedxMatch));

 // auto dedxPrescale = std::make_unique<edm::ValueMap<int>>();
 // edm::ValueMap<int>::Filler pfiller(*dedxPrescale);
 // pfiller.insert(dedxHitCollHandle, prescales.begin(), prescales.end());
 // pfiller.fill();
 // iEvent.put(std::move(dedxPrescale), "prescale");
}


int SiPixelTrackProbQXYProducer::factorial(int n) {
  return (n == 1 || n == 0) ? 1 : factorial(n - 1) * n;
}

//define this as a plug-in
DEFINE_FWK_MODULE(SiPixelTrackProbQXYProducer);
