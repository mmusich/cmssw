// -*- C++ -*-
//
// 
/**\class Convert Noise and APVGain payload into a TTree

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Mauro Verzetti
// Modified by:      Marco Musich
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"

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

class SiStripDB2Tree : public edm::EDAnalyzer {
public:
  explicit SiStripDB2Tree(const edm::ParameterSet&);
  ~SiStripDB2Tree() override;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


private:
  void beginJob() override;
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override;
  void setTopoInfo(uint32_t detId, const TrackerTopology* tTopo);

  // ----------member data ---------------------------
  TTree *tree_;
  SiStripDetInfoFileReader reader_; 
  bool isMC_;
  std::string qualityLabel_; 
  
  //branches
  uint32_t detId_, ring_, istrip_, det_type_; 
  Int_t layer_, side_,subdetId_;
  float noise_, gsim_, g1_, g2_, lenght_; 
  bool isTIB_, isTOB_, isTEC_, isTID_, isBad_; 
  TText *text_;
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
SiStripDB2Tree::SiStripDB2Tree(const edm::ParameterSet& iConfig):
  reader_(edm::FileInPath(std::string("CalibTracker/SiStripCommon/data/SiStripDetInfo.dat") ).fullPath()),
  detId_(0), ring_(0), istrip_(0), det_type_(0), layer_(0), side_(0), subdetId_(0),
  noise_(0), gsim_(0), g1_(0), g2_(0), lenght_(0),
  isTIB_(false), isTOB_(false), isTEC_(false), isTID_(false)
{
  edm::Service<TFileService> fs;
  //now do what ever initialization is needed
  text_ = fs->make<TText>(0., 0., "");
  text_->SetName("RunMode");
  tree_ = fs->make<TTree>( "StripDBTree","Tree with DB SiStrip info");

  tree_->Branch("detId"   , &detId_    ,"detId/i"   );
  tree_->Branch("detType" , &det_type_ ,"detType/i" );
  tree_->Branch("noise"   , &noise_    ,"noise/F"   ); 
  tree_->Branch("istrip"  , &istrip_   ,"istrip/i"  );
  tree_->Branch("gsim"    , &gsim_     ,"gsim/F"    ); 
  tree_->Branch("g1"      , &g1_       ,"g1/F"      ); 
  tree_->Branch("g2"      , &g2_       ,"g2/F"      ); 
  tree_->Branch("layer"   , &layer_    ,"layer/I"   ); 
  tree_->Branch("side"    , &side_     ,"side/I"    ); 
  tree_->Branch("subdetId", &subdetId_ ,"subdetId/I"); 
  tree_->Branch("ring"    , &ring_     ,"ring/i"    ); 
  tree_->Branch("length"  , &lenght_   ,"length/F"  ); 
  tree_->Branch("isBad"   , &isBad_    ,"isBad/O"   ); 
  tree_->Branch("isTIB"   , &isTIB_    ,"isTIB/O"   ); 
  tree_->Branch("isTOB"   , &isTOB_    ,"isTOB/O"   ); 
  tree_->Branch("isTEC"   , &isTEC_    ,"isTEC/O"   ); 
  tree_->Branch("isTID"   , &isTID_    ,"isTID/O"   ); 

  isMC_ = iConfig.getUntrackedParameter<bool>("isMC",false);
  qualityLabel_ = iConfig.getParameter<std::string>("StripQualityLabel"); 

}



SiStripDB2Tree::~SiStripDB2Tree()
{
}


//
// member functions
//

void SiStripDB2Tree::setTopoInfo(uint32_t detId,const TrackerTopology *tTopo)
{
  subdetId_ = DetId(detId).subdetId();
  switch(subdetId_){
  case StripSubdetector::TIB: //TIB
    isTIB_=true; isTOB_=false; isTEC_=false; isTID_=false;
    layer_ = tTopo->tibLayer(detId);
    side_ =0;
    ring_ =0;
    break;
  case StripSubdetector::TID: //TID
    isTIB_=false; isTOB_=false; isTEC_=false; isTID_=true;
    side_=tTopo->tidSide(detId);
    layer_=tTopo->tidWheel(detId);
    ring_ = 0;
    break;
  case StripSubdetector::TOB: //TOB
    isTIB_=false; isTOB_=true; isTEC_=false; isTID_=false;
    layer_ =  tTopo->tobLayer(detId);
    side_ =0;
    ring_ =0;
    break;
  case StripSubdetector::TEC: //TEC    
    isTIB_=false; isTOB_=false; isTEC_=true; isTID_=false;
    side_ =tTopo->tecSide(detId);
    layer_=tTopo->tecWheel(detId);
    ring_ =0;
    break;
  }
  return;
}


// ------------ method called for each event  ------------
void
SiStripDB2Tree::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::ESHandle<SiStripNoises> noiseHandle;
  iSetup.get<SiStripNoisesRcd>().get(noiseHandle);

  edm::ESHandle<SiStripApvGain> g1Handle;
  iSetup.get<SiStripApvGainRcd>().get(g1Handle);
  
  edm::ESHandle<SiStripApvGain> g2Handle;
  iSetup.get<SiStripApvGain2Rcd>().get(g2Handle);
  
  edm::ESHandle<SiStripQuality> siStripQualityHandle;   
  iSetup.get<SiStripQualityRcd>().get(qualityLabel_,siStripQualityHandle);

  edm::ESHandle<SiStripApvGain> gsimHandle;
  if(isMC_){
    iSetup.get<SiStripApvGainSimRcd>().get(gsimHandle);
  } else {
    LOGINFO("SiStripDB2Tree")<<"We have determined this Data" << std::endl;
  }  

  bool first = true;
  edm::ESHandle<SiStripLatency> latencyHandle;
  iSetup.get<SiStripLatencyRcd>().get(latencyHandle);
	
  std::vector<uint32_t> activeDetIds;
  noiseHandle->getDetIds(activeDetIds);

  edm::ESHandle<TrackerTopology> tTopoHandle;
  iSetup.get<TrackerTopologyRcd>().get(tTopoHandle);
  const TrackerTopology* tTopo_ = tTopoHandle.product();

  for(uint32_t detid : activeDetIds){

    setTopoInfo(detid,tTopo_);      

    SiStripNoises::Range noiseRange = noiseHandle->getRange(detid);
    SiStripApvGain::Range gsimRange;
    if(isMC_){
      gsimHandle->getRange(detid);
    }
    SiStripApvGain::Range g1Range = g1Handle->getRange(detid);
    SiStripApvGain::Range g2Range = g2Handle->getRange(detid);
    unsigned int nStrip = reader_.getNumberOfApvsAndStripLength(detid).first*128;
    lenght_ = reader_.getNumberOfApvsAndStripLength(detid).second;
    detId_=detid;
    det_type_ = SiStripDetId(detid).moduleGeometry();
    for(istrip_=0; istrip_<nStrip; ++istrip_){
      if(first){
	first = false;
	std::string run_op = ((latencyHandle->latency(detid, 1) & 8) == 8) ? "PEAK" : "DECO" ;
	text_->SetText(0., 0., run_op.c_str());
	LOGINFO("SiStripDB2Tree") << "SiStripOperationModeRcd " << ". . . " << run_op << std::endl;
      }
      gsim_ = isMC_ ? gsimHandle->getStripGain(istrip_, gsimRange) : 1.;
      g1_ = g1Handle->getStripGain(istrip_, g1Range) ? g1Handle->getStripGain(istrip_, g1Range) : 1.;
      g2_ = g2Handle->getStripGain(istrip_, g2Range) ? g2Handle->getStripGain(istrip_, g2Range) : 1.;
      noise_ = noiseHandle->getNoise(istrip_, noiseRange);
      isBad_ = siStripQualityHandle->IsStripBad(siStripQualityHandle->getRange(detid),istrip_);
      tree_->Fill();
    }
  }
}


// ------------ method called once each job just before starting event loop  ------------
void 
SiStripDB2Tree::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
SiStripDB2Tree::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
SiStripDB2Tree::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
#include "FWCore/PluginManager/interface/ModuleDef.h"
DEFINE_FWK_MODULE(SiStripDB2Tree);
