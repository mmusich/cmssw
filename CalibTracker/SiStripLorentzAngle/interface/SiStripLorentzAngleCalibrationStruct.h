#ifndef CalibTracker_SiStripLorentzAngle_SiStripLorentzAngleCalibrationStruct_h
#define CalibTracker_SiStripLorentzAngle_SiStripLorentzAngleCalibrationStruct_h

#include "DQMServices/Core/interface/DQMStore.h"
#include <map>
#include <vector>

struct SiStripLorentzAngleCalibrationHistograms {
public:
  SiStripLorentzAngleCalibrationHistograms() = default;

  // B field
  std::string bfield_;

  // la info tree
  std::vector<unsigned int>* inforawid_ = nullptr;
  std::vector<float>* infoglobalZofunitlocalY_ = nullptr;
  std::vector<float>* infolocalb_ = nullptr;
  std::vector<float>* infola_ = nullptr;

  std::map<unsigned int, int> orientation_;
  std::map<unsigned int, float> la_db_;

  // event data
  unsigned int eventnumber_ = 0;
  unsigned int runnumber_ = 0;
  unsigned int luminumber_ = 0;

  // calib data
  std::vector<unsigned int>* trackindex_ = nullptr;
  std::vector<unsigned int>* rawid_ = nullptr;
  std::vector<unsigned short>* nstrips_ = nullptr;
  std::vector<float>* localdirx_ = nullptr;
  std::vector<float>* localdiry_ = nullptr;
  std::vector<float>* localdirz_ = nullptr;
  std::vector<float>* variance_ = nullptr;

  // track data
  std::vector<float>* trackpt_ = nullptr;
  std::vector<float>* tracketa_ = nullptr;
  std::vector<float>* trackphi_ = nullptr;
  std::vector<unsigned int>* trackhitsvalid_ = nullptr;
  std::vector<float>* trackchi2ndof_ = nullptr;

  // histogramming
  std::map<std::string, dqm::reco::MonitorElement*> h1_;
  std::map<std::string, dqm::reco::MonitorElement*> h2_;

  std::map<int, dqm::reco::MonitorElement*> h2_ct_w_m_;
  std::map<int, dqm::reco::MonitorElement*> h2_ct_var2_m_;
  std::map<int, dqm::reco::MonitorElement*> h2_ct_var3_m_;

  std::map<int, dqm::reco::MonitorElement*> h2_t_w_m_;
  std::map<int, dqm::reco::MonitorElement*> h2_t_var2_m_;
  std::map<int, dqm::reco::MonitorElement*> h2_t_var3_m_;

  std::map<std::string, dqm::reco::MonitorElement*> hp_;

  // info
  std::map<std::string, int> nlayers_;
  std::vector<std::string> modtypes_;
  std::map<std::string, float> la_;
};

#endif
