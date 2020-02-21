// -*- C++ -*-
//
// Package:    CondTools/SiStrip
// Class:      SiStripChannelGainMultiIOVFixer
//
/**\class SiStripChannelGainMultiIOVFixer SiStripChannelGainMultiIOVFixer.cc CondTools/SiStrip/plugins/SiStripChannelGainMultiIOVFixer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Marco Musich
//         Created:  Wed, 21 Dec 2016 12:50:51 GMT
//
//

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/ESWatcher.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "CondFormats/RunInfo/interface/RunInfo.h"
#include "CondFormats/SiStripObjects/interface/SiStripApvGain.h"
#include "CondFormats/DataRecord/interface/SiStripApvGainRcd.h"
#include "CalibFormats/SiStripObjects/interface/SiStripGain.h"
#include "CalibTracker/Records/interface/SiStripGainRcd.h"
#include "CondCore/DBOutputService/interface/PoolDBOutputService.h"
#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/Records/interface/TrackerTopologyRcd.h"
#include "CalibFormats/SiStripObjects/interface/SiStripQuality.h"
#include "CalibTracker/Records/interface/SiStripQualityRcd.h"
#include "CalibTracker/Records/interface/SiStripDetCablingRcd.h"
#include "CalibFormats/SiStripObjects/interface/SiStripDetCabling.h"

// ROOT includes

#include "TFile.h"
#include "TFile.h"
#include "TH1D.h"
#include "TH1I.h"
#include "TH2D.h"
#include "TGraph.h"
#include "TGraphErrors.h"

#include <sstream>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <math.h>
#include <string>
#include <vector>

#define DEBUG 0

//
// constants, enums and typedefs
//
using packedTopo = std::pair<int, std::pair<int, int> >;

std::string detnames[7] = {"", "BPix", "FPix", "TIB", "TID", "TOB", "TEC"};
std::ostream& operator<<(std::ostream& ofs, const packedTopo& pt) {
  if (pt.first % 2 == 1) {
    ofs << "( " << detnames[pt.first].c_str() << " , layer " << pt.second.first << " )";
  } else {
    ofs << "( " << detnames[pt.first].c_str() << " , disk " << pt.second.first << " , side " << pt.second.second
        << " )";
  }
  return ofs;  // Note: the stream operator << returns ostream not ofstream
}

// add new entries before NUM_OF_TYPES
// otherwise will screw up the counts

namespace partitions {
  enum layers {
    TIB,
    TIBL1,
    TIBL2,
    TIBL3,
    TIBL4,
    TOB,
    TOBL1,
    TOBL2,
    TOBL3,
    TOBL4,
    TOBL5,
    TOBL6,
    TIDP,
    TIDM,
    TIDPD1,
    TIDPD2,
    TIDPD3,
    TIDMD1,
    TIDMD2,
    TIDMD3,
    TECP,
    TECM,
    NUM_OF_TYPES
  };
}

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class SiStripChannelGainMultiIOVFixer : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit SiStripChannelGainMultiIOVFixer(const edm::ParameterSet&);
  ~SiStripChannelGainMultiIOVFixer();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  virtual void beginJob() override;
  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
  virtual void endJob() override;
  std::string getStringFromEnum(partitions::layers e);
  std::unique_ptr<SiStripApvGain> getNewObject(const std::map<std::pair<uint32_t, int>, float>& theMap);
  packedTopo typeAndLayerFromDetId(const DetId& detId, const TrackerTopology* tTopo) const;

  // ----------member data ---------------------------
  const std::string m_Record;
  const uint32_t m_gainType;
  const double m_threshold;
  const double m_target;

  edm::Service<TFileService> fs;

  std::auto_ptr<std::ofstream> output_;
  int IOVcount_;
  int lastRun_;

  edm::ESWatcher<SiStripApvGain2Rcd> G2watcher_;
};

//
// static data member definitions
//

//
// constructors and destructor
//
SiStripChannelGainMultiIOVFixer::SiStripChannelGainMultiIOVFixer(const edm::ParameterSet& iConfig)
    : m_Record{iConfig.getUntrackedParameter<std::string>("record", "SiStripApvGainRcd")},
      m_gainType{iConfig.getUntrackedParameter<uint32_t>("gainType", 1)},
      m_threshold{iConfig.getUntrackedParameter<double>("threshold", 3.)},
      m_target{iConfig.getUntrackedParameter<double>("target", 1.)} {
  //now do what ever initialization is needed
  usesResource("TFileService");
  IOVcount_ = 0;
  lastRun_ = 0;
}

SiStripChannelGainMultiIOVFixer::~SiStripChannelGainMultiIOVFixer() {}

//
// member functions
//

// ------------ method called for each event  ------------
void SiStripChannelGainMultiIOVFixer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;

  //Retrieve tracker topology from geometry
  edm::ESHandle<TrackerTopology> tTopoHandle;
  iSetup.get<TrackerTopologyRcd>().get(tTopoHandle);
  const TrackerTopology* tTopo = tTopoHandle.product();

  int run = iEvent.id().run();

  if (run > lastRun_)
    lastRun_ = run;
  bool hasG2IOV = G2watcher_.check(iSetup);

  if (hasG2IOV) {
    std::cout << " G2 has a new IOV for run: " << iEvent.id().run() << std::endl;

    edm::ESHandle<SiStripGain> SiStripApvGain_;
    iSetup.get<SiStripGainRcd>().get(SiStripApvGain_);

    std::vector<uint32_t> detid;
    SiStripApvGain_->getDetIds(detid);

    std::map<std::pair<uint32_t, int>, float> theMap, oldPayloadMap;

    for (const auto& d : detid) {
      const auto range = SiStripApvGain_->getRange(d, m_gainType);
      const auto gainRange = SiStripApvGain_->getRange(d);

      const auto& info = typeAndLayerFromDetId(d, tTopo);
      float nAPV = 0;

      for (int it = 0; it < range.second - range.first; it++) {
        nAPV += 1;
        float Gain = SiStripApvGain_->getApvGain(it, range);
        float totalGain = SiStripApvGain_->getApvGain(it, gainRange);

        std::pair<uint32_t, int> index = std::make_pair(d, nAPV);

        oldPayloadMap[index] = Gain;

        if (Gain > m_threshold) {
          std::cout << d << ", APV " << nAPV << ": G2 Gain = " << Gain << " Total Gain = " << totalGain << " | "
                    << tTopo->print(d) << std::endl;  //info << std::endl;
          theMap[index] = m_target;
        } else {
          theMap[index] = Gain;
        }
      }  // loop over APVs
    }    // loop over DetIds

    std::unique_ptr<SiStripApvGain> theAPVGains = this->getNewObject(theMap);

    // write out the APVGains record
    edm::Service<cond::service::PoolDBOutputService> poolDbService;

    if (poolDbService.isAvailable())
      poolDbService->writeOne(theAPVGains.get(), poolDbService->currentTime(), m_Record);
    else
      throw std::runtime_error("PoolDBService required.");

    // increase the IOV counter
    IOVcount_++;

  }  // if there is a new IOV
}

// ------------ method called once each job just before starting event loop  ------------
void SiStripChannelGainMultiIOVFixer::beginJob() {}

// ------------ method called once each job just after ending the event loop  ------------
void SiStripChannelGainMultiIOVFixer::endJob() {}

// -------------- method to get the topology from the detID ------------------------------
packedTopo SiStripChannelGainMultiIOVFixer::typeAndLayerFromDetId(const DetId& detId,
                                                                  const TrackerTopology* tTopo) const {
  int layerNumber = 0;
  int sideNumber = 0;
  unsigned int subdetId = static_cast<unsigned int>(detId.subdetId());

  if (subdetId == SiStripSubdetector::TIB) {
    layerNumber = tTopo->tibLayer(detId.rawId());
    sideNumber = tTopo->tibSide(detId.rawId());
  } else if (subdetId == SiStripSubdetector::TOB) {
    layerNumber = tTopo->tobLayer(detId.rawId());
    sideNumber = tTopo->tobSide(detId.rawId());
  } else if (subdetId == SiStripSubdetector::TID) {
    layerNumber = tTopo->tidWheel(detId.rawId());
    sideNumber = tTopo->tidSide(detId.rawId());
  } else if (subdetId == SiStripSubdetector::TEC) {
    layerNumber = tTopo->tecWheel(detId.rawId());
    sideNumber = tTopo->tecSide(detId.rawId());
  } else if (subdetId == PixelSubdetector::PixelBarrel) {
    layerNumber = tTopo->pxbLayer(detId.rawId());
  } else if (subdetId == PixelSubdetector::PixelEndcap) {
    layerNumber = tTopo->pxfDisk(detId.rawId());
    sideNumber = tTopo->pxfSide(detId.rawId());
  } else
    edm::LogWarning("LogicError") << "Unknown subdetid: " << subdetId;

  return std::make_pair(subdetId, std::make_pair(layerNumber, sideNumber));
}

// -------------- method to get the topology from the detID ------------------------------
std::string SiStripChannelGainMultiIOVFixer::getStringFromEnum(partitions::layers e) {
  switch (e) {
    case partitions::TIB:
      return "TIB";
    case partitions::TIBL1:
      return "TIB L1";
    case partitions::TIBL2:
      return "TIB L2";
    case partitions::TIBL3:
      return "TIB L3";
    case partitions::TIBL4:
      return "TIB L4";
    case partitions::TOB:
      return "TOB";
    case partitions::TOBL1:
      return "TOB L1";
    case partitions::TOBL2:
      return "TOB L2";
    case partitions::TOBL3:
      return "TOB L3";
    case partitions::TOBL4:
      return "TOB L4";
    case partitions::TOBL5:
      return "TOB L5";
    case partitions::TOBL6:
      return "TOB L6";
    case partitions::TIDP:
      return "TIDplus";
    case partitions::TIDM:
      return "TIDminus";
    case partitions::TIDPD1:
      return "TID plus Disk 1";
    case partitions::TIDPD2:
      return "TID plus Disk 2";
    case partitions::TIDPD3:
      return "TID plus Disk 3";
    case partitions::TIDMD1:
      return "TID minus Disk 1";
    case partitions::TIDMD2:
      return "TID minus Disk 2";
    case partitions::TIDMD3:
      return "TID minus Disk 3";
    case partitions::TECP:
      return "TECplus";
    case partitions::TECM:
      return "TECminus";
    default:
      edm::LogWarning("LogicError") << "Unknown partition: " << e;
      return "";
  }
}

//********************************************************************************//
std::unique_ptr<SiStripApvGain> SiStripChannelGainMultiIOVFixer::getNewObject(
    const std::map<std::pair<uint32_t, int>, float>& theMap) {
  std::unique_ptr<SiStripApvGain> obj = std::unique_ptr<SiStripApvGain>(new SiStripApvGain());

  std::vector<float> theSiStripVector;
  uint32_t PreviousDetId = 0;
  for (const auto& element : theMap) {
    uint32_t DetId = element.first.first;
    if (DetId != PreviousDetId) {
      if (!theSiStripVector.empty()) {
        SiStripApvGain::Range range(theSiStripVector.begin(), theSiStripVector.end());
        if (!obj->put(PreviousDetId, range))
          printf("Bug to put detId = %i\n", PreviousDetId);
      }
      theSiStripVector.clear();
      PreviousDetId = DetId;
    }
    theSiStripVector.push_back(element.second);

    edm::LogInfo("SiStripChannelGainFromDBMiscalibrator")
        << " DetId: " << DetId << " APV:   " << element.first.second << " Gain:  " << element.second << std::endl;
  }

  if (!theSiStripVector.empty()) {
    SiStripApvGain::Range range(theSiStripVector.begin(), theSiStripVector.end());
    if (!obj->put(PreviousDetId, range))
      printf("Bug to put detId = %i\n", PreviousDetId);
  }

  return obj;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void SiStripChannelGainMultiIOVFixer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SiStripChannelGainMultiIOVFixer);
