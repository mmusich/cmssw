#include "SimTracker/VertexAssociation/interface/calculateVertexSharedTracks.h"

NumFrac calculateVertexSharedTracks(const reco::Vertex &recoV,
                                    const TrackingVertex &simV,
                                    const reco::RecoToSimCollection &trackRecoToSimAssociation,
                                    const bool weightPtSum2) {
  unsigned int sharedTracks = 0;
  float sharedTracksWeightPtSum2 = 0;
  float totalTracksWeightPtSum2 = 0;
  for (auto iTrack = recoV.tracks_begin(); iTrack != recoV.tracks_end(); ++iTrack) {
    totalTracksWeightPtSum2 += ((*iTrack)->pt() * (*iTrack)->pt());
    auto found = trackRecoToSimAssociation.find(*iTrack);

    if (found == trackRecoToSimAssociation.end())
      continue;

    // matched TP equal to any TP of sim vertex => increase counter
    for (const auto &tp : found->val) {
      if (std::find_if(simV.daughterTracks_begin(), simV.daughterTracks_end(), [&](const TrackingParticleRef &vtp) {
            return tp.first == vtp;
          }) != simV.daughterTracks_end()) {
        sharedTracks += 1;
        sharedTracksWeightPtSum2 += ((*iTrack)->pt() * (*iTrack)->pt());
        break;
      }
    }
  }
  if (weightPtSum2)
    return NumFrac(sharedTracks, sharedTracksWeightPtSum2 / totalTracksWeightPtSum2);
  else
    return NumFrac(sharedTracks, float(sharedTracks) / recoV.tracksSize());
}

NumFrac calculateVertexSharedTracks(const TrackingVertex &simV,
                                    const reco::Vertex &recoV,
                                    const reco::SimToRecoCollection &trackSimToRecoAssociation,
                                    const bool weightPtSum2) {
  unsigned int sharedTracks = 0;
  float sharedTracksWeightPtSum2 = 0;
  float totalTracksWeightPtSum2 = 0;

  for (auto iTP = simV.daughterTracks_begin(); iTP != simV.daughterTracks_end(); ++iTP) {
    auto found = trackSimToRecoAssociation.find(*iTP);

    if (found == trackSimToRecoAssociation.end())
      continue;

    // matched track equal to any track of reco vertex => increase counter
    for (const auto &tk : found->val) {
      if (std::find_if(recoV.tracks_begin(), recoV.tracks_end(), [&](const reco::TrackBaseRef &vtk) {
            totalTracksWeightPtSum2 += (tk.first->pt() * tk.first->pt());
            return ((tk.first.id() == vtk.id()) &&
                    (tk.first.key() == vtk.key()));  // tk.first == vtk; operator::== not working
          }) != recoV.tracks_end()) {
        sharedTracks += 1;
        sharedTracksWeightPtSum2 += (tk.first->pt() * tk.first->pt());
        break;
      }
    }
  }
  if (weightPtSum2)
    return NumFrac(sharedTracks, sharedTracksWeightPtSum2 / totalTracksWeightPtSum2);
  else
    return NumFrac(sharedTracks, float(sharedTracks) / recoV.tracksSize());
}
