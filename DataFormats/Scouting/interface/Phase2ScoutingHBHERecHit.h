#ifndef DataFormats_Scouting_Phase2ScoutingHBHERecHit_h
#define DataFormats_Scouting_Phase2ScoutingHBHERecHit_h

#include <vector>

// Phase 2 HLT-Scouting data format holding calo recHits information:
// - HBHERecHits collection (HCAL Barrel and Endcap)
// Saved information is specific to each hit type: energy and detId are available for HCAL recHits
//
// -- IMPORTANT: any changes to Phase2ScoutingHBHERecHit must be backward-compatible!

class Phase2ScoutingHBHERecHit {
public:
  Phase2ScoutingHBHERecHit(float energy, float time, unsigned int detId)
      : energy_{energy}, time_{time}, detId_{detId} {}

  Phase2ScoutingHBHERecHit() : energy_{0}, time_{0}, detId_{0} {}

  float energy() const { return energy_; }
  float time() const { return time_; }
  unsigned int detId() const { return detId_; }

private:
  float energy_;
  float time_;
  unsigned int detId_;
};

using Phase2ScoutingHBHERecHitCollection = std::vector<Phase2ScoutingHBHERecHit>;

#endif
