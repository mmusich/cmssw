#include "CondFormats/SiPixelObjects/interface/SiPixelFedCablingMap.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelQuality.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFEDChannelQualityContainer.h"
#include "CondFormats/SiPixelObjects/interface/CablingPathToDetUnit.h"
#include "CondFormats/SiPixelObjects/interface/PixelROC.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFedCablingTree.h"
#include "FWCore/Utilities/interface/Exception.h" 
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include <iostream>
#include <iomanip>      // std::setw

void SiPixelFEDChannelQualityContainer::setScenario(const std::string &theScenarioId, const SiPixelFEDChannelCollection &theBadFEDChannels) {
  //m_scenarioMap[theScenarioId]=theBadFEDChannels;
  m_scenarioMap.emplace(theScenarioId,theBadFEDChannels);
}

//****************************************************************************//
void SiPixelFEDChannelQualityContainer::setScenario(const std::string &theScenarioId, const SiPixelQuality & theQuality, const SiPixelFedCablingMap& theFedCabling) {
  //m_scenarioMap[theScenarioId]=theQuality;

  auto fedid_ = theFedCabling.det2fedMap();

  SiPixelFEDChannelQualityContainer::SiPixelFEDChannelCollection theBadChannelCollection;

  auto theDisabledModules = theQuality.getBadComponentList();
  for (const auto &mod : theDisabledModules){
    //mod.DetID, mod.errorType,mod.BadRocs
    
    int coded_badRocs = mod.BadRocs;
    std::vector<PixelFEDChannel> disabledChannelsDetSet;
    std::vector<sipixelobjects::CablingPathToDetUnit> path = theFedCabling.pathToDetUnit(mod.DetID);
    auto cabling_ = theFedCabling.cablingTree();
    unsigned int nrocs_inLink(0);
    if (path.size() != 0){
      const sipixelobjects::PixelFEDCabling * aFed = cabling_->fed(path.at(0).fed);
      const sipixelobjects::PixelFEDLink    * link = aFed->link(path.at(0).link);
      nrocs_inLink = link->numberOfROCs();
    }	
    
    std::bitset<16> bad_rocs(coded_badRocs);	  
    unsigned int n_ch = bad_rocs.size()/nrocs_inLink;
	  
    for (unsigned int i_roc = 0; i_roc < n_ch; ++i_roc){
	    
      unsigned int first_idx = nrocs_inLink*i_roc;
      unsigned int sec_idx   = nrocs_inLink*(i_roc+1)-1;
      unsigned int mask      = pow(2,nrocs_inLink)-1;
      unsigned int n_setbits = (coded_badRocs >> (i_roc*nrocs_inLink)) & mask;
      if (n_setbits==0){
	  continue;
      }
      if(n_setbits != mask){
	std::cout  << "Mismatch: " << n_setbits <<  " " <<  mask << std::endl;
	continue;
      }
	    
      std::cout << "passed" << std::endl;
      unsigned int link_id = 99999;
      unsigned int fed_id = 99999;
	    
      for (auto const&  p: path){
	//std::cout << p.fed << " " << p.link << " " << p.roc << std::endl;
	if (p.roc == bad_rocs[first_idx]){
	  link_id = p.link;
	  fed_id = p.fed;
	  break; 
	}
      }
      std::cout << " " << fed_id << " " << link_id << " " << first_idx << "  " 
		<< sec_idx << std::endl;
	    
      PixelFEDChannel ch = {fed_id, link_id, first_idx, sec_idx};
      disabledChannelsDetSet.push_back(ch);
      std::cout <<  i_roc << " " << coded_badRocs <<  " "  
		<< first_idx << " " << sec_idx << std::endl;
      std::cout << "=======================================" << std::endl;
    }
    
    if (!disabledChannelsDetSet.empty()) {
      theBadChannelCollection[mod.DetID] = disabledChannelsDetSet;
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
std::unique_ptr<edmNew::DetSetVector<PixelFEDChannel> > SiPixelFEDChannelQualityContainer::getDetSetBadPixelFedChannels(const std::string &theScenarioId) const {

  std::unique_ptr<edmNew::DetSetVector<PixelFEDChannel> > disabled_channelcollection = std::make_unique<edmNew::DetSetVector<PixelFEDChannel> >();
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
