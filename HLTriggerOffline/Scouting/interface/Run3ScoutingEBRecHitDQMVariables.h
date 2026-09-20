#ifndef HLTriggerOffline_Scouting_interface_Run3ScoutingEBRecHitDQMVariables_h
#define HLTriggerOffline_Scouting_interface_Run3ScoutingEBRecHitDQMVariables_h

#include "DQMServices/Components/interface/GenericObjectDQMSource.h"
#include "DataFormats/Scouting/interface/Run3ScoutingEBRecHit.h"

template <>
struct DQMVariableTraits<Run3ScoutingEBRecHit> {
  static std::vector<DQMVariable<Run3ScoutingEBRecHit>> variables() {
    return {
        {"energy", "energy [GeV]", 100, 0., 50., [](Run3ScoutingEBRecHit const& h) { return h.energy(); }},
        {"time", "time [ns]", 100, -25., 25., [](Run3ScoutingEBRecHit const& h) { return h.time(); }},
        {"detId", "detId", 100, 0., 1.e9, [](Run3ScoutingEBRecHit const& h) { return h.detId(); }},
        // flags is a packed status-flag bitmask, not a physical quantity -- histogramming the raw
        // integer value only tells you the bitmask's numeric spread, not which flags are set.
        {"flags", "flags (raw bitmask)", 64, 0., 64., [](Run3ScoutingEBRecHit const& h) { return h.flags(); }},
    };
  }

  static std::vector<DQMEtaPhiMapVariable<Run3ScoutingEBRecHit>> etaPhiMapVariables() {
    return {
        {"occupancy",
         "EB recHit occupancy",
         100,
         -1.5,
         1.5,
         100,
         -3.15,
         3.15,
         [](Run3ScoutingEBRecHit const& h) { return std::vector<uint32_t>{h.detId()}; }},
    };
  }
};

#endif
