#include "CondFormats/SiPixelObjects/interface/SiPixelQuality.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelQualityCollection.h"
#include "FWCore/Utilities/interface/Exception.h" 
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include <iostream>
#include <iomanip>      // std::setw

//****************************************************************************//
void SiPixelQualityCollection::setSiPixelQuality(const std::string &theScenarioId, const SiPixelQuality & theQuality) {
  m_qualities[theScenarioId]=theQuality;
}

//****************************************************************************//
SiPixelQuality SiPixelQualityCollection::getSiPixelQuality(const std::string &theScenarioId) const {
  quality_map::const_iterator it = m_qualities.find(theScenarioId);

  if (it != m_qualities.end()){
    return it->second;
  } else {
    throw cms::Exception("SiPixelQualityCollection")<< "No SiPixelQuality defined for Scenario id " << theScenarioId << "\n";
  }
}

//****************************************************************************//
SiPixelQuality& SiPixelQualityCollection::getSiPixelQuality(const std::string &theScenarioId) {
  return m_qualities[theScenarioId];
}


//****************************************************************************//
void SiPixelQualityCollection::printAll() const {
  
  edm::LogVerbatim("SiPixelQualityCollection")<<"SiPixelQualityCollection::printAll()";
  edm::LogVerbatim("SiPixelQualityCollection")<<" ===================================================================================================================";
  for(auto it = m_qualities.begin(); it != m_qualities.end() ; ++it){
    edm::LogVerbatim("SiPixelQualityCollection")<< "run :"<< it->first << "  \n ";
    auto theDisabledModules = (it->second).getBadComponentList();
    for (const auto &mod : theDisabledModules){
      edm::LogVerbatim("SiPixelQualityCollection")<<"detId: " <<  mod.DetID << " |error type: " << mod.errorType << " |BadRocs: "  <<  mod.BadRocs <<  std::endl;
    }
  }

}

//****************************************************************************//
std::vector<std::string> SiPixelQualityCollection::getScenarioList() const {
  std::vector<std::string> scenarios;
  scenarios.reserve(m_qualities.size());

  for(auto it = m_qualities.begin(); it != m_qualities.end() ; ++it){
    scenarios.push_back(it->first);
  }
  return scenarios;
}
