#ifndef RecoTracker_PixelTrackFitting_plugins_storeTracks_h
#define RecoTracker_PixelTrackFitting_plugins_storeTracks_h

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "DataFormats/TrajectoryState/interface/LocalTrajectoryParameters.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/TrackExtra.h"
#include "DataFormats/Common/interface/OrphanHandle.h"
#include "RecoTracker/PixelTrackFitting/interface/TracksWithHits.h"

#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"
#include "Geometry/Records/interface/TrackerTopologyRcd.h"

template <typename Ev, typename TWH>
void storeTracks(Ev& ev, const TWH& tracksWithHits, const TrackerTopology& ttopo) {
  auto tracks = std::make_unique<reco::TrackCollection>();
  auto recHits = std::make_unique<TrackingRecHitCollection>();
  auto trackExtras = std::make_unique<reco::TrackExtraCollection>();

  int cc = 0, nTracks = tracksWithHits.size();

  trackExtras->resize(nTracks);
  tracks->reserve(nTracks);
  recHits->reserve(4 * nTracks);

  for (int i = 0; i < nTracks; i++) {
    reco::Track* track = tracksWithHits[i].first;
    const auto& hits = tracksWithHits[i].second;

    for (unsigned int k = 0; k < hits.size(); k++) {
      auto* hit = hits[k]->clone();  // need to clone (at least if from SoA)
      track->appendHitPattern(*hit, ttopo);
      recHits->push_back(hit);
    }
    tracks->push_back(*track);
    delete track;
  }

  LogDebug("TrackProducer") << "put the collection of TrackingRecHit in the event"
                            << "\n";
  edm::OrphanHandle<TrackingRecHitCollection> ohRH = ev.put(std::move(recHits));

  edm::RefProd<TrackingRecHitCollection> hitCollProd(ohRH);

  /*
  for (int k = 0; k < nTracks; k++) {
    auto& aTrackExtra = (*trackExtras)[k];

    //fill the TrackExtra with TrackingRecHitRef
    unsigned int nHits = (*tracks)[k].numberOfValidHits();
    aTrackExtra.setHits(hitCollProd, cc, nHits);
    cc += nHits;
    AlgebraicVector5 v = AlgebraicVector5(0, 0, 0, 0, 0);
    reco::TrackExtra::TrajParams trajParams(nHits, LocalTrajectoryParameters(v, 1.));
    reco::TrackExtra::Chi2sFive chi2s(nHits, 0);
    aTrackExtra.setTrajParams(std::move(trajParams), std::move(chi2s));

    // set the inner and outer ids
    const auto& hits = tracksWithHits[k].second;
    aTrackExtra.setOuterId(hits[0]->geographicalId().rawId());
    aTrackExtra.setInnerId(hits[hits.size() - 1]->geographicalId().rawId());

    aTrackExtra.setSeedDirection(PropagationDirection::oppositeToMomentum);
  }
  */

  for (int k = 0; k < nTracks; k++) {
    auto& aTrackExtra = (*trackExtras)[k];
    
    const auto& hits = tracksWithHits[k].second;
    
    // // Estimate outer/inner positions and momenta (we can refine this)
    const auto& outerPos = hits[0]->globalPosition();
    const auto& innerPos = hits[hits.size() - 1]->globalPosition();

    const auto& outerMom = tracksWithHits[k].first->outerMomentum();
    const auto& innerMom = tracksWithHits[k].first->innerMomentum();
    
    reco::Track::Point xOuter(outerPos.x(), outerPos.y(), outerPos.z());
    reco::Track::Point xInner(innerPos.x(), innerPos.y(), innerPos.z());

    /*
    (*trackExtras)[k] = reco::TrackExtra(
					 // trackExtras->emplace_back(
					 xOuter,
					 outerMom,
					 true,
					 xInner,
					 innerMom
					 true,
					 reco::Track::CovarianceMatrix(),
					 hits[0]->geographicalId().rawId(),
					 reco::Track::CovarianceMatrix(),
					 hits[hits.size() - 1]->geographicalId().rawId(),
					 alongMomentum);
    */

    unsigned int nHits = (*tracks)[k].numberOfValidHits();
    aTrackExtra.setHits(hitCollProd, cc, nHits);
    cc += nHits;
  }

  LogDebug("TrackProducer") << "put the collection of TrackExtra in the event"
                            << "\n";
  edm::OrphanHandle<reco::TrackExtraCollection> ohTE = ev.put(std::move(trackExtras));

  for (int k = 0; k < nTracks; k++) {
    const reco::TrackExtraRef theTrackExtraRef(ohTE, k);
    (*tracks)[k].setExtra(theTrackExtraRef);
  }

  ev.put(std::move(tracks));
}

#endif
