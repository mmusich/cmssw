#ifndef DataFormats_Scouting_Phase2ScoutingEBRecHit_h
#define DataFormats_Scouting_Phase2ScoutingEBRecHit_h

#include <vector>
#include <stdint.h>

// Phase 2 HLT-Scouting data format holding calo recHits information:
// - EBRecHits collection (ECAL Barrel)
// Saved information is specific to each hit type: energy, time, flags, and detId are available for EB recHits
//
// IMPORTANT: any changes to Phase2ScoutingEBRecHit must be backward-compatible!

class Phase2ScoutingEBRecHit {
public:
  Phase2ScoutingEBRecHit(float energy, float time, unsigned int detId, uint32_t flags)
      : energy_{energy}, time_{time}, detId_{detId}, flags_{flags} {}

  Phase2ScoutingEBRecHit() : energy_{0}, time_{0}, detId_{0}, flags_{0} {}

  float energy() const { return energy_; }
  float time() const { return time_; }
  unsigned int detId() const { return detId_; }
  uint32_t flags() const { return flags_; }

private:
  float energy_;
  float time_;
  unsigned int detId_;
  uint32_t flags_;
  // NOTE: types are kept the same as in the origin of the data in reco::PFRecHit
};

using Phase2ScoutingEBRecHitCollection = std::vector<Phase2ScoutingEBRecHit>;

#endif
