// -*- C++ -*-
//
// Package:    CondFormats/SiPixelObjects
// Class:      SiPixelQualityHistoricAnalyzer
//
/**\class SiPixelQualityHistoricAnalyzer SiPixelQualityHistoricAnalyzer.cc CondFormats/SiPixelObjects/plugins/SiPixelQualityHistoricAnalyzer.cc
 Description: class to build history aggregate of SiPixelQuality payloads
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
#include "DataFormats/SiPixelDetId/interface/PixelSubdetector.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFEDChannelContainer.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFedCablingMap.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFedCablingTree.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelQuality.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFEDChannelContainer.h"
#include "CondFormats/DataRecord/interface/SiPixelStatusScenariosRcd.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelQualityProbabilities.h"
#include "CondFormats/DataRecord/interface/SiPixelStatusScenarioProbabilityRcd.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/ESWatcher.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

// ROOT includes
#include "TFile.h"
#include "TFile.h"
#include "TH1D.h"
#include "TH1I.h"
#include "TH2D.h"
#include "TGraph.h"
#include "TGraphErrors.h"

#include <sstream>
#include <fstream>
#include <iostream>
#include <map>
#include <math.h>
#include <string>
#include <vector>
#include <algorithm>
//
// class declaration
//

class SiPixelQualityHistoricAnalyzer : public edm::one::EDAnalyzer<> {
public:
  explicit SiPixelQualityHistoricAnalyzer(const edm::ParameterSet&);
  ~SiPixelQualityHistoricAnalyzer();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  std::tuple<int,int,int> countBadRocsInSiPixelQuality(const SiPixelQuality& theQuality);

private:
  virtual void beginJob() override;
  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
  virtual void endJob() override;

  // ----------member data ---------------------------
  const bool printdebug_;
  int IOVcount_;
  edm::Service<TFileService> fs; 
  TH1F* h_totalBadRocs;
  TH1F* h_BPixBadRocs; 
  TH1F* h_FPixBadRocs;
  
  edm::ESWatcher<SiPixelQualityFromDbRcd> SiPixelQualityWatcher_;
};

//
// constructors and destructor
//
SiPixelQualityHistoricAnalyzer::SiPixelQualityHistoricAnalyzer(const edm::ParameterSet& iConfig)
  : printdebug_(iConfig.getUntrackedParameter<bool>("printDebug", false)) {
}

SiPixelQualityHistoricAnalyzer::~SiPixelQualityHistoricAnalyzer() {
}

//
// member functions
//

std::tuple<int,int,int> SiPixelQualityHistoricAnalyzer::countBadRocsInSiPixelQuality(const SiPixelQuality& theQuality){
  int totalBadRocs(0);
  int BPixBadRocs(0);
  int FPixBadRocs(0);
  
  auto theDisabledModules = theQuality.getBadComponentList();
  
  for (const auto& mod : theDisabledModules) {
    int BadRocCount(0);
    for (unsigned short n = 0; n < 16; n++) {
      unsigned short mask = 1 << n;  // 1 << n = 2^{n} using bitwise shift
      if (mod.BadRocs & mask){
	BadRocCount++;
      }
    }
    totalBadRocs+=BadRocCount;

    int subid = DetId(mod.DetID).subdetId();
    if (subid == PixelSubdetector::PixelBarrel) {
      BPixBadRocs+=BadRocCount;
    } else if (subid == PixelSubdetector::PixelEndcap) {
      FPixBadRocs+=BadRocCount;
    }
  }
  return std::make_tuple(totalBadRocs,BPixBadRocs,FPixBadRocs);
}



// ------------ method called for each event  ------------
void SiPixelQualityHistoricAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;

  unsigned int RunNumber_ = iEvent.eventAuxiliary().run();
  unsigned int LuminosityBlockNumber_ = iEvent.eventAuxiliary().luminosityBlock();

  bool hasQualityIOV = SiPixelQualityWatcher_.check(iSetup);

  edm::ESHandle<SiPixelQualityProbabilities> scenarioProbabilityHandle;
  iSetup.get<SiPixelStatusScenarioProbabilityRcd>().get(scenarioProbabilityHandle);
  const SiPixelQualityProbabilities* myProbabilities = scenarioProbabilityHandle.product();
  auto averagedProbabilities = myProbabilities->getProbabilities(0);

  if (hasQualityIOV) {
    //Retrieve the strip quality from conditions
    edm::ESHandle<SiPixelQuality> siPixelQuality_;
    iSetup.get<SiPixelQualityFromDbRcd>().get(siPixelQuality_);
    const SiPixelQuality& theQuality = *(siPixelQuality_.product());

    std::string scenario = std::to_string(RunNumber_) + "_" + std::to_string(LuminosityBlockNumber_);
          
    edm::LogInfo("SiPixelQualityHistoricAnalyzer")<< "Found IOV:" << RunNumber_ << "(" << LuminosityBlockNumber_ << ")" << std::endl;
    
    float theProb(0.);
    std::map<std::string,float> coupled;
    std::for_each(averagedProbabilities.begin(),averagedProbabilities.end(),
		 [&coupled](const std::pair<std::string,float> &entry) 
		 {
		   coupled.insert(entry);
		 });

    std::cout << coupled.size() << std::endl;

    auto itToMap = coupled.find(scenario);
    if (itToMap !=  coupled.end()){
      theProb = itToMap->second;
      std::cout << "This scenario : "<< scenario  << " has probability: " << theProb << std::endl;
      } else {
      std::cout << "unfortunately this scenario "<< scenario << " has not been found ... " << std::endl;
    }

    auto counts = this->countBadRocsInSiPixelQuality(theQuality);
    
    h_totalBadRocs->Fill(std::get<0>(counts),theProb); 
    h_BPixBadRocs ->Fill(std::get<1>(counts),theProb);  
    h_FPixBadRocs ->Fill(std::get<2>(counts),theProb);
    
    IOVcount_++;
  }
}

void SiPixelQualityHistoricAnalyzer::beginJob() { 
  IOVcount_ = 0; 

  h_totalBadRocs = fs->make<TH1F>("totalBadRocs","Bad ROCs PDF;n. of total bad ROCs;probability",10000,0.,10000.);
  h_BPixBadRocs  = fs->make<TH1F>("BPixBadRocs","BPix Bad ROCs PDF;n. of BPix bad ROCc;probability",6000,0.,6000.);
  h_FPixBadRocs  = fs->make<TH1F>("FPixBadRocs","FPix Bad ROCs PDF;n. of BPix bad ROCs;probability",5000,0.,5000.);
 
}

// ------------ method called once each job just after ending the event loop  ------------
void SiPixelQualityHistoricAnalyzer::endJob() {

  std::cout << "Total Bad ROCs integral: "<< h_totalBadRocs->GetSumOfWeights() <<std::endl;
  std::cout << "BPix  Bad ROCs integral: "<< h_BPixBadRocs->GetSumOfWeights()  <<std::endl;
  std::cout << "FPix  Bad ROCs integral: "<< h_FPixBadRocs->GetSumOfWeights()  <<std::endl;

}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void SiPixelQualityHistoricAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.setComment("Historic Analyzer of SiPixelQuality tags");
  desc.addUntracked<bool>("printDebug", false);
  descriptions.add("SiPixelQualityHistoricAnalyzer", desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SiPixelQualityHistoricAnalyzer);
