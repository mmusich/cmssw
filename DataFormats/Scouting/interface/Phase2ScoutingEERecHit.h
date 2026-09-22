#ifndef DataFormats_Scouting_Phase2ScoutingEERecHit_h
#define DataFormats_Scouting_Phase2ScoutingEERecHit_h

#include <vector>

// Phase 2 HLT-Scouting data format holding calo recHits information:
// - EERecHits collection (ECAL Endcap)
// Saved information is specific to each hit type: energy, time, and detId are available for EE recHits
//
// IMPORTANT: any changes to Phase2ScoutingEERecHit must be backward-compatible !

class Phase2ScoutingEERecHit {
public:
  Phase2ScoutingEERecHit(float energy, float time, unsigned int detId) : energy_{energy}, time_{time}, detId_{detId} {}

  Phase2ScoutingEERecHit() : energy_{0}, time_{0}, detId_{0} {}

  float energy() const { return energy_; }
  float time() const { return time_; }
  unsigned int detId() const { return detId_; }

private:
  float energy_;
  float time_;
  unsigned int detId_;
};

using Phase2ScoutingEERecHitCollection = std::vector<Phase2ScoutingEERecHit>;

#endif
