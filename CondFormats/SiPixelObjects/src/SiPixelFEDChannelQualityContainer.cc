#include "CondFormats/SiPixelObjects/interface/SiPixelQuality.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFEDChannelQualityContainer.h"
#include "FWCore/Utilities/interface/Exception.h" 
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include <iostream>
#include <iomanip>      // std::setw

void SiPixelFEDChannelQualityContainer::setScenario(const std::string &theScenarioId, const SiPixelFEDChannelCollection &theBadFEDChannels) {
  //m_scenarioMap[theScenarioId]=theBadFEDChannels;
  m_scenarioMap.emplace(theScenarioId,theBadFEDChannels);
}

//****************************************************************************//
void SiPixelFEDChannelQualityContainer::setScenario(const std::string &theScenarioId, const SiPixelQuality & theQuality) {
  //m_scenarioMap[theScenarioId]=theQuality;

  SiPixelFEDChannelQualityContainer::SiPixelFEDChannelCollection theBadChannelCollection;
  auto theDisabledModules = theQuality.getBadComponentList();
  for (const auto &mod : theDisabledModules){
    //mod.DetID, mod.errorType,mod.BadRocs
    PixelFEDChannel theBadChannel{1, 2, 3, 4};
    unsigned int BadRocCount(0),ch(0);
    for (unsigned short n = 0; n < 16; n++){
      unsigned short mask = 1 << n;  // 1 << n = 2^{n} using bitwise shift
      if (mod.BadRocs & mask) BadRocCount++;
    }

    while(ch < BadRocCount){
      theBadChannelCollection[mod.DetID].push_back(theBadChannel);
      ch++;
    }
  }
  m_scenarioMap.emplace(theScenarioId,theBadChannelCollection);

}

//****************************************************************************//
SiPixelFEDChannelQualityContainer::SiPixelFEDChannelCollection SiPixelFEDChannelQualityContainer::getSiPixelBadFedChannels(const std::string &theScenarioId) const {
  SiPixelBadFEDChannelsScenarioMap::const_iterator it = m_scenarioMap.find(theScenarioId);

  if (it != m_scenarioMap.end()){
    return it->second;
  } else {
    throw cms::Exception("SiPixelFEDChannelQualityContainer")<< "No Bad Pixel FEDChannels defined for Scenario id: " << theScenarioId << "\n";
  }
}

//****************************************************************************//
SiPixelFEDChannelQualityContainer::SiPixelFEDChannelCollection& SiPixelFEDChannelQualityContainer::getSiPixelBadFedChannels(const std::string &theScenarioId) {
  return m_scenarioMap[theScenarioId];
}

//****************************************************************************//
void SiPixelFEDChannelQualityContainer::printAll() const {
  
  edm::LogVerbatim("SiPixelFEDChannelQualityContainer")<<"SiPixelFEDChannelQualityContainer::printAll()";
  edm::LogVerbatim("SiPixelFEDChannelQualityContainer")<<" ===================================================================================================================";
  for(auto it = m_scenarioMap.begin(); it != m_scenarioMap.end() ; ++it){
    edm::LogVerbatim("SiPixelFEDChannelQualityContainer")<< "run :"<< it->first << "  \n ";
    for (const auto& thePixelFEDChannel : it->second){
      
      DetId detId = thePixelFEDChannel.first;
	
      edm::LogVerbatim("SiPixelFEDChannelQualityContainer")<< "DetId :"<< detId << "  \n ";

      for(const auto& entry: thePixelFEDChannel.second) {
	//unsigned int fed, link, roc_first, roc_last;
	edm::LogVerbatim("SiPixelFEDChannelQualityContainer")<< "fed       :"<< entry.fed 
							     << "link      :"<< entry.link
							     << "roc_first :"<< entry.roc_first
							     << "roc_last: :"<< entry.roc_last       
							     << "  \n ";
      }
    }
  }
}

//****************************************************************************//
std::vector<std::string> SiPixelFEDChannelQualityContainer::getScenarioList() const {
  std::vector<std::string> scenarios;
  scenarios.reserve(m_scenarioMap.size());

  for(auto it = m_scenarioMap.begin(); it != m_scenarioMap.end() ; ++it){
    scenarios.push_back(it->first);
  }
  return scenarios;
}
