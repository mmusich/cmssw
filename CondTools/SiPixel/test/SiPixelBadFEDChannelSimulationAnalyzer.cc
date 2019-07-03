#include <string>
#include <iostream>
#include <map>
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "DataFormats/SiPixelDetId/interface/PixelSubdetector.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelQuality.h"
#include "CondFormats/DataRecord/interface/SiPixelQualityFromDbRcd.h"
#include "CondFormats/DataRecord/interface/SiPixelFedCablingMapRcd.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFedCablingMap.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFedCablingTree.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFEDChannelContainer.h"
#include "CondFormats/DataRecord/interface/SiPixelStatusScenariosRcd.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelQualityProbabilities.h"
#include "CondFormats/DataRecord/interface/SiPixelStatusScenarioProbabilityRcd.h"
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


class SiPixelBadFEDChannelSimulationAnalyzer : public edm::one::EDAnalyzer<> {
public:
  explicit SiPixelBadFEDChannelSimulationAnalyzer(edm::ParameterSet const& p);
  ~SiPixelBadFEDChannelSimulationAnalyzer();
  virtual void beginJob() override;
  virtual void endJob() override;
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  virtual void analyze(const edm::Event& e, const edm::EventSetup& c) override;
  std::tuple<int,int,int> countBadRocsInFEDChannel(const SiPixelFEDChannelContainer::SiPixelFEDChannelCollection& fc);

  // ----------member data ---------------------------
  const bool printdebug_;
  edm::Service<TFileService> fs; 
  TH1F* h_totalBadRocs;
  TH1F* h_BPixBadRocs; 
  TH1F* h_FPixBadRocs;
  
  // for the PU dependency
  std::vector<int> dpfv_;
  std::vector<double> dp_;

  // total counts
  int TotalBadRocsFromQuality_;
  int BPixBadRocsFromQuality_;
  int FPixBadRocsFromQuality_;
 
};

SiPixelBadFEDChannelSimulationAnalyzer::SiPixelBadFEDChannelSimulationAnalyzer(edm::ParameterSet const& pset): 
  printdebug_(pset.getUntrackedParameter<bool>("printDebug", true)) { 
  dpfv_ = pset.getParameter<std::vector<int> >("probFunctionVariable");
  dp_   = pset.getParameter<std::vector<double> >("probValue");
  edm::LogInfo("SiPixelBadFEDChannelSimulationAnalyzer")<< "SiPixelBadFEDChannelSimulationAnalyzer" << std::endl;
}

SiPixelBadFEDChannelSimulationAnalyzer::~SiPixelBadFEDChannelSimulationAnalyzer() { 
  edm::LogInfo("SiPixelBadFEDChannelSimulationAnalyzer")
    << "~SiPixelBadFEDChannelSimulationAnalyzer " << std::endl;
}

void SiPixelBadFEDChannelSimulationAnalyzer::beginJob()
{
  TotalBadRocsFromQuality_=0;
  BPixBadRocsFromQuality_=0;
  FPixBadRocsFromQuality_=0;

  h_totalBadRocs = fs->make<TH1F>("totalBadRocs","Bad ROCs PDF;n. of total bad ROCs;probability",1000,0.,10000.);
  h_BPixBadRocs  = fs->make<TH1F>("BPixBadRocs","BPix Bad ROCs PDF;n. of BPix bad ROCc;probability",6000,0.,6000.);
  h_FPixBadRocs  = fs->make<TH1F>("FPixBadRocs","FPix Bad ROCs PDF;n. of BPix bad ROCs;probability",5000,0.,5000.);
}

void SiPixelBadFEDChannelSimulationAnalyzer::endJob() 
{
  std::cout << "Total Bad ROCs integral: "<< h_totalBadRocs->GetSumOfWeights() <<std::endl;
  std::cout << "BPix  Bad ROCs integral: "<< h_BPixBadRocs->GetSumOfWeights()  <<std::endl;
  std::cout << "FPix  Bad ROCs integral: "<< h_FPixBadRocs->GetSumOfWeights()  <<std::endl;
}

std::tuple<int,int,int> SiPixelBadFEDChannelSimulationAnalyzer::countBadRocsInFEDChannel(const SiPixelFEDChannelContainer::SiPixelFEDChannelCollection& fc){

  int totalBadRocs(0);
  int BPixBadRocs(0);
  int FPixBadRocs(0);
  
  for (const auto& entry : fc) {

    int subid = DetId(entry.first).subdetId();
    for(const auto& channel : entry.second){
      //std::cout << "DetId" << entry.first << std::endl;;
      //unsigned int fed, link, roc_first, roc_last;
      //std:cout << "fed : "  << entry.fed <<"  | link : " << entry.link <<  " | roc_first : " << entry.roc_first  <<  " | roc_last: " << entry.roc_last << " \n" 
      totalBadRocs+=(channel.roc_last-channel.roc_first);

      if (subid == PixelSubdetector::PixelBarrel) {
	BPixBadRocs+=(channel.roc_last-channel.roc_first);
      } else if (subid == PixelSubdetector::PixelEndcap) {
	FPixBadRocs+=(channel.roc_last-channel.roc_first);
      }
    }
  }

  return std::make_tuple(totalBadRocs,BPixBadRocs,FPixBadRocs);
}

void SiPixelBadFEDChannelSimulationAnalyzer::analyze(const edm::Event& e, const edm::EventSetup& context) {
  edm::LogInfo("SiPixelBadFEDChannelSimulationAnalyzer")
    << "### SiPixelBadFEDChannelSimulationAnalyzer::analyze  ###" << std::endl;
  edm::LogInfo("SiPixelBadFEDChannelSimulationAnalyzer") << " I AM IN RUN NUMBER " << e.id().run() << std::endl;
  edm::LogInfo("SiPixelBadFEDChannelSimulationAnalyzer") << " ---EVENT NUMBER " << e.id().event() << std::endl;

  
  edm::ESHandle<SiPixelQuality> siPixelQuality_;
  context.get<SiPixelQualityFromDbRcd>().get(siPixelQuality_);

  edm::ESHandle<SiPixelFedCablingMap> cablingMapHandle;
  context.get<SiPixelFedCablingMapRcd>().get(cablingMapHandle);
    
  const SiPixelQuality& theQuality = *(siPixelQuality_.product());
  auto theDisabledModules = theQuality.getBadComponentList();
  
  for (const auto& mod : theDisabledModules) {
    int BadRocCount(0);
    for (unsigned short n = 0; n < 16; n++) {
      unsigned short mask = 1 << n;  // 1 << n = 2^{n} using bitwise shift
      if (mod.BadRocs & mask){
	BadRocCount++;
      }
    }
    //std::cout << "detId:" << mod.DetID << " error type:" << mod.errorType << " BadRocs:" << BadRocCount << std::endl;
    TotalBadRocsFromQuality_+=BadRocCount;

    int subid = DetId(mod.DetID).subdetId();
    if (subid == PixelSubdetector::PixelBarrel) {
      BPixBadRocsFromQuality_+=BadRocCount;
    } else if (subid == PixelSubdetector::PixelEndcap) {
      FPixBadRocsFromQuality_+=BadRocCount;
    }
  }

  edm::eventsetup::EventSetupRecordKey recordKey(
      edm::eventsetup::EventSetupRecordKey::TypeTag::findType("SiPixelStatusScenariosRcd"));
  if (recordKey.type() == edm::eventsetup::EventSetupRecordKey::TypeTag()) {
    //record not found
    edm::LogInfo("SiPixelBadFEDChannelSimulationAnalyzer") << "Record \"SiPixelStatusScenariosRcd"
							   << "\" does not exist " << std::endl;
  }

  //this part gets the handle of the event source and the record (i.e. the Database)
  edm::ESHandle<SiPixelFEDChannelContainer> qualityCollectionHandle;
  context.get<SiPixelStatusScenariosRcd>().get(qualityCollectionHandle);
  const SiPixelFEDChannelContainer* quality_map = qualityCollectionHandle.product();

  edm::eventsetup::EventSetupRecordKey recordKey2(
      edm::eventsetup::EventSetupRecordKey::TypeTag::findType("SiPixelStatusScenarioProbabilityRcd>"));

  if (recordKey2.type() == edm::eventsetup::EventSetupRecordKey::TypeTag()) {
    //record not found
    edm::LogWarning("SiPixelQualityProbabilitiesTestReader") << "Record \"SiPixelStatusScenarioProbabilityRcd>"
                                                             << "\" does not exist " << std::endl;
  }

  //this part gets the handle of the event source and the record (i.e. the Database)
  edm::ESHandle<SiPixelQualityProbabilities> scenarioProbabilityHandle;
  context.get<SiPixelStatusScenarioProbabilityRcd>().get(scenarioProbabilityHandle);
  const SiPixelQualityProbabilities* myProbabilities = scenarioProbabilityHandle.product();

  SiPixelFEDChannelContainer::SiPixelBadFEDChannelsScenarioMap m_qualities = quality_map->getScenarioMap();
  SiPixelQualityProbabilities::probabilityMap m_probabilities = myProbabilities->getProbability_Map();

  int counter(0);
  std::map<std::string,double> mapScenarioToProbability;

  for(const auto &puBin : dpfv_){
    double puProbValue = dp_.at(counter); 
    //std::cout << "count: "<< counter << " PU bin: " << puBin << " prob: " << puProbValue << std::endl;
    const auto& theProbabilitiesPerScenario = myProbabilities->getProbabilities(puBin);
    for (auto it = theProbabilitiesPerScenario.begin(); it != theProbabilitiesPerScenario.end(); it++) {
     
      auto itToMap = mapScenarioToProbability.find(it->first);
      if (itToMap != mapScenarioToProbability.end()){
	(*itToMap).second += it->second * puProbValue;
      } else {
	mapScenarioToProbability.insert(std::make_pair(it->first,it->second * puProbValue));
      }
      
      //std::cout << it->first << " : " << it->second << std::endl;
    }
    counter++;
  }


  // loop over all the scenarios
  for(const auto &scenarios : mapScenarioToProbability){
    // std::cout << scenarios.first << " probability: "<< scenarios.second << std::endl;
    auto PixelFEDChannelCollection_ = quality_map->getScenarioMap().at(scenarios.first);
    auto counts = this->countBadRocsInFEDChannel(PixelFEDChannelCollection_);
    
    h_totalBadRocs->Fill(TotalBadRocsFromQuality_+ std::get<0>(counts),scenarios.second); 
    h_BPixBadRocs ->Fill(BPixBadRocsFromQuality_+ std::get<0>(counts),scenarios.second);  
    h_FPixBadRocs ->Fill(FPixBadRocsFromQuality_+ std::get<0>(counts),scenarios.second);  
  }

  std::vector<std::string> allScenarios = quality_map->getScenarioList();
  std::vector<std::string> allScenariosInProb;

  for (auto it = m_probabilities.begin(); it != m_probabilities.end(); ++it) {
    //int PUbin = it->first;
    for (const auto& entry : it->second) {
      auto scenario = entry.first;
      auto probability = entry.second;
      if (probability != 0) {
        if (std::find(allScenariosInProb.begin(), allScenariosInProb.end(), scenario) == allScenariosInProb.end()) {
          allScenariosInProb.push_back(scenario);
        }

        // if(m_qualities.find(scenario) == m_qualities.end()){
        //   edm::LogWarning("SiPixelBadFEDChannelSimulationAnalyzer") <<"Pretty worrying! the scenario: " << scenario << " (prob:" << probability << ") is not found in the map!!"<<std::endl;
        // } else {
        //   edm::LogInfo("SiPixelBadFEDChannelSimulationAnalyzer") << "scenario: "<< scenario << " is in the map! (all is good)"<< std::endl;
        // }

      }  // if prob!=0
    }    // loop on the scenarios for that PU bin
  }      // loop on PU bins

  std::vector<std::string> notFound;
  std::copy_if(allScenariosInProb.begin(),
               allScenariosInProb.end(),
               std::back_inserter(notFound),
               [&allScenarios](const std::string& arg) {
                 return (std::find(allScenarios.begin(), allScenarios.end(), arg) == allScenarios.end());
               });

  if (notFound.size() != 0) {
    for (const auto& entry : notFound) {
      edm::LogWarning("SiPixelBadFEDChannelSimulationAnalyzer")
          << "Pretty worrying! the scenario: " << entry << "  is not found in the map!!" << std::endl;

      if (printdebug_) {
        edm::LogVerbatim("SiPixelBadFEDChannelSimulationAnalyzer") << " This scenario is found in: " << std::endl;
        for (auto it = m_probabilities.begin(); it != m_probabilities.end(); ++it) {
          int PUbin = it->first;

          for (const auto& pair : it->second) {
            if (pair.first == entry) {
              edm::LogVerbatim("SiPixelBadFEDChannelSimulationAnalyzer")
                  << " - PU bin " << PUbin << " with probability: " << pair.second << std::endl;
            }  // if the scenario matches
          }    // loop on scenarios
        }      // loop on PU
      }        // if printdebug
      edm::LogVerbatim("SiPixelBadFEDChannelSimulationAnalyzer")
          << "==============================================" << std::endl;
    }  // loop on scenarios not found

    edm::LogWarning("SiPixelBadFEDChannelSimulationAnalyzer")
        << " ====> A total of " << notFound.size() << " scenarios are not found in the map!" << std::endl;

  } else {
    edm::LogVerbatim("SiPixelBadFEDChannelSimulationAnalyzer")
        << "=================================================================================" << std::endl;
    edm::LogInfo("SiPixelBadFEDChannelSimulationAnalyzer")
        << " All scenarios in probability record are found in the scenario map, (all is good)!" << std::endl;
    edm::LogVerbatim("SiPixelBadFEDChannelSimulationAnalyzer")
        << "=================================================================================" << std::endl;
  }
}

void SiPixelBadFEDChannelSimulationAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.setComment("Tries sanity of Pixel Stuck TBM simulation");
  desc.addUntracked<bool>("printDebug", true);
  desc.add<std::vector<int> >("probFunctionVariable",{0});
  desc.add<std::vector<double> >("probValue",{1.});
  descriptions.add("SiPixelBadFEDChannelSimulationAnalyzer", desc);
}

DEFINE_FWK_MODULE(SiPixelBadFEDChannelSimulationAnalyzer);
