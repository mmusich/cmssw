#ifndef CondFormats_SiPixelObjects_SiPixelQualityCollection_h 
#define CondFormats_SiPixelObjects_SiPixelQualityCollection_h

#include "CondFormats/SiPixelObjects/interface/SiPixelQuality.h"
#include "CondFormats/Serialization/interface/Serializable.h"

#include <map>
#include <string>
#include <vector>

class SiPixelQualityCollection{
public:
  typedef std::map<std::string,SiPixelQuality> quality_map;
  
  SiPixelQualityCollection(){}
  virtual ~SiPixelQualityCollection(){}

  void setSiPixelQuality(const std::string &theScenarioId, const SiPixelQuality &theQuality);
                  
  const quality_map& getQuality_Map () const  {return m_qualities;}

  SiPixelQuality   getSiPixelQuality(const std::string &ScenarioId) const;
  SiPixelQuality & getSiPixelQuality(const std::string &ScenarioId);
  
  double size()const {return m_qualities.size();}
  std::vector<std::string> getScenarioList() const;

  void printAll() const;

private:

  quality_map m_qualities;

  COND_SERIALIZABLE;

};

#endif
