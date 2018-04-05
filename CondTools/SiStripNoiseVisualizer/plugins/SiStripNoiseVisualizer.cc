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

class SiStripNoiseVisualizer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit SiStripNoiseVisualizer(const edm::ParameterSet&);
      ~SiStripNoiseVisualizer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      std::map<uint32_t, TH1F*>  bookModuleHistograms();
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      // ----------member data ---------------------------
      edm::Service<TFileService> fs;
      SiStripDetInfoFileReader reader_;
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

   // edm::ESHandle<TrackerTopology> tTopoHandle;
   // iSetup.get<TrackerTopologyRcd>().get(tTopoHandle);
   // const TrackerTopology* tTopo_ = tTopoHandle.product();

  for(uint32_t detid : activeDetIds){

    //setTopoInfo(detid,tTopo_);      

    SiStripNoises::Range noiseRange = noiseHandle->getRange(detid);
    unsigned int nStrip = reader_.getNumberOfApvsAndStripLength(detid).first*128;

    for(unsigned int istrip_=0; istrip_<nStrip; ++istrip_){ 
      float noise_ = noiseHandle->getNoise(istrip_, noiseRange);
      histoMap_[detid]->SetBinContent(istrip_,noise_);
    } // loop on the strips
  } // loop on the active detids

}

 


// ------------ method called once each job just before starting event loop  ------------
void
SiStripNoiseVisualizer::beginJob()
{
  histoMap_ = this->bookModuleHistograms();
}

// ------------ method called once to book all the module level histograms = ------------
std::map<uint32_t, TH1F*> SiStripNoiseVisualizer::bookModuleHistograms()
{

  TH1F::SetDefaultSumw2(kTRUE);
  std::map<uint32_t, TH1F*> h;

  const std::map<uint32_t, SiStripDetInfoFileReader::DetInfo > DetInfos  = reader_.getAllData();

  for(std::map<uint32_t, SiStripDetInfoFileReader::DetInfo >::const_iterator it = DetInfos.begin(); it != DetInfos.end(); it++){    
    // check if det id is correct and if it is actually cabled in the detector
    if( it->first==0 || it->first==0xFFFFFFFF ) {
      edm::LogError("DetIdNotGood") << "@SUB=analyze" << "Wrong det id: " << it->first 
                                    << "  ... neglecting!" << std::endl;
      continue;
    }
    unsigned int nStrip = reader_.getNumberOfApvsAndStripLength(it->first).first*128;

    h[it->first] = fs->make<TH1F>(Form("NoiseProfile_%i",it->first),Form("Noise for module %i;n. strip; noise [ADC counts]",it->first),nStrip,-0.5,nStrip+0.5);

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
