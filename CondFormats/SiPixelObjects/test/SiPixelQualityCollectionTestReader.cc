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
#include "CondFormats/SiPixelObjects/interface/SiPixelQualityCollection.h"
#include "CondFormats/DataRecord/interface/SiPixelQualityFromDbRcd.h"
#include "CondFormats/DataRecord/interface/SiPixelStatusScenariosRcd.h"

class SiPixelQualityCollectionTestReader : public edm::one::EDAnalyzer<> {
public:
  explicit SiPixelQualityCollectionTestReader(edm::ParameterSet const& p); 
  ~SiPixelQualityCollectionTestReader(); 

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
private:
    
  virtual void analyze(const edm::Event& e, const edm::EventSetup& c) override;

  // ----------member data ---------------------------
  const bool printdebug_;
  const std::string formatedOutput_;
  
};
  
SiPixelQualityCollectionTestReader::SiPixelQualityCollectionTestReader(edm::ParameterSet const& p):
  printdebug_(p.getUntrackedParameter<bool>("printDebug",true)),
  formatedOutput_(p.getUntrackedParameter<std::string>("outputFile",""))
{ 
  edm::LogInfo("SiPixelQualityCollectionTestReader")<<"SiPixelQualityCollectionTestReader"<<std::endl;
}

SiPixelQualityCollectionTestReader::~SiPixelQualityCollectionTestReader() {  
  edm::LogInfo("SiPixelQualityCollectionTestReader")<<"~SiPixelQualityCollectionTestReader "<<std::endl;
}

void
SiPixelQualityCollectionTestReader::analyze(const edm::Event& e, const edm::EventSetup& context){
  
  edm::LogInfo("SiPixelQualityCollectionTestReader") <<"### SiPixelQualityCollectionTestReader::analyze  ###"<<std::endl;
  edm::LogInfo("SiPixelQualityCollectionTestReader") <<" I AM IN RUN NUMBER "<<e.id().run() <<std::endl;
  edm::LogInfo("SiPixelQualityCollectionTestReader") <<" ---EVENT NUMBER "<<e.id().event() <<std::endl;
  
  edm::eventsetup::EventSetupRecordKey recordKey(edm::eventsetup::EventSetupRecordKey::TypeTag::findType("SiPixelStatusScenariosRcd"));
    
  if( recordKey.type() == edm::eventsetup::EventSetupRecordKey::TypeTag()) {
    //record not found
    edm::LogInfo("SiPixelQualityCollectionTestReader") <<"Record \"SiPixelStatusScenariosRcd"<<"\" does not exist "<<std::endl;
  }
  
  //this part gets the handle of the event source and the record (i.e. the Database)
  edm::ESHandle<SiPixelQualityCollection> qualityCollectionHandle;
  edm::LogInfo("SiPixelQualityCollectionTestReader") <<"got eshandle"<<std::endl;
  
  context.get<SiPixelStatusScenariosRcd>().get(qualityCollectionHandle);
  edm::LogInfo("SiPixelQualityCollectionTestReader") <<"got context"<<std::endl;

  const SiPixelQualityCollection* quality_map=qualityCollectionHandle.product();
  edm::LogInfo("SiPixelQualityCollectionTestReader") <<"got SiPixelQualityCollection* "<< std::endl;
  edm::LogInfo("SiPixelQualityCollectionTestReader") << "print  pointer address : " ;
  edm::LogInfo("SiPixelQualityCollectionTestReader") << quality_map << std::endl;
  
  edm::LogInfo("SiPixelQualityCollectionTestReader") << "Size "  <<  quality_map->size() << std::endl;     
  edm::LogInfo("SiPixelQualityCollectionTestReader") <<"Content of myQuality_Map "<<std::endl;
  // use built-in method in the CondFormat to print the content
  if(printdebug_){
    quality_map->printAll();
  }
  
  FILE* pFile=NULL;
  if(formatedOutput_!="")pFile=fopen(formatedOutput_.c_str(), "w");
  if(pFile){
    
    fprintf(pFile,"SiPixelQualityCollection::printAll() \n");
    fprintf(pFile," =================================================================================================================== \n"); 

    SiPixelQualityCollection::quality_map m_qualities = quality_map->getQuality_Map();
      
    for(auto it = m_qualities.begin(); it != m_qualities.end() ; ++it){
      fprintf(pFile," =================================================================================================================== \n");
      fprintf(pFile,"run : %s \n ",(it->first).c_str());
      auto theDisabledModules = (it->second).getBadComponentList();
      for (const auto &mod : theDisabledModules){
	fprintf(pFile,"detId: %i  | error type: %i  |BadRocs: %i \n",  mod.DetID, mod.errorType,mod.BadRocs);
      }
    }
  }
}

void
SiPixelQualityCollectionTestReader::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.setComment("Reads payloads of type SiPixelQualityCollection");
  desc.addUntracked<bool>("printDebug",true);
  desc.addUntracked<std::string>("outputFile","");
  descriptions.add("SiPixelQualityCollectionTestReader",desc);
}

DEFINE_FWK_MODULE(SiPixelQualityCollectionTestReader);
