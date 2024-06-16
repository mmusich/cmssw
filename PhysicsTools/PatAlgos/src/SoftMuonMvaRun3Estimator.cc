#include "PhysicsTools/PatAlgos/interface/SoftMuonMvaRun3Estimator.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "PhysicsTools/XGBoost/interface/XGBooster.h"

typedef std::pair<const reco::MuonChamberMatch*, const reco::MuonSegmentMatch*> MatchPair;

const MatchPair& getBetterMatch(const MatchPair& match1, const MatchPair& match2) {
  // Prefer DT over CSC simply because it's closer to IP
  // and will have less multiple scattering (at least for
  // RB1 vs ME1/3 case). RB1 & ME1/2 overlap is tiny
  if (match2.first->detector() == MuonSubdetId::DT and match1.first->detector() != MuonSubdetId::DT)
    return match2;

  // For the rest compare local x match. We expect that
  // segments belong to the muon, so the difference in
  // local x is a reflection on how well we can measure it
  if (abs(match1.first->x - match1.second->x) > abs(match2.first->x - match2.second->x))
    return match2;

  return match1;
}

float dX(const MatchPair& match) {
  if (match.first and match.second->hasPhi())
    return (match.first->x - match.second->x);
  else
    return 9999.;
}

float pullX(const MatchPair& match) {
  if (match.first and match.second->hasPhi())
    return dX(match) / sqrt(pow(match.first->xErr, 2) + pow(match.second->xErr, 2));
  else
    return 9999.;
}

float pullDxDz(const MatchPair& match) {
  if (match.first and match.second->hasPhi())
    return (match.first->dXdZ - match.second->dXdZ) /
           sqrt(pow(match.first->dXdZErr, 2) + pow(match.second->dXdZErr, 2));
  else
    return 9999.;
}

float dY(const MatchPair& match) {
  if (match.first and match.second->hasZed())
    return (match.first->y - match.second->y);
  else
    return 9999.;
}

float pullY(const MatchPair& match) {
  if (match.first and match.second->hasZed())
    return dY(match) / sqrt(pow(match.first->yErr, 2) + pow(match.second->yErr, 2));
  else
    return 9999.;
}

float pullDyDz(const MatchPair& match) {
  if (match.first and match.second->hasZed())
    return (match.first->dYdZ - match.second->dYdZ) /
           sqrt(pow(match.first->dYdZErr, 2) + pow(match.second->dYdZErr, 2));
  else
    return 9999.;
}

void fillMatchInfoForStation(std::string prefix,
                             pat::XGBooster& booster,
                             const MatchPair& match,
                             std::vector<float>& features) {
  booster.addFeature(prefix + "_dX");
  features.push_back(dX(match));
  booster.addFeature(prefix + "_pullX");
  features.push_back(pullX(match));
  booster.addFeature(prefix + "_pullDxDz");
  features.push_back(pullDxDz(match));
  booster.addFeature(prefix + "_dY");
  features.push_back(dY(match));
  booster.addFeature(prefix + "_pullY");
  features.push_back(pullY(match));
  booster.addFeature(prefix + "_pullDyDz");
  features.push_back(pullDyDz(match));
}

void fillMatchInfo(pat::XGBooster& booster, const pat::Muon& muon, std::vector<float>& features) {
  // Initiate containter for results
  const int n_stations = 2;
  std::vector<MatchPair> matches;
  for (unsigned int i = 0; i < n_stations; ++i)
    matches.push_back(std::pair(nullptr, nullptr));

  // Find best matches
  for (auto& chamberMatch : muon.matches()) {
    unsigned int station = chamberMatch.station() - 1;
    if (station >= n_stations)
      continue;

    // Find best segment match.
    // We could consider all segments, but we will restrict to segments
    // that match to this candidate better than to other muon candidates
    for (auto& segmentMatch : chamberMatch.segmentMatches) {
      if (not segmentMatch.isMask(reco::MuonSegmentMatch::BestInStationByDR) ||
          not segmentMatch.isMask(reco::MuonSegmentMatch::BelongsToTrackByDR))
        continue;

      // Multiple segment matches are possible in different
      // chambers that are either overlapping or belong to
      // different detectors. We need to select one.
      auto match_pair = MatchPair(&chamberMatch, &segmentMatch);

      if (matches[station].first)
        matches[station] = getBetterMatch(matches[station], match_pair);
      else
        matches[station] = match_pair;
    }
  }

  // Fill matching information
  fillMatchInfoForStation("match1", booster, matches[0], features);
  fillMatchInfoForStation("match2", booster, matches[1], features);
}

float pat::computeSoftMvaRun3(pat::XGBooster& booster, const pat::Muon& muon) {
  if (!muon.isTrackerMuon() && !muon.isGlobalMuon())
    return 0;

  std::vector<float> features;
  features.reserve(26);  // Allocate space for 14 muon features and 6 times 2 station features

  fillMatchInfo(booster, muon, features);

  booster.addFeature("pt");
  features.push_back(muon.pt());
  booster.addFeature("eta");
  features.push_back(muon.eta());
  booster.addFeature("trkValidFrac");
  features.push_back(muon.innerTrack()->validFraction());
  booster.addFeature("glbTrackProbability");
  features.push_back(muon.combinedQuality().glbTrackProbability);
  booster.addFeature("nLostHitsInner");
  features.push_back(muon.innerTrack()->hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_INNER_HITS));
  booster.addFeature("nLostHitsOuter");
  features.push_back(muon.innerTrack()->hitPattern().numberOfLostTrackerHits(reco::HitPattern::MISSING_OUTER_HITS));
  booster.addFeature("trkKink");
  features.push_back(muon.combinedQuality().trkKink);
  booster.addFeature("chi2LocalPosition");
  features.push_back(muon.combinedQuality().chi2LocalPosition);
  booster.addFeature("nPixels");
  features.push_back(muon.innerTrack()->hitPattern().numberOfValidPixelHits());
  booster.addFeature("nValidHits");
  features.push_back(muon.innerTrack()->hitPattern().numberOfValidTrackerHits());
  booster.addFeature("nLostHitsOn");
  features.push_back(muon.innerTrack()->hitPattern().numberOfLostTrackerHits(reco::HitPattern::TRACK_HITS));
  booster.addFeature("glbNormChi2");
  features.push_back((muon.isGlobalMuon() ? muon.globalTrack()->normalizedChi2() : 9999.));
  booster.addFeature("trkLayers");
  features.push_back(muon.innerTrack()->hitPattern().trackerLayersWithMeasurement());
  booster.addFeature("highPurity");
  features.push_back(muon.innerTrack()->quality(reco::Track::highPurity));

  return booster.predict(features);
}
