#ifndef CALIBTRACKER_SISTRIPCHANNELGAIN_APVGAINHELPERS_H
#define CALIBTRACKER_SISTRIPCHANNELGAIN_APVGAINHELPERS_H

#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"
#include "DQMServices/Core/interface/ConcurrentMonitorElement.h"

#include <string>
#include <vector>
#include <utility>
#include <cstdint>


namespace APVGain {

  int subdetectorId(uint32_t);
  int subdetectorId(const std::string&);
  int subdetectorSide(uint32_t,const TrackerTopology*);
  int subdetectorSide(const std::string&);
  int subdetectorPlane(uint32_t,const TrackerTopology*);
  int subdetectorPlane(const std::string&);
  
  std::vector<std::pair<std::string,std::string>> monHnames(std::vector<std::string>,bool,const char* tag);

  struct APVmon{

    int subdetectorId;
    int subdetectorSide;
    int subdetectorPlane;
    ConcurrentMonitorElement monitor;
    
    APVmon(int v1, int v2, int v3, ConcurrentMonitorElement& v4) :
      subdetectorId(v1),
      subdetectorSide(v2),
      subdetectorPlane(v3),
      monitor(std::move(v4))
    {
    }

    // copy constructor
    APVmon(APVmon&& mon) :
      subdetectorId(mon.subdetectorId),
      subdetectorSide(mon.subdetectorSide),
      subdetectorPlane(mon.subdetectorPlane),
      monitor(std::move(mon.monitor))
    {
    }

    //~APVmon() = default;
  };
  
  std::vector<ConcurrentMonitorElement> FetchMonitor(std::vector<APVmon>, uint32_t, const TrackerTopology* topo=nullptr);

  struct APVGainHistograms {
  public:
    APVGainHistograms():
      Charge_Vs_Index(),
      Charge_1(),
      Charge_2(),
      Charge_3(),
      Charge_4(),
      Charge_Vs_PathlengthTIB(), 
      Charge_Vs_PathlengthTOB(),
      Charge_Vs_PathlengthTIDP(),
      Charge_Vs_PathlengthTIDM(),
      Charge_Vs_PathlengthTECP1(),
      Charge_Vs_PathlengthTECP2(),
      Charge_Vs_PathlengthTECM1(),
      Charge_Vs_PathlengthTECM2()
    {
    }
    
    std::vector<ConcurrentMonitorElement>  Charge_Vs_Index;  /*!< Charge per cm for each detector id */
    std::array< std::vector<APVGain::APVmon>,7 > Charge_1;   /*!< Charge per cm per layer / wheel */
    std::array< std::vector<APVGain::APVmon>,7 > Charge_2;   /*!< Charge per cm per layer / wheel without G2 */
    std::array< std::vector<APVGain::APVmon>,7 > Charge_3;   /*!< Charge per cm per layer / wheel without G1 */
    std::array< std::vector<APVGain::APVmon>,7 > Charge_4;   /*!< Charge per cm per layer / wheel without G1 and G1*/

    std::vector<ConcurrentMonitorElement>  Charge_Vs_PathlengthTIB;   /*!< Charge vs pathlength in TIB */
    std::vector<ConcurrentMonitorElement>  Charge_Vs_PathlengthTOB;   /*!< Charge vs pathlength in TOB */
    std::vector<ConcurrentMonitorElement>  Charge_Vs_PathlengthTIDP;  /*!< Charge vs pathlength in TIDP */
    std::vector<ConcurrentMonitorElement>  Charge_Vs_PathlengthTIDM;  /*!< Charge vs pathlength in TIDM */
    std::vector<ConcurrentMonitorElement>  Charge_Vs_PathlengthTECP1; /*!< Charge vs pathlength in TECP thin */
    std::vector<ConcurrentMonitorElement>  Charge_Vs_PathlengthTECP2; /*!< Charge vs pathlength in TECP thick */
    std::vector<ConcurrentMonitorElement>  Charge_Vs_PathlengthTECM1; /*!< Charge vs pathlength in TECP thin */
    std::vector<ConcurrentMonitorElement>  Charge_Vs_PathlengthTECM2; /*!< Charge vs pathlength in TECP thick */
  };

};

#endif
