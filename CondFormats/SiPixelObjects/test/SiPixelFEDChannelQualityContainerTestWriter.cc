// -*- C++ -*-
//
// Package:    CondFormats/SiPixelObjects
// Class:      SiPixelFEDChannelQualityContainerTestWriter
// 
/**\class SiPixelFEDChannelQualityContainerTestWriter SiPixelFEDChannelQualityContainerTestWriter.cc CondFormats/SiPixelObjects/plugins/SiPixelFEDChannelQualityContainerTestWriter.cc
 Description: class to build the SiPixelFEDChannelQualityContainer payloads
*/
//
// Original Author:  Marco Musich
//         Created:  Wed, 27 Nov 2018 12:04:36 GMT
//
//

// system include files
#include <memory>

// user include files
#include "CondCore/DBOutputService/interface/PoolDBOutputService.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelQuality.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFEDChannelQualityContainer.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFedCablingMap.h"
#include "CondFormats/DataRecord/interface/SiPixelFedCablingMapRcd.h"
#include "CondFormats/DataRecord/interface/SiPixelQualityFromDbRcd.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/ESWatcher.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

//
// class declaration
//

class SiPixelFEDChannelQualityContainerTestWriter : public edm::one::EDAnalyzer<>  {
   public:
      explicit SiPixelFEDChannelQualityContainerTestWriter(const edm::ParameterSet&);
      ~SiPixelFEDChannelQualityContainerTestWriter();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      // ----------member data ---------------------------
      const std::string m_record;
      const bool printdebug_;
      SiPixelFEDChannelQualityContainer* myQualities;

      int IOVcount_;
      edm::ESWatcher<SiPixelQualityFromDbRcd> SiPixelQualityWatcher_;

};

//
// constructors and destructor
//
SiPixelFEDChannelQualityContainerTestWriter::SiPixelFEDChannelQualityContainerTestWriter(const edm::ParameterSet& iConfig):
  m_record(iConfig.getParameter<std::string>("record")),
  printdebug_(iConfig.getUntrackedParameter<bool>("printDebug",false))
{
  //now do what ever initialization is needed
  myQualities = new SiPixelFEDChannelQualityContainer();
}


SiPixelFEDChannelQualityContainerTestWriter::~SiPixelFEDChannelQualityContainerTestWriter()
{
  delete myQualities;
}

//
// member functions
//

// ------------ method called for each event  ------------
void
SiPixelFEDChannelQualityContainerTestWriter::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   
   unsigned int RunNumber_= iEvent.eventAuxiliary().run();
   unsigned int LuminosityBlockNumber_ = iEvent.eventAuxiliary().luminosityBlock();
      
   bool hasQualityIOV = SiPixelQualityWatcher_.check(iSetup);
   
   if(hasQualityIOV){

     //Retrieve the strip quality from conditions
     edm::ESHandle<SiPixelQuality> siPixelQuality_;
     iSetup.get<SiPixelQualityFromDbRcd>().get(siPixelQuality_);

     edm::ESHandle<SiPixelFedCablingMap> cablingMapHandle;
     iSetup.get<SiPixelFedCablingMapRcd>().get(cablingMapHandle);

     std::string scenario = std::to_string(RunNumber_)+"_"+std::to_string(LuminosityBlockNumber_);

     edm::LogInfo("SiPixelFEDChannelQualityContainerTestWriter")<<"Found IOV:" << RunNumber_ <<"("<< LuminosityBlockNumber_ <<")"<<std::endl;
     
     myQualities->setScenario(scenario,*(siPixelQuality_.product()),*(cablingMapHandle.product()));

   }
   
   if(printdebug_){
     edm::LogInfo("SiPixelFEDChannelQualityContainerTestWriter")<<"Content of SiPixelFEDChannelQualityContainer "<<std::endl;

     // use buil-in method in the CondFormat
     myQualities->printAll();
   }
}
   
// ------------ method called once each job just before starting event loop  ------------
void 
SiPixelFEDChannelQualityContainerTestWriter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
SiPixelFEDChannelQualityContainerTestWriter::endJob() 
{

  edm::LogInfo("SiPixelFEDChannelQualityContainerTestWriter")<<"Size of SiPixelFEDChannelQualityContainer object "<< myQualities->size() <<std::endl<<std::endl;

  // Form the data here
  edm::Service<cond::service::PoolDBOutputService> poolDbService;
  if( poolDbService.isAvailable() ){
    cond::Time_t valid_time = poolDbService->currentTime(); 
    // this writes the payload to begin in current run defined in cfg
    poolDbService->writeOne(myQualities,valid_time, m_record);
  } 
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
SiPixelFEDChannelQualityContainerTestWriter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SiPixelFEDChannelQualityContainerTestWriter);
