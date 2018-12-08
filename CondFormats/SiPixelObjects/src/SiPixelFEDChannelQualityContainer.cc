#include "CondFormats/SiPixelObjects/interface/SiPixelFEDChannelQualityContainer.h"
#include "FWCore/Utilities/interface/Exception.h" 
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include <iostream>
#include <iomanip>      // std::setw

void SiPixelFEDChannelQualityContainer::setScenario(const std::string &theScenarioId, const SiPixelFEDChannelCollection &theBadFEDChannels) {
  m_scenarioMap.emplace(theScenarioId,theBadFEDChannels);
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
std::unique_ptr<PixelFEDChannelCollection> SiPixelFEDChannelQualityContainer::getDetSetBadPixelFedChannels(const std::string &theScenarioId) const {

  std::unique_ptr<PixelFEDChannelCollection> disabled_channelcollection = std::make_unique<edmNew::DetSetVector<PixelFEDChannel> >();
  auto SiPixelBadFedChannels = m_scenarioMap.at(theScenarioId);
  for(const auto &entry : SiPixelBadFedChannels){
    disabled_channelcollection->insert(entry.first, entry.second.data(), entry.second.size());
  }
  return disabled_channelcollection;
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
	edm::LogVerbatim("SiPixelFEDChannelQualityContainer")<< " fed : "<< entry.fed 
							     << " link : "<< entry.link
							     << " roc_first : "<< entry.roc_first
							     << " roc_last: : "<< entry.roc_last;       
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
