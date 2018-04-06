// -*- C++ -*-
//
// Package:    CondTools/SiStripNoiseVisualizer
// Class:      SiStripNoiseVisualizer
//
/**\class SiStripNoiseVisualizer SiStripNoiseVisualizer.cc CondTools/SiStripNoiseVisualizer/plugins/SiStripNoiseVisualizer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Marco Musich
//         Created:  Thu, 05 Apr 2018 15:32:25 GMT
//
//


// system include files

#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/EventSetup.h"

#include "CondFormats/SiStripObjects/interface/SiStripPedestals.h"
#include "CondFormats/DataRecord/interface/SiStripPedestalsRcd.h"
#include "CondFormats/SiStripObjects/interface/SiStripNoises.h"
#include "CondFormats/DataRecord/interface/SiStripNoisesRcd.h"
#include "CondFormats/SiStripObjects/interface/SiStripApvGain.h"
#include "CalibTracker/Records/interface/SiStripQualityRcd.h"
#include "CalibFormats/SiStripObjects/interface/SiStripQuality.h"
#include "CondFormats/DataRecord/interface/SiStripApvGainRcd.h"
#include "CondFormats/SiStripObjects/interface/SiStripLatency.h"
#include "CondFormats/DataRecord/interface/SiStripCondDataRecords.h"
#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"
#include "Geometry/Records/interface/TrackerTopologyRcd.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TTree.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"
#define LOGERROR(x) edm::LogError(x)
#define LOGWARNING(x) edm::LogWarning(x)
#define LOGINFO(x) edm::LogInfo(x)
#define LOGDEBUG(x) LogDebug(x)

#include "CalibTracker/SiStripCommon/interface/SiStripDetInfoFileReader.h"

#include "DataFormats/Common/interface/DetSetNew.h"
#include "DataFormats/Common/interface/DetSetVectorNew.h"
#include <vector>
#include <unordered_map>
#include <map>
#include <string>
#include "TText.h"
#include "TObjString.h"
#include "TNamed.h"

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<>
// This will improve performance in multithreaded jobs.

class SiStripNoiseVisualizer : public edm::one::EDAnalyzer<edm::one::SharedResources,edm::one::WatchRuns>  {
   public:
      explicit SiStripNoiseVisualizer(const edm::ParameterSet&);
      ~SiStripNoiseVisualizer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      void beginRun(edm::Run const&, edm::EventSetup const&) override;
      void endRun(edm::Run const&, edm::EventSetup const&) override {};
      std::map<uint32_t, TH1F*>  bookModuleHistograms(const TrackerTopology* tTopo);
      std::tuple<std::string,int,int,int> setTopoInfo(uint32_t detId,const TrackerTopology *tTopo);
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      // ----------member data ---------------------------
      edm::Service<TFileService> fs;
      SiStripDetInfoFileReader reader_;
      std::map<std::string,TFileDirectory> outputFolders;
      std::map<uint32_t,TH1F*> histoMap_;
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
SiStripNoiseVisualizer::SiStripNoiseVisualizer(const edm::ParameterSet& iConfig):
  reader_(edm::FileInPath(std::string("CalibTracker/SiStripCommon/data/SiStripDetInfo.dat") ).fullPath())
{
   //now do what ever initialization is needed

}


SiStripNoiseVisualizer::~SiStripNoiseVisualizer()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
SiStripNoiseVisualizer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   
   edm::ESHandle<SiStripNoises> noiseHandle;
   iSetup.get<SiStripNoisesRcd>().get(noiseHandle);

   std::vector<uint32_t> activeDetIds;
   noiseHandle->getDetIds(activeDetIds);

   LOGINFO("SiStripNoiseVisualizer")<<"@SUB=SiStripNoiseVisualizer::analyze() histoMap_.size(): "<< histoMap_.size() << std::endl;

   for(uint32_t detid : activeDetIds){

    SiStripNoises::Range noiseRange = noiseHandle->getRange(detid);
    unsigned int nStrip = reader_.getNumberOfApvsAndStripLength(detid).first*128;

    for(unsigned int istrip_=0; istrip_<nStrip; ++istrip_){ 
      float noise_ = noiseHandle->getNoise(istrip_, noiseRange);

      if(!histoMap_.count(detid)){
	LOGWARNING("SiStripNoiseVisualizer")<<"@SUB=SiStripNoiseVisualizer::analyze(): "<<detid<<" was not found!!!"<< std::endl;
      } else {
	histoMap_[detid]->SetBinContent(istrip_,noise_);
      }
    } // loop on the strips
  } // loop on the active detids

}

 


// ------------ method called once each job just before starting event loop  ------------
void
SiStripNoiseVisualizer::beginJob()
{
  //  histoMap_ = this->bookModuleHistograms();
}

// ------------ method called for each run  ------------
void 
SiStripNoiseVisualizer::beginRun(const edm::Run& iRun, edm::EventSetup const& iSetup ) 
{
  LOGINFO("SiStripNoiseVisualizer")<<"@SUB=SiStripNoiseVisualizer::beginRun() before booking histoMap_.size(): "<< histoMap_.size() << std::endl;
  
  edm::ESHandle<TrackerTopology> tTopoHandle;
  iSetup.get<TrackerTopologyRcd>().get(tTopoHandle);
  const TrackerTopology* tTopo_ = tTopoHandle.product();

  const std::map<uint32_t, SiStripDetInfoFileReader::DetInfo > DetInfos  = reader_.getAllData();
  
  for(const auto &it : DetInfos){
    auto topolInfo =  setTopoInfo(it.first,tTopo_);    

    std::string thePart = std::get<0>(topolInfo);

    // book the TFileDirectory if it's not already done
    if(!outputFolders.count(thePart)){
      outputFolders[thePart] = fs->mkdir(thePart.c_str());
    }
  } 

  histoMap_ = bookModuleHistograms(tTopo_);

  LOGINFO("SiStripNoiseVisualizer")<<"@SUB=SiStripNoiseVisualizer::beginRun()\n After booking histoMap_.size(): "<< histoMap_.size() << std::endl;

} 

// ------------ method called to determine the topology  ------------
std::tuple<std::string,int,int,int>
SiStripNoiseVisualizer::setTopoInfo(uint32_t detId,const TrackerTopology *tTopo)
{

  std::tuple<int,int,int,int> tuple;
  int  subdetId_(-999),layer_(-999),side_(-999);
  std::string ret="";
  
  subdetId_ = DetId(detId).subdetId();
  switch(subdetId_){
  case StripSubdetector::TIB: //TIB
    layer_ = tTopo->tibLayer(detId);
    side_  =0;
    ret+=Form("TIB_Layer%i",layer_);
    break;
  case StripSubdetector::TID: //TID
    side_ =tTopo->tidSide(detId);
    layer_=tTopo->tidWheel(detId);
    ret+=("TID_");
    ret+= (side_ == 1) ? Form("P_disk%i",layer_) : Form("M_disk%i",layer_);
    break;
  case StripSubdetector::TOB: //TOB
    layer_ =  tTopo->tobLayer(detId);
    side_  =0;
    ret+=Form("TOB_Layer%i",layer_);
    break;
  case StripSubdetector::TEC: //TEC    
    side_  =tTopo->tecSide(detId);
    layer_ =tTopo->tecWheel(detId);
    ret+=("TEC_");
    ret+= (side_ == 1) ? Form("P_disk%i",layer_) : Form("M_disk%i",layer_);
    break;
  }
  
  return std::make_tuple(ret,subdetId_,layer_,side_);
}

// ------------ method called once to book all the module level histograms  ------------
std::map<uint32_t, TH1F*> SiStripNoiseVisualizer::bookModuleHistograms(const TrackerTopology* tTopo_)
{

  TH1F::SetDefaultSumw2(kTRUE);
  std::map<uint32_t, TH1F*> h;

  const std::map<uint32_t, SiStripDetInfoFileReader::DetInfo > DetInfos  = reader_.getAllData();

  //  for(std::map<uint32_t, SiStripDetInfoFileReader::DetInfo >::const_iterator it = DetInfos.begin(); it != DetInfos.end(); it++){    

  for(const auto &it : DetInfos){
    // check if det id is correct and if it is actually cabled in the detector
    if( it.first==0 || it.first==0xFFFFFFFF ) {
      edm::LogError("DetIdNotGood") << "@SUB=analyze" << "Wrong det id: " << it.first 
                                    << "  ... neglecting!" << std::endl;
      continue;
    }

    auto topolInfo =  setTopoInfo(it.first,tTopo_);    
    std::string thePart = std::get<0>(topolInfo);

    unsigned int nStrip = reader_.getNumberOfApvsAndStripLength(it.first).first*128;

    h[it.first] = outputFolders[thePart].make<TH1F>(Form("NoiseProfile_%i",it.first),Form("Noise for module %i;n. strip; noise [ADC counts]",it.first),nStrip,-0.5,nStrip+0.5);

  }
  
  return h;
  
}

// ------------ method called once each job just after ending the event loop  ------------
void
SiStripNoiseVisualizer::endJob()
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
SiStripNoiseVisualizer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);

  //Specify that only 'tracks' is allowed
  //To use, remove the default given above and uncomment below
  //ParameterSetDescription desc;
  //desc.addUntracked<edm::InputTag>("tracks","ctfWithMaterialTracks");
  //descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SiStripNoiseVisualizer);
