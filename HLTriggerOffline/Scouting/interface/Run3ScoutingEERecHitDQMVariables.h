#ifndef HLTriggerOffline_Scouting_interface_Run3ScoutingEERecHitDQMVariables_h
#define HLTriggerOffline_Scouting_interface_Run3ScoutingEERecHitDQMVariables_h

#include "DQMServices/Components/interface/GenericObjectDQMSource.h"
#include "DataFormats/Scouting/interface/Run3ScoutingEERecHit.h"

template <>
struct DQMVariableTraits<Run3ScoutingEERecHit> {
  static std::vector<DQMVariable<Run3ScoutingEERecHit>> variables() {
    return {
        {"energy", "energy [GeV]", 100, 0., 50., [](Run3ScoutingEERecHit const& h) { return h.energy(); }},
        {"time", "time [ns]", 100, -25., 25., [](Run3ScoutingEERecHit const& h) { return h.time(); }},
        {"detId", "detId", 100, 0., 1.e9, [](Run3ScoutingEERecHit const& h) { return h.detId(); }},
    };
  }

  static std::vector<DQMEtaPhiMapVariable<Run3ScoutingEERecHit>> etaPhiMapVariables() {
    return {
        {"occupancy",
         "EE recHit occupancy",
         100,
         -3.,
         3.,
         100,
         -3.15,
         3.15,
         [](Run3ScoutingEERecHit const& h) { return std::vector<uint32_t>{h.detId()}; }},
    };
  }
};

#endif
