// -*- C++ -*-
//
// Package:    CondFormats/SiPixelObjects
// Class:      SiPixelQualityCollectionTestWriter
// 
/**\class SiPixelQualityCollectionTestWriter SiPixelQualityCollectionTestWriter.cc CondFormats/SiPixelObjects/plugins/SiPixelQualityCollectionTestWriter.cc
 Description: class to build the SiPixelQualityCollection payloads
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
#include "CondFormats/SiPixelObjects/interface/SiPixelQualityCollection.h"
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

class SiPixelQualityCollectionTestWriter : public edm::one::EDAnalyzer<>  {
   public:
      explicit SiPixelQualityCollectionTestWriter(const edm::ParameterSet&);
      ~SiPixelQualityCollectionTestWriter();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      // ----------member data ---------------------------
      const std::string m_record;
      const bool printdebug_;
      SiPixelQualityCollection* myQualities;

      int IOVcount_;
      edm::ESWatcher<SiPixelQualityFromDbRcd> SiPixelQualityWatcher_;

};

//
// constructors and destructor
//
SiPixelQualityCollectionTestWriter::SiPixelQualityCollectionTestWriter(const edm::ParameterSet& iConfig):
  m_record(iConfig.getParameter<std::string>("record")),
  printdebug_(iConfig.getUntrackedParameter<bool>("printDebug",false))
{
  //now do what ever initialization is needed
  myQualities = new SiPixelQualityCollection();
}


SiPixelQualityCollectionTestWriter::~SiPixelQualityCollectionTestWriter()
{
  delete myQualities;
}

//
// member functions
//

// ------------ method called for each event  ------------
void
SiPixelQualityCollectionTestWriter::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   
   unsigned int RunNumber_= iEvent.eventAuxiliary().run();
   unsigned int LuminosityBlockNumber_ = iEvent.eventAuxiliary().luminosityBlock();
      
   bool hasQualityIOV = SiPixelQualityWatcher_.check(iSetup);
   
   if(hasQualityIOV){

     //Retrieve the strip quality from conditions
     edm::ESHandle<SiPixelQuality> siPixelQuality_;
     iSetup.get<SiPixelQualityFromDbRcd>().get(siPixelQuality_);

     std::string scenario = std::to_string(RunNumber_)+"_"+std::to_string(LuminosityBlockNumber_);

     edm::LogInfo("SiPixelQualityCollectionTestWriter")<<"Found IOV:" << RunNumber_ <<"("<< LuminosityBlockNumber_ <<")"<<std::endl;

     myQualities->setSiPixelQuality(scenario,*(siPixelQuality_.product()));

     IOVcount_++;
   }
   
   if(printdebug_){
     edm::LogInfo("SiPixelQualityCollectionTestWriter")<<"Content of SiPixelQualityCollection "<<std::endl;

     // use buil-in method in the CondFormat
     myQualities->printAll();
   }
}
   
// ------------ method called once each job just before starting event loop  ------------
void 
SiPixelQualityCollectionTestWriter::beginJob()
{
  IOVcount_=0;
}

// ------------ method called once each job just after ending the event loop  ------------
void 
SiPixelQualityCollectionTestWriter::endJob() 
{
  
  edm::LogInfo("SiPixelQualityCollectionTestWriter")<<"Analyzed "<<IOVcount_<<" IOVs"<<std::endl;
  edm::LogInfo("SiPixelQualityCollectionTestWriter")<<"Size of SiPixelQualityCollection object "<< myQualities->size() <<std::endl<<std::endl;

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
SiPixelQualityCollectionTestWriter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
   desc.setComment("Writes payloads of type SiPixelQualityCollection");
   desc.addUntracked<bool>("printDebug",true);
   desc.add<std::string>("record","");
   descriptions.add("SiPixelQualityCollectionTestWriter",desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SiPixelQualityCollectionTestWriter);
