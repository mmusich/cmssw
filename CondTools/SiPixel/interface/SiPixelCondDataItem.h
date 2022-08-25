#ifndef CondTools_SiPixel_SiPixelCondDataItem_h
#define CondTools_SiPixel_SiPixelCondDataItem_h

// system includes
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <fmt/printf.h>

// user includes
#include "FWCore/Utilities/interface/Exception.h"
//#include "CondCore/Utilities/interface/PayloadInspector.h"
#include "CondFormats/Common/interface/Time.h"
#include "CondCore/CondDB/interface/Types.h"

//functions for correct representation of data in summary and plot
namespace SiPixelCondObjectRepresent {

  enum plotType { STANDARD, COMPARISON, DIFF, RATIO, MAP, END_OF_TYPES };

  enum granularity { PER_PIXEL = 1, PER_ROC = 2, PER_MODULE = 3, UNDEFINED = 99 };

  //##### for metadata
  using MetaData = std::tuple<cond::Time_t, cond::Hash>;

  //##### for plotting
  enum OpMode { PIXEL_BASED, ROC_BASED, MODULE_BASED };
}  // namespace SiPixelCondObjectRepresent

template <class type>
class SiPixelCondDataItem {
public:
  SiPixelCondDataItem() { init(); }

  virtual ~SiPixelCondDataItem() = default;

  void fillAll(const unsigned int detid, const std::vector<type> &store) {
    m_info[detid] = store;
    m_cached = true;
    return;
  }

  void fillByPushBack(const unsigned int detid, const type &value) {
    m_info[detid].push_back(value);
    m_cached = true;
  }

  void divide(const unsigned int detid, const std::vector<type> &denominator) {
    if (m_info[detid].size() != denominator.size()) {
      throw cms::Exception("Unaligned Conditions") << "data size of numerator mismatched the data size of denominator";
    }

    unsigned int counter = 0;
    for (const auto &den : denominator) {
      m_info[detid].at(counter) /= den;
      counter++;
    }
  }

  void subtract(const unsigned int detid, const std::vector<type> &subtractor) {
    if (m_info[detid].size() != subtractor.size()) {
      throw cms::Exception("Unaligned Conditions") << "data size of numerator mismatched the data size of denominator";
    }

    unsigned int counter = 0;
    for (const auto &sub : subtractor) {
      m_info[detid].at(counter) -= sub;
      counter++;
    }
  }

  std::vector<type> data(unsigned int detid) { return m_info[detid]; }

  std::pair<std::vector<type>, std::vector<type> > demuxedData(const unsigned int detid) {
    if (m_compared) {
      std::vector<type> v1(m_info[detid].begin(), m_info[detid].begin() + m_info[detid].size() / 2);
      std::vector<type> v2(m_info[detid].begin() + m_info[detid].size() / 2, m_info[detid].end());
      assert(v1.size() == v2.size());
      return std::make_pair(v1, v2);
    } else {
      throw cms::Exception("Logic error") << "not being in compared mode, data cannot be demultiplexed";
    }
  }

  void setGranularity(const bool isPerPixel, const bool isPerROC) {
    m_servedPerPixel = isPerPixel;
    m_servedPerROC = isPerROC;
  }

  bool isCached() { return m_cached; }

  void setComparedBit() { m_compared = true; }

  std::vector<unsigned int> detIds(bool verbose) {
    std::vector<unsigned int> v;
    for (const auto &element : m_info) {
      if (verbose) {
        std::cout << element.first << "\n";
      }
      v.push_back(element.first);
    }
    return v;
  }

private:
  std::map<unsigned int, std::vector<type> > m_info;
  bool m_servedPerPixel;
  bool m_servedPerROC;
  bool m_cached;
  bool m_compared;

  void init() {
    m_info.clear();
    m_servedPerPixel = false;
    m_servedPerROC = false;
    m_cached = false;
    m_compared = false;
  }
};

#endif
