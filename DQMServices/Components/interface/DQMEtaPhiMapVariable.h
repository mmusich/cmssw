#ifndef DQMOffline_Generic_interface_DQMEtaPhiMapVariable_h
#define DQMOffline_Generic_interface_DQMEtaPhiMapVariable_h

#include <cstdint>
#include <functional>
#include <string>
#include <vector>

// Describes an eta/phi occupancy map built from the detId(s) of an object of
// type T, to be booked as a single TH2F by GenericObjectDQMSource<T> and
// filled once per detId on every event. GenericObjectDQMSource converts each
// detId to a position using CaloGeometry, so this is only meaningful for
// types backed by calorimeter (or other geometry-mapped) detIds.
template <typename T>
struct DQMEtaPhiMapVariable {
  std::string name;
  std::string title;
  int nbinsEta;
  double etaMin;
  double etaMax;
  int nbinsPhi;
  double phiMin;
  double phiMax;
  std::function<std::vector<uint32_t>(T const&)> detIdAccessor;
};

#endif
