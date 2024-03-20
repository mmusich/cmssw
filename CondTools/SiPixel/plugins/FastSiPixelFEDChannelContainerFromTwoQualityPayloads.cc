// -*- C++ -*-
//
// Package:    SiPixelTools/SiPixelScenariosAndProbabilities
// Class:      FastSiPixelFEDChannelContainerFromTwoQualityPayloads
//
/**\class SiPixelScenariosAndProbabilities FastSiPixelFEDChannelContainerFromTwoQualityPayloads.cc SiPixelTools/SiPixelScenariosAndProbabilities/plugins/FastSiPixelFEDChannelContainerFromTwoQualityPayloads.cc

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
#include "CondFormats/DataRecord/interface/SiPixelFedCablingMapRcd.h"
#include "CondFormats/DataRecord/interface/SiPixelQualityFromDbRcd.h"
#include "CondFormats/SiPixelObjects/interface/CablingPathToDetUnit.h"
#include "CondFormats/SiPixelObjects/interface/PixelROC.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFEDChannelContainer.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFedCablingMap.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFedCablingTree.h"
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

//#include <TROOT.h>
//#include <TSystem.h>
//#include <TCanvas.h>
//#include <TFile.h>
//#include <TLegend.h>
//#include <TGraph.h>
//#include <TH1.h>

namespace SiPixelFEDChannelFromTwoQualityPayloadsUtils {
  std::pair<unsigned int, unsigned int> unpack(cond::Time_t since) {
    auto kLowMask = 0XFFFFFFFF;
    auto run = (since >> 32);
    auto lumi = (since & kLowMask);
    return std::make_pair(run, lumi);
  }
}  // namespace SiPixelFEDChannelFromTwoQualityPayloadsUtils

typedef std::map<DetId, std::vector<PixelFEDChannel> > DetIdPixelFEDChannelMap;
typedef std::map<DetId, unsigned short> CodedBadROCsMap;

class FastSiPixelFEDChannelContainerFromTwoQualityPayloads : public edm::one::EDAnalyzer<> {
public:
  explicit FastSiPixelFEDChannelContainerFromTwoQualityPayloads(const edm::ParameterSet& iConfig);
  ~FastSiPixelFEDChannelContainerFromTwoQualityPayloads() override;
  void analyze(const edm::Event& evt, const edm::EventSetup& evtSetup) override;
  void endJob() override;
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  SiPixelFEDChannelContainer::SiPixelFEDChannelCollection createFromSiPixelQuality(
      const SiPixelQuality& theQuality,
      const SiPixelFedCablingMap& theFedCabling,
      const SiPixelFedCablingTree& theCablingTree);

  /*
  DetIdPixelFEDChannelMap 
  fillFromSiPixelQuality(const SiPixelQuality& theQuality,
			 const SiPixelFedCablingMap& theFedCabling,
			 const SiPixelFedCablingTree& theCablingTree);
  */

  DetIdPixelFEDChannelMap fillFromSiPixelQuality(const SiPixelQuality& theQuality,
                                                 const SiPixelFedCablingMap& theFedCabling,
                                                 const SiPixelFedCablingTree& theCablingTree,
                                                 const CodedBadROCsMap& badROCsMapDCDC,
                                                 const CodedBadROCsMap& badROCsMapPerm,
                                                 const bool cleanPayload);

  /*
  SiPixelFEDChannelContainer::SiPixelFEDChannelCollection createFromSiPixelQualities(
      const SiPixelQuality& theQuality_1,
      const SiPixelQuality& theQuality_2,      
      const SiPixelFedCablingMap& theFedCabling,
      const SiPixelFedCablingTree& theCablingTree);
  */
private:
  cond::persistency::ConnectionPool m_connectionPool;
  //const std::string m_condDbQuality;
  const std::string m_condDbQuality_1;
  const std::string m_condDbQuality_2;
  const std::string m_condDbQuality_DCDC;
  const std::string m_condDbQuality_Perm;
  const std::string m_condDbCabling;
  const std::string m_QualityTagName_1;
  const std::string m_QualityTagName_2;
  const std::string m_QualityTagName_DCDC;
  const std::string m_QualityTagName_Perm;
  const std::string m_CablingTagName;
  const std::string m_record;

  // Specify output text file name. Leave empty if do not want to dump in a file
  const std::string m_output;

  // Manually specify the start/end time.
  unsigned long long m_startTime;
  unsigned long long m_endTime;

  const bool printdebug_;
  const bool isMC_;
  const bool removeEmptyPayloads_;

  std::unique_ptr<SiPixelFEDChannelContainer> myQualities;

  inline unsigned int closest_from_above(std::vector<unsigned int> const& vec, unsigned int value) {
    auto const it = std::lower_bound(vec.begin(), vec.end(), value);
    return vec.at(it - vec.begin() - 1);
  }

  inline unsigned int closest_from_below(std::vector<unsigned int> const& vec, unsigned int value) {
    auto const it = std::upper_bound(vec.begin(), vec.end(), value);
    return vec.at(it - vec.begin() - 1);
  }
  inline cond::Time_t closest_from_above(std::vector<cond::Time_t> const& vec, cond::Time_t value) {
    auto const it = std::lower_bound(vec.begin(), vec.end(), value);
    return vec.at(it - vec.begin() - 1);
  }
  inline cond::Time_t closest_from_below(std::vector<cond::Time_t> const& vec, cond::Time_t value) {
    auto const it = std::upper_bound(vec.begin(), vec.end(), value);
    return vec.at(it - vec.begin() - 1);
  }
};

FastSiPixelFEDChannelContainerFromTwoQualityPayloads::FastSiPixelFEDChannelContainerFromTwoQualityPayloads(
    const edm::ParameterSet& iConfig)
    : m_connectionPool(),
      m_condDbQuality_1(iConfig.getParameter<std::string>("condDBQuality_1")),
      m_condDbQuality_2(iConfig.getParameter<std::string>("condDBQuality_2")),
      m_condDbQuality_DCDC(iConfig.getParameter<std::string>("condDBQuality_DCDC")),
      m_condDbQuality_Perm(iConfig.getParameter<std::string>("condDBQuality_Perm")),
      m_condDbCabling(iConfig.getParameter<std::string>("condDBCabling")),
      m_QualityTagName_1(iConfig.getParameter<std::string>("qualityTagName_1")),
      m_QualityTagName_2(iConfig.getParameter<std::string>("qualityTagName_2")),
      m_QualityTagName_DCDC(iConfig.getParameter<std::string>("qualityTagName_DCDC")),
      m_QualityTagName_Perm(iConfig.getParameter<std::string>("qualityTagName_Perm")),

      m_CablingTagName(iConfig.getParameter<std::string>("cablingMapTagName")),
      m_record(iConfig.getParameter<std::string>("record")),
      m_output(iConfig.getParameter<std::string>("output")),
      m_startTime(iConfig.getParameter<unsigned long long>("startIOV")),
      m_endTime(iConfig.getParameter<unsigned long long>("endIOV")),
      printdebug_(iConfig.getUntrackedParameter<bool>("printDebug", false)),
      isMC_(iConfig.getUntrackedParameter<bool>("isMC", true)),
      removeEmptyPayloads_(iConfig.getUntrackedParameter<bool>("removeEmptyPayloads", false)) {
  m_connectionPool.setParameters(iConfig.getParameter<edm::ParameterSet>("DBParameters"));
  m_connectionPool.configure();

  //now do what ever initialization is needed
  myQualities = std::make_unique<SiPixelFEDChannelContainer>();
}

FastSiPixelFEDChannelContainerFromTwoQualityPayloads::~FastSiPixelFEDChannelContainerFromTwoQualityPayloads() = default;

void FastSiPixelFEDChannelContainerFromTwoQualityPayloads::analyze(const edm::Event& evt,
                                                                   const edm::EventSetup& evtSetup) {
  std::stringstream ss;
  cond::Time_t startIov = m_startTime;
  cond::Time_t endIov = m_endTime;

  if (startIov > endIov)
    throw cms::Exception("endTime must be greater than startTime!");
  edm::LogInfo("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
      << "[FastSiPixelFEDChannelContainerFromTwoQualityPayloads::" << __func__ << "] "
      << "Set start time " << startIov << "\n ... Set end time " << endIov;

  //QUALITY PAYLOAD 1
  // open db session for the quality payload
  edm::LogInfo("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
      << "[FastSiPixelFEDChannelContainerFromTwoQualityPayloads::" << __func__ << "] "
      << "Query the condition database " << m_condDbQuality_1;

  cond::persistency::Session condDbSession_1 = m_connectionPool.createSession(m_condDbQuality_1);
  condDbSession_1.transaction().start(true);

  // query the database
  edm::LogInfo("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
      << "[FastSiPixelFEDChannelContainerFromTwoQualityPayloads::" << __func__ << "] "
      << "Reading IOVs from tag " << m_QualityTagName_1;

  //QUALITY PAYLOAD 2

  edm::LogInfo("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
      << "[FastSiPixelFEDChannelContainerFromTwoQualityPayloads::" << __func__ << "] "
      << "Query the condition database " << m_condDbQuality_2;

  cond::persistency::Session condDbSession_2 = m_connectionPool.createSession(m_condDbQuality_2);
  condDbSession_2.transaction().start(true);

  // query the database
  edm::LogInfo("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
      << "[FastSiPixelFEDChannelContainerFromTwoQualityPayloads::" << __func__ << "] "
      << "Reading IOVs from tag " << m_QualityTagName_2;
  //=================================
  //QUALITY PAYLOAD DCDC
  // open db session for the quality payload
  edm::LogInfo("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
      << "[FastSiPixelFEDChannelContainerFromTwoQualityPayloads::" << __func__ << "] "
      << "Query the condition database " << m_condDbQuality_DCDC;

  cond::persistency::Session condDbSession_DCDC = m_connectionPool.createSession(m_condDbQuality_DCDC);
  condDbSession_DCDC.transaction().start(true);

  // query the database
  edm::LogInfo("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
      << "[FastSiPixelFEDChannelContainerFromTwoQualityPayloads::" << __func__ << "] "
      << "Reading IOVs from tag " << m_QualityTagName_DCDC;

  //QUALITY PAYLOAD 2

  edm::LogInfo("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
      << "[FastSiPixelFEDChannelContainerFromTwoQualityPayloads::" << __func__ << "] "
      << "Query the condition database " << m_condDbQuality_Perm;

  cond::persistency::Session condDbSession_Perm = m_connectionPool.createSession(m_condDbQuality_Perm);
  condDbSession_Perm.transaction().start(true);

  //====================================================

  // open db session for the cabling map
  edm::LogInfo("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
      << "[FastSiPixelFEDChannelContainerFromTwoQualityPayloads::" << __func__ << "] "
      << "Query the condition database " << m_condDbCabling;

  cond::persistency::Session condDbSession2 = m_connectionPool.createSession(m_condDbCabling);
  condDbSession2.transaction().start(true);

  // query the database
  edm::LogInfo("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
      << "[FastSiPixelFEDChannelContainerFromTwoQualityPayloads::" << __func__ << "] "
      << "Reading IOVs from tag " << m_CablingTagName;

  // get the list of payloads for the SiPixelQuality tag
  std::vector<std::tuple<cond::Time_t, cond::Hash> > m_iovs_1;
  condDbSession_1.readIov(m_QualityTagName_1).selectRange(startIov, endIov, m_iovs_1);

  std::vector<std::tuple<cond::Time_t, cond::Hash> > m_iovs_2;
  condDbSession_2.readIov(m_QualityTagName_2).selectRange(startIov, endIov, m_iovs_2);

  std::vector<std::tuple<cond::Time_t, cond::Hash> > m_iovs_DCDC;
  condDbSession_DCDC.readIov(m_QualityTagName_DCDC).selectRange(1, 1, m_iovs_DCDC);

  std::vector<std::tuple<cond::Time_t, cond::Hash> > m_iovs_Perm;
  condDbSession_Perm.readIov(m_QualityTagName_Perm).selectRange(startIov, endIov, m_iovs_Perm);

  //============================================================================
  std::vector<unsigned int> listOfIOVs_DCDC;
  std::transform(m_iovs_DCDC.begin(),
                 m_iovs_DCDC.end(),
                 std::back_inserter(listOfIOVs_DCDC),
                 [](std::tuple<cond::Time_t, cond::Hash> myIOV) { return std::get<0>(myIOV); });

  if (m_iovs_DCDC.size() != 1) {
    edm::LogError("FastSiPixelFEDChannelContainerFromTwoQualityPayload")
        << "FastSiPixelFEDChannelContainerFromTwoQualityPayload::" << __func__ << "] "
        << "Size of the payload " << m_QualityTagName_DCDC << " differnt from 1.\nThis should not happened.Aborting...";
    return;
  }

  auto hash_DCDC = std::get<1>(m_iovs_DCDC.at(0));
  auto payload_DCDC = condDbSession_DCDC.fetchPayload<SiPixelQuality>(hash_DCDC);
  auto theDisabledModules_DCDC = (*payload_DCDC).getBadComponentList();

  CodedBadROCsMap badRocsDCDC;
  for (const auto& mod : theDisabledModules_DCDC) {
    if (badRocsDCDC.find(mod.DetID) == badRocsDCDC.end()) {
      badRocsDCDC[mod.DetID] = mod.BadRocs;
    }
  }

  std::vector<unsigned int> listOfIOVs_Perm;
  std::transform(m_iovs_Perm.begin(),
                 m_iovs_Perm.end(),
                 std::back_inserter(listOfIOVs_Perm),
                 [](std::tuple<cond::Time_t, cond::Hash> myIOV) { return std::get<0>(myIOV); });

  if (m_iovs_Perm.size() != 1) {
    edm::LogError("FastSiPixelFEDChannelContainerFromTwoQualityPayload")
        << "FastSiPixelFEDChannelContainerFromTwoQualityPayload::" << __func__ << "] "
        << "Size of the payload " << m_QualityTagName_Perm << " differnt from 1.\nThis should not happened.Aborting...";
    return;
  }

  auto hash_Perm = std::get<1>(m_iovs_Perm.at(0));
  auto payload_Perm = condDbSession_Perm.fetchPayload<SiPixelQuality>(hash_Perm);
  auto theDisabledModules_Perm = (*payload_Perm).getBadComponentList();

  CodedBadROCsMap badRocsPerm;
  for (const auto& mod : theDisabledModules_Perm) {
    if (badRocsPerm.find(mod.DetID) == badRocsPerm.end()) {
      badRocsPerm[mod.DetID] = mod.BadRocs;
    }
  }

  //TS std::cout << "IOV size:" << m_iovs_DCDC.size() << " " << m_iovs_Perm.size() << std::endl;
  //TS std::cout << "# of modules:" << badRocsDCDC.size() << " " << badRocsPerm.size() << std::endl;

  //=============================================================================
  //  std::vector<std::tuple<cond::Time_t, cond::Hash> > m_iovs  = m_iovs_1;
  //m_iovs.insert(m_iovs.end(), m_iovs_2.begin(), m_iovs_2.end());

  const auto MIN_VAL = cond::timeTypeSpecs[cond::runnumber].beginValue;
  const auto MAX_VAL = cond::timeTypeSpecs[cond::runnumber].endValue;

  // get the list of payloads for the Cabling Map
  std::vector<std::tuple<cond::Time_t, cond::Hash> > m_cabling_iovs;
  condDbSession2.readIov(m_CablingTagName).selectRange(MIN_VAL, MAX_VAL, m_cabling_iovs);

  // create here the unpacked list of IOVs (run numbers)
  std::vector<unsigned int> listOfIOVs_1;
  std::transform(m_iovs_1.begin(),
                 m_iovs_1.end(),
                 std::back_inserter(listOfIOVs_1),
                 [](std::tuple<cond::Time_t, cond::Hash> myIOV) -> unsigned int {
                   return SiPixelFEDChannelFromTwoQualityPayloadsUtils::unpack(std::get<0>(myIOV)).first;
                 });

  std::vector<unsigned int> listOfIOVs_2;
  std::transform(m_iovs_2.begin(),
                 m_iovs_2.end(),
                 std::back_inserter(listOfIOVs_2),
                 [](std::tuple<cond::Time_t, cond::Hash> myIOV) -> unsigned int {
                   return SiPixelFEDChannelFromTwoQualityPayloadsUtils::unpack(std::get<0>(myIOV)).first;
                 });

  //  std::vector<unsigned int> listOfIOVs =listOfIOVs_1;
  std::vector<unsigned int> listOfIOVs(listOfIOVs_1.begin(), listOfIOVs_1.end());

  for (const auto myIOV : listOfIOVs_2) {
    if (std::find(listOfIOVs_1.begin(), listOfIOVs_1.end(), myIOV) == listOfIOVs_1.end()) {
      listOfIOVs.push_back(myIOV);
    }
  }
  //========
  // create here the  list of Lumi  (runNumbersLS) IOVs
  std::vector<cond::Time_t> listOfIOVsRunLS_1;
  std::transform(m_iovs_1.begin(),
                 m_iovs_1.end(),
                 std::back_inserter(listOfIOVsRunLS_1),
                 [](std::tuple<cond::Time_t, cond::Hash> myIOV) { return std::get<0>(myIOV); });

  std::vector<cond::Time_t> listOfIOVsRunLS_2;
  std::transform(m_iovs_2.begin(),
                 m_iovs_2.end(),
                 std::back_inserter(listOfIOVsRunLS_2),
                 [](std::tuple<cond::Time_t, cond::Hash> myIOV) { return std::get<0>(myIOV); });

  std::vector<cond::Time_t> listOfIOVsRunLS(listOfIOVsRunLS_1.begin(), listOfIOVsRunLS_1.end());
  for (const auto myIOV : listOfIOVsRunLS_2) {
    if (std::find(listOfIOVsRunLS_1.begin(), listOfIOVsRunLS_1.end(), myIOV) == listOfIOVsRunLS_1.end()) {
      listOfIOVsRunLS.push_back(myIOV);
    }
  }

  //======
  sort(listOfIOVs.begin(), listOfIOVs.end());
  sort(listOfIOVsRunLS.begin(), listOfIOVsRunLS.end());

  std::cout << "===============" << std::endl;
  /*
  for (const auto& myIOV : m_iovs_1){
    std::cout << " " << std::get<0>(myIOV) << " " << std::get<1>(myIOV) << std::endl;
  }
  for (const auto& myIOV : listOfIOVs_1){
    std::cout << " " << myIOV << std::endl;
  }
  
  std::cout << "-------" << std::endl;
  for (const auto& myIOV : m_iovs_2){
    std::cout << " " << std::get<0>(myIOV) << " " << std::get<1>(myIOV) << std::endl;
  }    
  for (const auto& myIOV : listOfIOVs_2){
    std::cout << " " << myIOV << std::endl;
  }
  
  std::cout << "-------" << std::endl;

  for (const auto& myIOV : listOfIOVsRunLS){
    std::cout << " " << myIOV<< std::endl;
  }
  for (const auto& myIOV : listOfIOVs){
    std::cout << " " << myIOV<< std::endl;
    }
  */
  std::vector<unsigned int> listOfCablingIOVs;
  std::transform(m_cabling_iovs.begin(),
                 m_cabling_iovs.end(),
                 std::back_inserter(listOfCablingIOVs),
                 [](std::tuple<cond::Time_t, cond::Hash> myIOV2) -> unsigned int { return std::get<0>(myIOV2); });

  edm::LogInfo("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
      << " Number of SiPixelQuality paloyads to analyze: " << listOfIOVs.size()
      << " Number of SiPixelFedCablngMap payloads: " << listOfCablingIOVs.size() << std::endl;

  if (listOfCablingIOVs.size() > 1) {
    if (closest_from_below(listOfCablingIOVs, listOfIOVs.front()) !=
        closest_from_above(listOfCablingIOVs, listOfIOVs.back())) {
      throw cms::Exception("") << " The Pixel FED Cabling map does not cover all the requested SiPixelQuality IOVs in "
                                  "the same interval of validity \n";
    }
  } else {
    if (listOfIOVs.front() < listOfCablingIOVs.front()) {
      throw cms::Exception("") << " The Pixel FED Cabling map does not cover all the requested IOVs \n";
    }
  }

  edm::LogInfo("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
      << " First run covered by SiPixelQuality tag: " << listOfIOVs.front()
      << " / last run covered by SiPixelQuality tag: " << listOfIOVs.back() << std::endl;

  edm::LogVerbatim("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
      << " SiPixel Cabling Map IOVs in the interval: ";
  for (const auto& cb : m_cabling_iovs) {
    edm::LogVerbatim("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
        << " " << std::setw(6) << std::get<0>(cb) << " : " << std::get<1>(cb);
  }
  edm::LogVerbatim("FastSiPixelFEDChannelContainerFromTwoQualityPayloads") << std::endl;

  if (printdebug_) {
    edm::LogInfo("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
        << " closest_from_above(listOfCablingIOVs,listOfIOVs.back()): "
        << closest_from_above(listOfCablingIOVs, listOfIOVs.back()) << std::endl;
    edm::LogInfo("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
        << " closest_from_below(listOfCablingIOVs,listOfIOVs.front()): "
        << closest_from_below(listOfCablingIOVs, listOfIOVs.front()) << std::endl;
  }

  auto it = std::find(
      listOfCablingIOVs.begin(), listOfCablingIOVs.end(), closest_from_below(listOfCablingIOVs, listOfIOVs.front()));
  int index = std::distance(listOfCablingIOVs.begin(), it);

  edm::LogInfo("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
      << " using the SiPixelFedCablingMap with hash: " << std::get<1>(m_cabling_iovs.at(index)) << std::endl;

  std::cout << "FastSiPixelFEDChannelContainerFromTwoQualityPayloads "
            << " using the SiPixelFedCablingMap with hash: " << std::get<1>(m_cabling_iovs.at(index)) << std::endl;

  auto theCablingMapPayload = condDbSession2.fetchPayload<SiPixelFedCablingMap>(std::get<1>(m_cabling_iovs.at(index)));

  auto theCablingTree = (*theCablingMapPayload).cablingTree();

  printf(
      "Progressing Bar                               :0%%       20%%       40%%       60%%       80%%       100%%\n");
  printf("Translating into SiPixelFEDChannelCollection  :");

  int step = (listOfIOVsRunLS.size() >= 50) ? listOfIOVsRunLS.size() / 50 : 1;
  int niov = 0;

  for (const auto& myRunLS : listOfIOVsRunLS) {
    if (niov % step == 0) {
      printf(".");
      fflush(stdout);
    }
    auto runLS = SiPixelFEDChannelFromTwoQualityPayloadsUtils::unpack(myRunLS);

    if (myRunLS < listOfIOVsRunLS_1.at(0) || myRunLS < listOfIOVsRunLS_2.at(0))
      continue;
    auto it_1 =
        std::find(listOfIOVsRunLS_1.begin(), listOfIOVsRunLS_1.end(), closest_from_below(listOfIOVsRunLS_1, myRunLS));

    if (it_1 == std::end(listOfIOVsRunLS_1)) {
      std::cout << "Element not found in first Quality" << std::endl;
      continue;
    }
    int index_1 = std::distance(listOfIOVsRunLS_1.begin(), it_1);
    auto it_2 =
        std::find(listOfIOVsRunLS_2.begin(), listOfIOVsRunLS_2.end(), closest_from_below(listOfIOVsRunLS_2, myRunLS));

    if (it_2 == std::end(listOfIOVsRunLS_2)) {
      std::cout << "Element not found in second Quality" << std::endl;
      continue;
    }
    int index_2 = std::distance(listOfIOVsRunLS_2.begin(), it_2);

    // auto payloadRunLumi_1 =  SiPixelFEDChannelFromTwoQualityPayloadsUtils::unpack(listOfIOVsRunLS_1.at(index_1));
    //auto payloadRunLumi_2 =  SiPixelFEDChannelFromTwoQualityPayloadsUtils::unpack(listOfIOVsRunLS_2.at(index_2));
    /*
    std::cout << "myRunLS + the rest: " << myRunLS 
	      << "\n  rest comes   " 
	      << runLS.first << " " << runLS.second 
	      << "\n     " 
	      << payloadRunLumi_1.first << " " << payloadRunLumi_1.second 
  	      << "\n     " 
	      << payloadRunLumi_2.first << " " << payloadRunLumi_2.second << std::endl; 
    */
    auto hash_1 = std::get<1>(m_iovs_1.at(index_1));
    auto key_1 = std::get<0>(m_iovs_1.at(index_1));
    auto hash_2 = std::get<1>(m_iovs_2.at(index_2));
    auto key_2 = std::get<0>(m_iovs_2.at(index_2));
    //std::cout << "HASHES: "  << key_1 << " " << hash_1 << std::endl;
    //std::cout << "        "  << key_2 << " " << hash_2 << std::endl;

    auto payload_1 = condDbSession_1.fetchPayload<SiPixelQuality>(hash_1);
    auto payload_2 = condDbSession_2.fetchPayload<SiPixelQuality>(hash_2);

    auto theDetIdPixelFEDChannelMap_1 = this->fillFromSiPixelQuality(
        *payload_1, *theCablingMapPayload, *theCablingTree, badRocsDCDC, badRocsPerm, true);
    auto theDetIdPixelFEDChannelMap_2 = this->fillFromSiPixelQuality(
        *payload_2, *theCablingMapPayload, *theCablingTree, badRocsDCDC, badRocsPerm, false);

    // std::cout << "SIZED: "
    //	      << theDetIdPixelFEDChannelMap_1.size() << " "
    //	      << theDetIdPixelFEDChannelMap_2.size() << std::endl;

    for (auto const& [key, channels] : theDetIdPixelFEDChannelMap_2) {
      //std::cout << key.rawId()       // string (key)
      //		<< ':'
      //	<< val        // string's value
      //		<< std::endl;
      if (theDetIdPixelFEDChannelMap_1.find(key) != theDetIdPixelFEDChannelMap_1.end()) {
        for (const auto channel : channels) {
          theDetIdPixelFEDChannelMap_1[key].push_back(channel);
        }
      } else {
        theDetIdPixelFEDChannelMap_1[key] = channels;
      }
    }

    //std::cout << "AFTER MERGING: " << theDetIdPixelFEDChannelMap_1.size () << std::endl;

    SiPixelFEDChannelContainer::SiPixelFEDChannelCollection theSiPixelFEDChannelCollection;
    for (auto const& [key, channels] : theDetIdPixelFEDChannelMap_1) {
      if (!theDetIdPixelFEDChannelMap_1[key].empty()) {
        theSiPixelFEDChannelCollection[key] = channels;
      }
    }

    std::string scenario = std::to_string(runLS.first) + "_" + std::to_string(runLS.second);
    // std::cout << "Scenario: " << scenario << std::endl;
    //std::cout << "\n=======================" << std::endl;

    ss << runLS.first << "," << runLS.second << " (" << myRunLS << "/" << key_1 << "/" << key_2 << ")"
       << " [hash_1: " << hash_1 << "] [hash_2: " << hash_2 << "]\n";

    //std::cout << " " << myRunLS.first  << "  " <<  payloadRunLumi_1 << " " <<  payloadRunLumi_2 << std::endl;

    /*
    auto payload = condDbSession_1.fetchPayload<SiPixelQuality>(std::get<1>(myIOV));
    auto runLS = SiPixelFEDChannelFromTwoQualityPayloadsUtils::unpack(std::get<0>(myIOV));
    
    // print IOVs summary

    std::string scenario = std::to_string(runLS.first) + "_" + std::to_string(runLS.second);
       
    if (printdebug_) {
    edm::LogInfo("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
    << "Found IOV:" << runLS.first << "(" << runLS.second << ")" << std::endl;
    }
    */

    /* auto theSiPixelFEDChannelCollection =
        this->createFromSiPixelQuality(*payload, *theCablingMapPayload, *theCablingTree);
    */
    if (removeEmptyPayloads_ && theSiPixelFEDChannelCollection.empty())
      return;

    myQualities->setScenario(scenario, theSiPixelFEDChannelCollection);
    ++niov;
  }

  //carriage return for tests
  printf("\n\n");

  edm::LogInfo("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
      << "[FastSiPixelFEDChannelContainerFromTwoQualityPayloads::" << __func__ << "] "
      << "Read " << niov << " IOVs from tag " << m_QualityTagName_1
      << " corresponding to the specified time interval.\n\n"
      << ss.str();

  if (printdebug_) {
    edm::LogInfo("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
        << "[FastSiPixelFEDChannelContainerFromTwoQualityPayloads::" << __func__ << "] " << ss.str();
  }

  condDbSession_1.transaction().commit();
  condDbSession_2.transaction().commit();
  condDbSession2.transaction().commit();

  if (!m_output.empty()) {
    std::ofstream fout;
    fout.open(m_output);
    fout << ss.str();
    fout.close();
  }
}

// ------------ method called once each job just before starting event loop  ------------
SiPixelFEDChannelContainer::SiPixelFEDChannelCollection
FastSiPixelFEDChannelContainerFromTwoQualityPayloads::createFromSiPixelQuality(
    const SiPixelQuality& theQuality,
    const SiPixelFedCablingMap& theFedCabling,
    const SiPixelFedCablingTree& theCablingTree) {
  auto fedid_ = theFedCabling.det2fedMap();

  SiPixelFEDChannelContainer::SiPixelFEDChannelCollection theBadChannelCollection;

  auto theDisabledModules = theQuality.getBadComponentList();
  for (const auto& mod : theDisabledModules) {
    //mod.DetID, mod.errorType,mod.BadRocs

    int coded_badRocs = mod.BadRocs;
    std::vector<PixelFEDChannel> disabledChannelsDetSet;
    std::vector<sipixelobjects::CablingPathToDetUnit> path = theFedCabling.pathToDetUnit(mod.DetID);
    unsigned int nrocs_inLink(0);
    if (!path.empty()) {
      const sipixelobjects::PixelFEDCabling* aFed = theCablingTree.fed(path.at(0).fed);
      const sipixelobjects::PixelFEDLink* link = aFed->link(path.at(0).link);
      nrocs_inLink = link->numberOfROCs();
    } else {
      throw cms::Exception("Inconsistent data") << "could not find CablingPathToDetUnit for detId:" << mod.DetID;
    }

    std::bitset<16> bad_rocs(coded_badRocs);
    unsigned int n_ch = bad_rocs.size() / nrocs_inLink;

    for (unsigned int i_roc = 0; i_roc < n_ch; ++i_roc) {
      unsigned int first_idx = nrocs_inLink * i_roc;
      unsigned int sec_idx = nrocs_inLink * (i_roc + 1) - 1;
      unsigned int mask = pow(2, nrocs_inLink) - 1;
      unsigned int n_setbits = (coded_badRocs >> (i_roc * nrocs_inLink)) & mask;

      if (n_setbits == 0) {
        continue;
      }

      if (n_setbits != mask) {
        if (printdebug_) {
          edm::LogWarning("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
              << "Mismatch! DetId: " << mod.DetID << " " << n_setbits << " " << mask << std::endl;
        }
        continue;
      }

      if (printdebug_) {
        edm::LogVerbatim("FastSiPixelFEDChannelContainerFromTwoQualityPayloads") << "passed" << std::endl;
      }

      unsigned int link_id = 99999;
      unsigned int fed_id = 99999;

      for (auto const& p : path) {
        const sipixelobjects::PixelFEDCabling* aFed = theCablingTree.fed(p.fed);
        const sipixelobjects::PixelFEDLink* link = aFed->link(p.link);
        const sipixelobjects::PixelROC* roc = link->roc(p.roc);
        unsigned int first_roc = roc->idInDetUnit();

        if (first_roc == first_idx) {
          link_id = p.link;
          fed_id = p.fed;
          break;
        }
      }

      if (printdebug_) {
        edm::LogVerbatim("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
            << " " << fed_id << " " << link_id << " " << first_idx << "  " << sec_idx << std::endl;
      }

      PixelFEDChannel ch = {fed_id, link_id, first_idx, sec_idx};
      disabledChannelsDetSet.push_back(ch);

      if (printdebug_) {
        edm::LogVerbatim("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
            << i_roc << " " << coded_badRocs << " " << first_idx << " " << sec_idx << std::endl;
        edm::LogVerbatim("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
            << "=======================================" << std::endl;
      }
    }

    if (!disabledChannelsDetSet.empty()) {
      theBadChannelCollection[mod.DetID] = disabledChannelsDetSet;
    }
  }
  return theBadChannelCollection;
}
//=================================================================
DetIdPixelFEDChannelMap FastSiPixelFEDChannelContainerFromTwoQualityPayloads::fillFromSiPixelQuality(
    const SiPixelQuality& theQuality,
    const SiPixelFedCablingMap& theFedCabling,
    const SiPixelFedCablingTree& theCablingTree,
    const CodedBadROCsMap& badROCsMapDCDC,
    const CodedBadROCsMap& badROCsMapPerm,
    const bool cleanPayload) {
  auto fedid_ = theFedCabling.det2fedMap();

  //SiPixelFEDChannelContainer::SiPixelFEDChannelCollection theBadChannelCollection;

  DetIdPixelFEDChannelMap detIdPixelFEDChannelMap;

  auto theDisabledModules = theQuality.getBadComponentList();
  for (const auto& mod : theDisabledModules) {
    //mod.DetID, mod.errorType,mod.BadRocs

    auto coded_badRocs = mod.BadRocs;
    //============
    if (cleanPayload) {
      std::cout << "------------------------" << std::endl;
      std::bitset<16> bad_rocs_test_1(coded_badRocs);
      std::cout << "Coded BadROCs start:      " << coded_badRocs << " " << bad_rocs_test_1 << std::endl;

      if (badROCsMapDCDC.find(mod.DetID) != badROCsMapDCDC.end()) {
        coded_badRocs &= ~badROCsMapDCDC.at(mod.DetID);
        std::bitset<16> bad_rocs_test_DCDC(badROCsMapDCDC.at(mod.DetID));
        std::cout << "DCDC:                     " << badROCsMapDCDC.at(mod.DetID) << " " << bad_rocs_test_DCDC
                  << std::endl;
      }
      std::bitset<16> bad_rocs_test_2(coded_badRocs);
      std::cout << "Coded BadROCs after DCDC: " << coded_badRocs << " " << bad_rocs_test_2 << std::endl;

      if (badROCsMapPerm.find(mod.DetID) != badROCsMapPerm.end()) {
        coded_badRocs &= ~badROCsMapPerm.at(mod.DetID);
        std::bitset<16> bad_rocs_test_Perm(badROCsMapPerm.at(mod.DetID));
        std::cout << "Perm:                     " << badROCsMapPerm.at(mod.DetID) << " " << bad_rocs_test_Perm
                  << std::endl;
      }
      std::bitset<16> bad_rocs_test_3(coded_badRocs);

      std::cout << "Coded BadROCs after Perm: " << coded_badRocs << " " << bad_rocs_test_3 << std::endl;

      //if (mod.BadRocs != coded_badRocs){

      std::cout << "mod.DetID: " << bad_rocs_test_1 << " " << bad_rocs_test_2 << " " << bad_rocs_test_3 << std::endl;
      std::cout << "------------------------" << std::endl;
    }

    // }

    //=====================================
    std::vector<PixelFEDChannel> disabledChannelsDetSet;
    std::vector<sipixelobjects::CablingPathToDetUnit> path = theFedCabling.pathToDetUnit(mod.DetID);
    unsigned int nrocs_inLink(0);
    if (!path.empty()) {
      const sipixelobjects::PixelFEDCabling* aFed = theCablingTree.fed(path.at(0).fed);
      const sipixelobjects::PixelFEDLink* link = aFed->link(path.at(0).link);
      nrocs_inLink = link->numberOfROCs();
    } else {
      throw cms::Exception("Inconsistent data") << "could not find CablingPathToDetUnit for detId:" << mod.DetID;
    }

    std::bitset<16> bad_rocs(coded_badRocs);
    unsigned int n_ch = bad_rocs.size() / nrocs_inLink;

    for (unsigned int i_roc = 0; i_roc < n_ch; ++i_roc) {
      unsigned int first_idx = nrocs_inLink * i_roc;
      unsigned int sec_idx = nrocs_inLink * (i_roc + 1) - 1;
      unsigned int mask = pow(2, nrocs_inLink) - 1;
      unsigned int n_setbits = (coded_badRocs >> (i_roc * nrocs_inLink)) & mask;

      if (n_setbits == 0) {
        continue;
      }

      if (n_setbits != mask) {
        if (printdebug_) {
          edm::LogWarning("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
              << "Mismatch! DetId: " << mod.DetID << " " << n_setbits << " " << mask << std::endl;
        }
        continue;
      }

      if (printdebug_) {
        edm::LogVerbatim("FastSiPixelFEDChannelContainerFromTwoQualityPayloads") << "passed" << std::endl;
      }

      unsigned int link_id = 99999;
      unsigned int fed_id = 99999;

      for (auto const& p : path) {
        const sipixelobjects::PixelFEDCabling* aFed = theCablingTree.fed(p.fed);
        const sipixelobjects::PixelFEDLink* link = aFed->link(p.link);
        const sipixelobjects::PixelROC* roc = link->roc(p.roc);
        unsigned int first_roc = roc->idInDetUnit();

        if (first_roc == first_idx) {
          link_id = p.link;
          fed_id = p.fed;
          break;
        }
      }

      if (printdebug_) {
        edm::LogVerbatim("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
            << " " << fed_id << " " << link_id << " " << first_idx << "  " << sec_idx << std::endl;
      }

      PixelFEDChannel ch = {fed_id, link_id, first_idx, sec_idx};
      disabledChannelsDetSet.push_back(ch);

      if (printdebug_) {
        edm::LogVerbatim("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
            << i_roc << " " << coded_badRocs << " " << first_idx << " " << sec_idx << std::endl;
        edm::LogVerbatim("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
            << "=======================================" << std::endl;
      }
    }

    detIdPixelFEDChannelMap[mod.DetID] = disabledChannelsDetSet;
    //if (!disabledChannelsDetSet.empty()) {
    //  theBadChannelCollection[mod.DetID] = disabledChannelsDetSet;
    //}
  }

  return detIdPixelFEDChannelMap;
}
//=================================
void FastSiPixelFEDChannelContainerFromTwoQualityPayloads::fillDescriptions(
    edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.setComment("Writes payloads of type SiPixelFEDChannelContainer");
  desc.addUntracked<bool>("printDebug", false);
  desc.addUntracked<bool>("removeEmptyPayloads", false);
  desc.add<std::string>("record", "SiPixelStatusScenariosRcd");
  desc.add<std::string>("condDBQuality_1", "frontier://FrontierProd/CMS_CONDITIONS");
  desc.add<std::string>("condDBQuality_2", "frontier://FrontierProd/CMS_CONDITIONS");
  desc.add<std::string>("condDBQuality_DCDC",
                        "sqlite_file:/afs/cern.ch/work/t/tsusacms/public/SiPixelScenariosAndProbabilities/CMSSW_14_0_0/"
                        "src/SiPixelAnalysis/PixelMaskedChannels/test/test_2024/SiPixelQualityTest.db");
  desc.add<std::string>("condDBQuality_Perm",
                        "sqlite_file:/afs/cern.ch/work/t/tsusacms/public/SiPixelScenariosAndProbabilities/CMSSW_14_0_0/"
                        "src/SiPixelAnalysis/PixelMaskedChannels/test/test_2024/SiPixelQuality_forDigitizer_test.db");
  desc.add<std::string>("qualityTagName_1", "SiPixelQuality_byPCL_prompt_v2");
  desc.add<std::string>("qualityTagName_2", "SiPixelQuality_byPCL_stuckTBM_v1");
  desc.add<std::string>("qualityTagName_DCDC", "SiPixelQualityTest");
  desc.add<std::string>("qualityTagName_Perm", "SiPixelQuality_forDigitizer_test");
  desc.add<std::string>("condDBCabling", "frontier://FrontierProd/CMS_CONDITIONS");
  desc.add<std::string>("cablingMapTagName", "SiPixelFedCablingMap_v1");
  desc.add<unsigned long long>("startIOV", 1592470794141697);
  desc.add<unsigned long long>("endIOV", 1592530923683896);
  desc.add<std::string>("output", "summary.txt");
  desc.add<std::string>("connect", "");

  edm::ParameterSetDescription descDBParameters;
  descDBParameters.addUntracked<std::string>("authenticationPath", "");
  descDBParameters.addUntracked<int>("authenticationSystem", 0);
  descDBParameters.addUntracked<std::string>("security", "");
  descDBParameters.addUntracked<int>("messageLevel", 0);

  desc.add<edm::ParameterSetDescription>("DBParameters", descDBParameters);
  descriptions.add("FastSiPixelFEDChannelContainerFromTwoQualityPayloads", desc);
}

void FastSiPixelFEDChannelContainerFromTwoQualityPayloads::endJob() {
  //  edm::LogInfo("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")<<"Analyzed "<<IOVcount_<<" IOVs"<<std::endl;
  edm::LogInfo("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
      << "Size of SiPixelFEDChannelContainer object " << myQualities->size() << std::endl
      << std::endl;

  if (printdebug_) {
    edm::LogInfo("FastSiPixelFEDChannelContainerFromTwoQualityPayloads")
        << "Content of SiPixelFEDChannelContainer " << std::endl;

    // use built-in method in the CondFormat
    myQualities->printAll();
  }

  // Form the data here
  edm::Service<cond::service::PoolDBOutputService> poolDbService;
  if (poolDbService.isAvailable()) {
    cond::Time_t valid_time = poolDbService->currentTime();
    // this writes the payload to begin in current run defined in cfg
    if (!isMC_) {
      poolDbService->writeOneIOV(*myQualities, valid_time, m_record);
    } else {
      // for MC IOV since=1
      poolDbService->writeOneIOV(*myQualities, 1, m_record);
    }
  }
}

DEFINE_FWK_MODULE(FastSiPixelFEDChannelContainerFromTwoQualityPayloads);
