// -*- C++ -*-
//
// Package:    SiStripMiscellanea/SiStripChannelGain
// Class:      CreateSiStripChannelGain
// 
/**\class CreateSiStripChannelGain CreateSiStripChannelGain.cc SiStripMiscellanea/SiStripChannelGain/plugins/CreateSiStripChannelGain.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Marco Musich
//         Created:  Tue, 03 Oct 2017 12:57:34 GMT
//
//


// system include files
#include <memory>
#include <iostream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "CondFormats/SiStripObjects/interface/SiStripApvGain.h"
#include "CondFormats/DataRecord/interface/SiStripApvGainRcd.h"
#include "CalibFormats/SiStripObjects/interface/SiStripGain.h"
#include "CalibTracker/Records/interface/SiStripGainRcd.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CondCore/DBOutputService/interface/PoolDBOutputService.h"
#include "FWCore/Framework/interface/EventSetup.h"

#include "TRandom3.h"

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class CreateSiStripChannelGain : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit CreateSiStripChannelGain(const edm::ParameterSet&);
      ~CreateSiStripChannelGain();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      std::unique_ptr<SiStripApvGain> getNewObject(const std::map<std::pair<uint32_t,int>,float>& theMap);
      virtual void endJob() override;

      // ----------member data ---------------------------
      std::string m_Record;  
      uint32_t m_gainType;
      bool m_doScale;
      bool m_doSmear;
      double m_scaleFactor;
      double m_smearFactor;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
CreateSiStripChannelGain::CreateSiStripChannelGain(const edm::ParameterSet& iConfig)
{
   //now do what ever initialization is needed
   usesResource("TFileService");
   m_Record  = iConfig.getUntrackedParameter<std::string> ("Record" , "SiStripApvGainRcd");
   m_gainType = iConfig.getUntrackedParameter<uint32_t>("gainType",1);
   m_doScale   = iConfig.getUntrackedParameter<bool>("doScale",false);
   m_doSmear   = iConfig.getUntrackedParameter<bool>("doSmear",false);
   m_scaleFactor = iConfig.getUntrackedParameter<double>("scaleFactor",1.);
   m_smearFactor = iConfig.getUntrackedParameter<double>("smearFactor",0.);
}


CreateSiStripChannelGain::~CreateSiStripChannelGain()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
CreateSiStripChannelGain::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   /*
     edm::ESHandle<SiStripGain> SiStripApvGain_;
     iSetup.get<SiStripApvGain2Rcd>().get(SiStripApvGain_);
   */

   edm::ESHandle<SiStripGain> SiStripApvGain_;
   iSetup.get<SiStripGainRcd>().get(SiStripApvGain_);

   std::map<std::pair<uint32_t,int>,float> theMap;
   std::shared_ptr<TRandom3> random(new TRandom3(1));
   
   std::vector<uint32_t> detid;
   SiStripApvGain_->getDetIds(detid);
   for (const auto & d : detid) {
     SiStripApvGain::Range range=SiStripApvGain_->getRange(d,m_gainType);
     float nAPV=0;
     for(int it=0;it<range.second-range.first;it++){
       nAPV+=1;
       float Gain=SiStripApvGain_->getApvGain(it,range);
       std::pair<uint32_t,int> index = std::make_pair(d,nAPV);
       
       if(m_doScale){
	 Gain*=m_scaleFactor;
       }
       
       if(m_doSmear){
	 float smearedGain = random->Gaus(Gain,m_smearFactor);
	 Gain=smearedGain;
       }

       theMap[index]=Gain;
       
     } // loop over APVs
   } // loop over DetIds

   std::unique_ptr<SiStripApvGain> theAPVGains = this->getNewObject(theMap);

   // write out the APVGains record
   edm::Service<cond::service::PoolDBOutputService> poolDbService;
  
   if( poolDbService.isAvailable() )
     poolDbService->writeOne(theAPVGains.get(),poolDbService->currentTime(),m_Record);
   else
     throw std::runtime_error("PoolDBService required.");
 
}


// ------------ method called once each job just before starting event loop  ------------
void 
CreateSiStripChannelGain::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
CreateSiStripChannelGain::endJob() 
{
}

//********************************************************************************//
std::unique_ptr<SiStripApvGain>
CreateSiStripChannelGain::getNewObject(const std::map<std::pair<uint32_t,int>,float>& theMap) 
{
  std::unique_ptr<SiStripApvGain> obj = std::unique_ptr<SiStripApvGain>(new SiStripApvGain());
  
  std::vector<float> theSiStripVector;
  uint32_t PreviousDetId = 0; 
  for(const auto &element : theMap){
    uint32_t DetId = element.first.first;
    if(DetId != PreviousDetId){
      if(!theSiStripVector.empty()){
	SiStripApvGain::Range range(theSiStripVector.begin(),theSiStripVector.end());
	if ( !obj->put(PreviousDetId,range) )  printf("Bug to put detId = %i\n",PreviousDetId);
      }
      theSiStripVector.clear();
      PreviousDetId = DetId;
    }
    theSiStripVector.push_back(element.second);
    
    edm::LogInfo("CreateSiStripChannelGain")<<" DetId: "<<DetId 
					    <<" APV:   "<<element.first.second
					    <<" Gain:  "<<element.second
					    <<std::endl;
  }
  
  if(!theSiStripVector.empty()){
    SiStripApvGain::Range range(theSiStripVector.begin(),theSiStripVector.end());
    if ( !obj->put(PreviousDetId,range) )  printf("Bug to put detId = %i\n",PreviousDetId);
  }
  
  return obj;
}


// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
CreateSiStripChannelGain::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(CreateSiStripChannelGain);
