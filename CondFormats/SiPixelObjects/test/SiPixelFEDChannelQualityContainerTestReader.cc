#include <string>
#include <iostream>
#include <map>
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelQuality.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFEDChannelQualityContainer.h"
#include "CondFormats/DataRecord/interface/SiPixelQualityFromDbRcd.h"
#include "CondFormats/DataRecord/interface/SiPixelStatusScenariosRcd.h"

class SiPixelFEDChannelQualityContainerTestReader : public edm::one::EDAnalyzer<> {
public:
  explicit SiPixelFEDChannelQualityContainerTestReader(edm::ParameterSet const& p); 
  ~SiPixelFEDChannelQualityContainerTestReader(); 

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
private:
    
  virtual void analyze(const edm::Event& e, const edm::EventSetup& c) override;

  // ----------member data ---------------------------
  const bool printdebug_;
  const std::string formatedOutput_;
  
};
  
SiPixelFEDChannelQualityContainerTestReader::SiPixelFEDChannelQualityContainerTestReader(edm::ParameterSet const& p):
  printdebug_(p.getUntrackedParameter<bool>("printDebug",true)),
  formatedOutput_(p.getUntrackedParameter<std::string>("outputFile",""))
{ 
  edm::LogInfo("SiPixelFEDChannelQualityContainerTestReader")<<"SiPixelFEDChannelQualityContainerTestReader"<<std::endl;
}

SiPixelFEDChannelQualityContainerTestReader::~SiPixelFEDChannelQualityContainerTestReader() {  
  edm::LogInfo("SiPixelFEDChannelQualityContainerTestReader")<<"~SiPixelFEDChannelQualityContainerTestReader "<<std::endl;
}

void
SiPixelFEDChannelQualityContainerTestReader::analyze(const edm::Event& e, const edm::EventSetup& context){
  
  edm::LogInfo("SiPixelFEDChannelQualityContainerTestReader") <<"### SiPixelFEDChannelQualityContainerTestReader::analyze  ###"<<std::endl;
  edm::LogInfo("SiPixelFEDChannelQualityContainerTestReader") <<" I AM IN RUN NUMBER "<<e.id().run() <<std::endl;
  edm::LogInfo("SiPixelFEDChannelQualityContainerTestReader") <<" ---EVENT NUMBER "<<e.id().event() <<std::endl;
  
  edm::eventsetup::EventSetupRecordKey recordKey(edm::eventsetup::EventSetupRecordKey::TypeTag::findType("SiPixelStatusScenariosRcd"));
    
  if( recordKey.type() == edm::eventsetup::EventSetupRecordKey::TypeTag()) {
    //record not found
    edm::LogInfo("SiPixelFEDChannelQualityContainerTestReader") <<"Record \"SiPixelStatusScenariosRcd"<<"\" does not exist "<<std::endl;
  }
  
  //this part gets the handle of the event source and the record (i.e. the Database)
  edm::ESHandle<SiPixelFEDChannelQualityContainer> qualityCollectionHandle;
  edm::LogInfo("SiPixelFEDChannelQualityContainerTestReader") <<"got eshandle"<<std::endl;
  
  context.get<SiPixelStatusScenariosRcd>().get(qualityCollectionHandle);
  edm::LogInfo("SiPixelFEDChannelQualityContainerTestReader") <<"got context"<<std::endl;

  const SiPixelFEDChannelQualityContainer* quality_map=qualityCollectionHandle.product();
  edm::LogInfo("SiPixelFEDChannelQualityContainerTestReader") <<"got SiPixelFEDChannelQualityContainer* "<< std::endl;
  edm::LogInfo("SiPixelFEDChannelQualityContainerTestReader") << "print  pointer address : " ;
  edm::LogInfo("SiPixelFEDChannelQualityContainerTestReader") << quality_map << std::endl;
  
  edm::LogInfo("SiPixelFEDChannelQualityContainerTestReader") << "Size "  <<  quality_map->size() << std::endl;     
  edm::LogInfo("SiPixelFEDChannelQualityContainerTestReader") <<"Content of myQuality_Map "<<std::endl;
  // use built-in method in the CondFormat to print the content
  if(printdebug_){
    quality_map->printAll();
  }
  
  FILE* pFile=NULL;
  if(formatedOutput_!="")pFile=fopen(formatedOutput_.c_str(), "w");
  if(pFile){
    
    fprintf(pFile,"SiPixelFEDChannelQualityContainer::printAll() \n");
    fprintf(pFile," =================================================================================================================== \n"); 

    SiPixelFEDChannelQualityContainer::SiPixelBadFEDChannelsScenarioMap m_qualities = quality_map-> getScenarioMap();
      
    for(auto it = m_qualities.begin(); it != m_qualities.end() ; ++it){
      fprintf(pFile," =================================================================================================================== \n");
      fprintf(pFile,"run : %s \n ",(it->first).c_str());
      for (const auto& thePixelFEDChannel : it->second){
	DetId detId = thePixelFEDChannel.first;
	fprintf(pFile,"DetId : %i \n",detId.rawId());
	for(const auto& entry: thePixelFEDChannel.second) {
	  //unsigned int fed, link, roc_first, roc_last;
	  fprintf(pFile,"fed : %i | link : %i | roc_first : %i | roc_last: %i: \n",entry.fed, entry.link,  entry.roc_first, entry.roc_last);	  
	}
      }
    }
  }
}

void
SiPixelFEDChannelQualityContainerTestReader::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.setComment("Reads payloads of type SiPixelFEDChannelQualityContainer");
  desc.addUntracked<bool>("printDebug",true);
  desc.addUntracked<std::string>("outputFile","");
  descriptions.add("SiPixelFEDChannelQualityContainerTestReader",desc);
}

DEFINE_FWK_MODULE(SiPixelFEDChannelQualityContainerTestReader);
