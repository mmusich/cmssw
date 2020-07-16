// -*- C++ -*-
//
// Package:    Tools/SiPixelGainCalibScaler
// Class:      SiPixelGainCalibScaler
//
/**\class SiPixelGainCalibScaler SiPixelGainCalibScaler.cc Tools/SiPixelGainCalibScaler/plugins/SiPixelGainCalibScaler.cc

 Description: Scales Pixel Gain Payloads by applying the VCal offset and slopes.

 Implementation:
     Makes use of trick to loop over all IOVs in a tag by running on all the runs with EmptySource and just access DB once the IOV has changed via ESWatcher mechanism
*/
//
// Original Author:  Marco Musich
//         Created:  Thu, 16 Jul 2020 10:36:21 GMT
//
//

// system include files
#include <memory>

// user include files
#include "CalibTracker/StandaloneTrackerTopology/interface/StandaloneTrackerTopology.h"
#include "CondCore/DBOutputService/interface/PoolDBOutputService.h"
#include "CondFormats/DataRecord/interface/SiPixelGainCalibrationForHLTRcd.h"
#include "CondFormats/DataRecord/interface/SiPixelGainCalibrationOfflineRcd.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelGainCalibrationOffline.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelGainCalibrationForHLT.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/SiPixelDetId/interface/PixelSubdetector.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"
#include "FWCore/Framework/interface/ESWatcher.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "Geometry/CommonDetUnit/interface/PixelGeomDetUnit.h"
#include "Geometry/CommonTopologies/interface/PixelTopology.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/Records/interface/TrackerTopologyRcd.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<>
// This will improve performance in multithreaded jobs.

class SiPixelGainCalibScaler : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit SiPixelGainCalibScaler(const edm::ParameterSet&);
  ~SiPixelGainCalibScaler() override;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void beginJob() override;
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override;
  template <class tokenType, class PayloadType>
  void computeAndStorePalyoads(const edm::EventSetup& iSetup, const tokenType& token);

  // ----------member data ---------------------------
  std::string recordName_;
  bool isForHLT_;
  double conversionFactor_;
  double conversionFactorL1_;
  double offset_;
  double offsetL1_;
  bool verbose_;

  edm::ESGetToken<SiPixelGainCalibrationForHLT, SiPixelGainCalibrationForHLTRcd> gainHLTCalibToken_;
  edm::ESGetToken<SiPixelGainCalibrationOffline, SiPixelGainCalibrationOfflineRcd> gainOfflineCalibToken_;

  edm::ESWatcher<SiPixelGainCalibrationForHLTRcd> pixelHLTGainWatcher_;
  edm::ESWatcher<SiPixelGainCalibrationOfflineRcd> pixelOfflineGainWatcher_;
};

//
// constructors and destructor
//
SiPixelGainCalibScaler::SiPixelGainCalibScaler(const edm::ParameterSet& iConfig)
    : recordName_(iConfig.getParameter<std::string>("record")),
      isForHLT_(iConfig.getParameter<bool>("isForHLT")),
      conversionFactor_(iConfig.getParameter<double>("conversionFactor")),
      conversionFactorL1_(iConfig.getParameter<double>("conversionFactorL1")),
      offset_(iConfig.getParameter<double>("offset")),
      offsetL1_(iConfig.getParameter<double>("offsetL1")),
      verbose_(iConfig.getUntrackedParameter<bool>("verbose", false)) {
  gainHLTCalibToken_ = esConsumes<SiPixelGainCalibrationForHLT, SiPixelGainCalibrationForHLTRcd>();
  gainOfflineCalibToken_ = esConsumes<SiPixelGainCalibrationOffline, SiPixelGainCalibrationOfflineRcd>();
}

SiPixelGainCalibScaler::~SiPixelGainCalibScaler() {}

//
// member functions
//

// ------------ method called for each event  ------------
void SiPixelGainCalibScaler::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;

  int run = iEvent.id().run();
  bool hasPixelHLTGainIOV = pixelHLTGainWatcher_.check(iSetup);
  bool hasPixelOfflineGainIOV = pixelOfflineGainWatcher_.check(iSetup);

  if ((hasPixelHLTGainIOV && isForHLT_) || (hasPixelOfflineGainIOV && !isForHLT_)) {
    edm::LogPrint("SiPixelGainCalibScaler") << " Pixel Gains have a new IOV for run: " << run << std::endl;

    if (isForHLT_) {
      computeAndStorePalyoads<edm::ESGetToken<SiPixelGainCalibrationForHLT, SiPixelGainCalibrationForHLTRcd>,
                              SiPixelGainCalibrationForHLT>(iSetup, gainHLTCalibToken_);
    } else {
      computeAndStorePalyoads<edm::ESGetToken<SiPixelGainCalibrationOffline, SiPixelGainCalibrationOfflineRcd>,
                              SiPixelGainCalibrationOffline>(iSetup, gainOfflineCalibToken_);
    }
  }  // if new IOV
}

// ------------ template method to construct the payloads  ------------
template <class tokenType, class PayloadType>
void SiPixelGainCalibScaler::computeAndStorePalyoads(const edm::EventSetup& iSetup, const tokenType& token) {
  // if need the ESHandle to check if the SetupData was there or not
  auto payload = iSetup.getHandle(token);
  std::vector<uint32_t> detids;
  payload->getDetIds(detids);

  float mingain = payload->getGainLow();
  float maxgain = (payload->getGainHigh()) * conversionFactorL1_;
  float minped = payload->getPedLow();
  float maxped = payload->getPedHigh() * 1.10;

  auto SiPixelGainCalibration_ = new PayloadType(minped, maxped, mingain, maxgain);

  //Retrieve tracker topology from geometry
  edm::ESHandle<TrackerTopology> tTopoHandle;
  iSetup.get<TrackerTopologyRcd>().get(tTopoHandle);
  const TrackerTopology* tTopo = tTopoHandle.product();

  //const char* path_toTopologyXML = "Geometry/TrackerCommonData/data/PhaseI/trackerParameters.xml";
  //TrackerTopology tTopo = StandaloneTrackerTopology::fromTrackerParametersXMLFile(edm::FileInPath(path_toTopologyXML).fullPath());

  for (const auto& d : detids) {
    bool isLayer1 = false;
    int subid = DetId(d).subdetId();
    if (subid == PixelSubdetector::PixelBarrel) {
      auto layer = tTopo->pxbLayer(DetId(d));
      if (layer == 1) {
        isLayer1 = true;
      }
    }

    std::vector<char> theSiPixelGainCalibration;

    auto range = payload->getRange(d);
    int numberOfRowsToAverageOver = payload->getNumberOfRowsToAverageOver();
    int ncols = payload->getNCols(d);
    int nRocsInRow = (range.second - range.first) / ncols / numberOfRowsToAverageOver;
    unsigned int nRowsForHLT = 1;
    int nrows = std::max((payload->getNumberOfRowsToAverageOver() * nRocsInRow),
                         nRowsForHLT);  // dirty trick to make it work for the HLT payload

    auto rangeAndCol = payload->getRangeAndNCols(d);
    bool isDeadColumn;
    bool isNoisyColumn;

    if (verbose_) {
      edm::LogVerbatim("SiPixelGainCalibScaler")
          << "NCOLS: " << payload->getNCols(d) << " " << rangeAndCol.second << " NROWS:" << nrows
          << ", RANGES: " << rangeAndCol.first.second - rangeAndCol.first.first
          << ", Ratio: " << float(rangeAndCol.first.second - rangeAndCol.first.first) / rangeAndCol.second << std::endl;
    }

    for (int col = 0; col < ncols; col++) {
      for (int row = 0; row < nrows; row++) {
        float gain = payload->getGain(col, row, rangeAndCol.first, rangeAndCol.second, isDeadColumn, isNoisyColumn);
        float ped = payload->getPed(col, row, rangeAndCol.first, rangeAndCol.second, isDeadColumn, isNoisyColumn);

        if (verbose_)
          edm::LogInfo("SiPixelGainCalibScaler") << "pre-change gain: " << gain << " pede:" << ped << std::endl;

        //
        // From here https://github.com/cms-sw/cmssw/blob/master/CalibTracker/SiPixelESProducers/src/SiPixelGainCalibrationForHLTService.cc#L20-L47
        //
        // vcal = ADC * DBgain - DBped * DBgain
        // electrons = vcal * conversionFactor + offset
        //
        // follows:
        // electrons = (ADC*DBgain – DBped*DBgain)*conversionFactor + offset
        // electrons = ADC*conversionFactor*DBgain - conversionFactor*DBped*DBgain + offset
        //
        // this should equal the new equation:
        //
        // electrons = ADC*DBgain' - DBPed' * DBgain'
        //
        // So equating piece by piece:
        //
        // DBgain' = conversionFactor*DBgain
        // DBped' = (conversionFactor*DBped*Dbgain – offset)/(conversionFactor*DBgain)
        //        = DBped - offset/DBgain'
        //

        if (isLayer1) {
          gain = gain * conversionFactorL1_;
          ped = ped - offsetL1_ / gain;
        } else {
          gain = gain * conversionFactor_;
          ped = ped - offset_ / gain;
        }

        if (verbose_)
          edm::LogInfo("SiPixelGainCalibScaler") << "post-change gain: " << gain << " pede:" << ped << std::endl;

        if constexpr (std::is_same_v<PayloadType, SiPixelGainCalibrationForHLT>) {
          SiPixelGainCalibration_->setData(ped, gain, theSiPixelGainCalibration, false, false);
        } else {
          SiPixelGainCalibration_->setDataPedestal(ped, theSiPixelGainCalibration);
          if ((row + 1) % numberOfRowsToAverageOver == 0) {  // fill the column average after every ROC!
            SiPixelGainCalibration_->setDataGain(gain, numberOfRowsToAverageOver, theSiPixelGainCalibration);
          }
        }
      }  // loop on rows
    }    // loop on columns

    typename PayloadType::Range outrange(theSiPixelGainCalibration.begin(), theSiPixelGainCalibration.end());
    if (!SiPixelGainCalibration_->put(d, outrange, ncols))
      edm::LogError("SiPixelGainCalibScaler") << "[SiPixelGainCalibScaler::analyze] detid already exists" << std::endl;
  }  // loop on DetIds

  // Write into DB
  edm::LogInfo(" --- writing to DB!");
  edm::Service<cond::service::PoolDBOutputService> mydbservice;
  if (!mydbservice.isAvailable()) {
    edm::LogError("db service unavailable");
    return;
  } else {
    edm::LogInfo("DB service OK");
  }

  try {
    if (mydbservice->isNewTagRequest(recordName_)) {
      mydbservice->createNewIOV<PayloadType>(
          SiPixelGainCalibration_, mydbservice->beginOfTime(), mydbservice->endOfTime(), recordName_);
    } else {
      mydbservice->appendSinceTime<PayloadType>(SiPixelGainCalibration_, mydbservice->currentTime(), recordName_);
    }
    edm::LogInfo(" --- all OK");
  } catch (const cond::Exception& er) {
    edm::LogError("SiPixelGainCalibScaler") << er.what() << std::endl;
  } catch (const std::exception& er) {
    edm::LogError("SiPixelGainCalibScaler") << "caught std::exception " << er.what() << std::endl;
  } catch (...) {
    edm::LogError("SiPixelGainCalibScaler") << "Funny error" << std::endl;
  }
}

// ------------ method called once each job just before starting event loop  ------------
void SiPixelGainCalibScaler::beginJob() {}

// ------------ method called once each job just after ending the event loop  ------------
void SiPixelGainCalibScaler::endJob() {}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void SiPixelGainCalibScaler::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<std::string>("record", "SiPixelGainCalibrationForHLTRcd");
  desc.add<bool>("isForHLT", true);
  desc.add<double>("conversionFactor", 47.);
  desc.add<double>("conversionFactorL1", 50.);
  desc.add<double>("offset", -60.);
  desc.add<double>("offsetL1", -670.);
  desc.add<bool>("verbose", false);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SiPixelGainCalibScaler);
