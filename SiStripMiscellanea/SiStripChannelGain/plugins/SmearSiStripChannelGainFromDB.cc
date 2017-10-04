// -*- C++ -*-
//
// Package:    SiStripMiscellanea/SiStripChannelGain
// Class:      SmearSiStripChannelGainFromDB
// 
/**\class SmearSiStripChannelGainFromDB SmearSiStripChannelGainFromDB.cc SiStripMiscellanea/SiStripChannelGain/plugins/SmearSiStripChannelGainFromDB.cc

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
#include "DataFormats/SiStripDetId/interface/StripSubdetector.h" 


#include "TRandom3.h"

//
// class declaration
//

namespace ApvGain {
  struct GainSmearings{
    GainSmearings(){
      m_doScale = false;
      m_doSmear = false;
      m_scaleFactor = 1.;
      m_smearFactor = 0.;
    }
    ~GainSmearings(){}
    
    void setSmearing(bool doScale,bool doSmear,double the_scaleFactor,double the_smearFactor){
      m_doScale = doScale;
      m_doSmear = doSmear;
      m_scaleFactor = the_scaleFactor;
      m_smearFactor = the_smearFactor;
    }
    
    bool m_doScale;
    bool m_doSmear;
    double m_scaleFactor;
    double m_smearFactor;
  };

}

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class SmearSiStripChannelGainFromDB : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit SmearSiStripChannelGainFromDB(const edm::ParameterSet&);
      ~SmearSiStripChannelGainFromDB();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      std::unique_ptr<SiStripApvGain> getNewObject(const std::map<std::pair<uint32_t,int>,float>& theMap);
      StripSubdetector::SubDetector getSubdetFromString(std::string sub);
      virtual void endJob() override;

      // ----------member data ---------------------------
      std::string m_Record;  
      uint32_t m_gainType;
      std::vector<edm::ParameterSet> m_parameters;
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
SmearSiStripChannelGainFromDB::SmearSiStripChannelGainFromDB(const edm::ParameterSet& iConfig)
{
   //now do what ever initialization is needed
   usesResource("TFileService");
   m_Record  = iConfig.getUntrackedParameter<std::string> ("Record" , "SiStripApvGainRcd");
   m_gainType = iConfig.getUntrackedParameter<uint32_t>("gainType",1);
   m_parameters = iConfig.getParameter<std::vector<edm::ParameterSet> >("thresholds");
}


SmearSiStripChannelGainFromDB::~SmearSiStripChannelGainFromDB()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
SmearSiStripChannelGainFromDB::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   std::vector<std::string> partitions;

   // fill the list of alignables
   for(auto& thePSet : m_parameters){
     const std::string partition(thePSet.getParameter<std::string>("partition"));
     // only if it is not yet in the list
     if(std::find(partitions.begin(), partitions.end(), partition) == partitions.end()) {
       partitions.push_back(partition);
     }
   }

   std::map<StripSubdetector::SubDetector,ApvGain::GainSmearings> mapOfSmearings;

    for(auto& thePSet : m_parameters){
     
       const std::string partition(thePSet.getParameter<std::string>("partition"));
       StripSubdetector::SubDetector sub = this->getSubdetFromString(partition);
       
       bool    m_doScale(thePSet.getParameter<bool>("doScale"));
       bool    m_doSmear(thePSet.getParameter<bool>("doSmear"));
       double  m_scaleFactor(thePSet.getParameter<double>("scaleFactor"));
       double  m_smearFactor(thePSet.getParameter<double>("smearFactor"));
    
       ApvGain::GainSmearings params = ApvGain::GainSmearings();
       params.setSmearing(m_doScale,m_doSmear,m_scaleFactor,m_smearFactor);
       mapOfSmearings[sub]=params;
    }


   edm::ESHandle<SiStripGain> SiStripApvGain_;
   iSetup.get<SiStripGainRcd>().get(SiStripApvGain_);

   std::map<std::pair<uint32_t,int>,float> theMap;
   std::shared_ptr<TRandom3> random(new TRandom3(1));
   
   std::vector<uint32_t> detid;
   SiStripApvGain_->getDetIds(detid);
   for (const auto & d : detid) {
     SiStripApvGain::Range range=SiStripApvGain_->getRange(d,m_gainType);
     float nAPV=0;

     StripSubdetector::SubDetector subid =  static_cast<StripSubdetector::SubDetector>(DetId(d).subdetId()); 
     ApvGain::GainSmearings params =  mapOfSmearings[subid];

     for(int it=0;it<range.second-range.first;it++){
       nAPV+=1;
       float Gain=SiStripApvGain_->getApvGain(it,range);
       std::pair<uint32_t,int> index = std::make_pair(d,nAPV);
       
       if(params.m_doScale){
	 Gain*=params.m_scaleFactor;
       }
       
       if(params.m_doSmear){
	 float smearedGain = random->Gaus(Gain,params.m_smearFactor);
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
SmearSiStripChannelGainFromDB::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
SmearSiStripChannelGainFromDB::endJob() 
{
}

//********************************************************************************//
std::unique_ptr<SiStripApvGain>
SmearSiStripChannelGainFromDB::getNewObject(const std::map<std::pair<uint32_t,int>,float>& theMap) 
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
    
    edm::LogInfo("SmearSiStripChannelGainFromDB")<<" DetId: "<<DetId 
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
SmearSiStripChannelGainFromDB::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

/*--------------------------------------------------------------------*/
StripSubdetector::SubDetector SmearSiStripChannelGainFromDB::getSubdetFromString(std::string sub)
/*--------------------------------------------------------------------*/
{
  if(sub.find("TIB")!=std::string::npos){
    return StripSubdetector::TIB ;
  } else if(sub.find("TOB")!=std::string::npos){ 
    return StripSubdetector::TOB ;
  } else if(sub.find("TID")!=std::string::npos){   
    return StripSubdetector::TID ;
  } else if(sub.find("TEC")!=std::string::npos) {
    return StripSubdetector::TEC ;
  } else {
    edm::LogError("LogicError") << "Unknown partition: " << sub;
    throw cms::Exception("Invalid Partition passed"); 
  }  
}


//define this as a plug-in
DEFINE_FWK_MODULE(SmearSiStripChannelGainFromDB);
