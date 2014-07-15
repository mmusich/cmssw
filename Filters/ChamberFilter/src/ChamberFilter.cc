// -*- C++ -*-
//
// Package:    ChamberFilter
// Class:      ChamberFilter
// 
/**\class ChamberFilter ChamberFilter.cc ChamberFilter/src/ChamberFilter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Yuriy Pakhotin,,,
//         Created:  Wed Aug 28 17:03:10 CDT 2013
// $Id: ChamberFilter.cc,v 1.3 2013/08/29 04:30:53 pakhotin Exp $
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackBase.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackingRecHit/interface/TrackingRecHit.h"
#include "DataFormats/TrackingRecHit/interface/TrackingRecHitFwd.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/MuonDetId/interface/MuonSubdetId.h"
#include "DataFormats/MuonDetId/interface/DTChamberId.h"
#include "DataFormats/MuonDetId/interface/CSCDetId.h"

//
// class declaration
//

class ChamberFilter : public edm::EDFilter {
  public:
    explicit ChamberFilter(const edm::ParameterSet&);
    ~ChamberFilter();

  private:
    virtual void beginJob() ;
    virtual bool filter(edm::Event&, const edm::EventSetup&);
    virtual void endJob() ;
      
  // ----------member data ---------------------------
  
  edm::InputTag m_tracksTag;
  double m_minTrackPt;
  double m_minTrackEta;
  double m_maxTrackEta;
  int m_minTrackerHits;
  int m_minDTHits;
  int m_minCSCHits;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
ChamberFilter::ChamberFilter(const edm::ParameterSet& iConfig)
  : m_tracksTag(      iConfig.getParameter<edm::InputTag>("tracksTag"))
  , m_minTrackPt(     iConfig.getParameter<double>("minTrackPt"))
  , m_minTrackEta(    iConfig.getParameter<double>("minTrackEta"))
  , m_maxTrackEta(    iConfig.getParameter<double>("maxTrackEta"))
  , m_minTrackerHits( iConfig.getParameter<int>("minTrackerHits"))
  , m_minDTHits(      iConfig.getParameter<int>("minDTHits"))
  , m_minCSCHits(     iConfig.getParameter<int>("minCSCHits"))
{}


ChamberFilter::~ChamberFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool ChamberFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  edm::Handle<reco::TrackCollection> trackColl;
  iEvent.getByLabel(m_tracksTag, trackColl);

  for (reco::TrackCollection::const_iterator it = trackColl->begin();  it != trackColl->end();  ++it) {
    const reco::Track* track = &(*it);

    std::cout << "track->pt(): " << track->pt() << std::endl;
    if ( track->pt() < m_minTrackPt ) continue;
    
    std::cout << "track->eta(): " << track->eta() << std::endl;
    if (track->eta() < m_minTrackEta || track->eta() > m_maxTrackEta ) continue;
    
    int tracker_numHits = 0;
    int dt_numHits      = 0;
    int csc_numHits     = 0;
    
    for ( trackingRecHit_iterator hit = track->recHitsBegin(); hit != track->recHitsEnd();  ++hit ) {
      DetId hitId = (*hit)->geographicalId();        
      if ( hitId.det() == DetId::Tracker ) tracker_numHits++;
      
      if ( hitId.det() == DetId::Muon && hitId.subdetId() == MuonSubdetId::DT ) {
        const DTChamberId dtChamberId(hitId.rawId());
        std::cout << "hit DT wheel: " << dtChamberId.wheel()
                  << " station: "     << dtChamberId.station()
                  << " sector: "      << dtChamberId.sector() << std::endl;
        if ( (   dtChamberId.wheel()    == 1
               && dtChamberId.station() == 1
               && dtChamberId.sector()  == 5 )
             ||
             (   dtChamberId.wheel()    == 1
               && dtChamberId.station() == 2
               && dtChamberId.sector()  == 5 )
             ||
             (   dtChamberId.wheel()    == 1
               && dtChamberId.station() == 3
               && dtChamberId.sector()  == 5 )
             ||
             (   dtChamberId.wheel()    == 1
               && dtChamberId.station() == 4
               && dtChamberId.sector()  == 5 )
             ||
             (   dtChamberId.wheel()    == 2
               && dtChamberId.station() == 2
               && dtChamberId.sector()  == 5 )
             ||
             (   dtChamberId.wheel()    == 2
               && dtChamberId.station() == 3
               && dtChamberId.sector()  == 5 )
             ||
             (   dtChamberId.wheel()    == 2
               && dtChamberId.station() == 4
               && dtChamberId.sector()  == 5 )
            ) {
          dt_numHits++;
        }
      }
      
//      if ( hitId.det() == DetId::Muon && hitId.subdetId() == MuonSubdetId::CSC ) {
//        const CSCDetId cscChamberId(hitId.rawId());
//        std::cout << "hit CSC endcap: " << cscChamberId.endcap()
//                  << " station: "       << cscChamberId.station()
//                  << " ring: "          << cscChamberId.ring()
//                  << " chamber: "       << cscChamberId.chamber() << std::endl;
//        if (    cscChamberId.endcap()  == m_CSCEndcap
//             && cscChamberId.station() == m_CSCStation
//             && cscChamberId.ring()    == m_CSCRing
//             && cscChamberId.chamber() == m_CSCChamber ) {
//          csc_numHits++;
//        }
//      }
    }
    
    std::cout << "track tracker_numHits: " << tracker_numHits << std::endl;
    std::cout << "track dt_numHits:      " << dt_numHits << std::endl;
    std::cout << "track csc_numHits:     " << csc_numHits << std::endl;
    
    if (    m_minTrackerHits <= tracker_numHits
         && ( m_minDTHits <= dt_numHits  ||  m_minCSCHits <= csc_numHits ) )  return true;

  }
  
  return false;
}

// ------------ method called once each job just before starting event loop  ------------
void 
ChamberFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
ChamberFilter::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(ChamberFilter);
