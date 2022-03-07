// -*- C++ -*-
//
// Package:    CalibTracker/SiPhase2TrackerESProducers
// Class:      SiPhase2BadStripConfigurableFakeESSource
//
/**\class SiPhase2BadStripConfigurableFakeESSource SiPhase2BadStripConfigurableFakeESSource.h CalibTracker/SiPhase2TrackerESProducers/plugins/SiPhase2BadStripConfigurableFakeESSource.cc

 Description: "fake" SiStripBadStrip ESProducer - configurable list of bad modules

 Implementation:
     Adapted to Phase-2 from CalibTracker/SiStripESProducers/plugins/fake/SiStripBadModuleConfigurableFakeESSource.cc
*/

// system include files
#include <memory>

// user include files
#include "CondFormats/DataRecord/interface/SiPhase2OuterTrackerCondDataRecords.h"
#include "CondFormats/SiStripObjects/interface/SiStripBadStrip.h"
#include "DataFormats/SiStripDetId/interface/SiStripDetId.h"
#include "DataFormats/SiStripDetId/interface/StripSubdetector.h"
#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/ESProducer.h"
#include "FWCore/Framework/interface/EventSetupRecordIntervalFinder.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/FileInPath.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "FWCore/Utilities/interface/RandomNumberGenerator.h"
#include "Geometry/CommonDetUnit/interface/PixelGeomDetUnit.h"
#include "Geometry/CommonTopologies/interface/PixelTopology.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/Records/interface/TrackerTopologyRcd.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"

class SiPhase2BadStripConfigurableFakeESSource : public edm::ESProducer, public edm::EventSetupRecordIntervalFinder {
public:
  SiPhase2BadStripConfigurableFakeESSource(const edm::ParameterSet&);
  ~SiPhase2BadStripConfigurableFakeESSource() override = default;

  void setIntervalFor(const edm::eventsetup::EventSetupRecordKey&,
                      const edm::IOVSyncValue& iov,
                      edm::ValidityInterval& iValidity) override;

  typedef std::unique_ptr<SiStripBadStrip> ReturnType;
  ReturnType produce(const SiPhase2OuterTrackerBadStripRcd&);

private:
  using Parameters = std::vector<edm::ParameterSet>;
  Parameters m_badComponentList;
  bool m_printDebug;
  edm::ESGetToken<TrackerTopology, TrackerTopologyRcd> trackTopoToken_;
  edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> geomToken_;

  std::vector<uint32_t> selectDetectors(const TrackerTopology* tTopo, const std::vector<uint32_t>& detIds) const;
};

SiPhase2BadStripConfigurableFakeESSource::SiPhase2BadStripConfigurableFakeESSource(const edm::ParameterSet& iConfig)
/* : trackTopoToken_(setWhatProduced(this).consumes())*/ {
  auto cc = setWhatProduced(this);
  trackTopoToken_ = cc.consumes();
  geomToken_ = cc.consumes();
  findingRecord<SiPhase2OuterTrackerBadStripRcd>();

  m_badComponentList = iConfig.getUntrackedParameter<Parameters>("BadComponentList");
  m_printDebug = iConfig.getUntrackedParameter<bool>("printDebug", false);
}

void SiPhase2BadStripConfigurableFakeESSource::setIntervalFor(const edm::eventsetup::EventSetupRecordKey&,
                                                              const edm::IOVSyncValue& iov,
                                                              edm::ValidityInterval& iValidity) {
  iValidity = edm::ValidityInterval{iov.beginOfTime(), iov.endOfTime()};
}

// ------------ method called to produce the data  ------------
SiPhase2BadStripConfigurableFakeESSource::ReturnType SiPhase2BadStripConfigurableFakeESSource::produce(
    const SiPhase2OuterTrackerBadStripRcd& iRecord) {
  using namespace edm::es;

  TrackerTopology const& tTopo = iRecord.get(trackTopoToken_);
  TrackerGeometry const& tGeom = iRecord.get(geomToken_);

  auto badStrips = std::make_unique<SiStripBadStrip>();

  /*
  if (!m_doByAPVs) {
    std::vector<uint32_t> selDetIds{selectDetectors(&tTopo, m_detInfo.getAllDetIds())};
    edm::LogInfo("SiStripQualityConfigurableFakeESSource")
        << "[produce] number of selected dets to be removed " << selDetIds.size() << std::endl;

    std::stringstream ss;
    for (const auto selId : selDetIds) {
      SiStripQuality::InputVector theSiStripVector;

      unsigned short firstBadStrip{0};
      unsigned short NconsecutiveBadStrips = m_detInfo.getNumberOfApvsAndStripLength(selId).first * 128;
      unsigned int theBadStripRange{quality->encode(firstBadStrip, NconsecutiveBadStrips)};

      if (m_printDebug) {
        ss << "detid " << selId << " \t"
           << " firstBadStrip " << firstBadStrip << "\t "
           << " NconsecutiveBadStrips " << NconsecutiveBadStrips << "\t "
           << " packed integer " << std::hex << theBadStripRange << std::dec << std::endl;
      }

      theSiStripVector.push_back(theBadStripRange);

      if (!quality->put(selId, SiStripBadStrip::Range{theSiStripVector.begin(), theSiStripVector.end()})) {
        edm::LogError("SiStripQualityConfigurableFakeESSource") << "[produce] detid already exists";
      }
    }
    if (m_printDebug) {
      edm::LogInfo("SiStripQualityConfigurableFakeESSource") << ss.str();
    }
    quality->cleanUp();
    //quality->fillBadComponents();
  } else {
    std::vector<std::pair<uint32_t, std::vector<uint32_t>>> selAPVs{selectAPVs()};
    edm::LogInfo("SiStripQualityConfigurableFakeESSource")
        << "[produce] number of selected dets to be removed " << selAPVs.size() << std::endl;

    std::stringstream ss;
    for (const auto& selId : selAPVs) {
      SiStripQuality::InputVector theSiStripVector;
      auto the_detid = selId.first;

      for (const auto apv : selId.second) {
        unsigned short firstBadStrip = apv * 128;
        unsigned short NconsecutiveBadStrips = 128;
        unsigned int theBadStripRange{quality->encode(firstBadStrip, NconsecutiveBadStrips)};

        if (m_printDebug) {
          ss << "detid " << the_detid << " \t"
             << " firstBadStrip " << firstBadStrip << "\t "
             << " NconsecutiveBadStrips " << NconsecutiveBadStrips << "\t "
             << " packed integer " << std::hex << theBadStripRange << std::dec << std::endl;
        }

        theSiStripVector.push_back(theBadStripRange);
      }

      if (!quality->put(the_detid, SiStripBadStrip::Range{theSiStripVector.begin(), theSiStripVector.end()})) {
        edm::LogError("SiStripQualityConfigurableFakeESSource") << "[produce] detid already exists";
      }
    }  // loop on the packed list of detid/apvs

    if (m_printDebug) {
      edm::LogInfo("SiStripQualityConfigurableFakeESSource") << ss.str();
    }
    quality->cleanUp();

  }  // do it by APVs

  if (m_printDebug) {
    std::stringstream ss1;
    for (const auto& badComp : quality->getBadComponentList()) {
      ss1 << "bad module " << badComp.detid << " " << badComp.BadModule << "\n";
    }
    edm::LogInfo("SiStripQualityConfigurableFakeESSource") << ss1.str();
  }
  */

  return badStrips;
}

namespace {
  bool _isSel(uint32_t requested,
              uint32_t i) {  // internal helper: accept all i if requested is 0, otherwise require match
    return (requested == 0) || (requested == i);
  }

  SiStripDetId::SubDetector subDetFromString(const std::string& subDetStr) {
    SiStripDetId::SubDetector subDet = SiStripDetId::UNKNOWN;
    if (subDetStr == "TIB")
      subDet = SiStripDetId::TIB;
    else if (subDetStr == "TID")
      subDet = SiStripDetId::TID;
    else if (subDetStr == "TOB")
      subDet = SiStripDetId::TOB;
    else if (subDetStr == "TEC")
      subDet = SiStripDetId::TEC;
    return subDet;
  }
}  // namespace

std::vector<uint32_t> SiPhase2BadStripConfigurableFakeESSource::selectDetectors(
    const TrackerTopology* tTopo, const std::vector<uint32_t>& detIds) const {
  std::vector<uint32_t> selList;
  std::stringstream ss;
  for (const auto& badComp : m_badComponentList) {
    const std::string subDetStr{badComp.getParameter<std::string>("SubDet")};
    if (m_printDebug)
      ss << "Bad SubDet " << subDetStr << " \t";
    const SiStripDetId::SubDetector subDet = subDetFromString(subDetStr);

    const std::vector<uint32_t> genericBadDetIds{
        badComp.getUntrackedParameter<std::vector<uint32_t>>("detidList", std::vector<uint32_t>())};
    const bool anySubDet{!genericBadDetIds.empty()};

    std::cout << "genericBadDetIds.size() = " << genericBadDetIds.size() << std::endl;

    using DetIdIt = std::vector<uint32_t>::const_iterator;
    const DetIdIt beginDetIt = std::lower_bound(
        detIds.begin(), detIds.end(), DetId(DetId::Tracker, anySubDet ? SiStripDetId::TIB : subDet).rawId());
    const DetIdIt endDetIt = std::lower_bound(
        detIds.begin(), detIds.end(), DetId(DetId::Tracker, anySubDet ? SiStripDetId::TEC + 1 : subDet + 1).rawId());

    if (anySubDet) {
      std::copy_if(beginDetIt, endDetIt, std::back_inserter(selList), [&genericBadDetIds](uint32_t detId) {
        std::cout << "AnySubDet" << detId << std::endl;
        return std::find(genericBadDetIds.begin(), genericBadDetIds.end(), detId) != genericBadDetIds.end();
      });
    } else {
      switch (subDet) {
        case SiStripDetId::TIB:
          std::copy_if(beginDetIt, endDetIt, std::back_inserter(selList), [tTopo, &badComp](uint32_t detectorId) {
            const DetId detId{detectorId};
            return ((detId.subdetId() == SiStripDetId::TIB) &&
                    _isSel(badComp.getParameter<uint32_t>("layer"), tTopo->tibLayer(detId)) &&
                    _isSel(badComp.getParameter<uint32_t>("bkw_frw"), tTopo->tibIsZPlusSide(detId) ? 2 : 1) &&
                    _isSel(badComp.getParameter<uint32_t>("int_ext"), tTopo->tibIsInternalString(detId) ? 1 : 2) &&
                    _isSel(badComp.getParameter<uint32_t>("ster"),
                           tTopo->tibIsStereo(detId) ? 1 : (tTopo->tibIsRPhi(detId) ? 2 : -1)) &&
                    _isSel(badComp.getParameter<uint32_t>("string_"), tTopo->tibString(detId)) &&
                    _isSel(badComp.getParameter<uint32_t>("detid"), detId.rawId()));
          });
          break;
        case SiStripDetId::TID:
          std::copy_if(beginDetIt, endDetIt, std::back_inserter(selList), [tTopo, &badComp](uint32_t detectorId) {
            const DetId detId{detectorId};
            return ((detId.subdetId() == SiStripDetId::TID) &&
                    _isSel(badComp.getParameter<uint32_t>("wheel"), tTopo->tidWheel(detId)) &&
                    _isSel(badComp.getParameter<uint32_t>("side"), tTopo->tidIsZPlusSide(detId) ? 2 : 1) &&
                    _isSel(badComp.getParameter<uint32_t>("ster"),
                           tTopo->tidIsStereo(detId) ? 1 : (tTopo->tidIsRPhi(detId) ? 2 : -1)) &&
                    _isSel(badComp.getParameter<uint32_t>("ring"), tTopo->tidRing(detId)) &&
                    _isSel(badComp.getParameter<uint32_t>("detid"), detId.rawId()));
          });
          break;
        case SiStripDetId::TOB:
          std::copy_if(beginDetIt, endDetIt, std::back_inserter(selList), [tTopo, &badComp](uint32_t detectorId) {
            const DetId detId{detectorId};
            return ((detId.subdetId() == SiStripDetId::TOB) &&
                    _isSel(badComp.getParameter<uint32_t>("layer"), tTopo->tobLayer(detId)) &&
                    _isSel(badComp.getParameter<uint32_t>("bkw_frw"), tTopo->tobIsZPlusSide(detId) ? 2 : 1) &&
                    _isSel(badComp.getParameter<uint32_t>("ster"),
                           tTopo->tobIsStereo(detId) ? 1 : (tTopo->tobIsRPhi(detId) ? 2 : -1)) &&
                    _isSel(badComp.getParameter<uint32_t>("rod"), tTopo->tobRod(detId)) &&
                    _isSel(badComp.getParameter<uint32_t>("detid"), detId.rawId()));
          });
          break;
        case SiStripDetId::TEC:
          std::copy_if(beginDetIt, endDetIt, std::back_inserter(selList), [tTopo, &badComp](uint32_t detectorId) {
            const DetId detId{detectorId};
            return ((detId.subdetId() == SiStripDetId::TEC) &&
                    _isSel(badComp.getParameter<uint32_t>("wheel"), tTopo->tecWheel(detId)) &&
                    _isSel(badComp.getParameter<uint32_t>("side"), tTopo->tecIsZPlusSide(detId) ? 2 : 1) &&
                    _isSel(badComp.getParameter<uint32_t>("ster"), tTopo->tecIsStereo(detId) ? 1 : 2) &&
                    _isSel(badComp.getParameter<uint32_t>("petal_bkw_frw"), tTopo->tecIsFrontPetal(detId) ? 2 : 2) &&
                    _isSel(badComp.getParameter<uint32_t>("petal"), tTopo->tecPetalNumber(detId)) &&
                    _isSel(badComp.getParameter<uint32_t>("ring"), tTopo->tecRing(detId)) &&
                    _isSel(badComp.getParameter<uint32_t>("detid"), detId.rawId()));
          });
          break;
        default:
          break;
      }
    }
  }
  if (m_printDebug) {
    edm::LogInfo("SiStripBadModuleGenerator") << ss.str();
  }
  return selList;
}

//define this as a plug-in
#include "FWCore/Framework/interface/SourceFactory.h"
DEFINE_FWK_EVENTSETUP_SOURCE(SiPhase2BadStripConfigurableFakeESSource);
