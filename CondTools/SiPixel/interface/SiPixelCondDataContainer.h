#ifndef CondTools_SiPixel_SiPixelCondDataContainer_h
#define CondTools_SiPixel_SiPixelCondDataContainer_h

// system includes
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <fmt/printf.h>

// user includes
#include "CalibTracker/StandaloneTrackerTopology/interface/StandaloneTrackerTopology.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelDetSummary.h"
#include "CondTools/SiPixel/interface/SiPixelCondDataItem.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "FWCore/Utilities/interface/Exception.h"

// ROOT includes
#include "TCanvas.h"
#include "TColor.h"
#include "TGaxis.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TLatex.h"
#include "TLegend.h"
#include "TLine.h"
#include "TPaveLabel.h"
#include "TProfile.h"
#include "TROOT.h"
#include "TStyle.h"

using namespace SiPixelCondObjectRepresent;

//used to produce all display objects for payload inspector
template <class Item, class type>
class SiPixelCondDataContainer {
public:
  SiPixelCondDataContainer(const std::shared_ptr<Item> &payload,
                           const SiPixelCondObjectRepresent::MetaData &metadata,
                           const std::string &tagname)
      : payload_(payload),
        run_(std::get<0>(metadata)),
        hash_(std::get<1>(metadata)),
        tagname_(tagname),
        m_trackerTopo(StandaloneTrackerTopology::fromTrackerParametersXMLFile(
            edm::FileInPath("Geometry/TrackerCommonData/data/trackerParameters.xml").fullPath())) {
    payloadType_ = std::string();
    granularity_ = SiPixelCondObjectRepresent::PER_PIXEL;
    plotMode_ = STANDARD;
    additionalIOV_ = std::make_tuple(-1, "", "");
  }

  virtual ~SiPixelCondDataContainer() = default;

  ///////////////// public get functions  /////////////////
  const unsigned int run() const { return run_; }
  const unsigned int run2() const { return std::get<0>(additionalIOV_); }
  const std::string &hash() const { return hash_; }
  const std::string &hash2() const { return std::get<1>(additionalIOV_); }
  const SiPixelCondObjectRepresent::MetaData metaData() const { return std::make_tuple(run_, hash_); }
  const std::string &tagName() const { return tagname_; }
  const std::string &tagName2() const { return std::get<2>(additionalIOV_); }
  const std::string &topoMode() const { return TopoMode_; }
  const std::string &payloadName() const { return payloadType_; }
  const plotType &getPlotType() const { return plotMode_; }
  const bool isMultiTag() { return (tagname_ != this->tagName2() && !(this->tagName2()).empty()); }

  void setPlotType(plotType myType) { plotMode_ = myType; }
  void setPayloadType(std::string myPayloadType) { payloadType_ = myPayloadType; }
  void setGranularity(granularity myGranularity) {
    granularity_ = myGranularity;

    switch (myGranularity) {
      case SiPixelCondObjectRepresent::PER_PIXEL:
        SiPixelCondData_.setGranularity(true, false);
        break;
      case SiPixelCondObjectRepresent::PER_ROC:
        SiPixelCondData_.setGranularity(false, true);
        break;
      case SiPixelCondObjectRepresent::PER_MODULE:
        SiPixelCondData_.setGranularity(false, false);
        break;
      default:
        edm::LogError("LogicError") << "Unknown granularity type: " << myGranularity;
    }
  }

  void setAdditionalIOV(const unsigned int run, const std::string &hash, const std::string &tagname) {
    std::get<0>(additionalIOV_) = run;
    std::get<1>(additionalIOV_) = hash;
    std::get<2>(additionalIOV_) = tagname;
  };

  ////NOTE to be implemented in PayloadInspector classes
  virtual void storeAllValues() {
    throw cms::Exception("Value definition not found")
        << "storeAllValues definition not found for " << payloadName() << "\n;";
  };

  SiPixelCondDataItem<type> siPixelCondData() { return SiPixelCondData_; }

  /***********************************************************************/
  const char *plotDescriptor()
  /***********************************************************************/
  {
    const char *thePlotType = "";
    switch (plotMode_) {
      case STANDARD:
        thePlotType = Form("Display - IOV: %i", run_);
        break;
      case COMPARISON:
        thePlotType = "Display";
        break;
      case DIFF:
        thePlotType = Form("#Delta (%i-%i)", run_, std::get<0>(additionalIOV_));
        break;
      case RATIO:
        thePlotType = Form("Ratio (%i/%i)", run_, std::get<0>(additionalIOV_));
        break;
      case MAP:
        thePlotType = Form("TrackerMap - %s", hash_.c_str());
        break;
      case END_OF_TYPES:
        edm::LogError("LogicError") << "Unknown plot type: " << plotMode_;
        break;
      default:
        edm::LogError("LogicError") << "Unknown plot type: " << plotMode_;
        break;
    }

    return thePlotType;
  }

  // all methods needed for comparison of 2 IOVs

  /***********************************************************************/
  void compare(SiPixelCondDataContainer *dataCont2)
  /***********************************************************************/
  {
    plotMode_ = COMPARISON;
    dataCont2->setPlotType(COMPARISON);
    SiPixelCondData_.setComparedBit();

    setAdditionalIOV(dataCont2->run(), dataCont2->hash(), dataCont2->tagName());

    if (!SiPixelCondData_.isCached())
      storeAllValues();
    dataCont2->storeAllValues();
    auto SiPixelCondData2_ = dataCont2->siPixelCondData();

    auto listOfDetIds = SiPixelCondData_.detIds(false);
    for (const auto &detId : listOfDetIds) {
      auto entriesToAdd = SiPixelCondData2_.data(detId);
      for (const auto &entry : entriesToAdd) {
        SiPixelCondData_.fillByPushBack(detId, entry);
      }
    }
  }

  /***********************************************************************/
  void divide(SiPixelCondDataContainer *dataCont2)
  /***********************************************************************/
  {
    plotMode_ = RATIO;
    dataCont2->setPlotType(RATIO);

    setAdditionalIOV(dataCont2->run(), dataCont2->hash(), dataCont2->tagName());

    if (!SiPixelCondData_.isCached())
      storeAllValues();
    dataCont2->storeAllValues();
    auto SiPixelCondData2_ = dataCont2->siPixelCondData();

    auto listOfDetIds = SiPixelCondData_.detIds(false);
    for (const auto &detId : listOfDetIds) {
      SiPixelCondData_.divide(detId, SiPixelCondData2_.data(detId));
    }
  }

  /***********************************************************************/
  void subtract(SiPixelCondDataContainer *dataCont2)
  /***********************************************************************/
  {
    plotMode_ = DIFF;
    dataCont2->setPlotType(DIFF);

    setAdditionalIOV(dataCont2->run(), dataCont2->hash(), dataCont2->tagName());

    if (!SiPixelCondData_.isCached())
      storeAllValues();
    dataCont2->storeAllValues();
    auto SiPixelCondData2_ = dataCont2->siPixelCondData();

    auto listOfDetIds = SiPixelCondData_.detIds(false);
    for (const auto &detId : listOfDetIds) {
      SiPixelCondData_.subtract(detId, SiPixelCondData2_.data(detId));
    }
  }

  /***********************************************************************/
  void printAll()
  /***********************************************************************/
  {
    if (!SiPixelCondData_.isCached())
      storeAllValues();
    auto listOfDetIds = SiPixelCondData_.detIds(false);
    for (const auto &detId : listOfDetIds) {
      std::cout << detId << ": ";
      auto values = SiPixelCondData_.data(detId);
      for (const auto &value : values) {
        std::cout << value << " ";
      }
      std::cout << "\n";
    }
  }

protected:
  std::shared_ptr<Item> payload_;
  std::string payloadType_;
  SiPixelCondDataItem<type> SiPixelCondData_;

private:
  unsigned int run_;
  std::string hash_;
  std::string tagname_;
  granularity granularity_;
  std::string TopoMode_;
  TrackerTopology m_trackerTopo;
  SiPixelDetSummary summary{0};
  // "Map", "Ratio", or "Diff"
  plotType plotMode_;
  std::tuple<int, std::string, std::string> additionalIOV_;

  std::map<std::string, std::string> units_ = {{"SiPixelPedestals", "[ADC counts]"},
                                               {"SiPixelApvGain", ""},  //dimensionless TODO: verify
                                               {"SiPixelNoises", "[ADC counts]"},
                                               {"SiPixelLorentzAngle", "[1/T}]"},
                                               {"SiPixelBackPlaneCorrection", ""},
                                               {"SiPixelBadPixel", ""},  // dimensionless
                                               {"SiPixelDetVOff", ""}};  // dimensionless

  std::string opType(SiPixelCondObjectRepresent::OpMode mode) {
    std::string types[3] = {"Pixel", "ROC", "Module"};
    return types[mode];
  }
};

#endif
