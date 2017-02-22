#include <string>
#include <iostream>
#include <map>
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "CondFormats/PCLConfig/interface/AlignPCLThresholds.h"
#include "CondFormats/DataRecord/interface/AlignPCLThresholdsRcd.h"

namespace edmtest
{
  class AlignPCLThresholdsReader : public edm::EDAnalyzer
  {
  public:
    explicit  AlignPCLThresholdsReader(edm::ParameterSet const& p) { 
      std::cout<<"AlignPCLThresholdsReader"<<std::endl;
          }
    explicit  AlignPCLThresholdsReader(int i) {
      std::cout<<"AlignPCLThresholdsReader "<<i<<std::endl; 
    }
    virtual ~AlignPCLThresholdsReader() {  
      std::cout<<"~AlignPCLThresholdsReader "<<std::endl;
    }
        virtual void analyze(const edm::Event& e, const edm::EventSetup& c) override;
  };
  
  void
  AlignPCLThresholdsReader::analyze(const edm::Event& e, const edm::EventSetup& context){

    std::cout <<"### AlignPCLThresholdsReader::analyze"<<std::endl;
    std::cout <<" I AM IN RUN NUMBER "<<e.id().run() <<std::endl;
    std::cout <<" ---EVENT NUMBER "<<e.id().event() <<std::endl;
    
    edm::eventsetup::EventSetupRecordKey recordKey(edm::eventsetup::EventSetupRecordKey::TypeTag::findType("AlignPCLThresholdsRcd"));
    
    if( recordKey.type() == edm::eventsetup::EventSetupRecordKey::TypeTag()) {
      //record not found
      std::cout <<"Record \"AlignPCLThresholdsRcd"<<"\" does not exist "<<std::endl;
    }
    
    //this part gets the handle of the event source and the record (i.e. the Database)
    edm::ESHandle<AlignPCLThresholds> thresholdHandle;
    std::cout<<"got eshandle"<<std::endl;

    context.get<AlignPCLThresholdsRcd>().get(thresholdHandle);
    std::cout<<"got context"<<std::endl;

    const AlignPCLThresholds* thresholds=thresholdHandle.product();
    std::cout<<"got AlignPCLThresholds* "<< std::endl;
    std::cout<< "print  pointer address : " ;
    std::cout << thresholds << std::endl;

    std::cout << "Size "  <<  thresholds->size() << std::endl;
    const AlignPCLThresholds::threshold_map & mymap = thresholds->getThreshold_Map();
     
    std::cout<<"Content of myThresholds "<<std::endl;
    for(AlignPCLThresholds::threshold_map::const_iterator it = mymap.begin(); it != mymap.end() ; ++it){
      std::cout<<"keys : " << it->first <<std::endl
	       <<"- sigCut    : " << (it->second).getSigCut()     << std::endl
	       <<"- Xcut      : " << (it->second).getXcut()       <<" um"     << std::endl
	       <<"- thetaXcut : " << (it->second).getThetaXcut()  <<" urad"   << std::endl
	       <<"- Ycut      : " << (it->second).getYcut()       <<" um"     << std::endl
	       <<"- thetaYcut : " << (it->second).getThetaYcut()  <<" urad"   << std::endl
	       <<"- Zcut      : " << (it->second).getZcut()       <<" um"     << std::endl
	       <<"- thetaZcut : " << (it->second).getThetaZcut()  <<" urad"   << std::endl
	       <<"- MaxMove   : " << (it->second).getMaxMoveCut() <<" um/rad" << std::endl
	       <<"- MaxError  : " << (it->second).getMaxErrorCut()<<" um/rad" << std::endl
	       <<std::endl;
    }
  }
  DEFINE_FWK_MODULE(AlignPCLThresholdsReader);
}
