// -*- C++ -*-
//
// Package:    SiPixelTools/SiPixelScenariosAndProbabilities
// Class:      SiPixelWriteForDigitizerFromHLT
//
/**\class SiPixelScenariosAndProbabilities SiPixelWriteForDigitizerFromHLT SiPixelTools/SiPixelScenariosAndProbabilities/plugins/SiPixelWriteForDigitizerFromHLT.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Tatjana Susa
//         Created:  Mon, 18 Mar 2024 15:51:12 GMT
//
//

// system include files
#include <memory>

#include "CondCore/CondDB/interface/ConnectionPool.h"
#include "CondCore/DBOutputService/interface/PoolDBOutputService.h"
#include "CondFormats/Common/interface/Time.h"
#include "CondFormats/Common/interface/TimeConversions.h"
#include "CondFormats/DataRecord/interface/SiPixelQualityFromDbRcd.h"
#include "CondFormats/SiPixelObjects/interface/PixelROC.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelQuality.h"
#include "FWCore/Framework/interface/ESWatcher.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include <iomanip>  // std::setw
#include <iostream>
#include <fstream>
#include <sstream>

#include <TROOT.h>
#include <TSystem.h>
#include <TCanvas.h>
#include <TFile.h>
#include <TLegend.h>
#include <TGraph.h>
#include <TH1.h>

typedef std::map<DetId, std::vector<unsigned int> > BadChannelCounterMap;
typedef std::map<DetId, std::bitset<16> > BadROCsMap;

class SiPixelWriteForDigitizerFromHLT : public edm::one::EDAnalyzer<> {
public:
  explicit SiPixelWriteForDigitizerFromHLT(const edm::ParameterSet& iConfig);
  ~SiPixelWriteForDigitizerFromHLT() override;
  void analyze(const edm::Event& evt, const edm::EventSetup& evtSetup) override;
  void endJob() override;
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  cond::persistency::ConnectionPool m_connectionPool;

  const std::string m_condDbQuality_1;
  const std::string m_condDbQuality_2;
  const std::string m_QualityTagName_1;
  const std::string m_QualityTagName_2;
  const std::string m_record;

  // Manually specify the start/end time.
  unsigned long long m_startTime;
  unsigned long long m_endTime;

  const bool printdebug_;
  const bool removeEmptyPayloads_;

  std::unique_ptr<SiPixelQuality> myQualities;
};

SiPixelWriteForDigitizerFromHLT::SiPixelWriteForDigitizerFromHLT(const edm::ParameterSet& iConfig)
    : m_connectionPool(),
      m_condDbQuality_1(iConfig.getParameter<std::string>("condDBQuality_1")),
      m_condDbQuality_2(iConfig.getParameter<std::string>("condDBQuality_2")),
      m_QualityTagName_1(iConfig.getParameter<std::string>("qualityTagName_1")),
      m_QualityTagName_2(iConfig.getParameter<std::string>("qualityTagName_2")),
      m_record(iConfig.getParameter<std::string>("record")),
      m_startTime(iConfig.getParameter<unsigned long long>("startIOV")),
      m_endTime(iConfig.getParameter<unsigned long long>("endIOV")),
      printdebug_(iConfig.getUntrackedParameter<bool>("printDebug", false)),
      removeEmptyPayloads_(iConfig.getUntrackedParameter<bool>("removeEmptyPayloads", false)) {
  m_connectionPool.setParameters(iConfig.getParameter<edm::ParameterSet>("DBParameters"));
  m_connectionPool.configure();

  //now do what ever initialization is needed
  myQualities = std::make_unique<SiPixelQuality>();
}

SiPixelWriteForDigitizerFromHLT::~SiPixelWriteForDigitizerFromHLT() = default;

void SiPixelWriteForDigitizerFromHLT::analyze(const edm::Event& evt, const edm::EventSetup& evtSetup) {
  std::stringstream ss;
  cond::Time_t startIov = m_startTime;
  cond::Time_t endIov = m_endTime;

  if (startIov > endIov)
    throw cms::Exception("endTime must be greater than startTime!");
  edm::LogInfo("SiPixelWriteForDigitizerFromHLT") << "[SiPixelWriteForDigitizerFromHLT::" << __func__ << "] "
                                                  << "Set start time " << startIov << "\n ... Set end time " << endIov;

  //QUALITY PAYLOAD 1
  // open db session for the quality payload
  edm::LogInfo("SiPixelWriteForDigitizerFromHLT") << "[SiPixelWriteForDigitizerFromHLT::" << __func__ << "] "
                                                  << "Query the condition database " << m_condDbQuality_1;

  cond::persistency::Session condDbSession_1 = m_connectionPool.createSession(m_condDbQuality_1);
  condDbSession_1.transaction().start(true);

  //QUALITY PAYLOAD 2
  edm::LogInfo("SiPixelWriteForDigitizerFromHLT") << "[SiPixelWriteForDigitizerFromHLT::" << __func__ << "] "
                                                  << "Query the condition database " << m_condDbQuality_2;

  cond::persistency::Session condDbSession_2 = m_connectionPool.createSession(m_condDbQuality_2);
  condDbSession_2.transaction().start(true);
  // query the database
  edm::LogInfo("SiPixelWriteForDigitizerFromHLT") << "[SiPixelWriteForDigitizerFromHLT::" << __func__ << "] "
                                                  << "Reading IOVs from tag " << m_QualityTagName_1;

  // GetList Of iovs_1
  std::vector<std::tuple<cond::Time_t, cond::Hash> > m_iovs_1;
  condDbSession_1.readIov(m_QualityTagName_1).selectRange(startIov, endIov, m_iovs_1);

  // create here the unpacked list of IOVs (run numbers)
  std::vector<unsigned int> listOfIOVs_1;
  std::transform(m_iovs_1.begin(),
                 m_iovs_1.end(),
                 std::back_inserter(listOfIOVs_1),
                 [](std::tuple<cond::Time_t, cond::Hash> myIOV) { return std::get<0>(myIOV); });

  // GetList Of iovs_2

  std::vector<std::tuple<cond::Time_t, cond::Hash> > m_iovs_2;
  condDbSession_2.readIov(m_QualityTagName_2).selectRange(1, 1, m_iovs_2);

  // create here the unpacked list of IOVs (run numbers)
  std::vector<unsigned int> listOfIOVs_2;
  std::transform(m_iovs_2.begin(),
                 m_iovs_2.end(),
                 std::back_inserter(listOfIOVs_2),
                 [](std::tuple<cond::Time_t, cond::Hash> myIOV) { return std::get<0>(myIOV); });

  if (m_iovs_2.size() != 1) {
    edm::LogError("SiPixelWriteFromDigitizerFromHLT")
        << "SiPixelWriteFromDigitizerFromHLT::" << __func__ << "] "
        << "Size of the payload " << m_QualityTagName_2 << " differnt from 1.\nThis should not happened.Aborting...";
    return;
  }
  auto hash_2 = std::get<1>(m_iovs_2.at(0));
  //auto key_2 = std::get<0>(m_iovs_2.at(0));
  auto payload_2 = condDbSession_2.fetchPayload<SiPixelQuality>(hash_2);
  auto theDisabledModules_2 = (*payload_2).getBadComponentList();

  BadROCsMap badRocsDCDC;
  for (const auto& mod : theDisabledModules_2) {
    if (badRocsDCDC.find(mod.DetID) == badRocsDCDC.end()) {
      badRocsDCDC[mod.DetID] = mod.BadRocs;
    }
  }

  BadChannelCounterMap badChannelCounterMap;

  for (auto const& myIOV_1 : m_iovs_1) {
    auto hash_1 = std::get<1>(myIOV_1);
    //auto key_1 = std::get<0>(myIOV_1);

    auto payload_1 = condDbSession_1.fetchPayload<SiPixelQuality>(hash_1);
    auto theDisabledModules = (*payload_1).getBadComponentList();
    for (const auto& mod : theDisabledModules) {
      auto detID = mod.DetID;
      int coded_badRocs = mod.BadRocs;
      std::bitset<16> bad_rocs(coded_badRocs);
      if (badChannelCounterMap.find(detID) == badChannelCounterMap.end()) {
        badChannelCounterMap[detID] = std::vector(16, 0u);
      }
      for (unsigned int index = 0; index < 16; ++index) {
        badChannelCounterMap[detID].at(index) += bad_rocs.test(index);
      }
    }
  }

  for (auto const& [DetID, badRocsCount] : badChannelCounterMap) {
    std::bitset<16> bad_rocs(0);
    for (unsigned int index = 0; index < badRocsCount.size(); ++index) {
      if (badRocsCount.at(index) == m_iovs_1.size()) {
        if (badRocsDCDC.find(DetID) != badRocsDCDC.end() && badRocsDCDC[DetID].test(index)) {
          continue;
        } else
          bad_rocs.set(index);
      }
    }

    if (bad_rocs.none())
      continue;
    auto BadRocs = static_cast<unsigned short>(bad_rocs.to_ulong());
    SiPixelQuality::disabledModuleType BadModule;
    BadModule.DetID = DetID;
    if (BadRocs == 65535) {  // "whole"
      BadModule.errorType = 0;
      BadModule.BadRocs = 65535;
    }                           //corresponds to all rocs being bad
    else if (BadRocs == 255) {  // "tbmA"
      BadModule.errorType = 1;
      BadModule.BadRocs = 255;
    }                             //corresponds to Rocs 0-7 being bad
    else if (BadRocs == 65280) {  // "tbmB"
      BadModule.errorType = 2;
      BadModule.BadRocs = 65280;
    }       //corresponds to Rocs 8-15 being bad
    else {  // "none"
      BadModule.errorType = 3;
      BadModule.BadRocs = BadRocs;
    }
    myQualities->addDisabledModule(BadModule);
  }  // loop over modules
}  // end analyze

//=================================
void SiPixelWriteForDigitizerFromHLT::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.setComment("Writes payloads of type SiPixelQuality");

  desc.addUntracked<bool>("printDebug", false);
  desc.addUntracked<bool>("removeEmptyPayloads", false);
  desc.add<std::string>("record", "SiPixelQualityFromDbRcd");
  desc.add<std::string>("condDBQuality_1", "frontier://FrontierProd/CMS_CONDITIONS");
  desc.add<std::string>("condDBQuality_2",
                        "sqlite_file:/afs/cern.ch/work/t/tsusacms/public/SiPixelScenariosAndProbabilities/CMSSW_14_0_0/"
                        "src/SiPixelAnalysis/PixelMaskedChannels/test/test_2024/SiPixelQualityTest.db");
  desc.add<std::string>("qualityTagName_1", "SiPixelQuality_v03_dup_hlt");
  desc.add<std::string>("qualityTagName_2", "SiPixelQualityTest");
  desc.add<unsigned long long>("startIOV", 362447);
  desc.add<unsigned long long>("endIOV", 373616);
  desc.add<std::string>("connect", "");
  edm::ParameterSetDescription descDBParameters;
  descDBParameters.addUntracked<std::string>("authenticationPath", "");
  descDBParameters.addUntracked<int>("authenticationSystem", 0);
  descDBParameters.addUntracked<std::string>("security", "");
  descDBParameters.addUntracked<int>("messageLevel", 0);
  desc.add<edm::ParameterSetDescription>("DBParameters", descDBParameters);
  descriptions.add("SiPixelWriteForDigitizerFromHLT", desc);
}

void SiPixelWriteForDigitizerFromHLT::endJob() {
  edm::Service<cond::service::PoolDBOutputService> poolDbService;
  if (poolDbService.isAvailable()) {
    poolDbService->writeOneIOV(*myQualities, 1, m_record);
  }
}

DEFINE_FWK_MODULE(SiPixelWriteForDigitizerFromHLT);
