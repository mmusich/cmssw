#ifndef CondFormats_SiPixelObjects_SiPixelFEDChannelQualityContainer_h 
#define CondFormats_SiPixelObjects_SiPixelFEDChannelQualityContainer_h

#include "CondFormats/SiPixelObjects/interface/SiPixelQuality.h"
#include "DataFormats/SiPixelDetId/interface/PixelFEDChannel.h"
#include "CondFormats/Serialization/interface/Serializable.h"
#include "DataFormats/Common/interface/DetSetVector.h"

#include <map>
#include <string>
#include <vector>

class SiPixelFEDChannelQualityContainer{
public:
  typedef std::map<DetId,std::vector<PixelFEDChannel> > SiPixelFEDChannelCollection;
  typedef std::unordered_map<std::string, SiPixelFEDChannelCollection> SiPixelBadFEDChannelsScenarioMap;
  
  SiPixelFEDChannelQualityContainer(){}
  virtual ~SiPixelFEDChannelQualityContainer(){}

  void setScenario(const std::string &theScenarioId, const SiPixelFEDChannelCollection &theBadFEDChannels);
  void setScenario(const std::string &theScenarioId, const SiPixelQuality &theSiPixelQuality, const SiPixelFedCablingMap& theFedCabling);
                  
  const SiPixelBadFEDChannelsScenarioMap& getScenarioMap () const  {return m_scenarioMap;}

  SiPixelFEDChannelCollection   getSiPixelBadFedChannels(const std::string &ScenarioId) const;
  SiPixelFEDChannelCollection & getSiPixelBadFedChannels(const std::string &ScenarioId);

  std::unique_ptr<edmNew::DetSetVector<PixelFEDChannel> > getDetSetBadPixelFedChannels(const std::string &ScenarioId) const;
  
  double size()const {return m_scenarioMap.size();}
  std::vector<std::string> getScenarioList() const;

  void printAll() const;

private:

  SiPixelBadFEDChannelsScenarioMap m_scenarioMap;

  COND_SERIALIZABLE;

};

#endif
