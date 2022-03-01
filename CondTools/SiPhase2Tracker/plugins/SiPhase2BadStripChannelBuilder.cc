// system include files
#include <vector>
#include <memory>
#include <iostream>
#include <fstream>

// user include files
#include "CommonTools/ConditionDBWriter/interface/ConditionDBWriter.h"
#include "CondFormats/SiStripObjects/interface/SiStripBadStrip.h"
#include "DataFormats/SiStripDetId/interface/StripSubdetector.h"
#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"
#include "FWCore/Framework/interface/ESHandle.h"
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

#include "CLHEP/Random/RandFlat.h"
#include "CLHEP/Random/RandGauss.h"

class SiPhase2BadStripChannelBuilder : public ConditionDBWriter<SiStripBadStrip> {
public:
  explicit SiPhase2BadStripChannelBuilder(const edm::ParameterSet&);
  ~SiPhase2BadStripChannelBuilder() override = default;

private:
  std::unique_ptr<SiStripBadStrip> getNewObject() override;

  void algoBeginRun(const edm::Run& run, const edm::EventSetup& es) override {
    if (!tTopo_) {
      tTopo_ = std::make_unique<TrackerTopology>(es.getData(topoToken_));
      tGeom_ = std::make_unique<TrackerGeometry>(es.getData(geomToken_));
    }
  };

  void algoAnalyze(const edm::Event& event, const edm::EventSetup& es) override {
    edm::Service<edm::RandomNumberGenerator> rng;
    if (!engine) {
      engine = &rng->getEngine(event.streamID());
    }
  }

  std::unique_ptr<TrackerTopology> tTopo_;
  std::unique_ptr<TrackerGeometry> tGeom_;
  CLHEP::HepRandomEngine* engine;

  bool printdebug_;
  typedef std::vector<edm::ParameterSet> Parameters;
  Parameters BadComponentList_;

  // ----------member data ---------------------------
  const edm::ESGetToken<TrackerTopology, TrackerTopologyRcd> topoToken_;
  const edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> geomToken_;
};

//__________________________________________________________________________________________________
SiPhase2BadStripChannelBuilder::SiPhase2BadStripChannelBuilder(const edm::ParameterSet& iConfig)
    : ConditionDBWriter<SiStripBadStrip>(iConfig),
      topoToken_(esConsumes<edm::Transition::BeginRun>()),
      geomToken_(esConsumes<edm::Transition::BeginRun>()) {
  printdebug_ = iConfig.getUntrackedParameter<bool>("printDebug", false);
  //BadComponentList_ = iConfig.getUntrackedParameter<Parameters>("BadComponentList");
}

//__________________________________________________________________________________________________
std::unique_ptr<SiStripBadStrip> SiPhase2BadStripChannelBuilder::getNewObject() {
  using Phase2TrackerGeomDetUnit = PixelGeomDetUnit;
  edm::LogInfo("SiPhase2BadStripChannelBuilder") << "... creating dummy SiStripBadStrip Data" << std::endl;

  auto obj = std::make_unique<SiStripBadStrip>();

  edm::LogInfo("SiPhase2BadStripChannelBuilder")
      << " There are " << tGeom_->detUnits().size() << " modules in this geometry." << std::endl;

  for (auto const& det_u : tGeom_->detUnits()) {
    const DetId detid = det_u->geographicalId();
    uint32_t rawId = detid.rawId();
    int subid = detid.subdetId();
    if (detid.det() == DetId::Detector::Tracker) {
      const Phase2TrackerGeomDetUnit* pixdet = dynamic_cast<const Phase2TrackerGeomDetUnit*>(det_u);
      assert(pixdet);
      LogDebug("SiPhase2BadStripChannelBuilder") << rawId << " is a " << subid << " det" << std::endl;
      if (subid == StripSubdetector::TOB || subid == StripSubdetector::TID) {
        if (tGeom_->getDetectorType(rawId) == TrackerGeometry::ModuleType::Ph2PSS ||
            tGeom_->getDetectorType(rawId) == TrackerGeometry::ModuleType::Ph2SS) {
          const PixelTopology& topol(pixdet->specificTopology());
          std::cout << "DetId: " << rawId << " subdet: " << subid << " nrows: " << topol.nrows()
                    << " ncols: " << topol.ncolumns() << std::endl;

          std::vector<unsigned int> theSiStripVector;
          unsigned short firstBadStrip = std::floor(CLHEP::RandFlat::shoot(engine, 0, topol.nrows()));
          unsigned short NconsecutiveBadStrips = std::floor(CLHEP::RandFlat::shoot(engine, 1, 10));

          // if the interval exceeds the end of the module
          if (firstBadStrip + NconsecutiveBadStrips > topol.nrows()) {
            NconsecutiveBadStrips = topol.nrows() - firstBadStrip;
          }

          unsigned int theBadStripRange;

          theBadStripRange = obj->encode(firstBadStrip, NconsecutiveBadStrips);

          if (printdebug_)
            edm::LogInfo("SiPhase2BadStripChannelBuilder")
                << "detid " << rawId << " \t"
                << " firstBadStrip " << firstBadStrip << "\t "
                << " NconsecutiveBadStrips " << NconsecutiveBadStrips << "\t "
                << " packed integer " << std::hex << theBadStripRange << std::dec << std::endl;

          theSiStripVector.push_back(theBadStripRange);

          SiStripBadStrip::Range range(theSiStripVector.begin(), theSiStripVector.end());
          if (!obj->put(rawId, range))
            edm::LogError("SiPhase2BadStripChannelBuilder")
                << "[SiPhase2BadStripChannelBuilder::getNewObject] detid already exists" << std::endl;

        }  // if it's a Strip module
      }    // if it's OT
    }      // if it's Tracker
  }        // loop of geomdets

  //End now write sistripbadChannel data in DB
  edm::Service<cond::service::PoolDBOutputService> mydbservice;

  if (mydbservice.isAvailable()) {
    if (mydbservice->isNewTagRequest("SiStripBadStripRcd")) {
      mydbservice->createOneIOV<SiStripBadStrip>(*obj, mydbservice->beginOfTime(), "SiStripBadStripRcd");
    } else {
      mydbservice->appendOneIOV<SiStripBadStrip>(*obj, mydbservice->currentTime(), "SiStripBadStripRcd");
    }
  } else {
    edm::LogError("SiPhase2BadStripChannelBuilder") << "Service is unavailable" << std::endl;
  }

  tGeom_.release();

  /*
  for (Parameters::iterator iBadComponent = BadComponentList_.begin(); iBadComponent != BadComponentList_.end();
       ++iBadComponent) {
    uint32_t BadModule_ = iBadComponent->getParameter<uint32_t>("BadModule");
    std::vector<uint32_t> BadChannelList_ = iBadComponent->getParameter<std::vector<uint32_t> >("BadChannelList");

    std::vector<unsigned int> theSiStripVector;
    unsigned int NStrips = detInfo.getNumberOfApvsAndStripLength(BadModule_).first * 128;

    uint32_t lastBad = 999;
    unsigned short firstBadStrip = 0, NconsecutiveBadStrips = 0;
    unsigned int theBadStripRange;

    for (std::vector<uint32_t>::const_iterator is = BadChannelList_.begin(); is != BadChannelList_.end(); ++is) {
      if (*is > NStrips - 1)
        break;
      if (*is != lastBad + 1) {
        //new set

        if (lastBad != 999) {
          //save previous set
          theBadStripRange = obj->encode(firstBadStrip, NconsecutiveBadStrips);

          if (printdebug_)
            edm::LogInfo("SiPhase2BadStripChannelBuilder")
                << "detid " << BadModule_ << " \t"
                << " firstBadStrip " << firstBadStrip << "\t "
                << " NconsecutiveBadStrips " << NconsecutiveBadStrips << "\t "
                << " packed integer " << std::hex << theBadStripRange << std::dec << std::endl;

          theSiStripVector.push_back(theBadStripRange);
        }

        firstBadStrip = *is;
        NconsecutiveBadStrips = 0;
      }
      NconsecutiveBadStrips++;
      lastBad = *is;
    }

    theBadStripRange = obj->encode(firstBadStrip, NconsecutiveBadStrips);
    if (printdebug_)
      edm::LogInfo("SiPhase2BadStripChannelBuilder")
          << "detid " << BadModule_ << " \t"
          << " firstBadStrip " << firstBadStrip << "\t "
          << " NconsecutiveBadStrips " << NconsecutiveBadStrips << "\t "
          << " packed integer " << std::hex << theBadStripRange << std::dec << std::endl;

    theSiStripVector.push_back(theBadStripRange);

    SiStripBadStrip::Range range(theSiStripVector.begin(), theSiStripVector.end());
    if (!obj->put(BadModule_, range))
      edm::LogError("SiPhase2BadStripChannelBuilder")
          << "[SiPhase2BadStripChannelBuilder::analyze] detid already exists" << std::endl;
  }
  */

  return obj;
}

#include "FWCore/PluginManager/interface/ModuleDef.h"
#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE(SiPhase2BadStripChannelBuilder);
