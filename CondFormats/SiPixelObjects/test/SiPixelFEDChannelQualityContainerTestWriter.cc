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
#include "CondFormats/DataRecord/interface/SiPixelFedCablingMapRcd.h"
#include "CondFormats/DataRecord/interface/SiPixelQualityFromDbRcd.h"
#include "CondFormats/SiPixelObjects/interface/CablingPathToDetUnit.h"
#include "CondFormats/SiPixelObjects/interface/PixelROC.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFEDChannelQualityContainer.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFedCablingMap.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFedCablingTree.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelQuality.h"
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
      SiPixelFEDChannelQualityContainer::SiPixelFEDChannelCollection createFromSiPixelQuality(const SiPixelQuality & theQuality, const SiPixelFedCablingMap& theFedCabling);

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
     
     auto theSiPixelFEDChannelCollection = this->createFromSiPixelQuality(*(siPixelQuality_.product()),*(cablingMapHandle.product()));
     myQualities->setScenario(scenario,theSiPixelFEDChannelCollection);

     IOVcount_++;

   }
   
   if(printdebug_){
     edm::LogInfo("SiPixelFEDChannelQualityContainerTestWriter")<<"Content of SiPixelFEDChannelQualityContainer "<<std::endl;

     // use built-in method in the CondFormat
     myQualities->printAll();
   }
}
   
// ------------ method called once each job just before starting event loop  ------------
SiPixelFEDChannelQualityContainer::SiPixelFEDChannelCollection
SiPixelFEDChannelQualityContainerTestWriter::createFromSiPixelQuality(const SiPixelQuality & theQuality, const SiPixelFedCablingMap& theFedCabling)
{
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
	edm::LogWarning("SiPixelFEDChannelQualityContainerTestWriter")  << "Mismatch! DetId: "<< mod.DetID << " " << n_setbits <<  " " <<  mask << std::endl;
	continue;
      }
	    
      edm::LogVerbatim("SiPixelFEDChannelQualityContainerTestWriter") << "passed" << std::endl;
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

      edm::LogVerbatim("SiPixelFEDChannelQualityContainerTestWriter") << " " << fed_id << " " << link_id << " " << first_idx << "  " << sec_idx << std::endl;
	 
      PixelFEDChannel ch = {fed_id, link_id, first_idx, sec_idx};
      disabledChannelsDetSet.push_back(ch);
      edm::LogVerbatim("SiPixelFEDChannelQualityContainerTestWriter") << i_roc << " " << coded_badRocs <<  " " << first_idx << " " << sec_idx << std::endl;
      edm::LogVerbatim("SiPixelFEDChannelQualityContainerTestWriter") << "=======================================" << std::endl;
    }
    
    if (!disabledChannelsDetSet.empty()) {
      theBadChannelCollection[mod.DetID] = disabledChannelsDetSet;
    }
  }
  return theBadChannelCollection;
}

void 
SiPixelFEDChannelQualityContainerTestWriter::beginJob()
{
  IOVcount_=0;
}

// ------------ method called once each job just after ending the event loop  ------------
void 
SiPixelFEDChannelQualityContainerTestWriter::endJob() 
{

  edm::LogInfo("SiPixelFEDChannelQualityContainerTestWriter")<<"Analyzed "<<IOVcount_<<" IOVs"<<std::endl;
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
