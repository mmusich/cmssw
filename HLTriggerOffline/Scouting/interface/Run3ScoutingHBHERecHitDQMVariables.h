#ifndef HLTriggerOffline_Scouting_interface_Run3ScoutingHBHERecHitDQMVariables_h
#define HLTriggerOffline_Scouting_interface_Run3ScoutingHBHERecHitDQMVariables_h

#include "DQMServices/Components/interface/GenericObjectDQMSource.h"
#include "DataFormats/Scouting/interface/Run3ScoutingHBHERecHit.h"

template <>
struct DQMVariableTraits<Run3ScoutingHBHERecHit> {
  static std::vector<DQMVariable<Run3ScoutingHBHERecHit>> variables() {
    return {
        {"energy", "energy [GeV]", 100, 0., 100., [](Run3ScoutingHBHERecHit const& h) { return h.energy(); }},
        {"time", "time [ns]", 100, -25., 25., [](Run3ScoutingHBHERecHit const& h) { return h.time(); }},
        {"detId", "detId", 100, 0., 1.e9, [](Run3ScoutingHBHERecHit const& h) { return h.detId(); }},
    };
  }

  static std::vector<DQMEtaPhiMapVariable<Run3ScoutingHBHERecHit>> etaPhiMapVariables() {
    return {
        {"occupancy",
         "HBHE recHit occupancy",
         100,
         -3.,
         3.,
         100,
         -3.15,
         3.15,
         [](Run3ScoutingHBHERecHit const& h) { return std::vector<uint32_t>{h.detId()}; }},
    };
  }
};

#endif
