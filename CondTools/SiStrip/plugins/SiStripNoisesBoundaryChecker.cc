// system includes
#include <iostream>
#include <fstream>

// user includes
#include "CalibTracker/Records/interface/SiStripDependentRecords.h"
#include "CalibTracker/SiStripCommon/interface/SiStripDetInfoFileReader.h"
#include "CondCore/DBOutputService/interface/PoolDBOutputService.h"
#include "CondFormats/DataRecord/interface/SiStripCondDataRecords.h"
#include "CondFormats/SiStripObjects/interface/SiStripBadStrip.h"
#include "CondFormats/SiStripObjects/interface/SiStripNoises.h"
#include "DataFormats/SiStripCommon/interface/SiStripConstants.h" /* for STRIPS_PER_APV*/
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/FileInPath.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/PluginManager/interface/ModuleDef.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/Exception.h"

class SiStripNoisesBoundaryChecker : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit SiStripNoisesBoundaryChecker(const edm::ParameterSet& iConfig);

  ~SiStripNoisesBoundaryChecker() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

  void analyze(const edm::Event&, const edm::EventSetup&) override;

private:
  const edm::FileInPath fp_;
  const int stripToTry_;
  const uint32_t printdebug_;
  const edm::ESGetToken<SiStripNoises, SiStripNoisesRcd> noiseToken_;

  const std::string k_Name_ = "SiStripNoisesBoundaryChecker";
  const std::string k_Record_ = "SiStripNoisesRcd";
};

SiStripNoisesBoundaryChecker::SiStripNoisesBoundaryChecker(const edm::ParameterSet& iConfig)
    : fp_(iConfig.getUntrackedParameter<edm::FileInPath>("file",
                                                         edm::FileInPath(SiStripDetInfoFileReader::kDefaultFile))),
      stripToTry_(iConfig.getUntrackedParameter<int32_t>("stripToTest", -1)),
      printdebug_(iConfig.getUntrackedParameter<uint32_t>("printDebug", std::numeric_limits<unsigned int>::max())),
      noiseToken_(esConsumes()) {}

void SiStripNoisesBoundaryChecker::analyze(const edm::Event& evt, const edm::EventSetup& iSetup) {
  unsigned int count{0};

  const auto& reader = SiStripDetInfoFileReader::read(fp_.fullPath());
  const auto& DetInfos = reader.getAllData();

  auto const& noise = iSetup.getData(noiseToken_);

  for (const auto& it : DetInfos) {
    const auto& nAPVs = it.second.nApvs;

    SiStripNoises::Range detNoiseRange = noise.getRange(it.first);

    const uint16_t stripToTry = stripToTry_ > 0 ? stripToTry_ : nAPVs * sistrip::STRIPS_PER_APV + 1;

    try {
      noise.verify(stripToTry, detNoiseRange);
      const auto& theNoise = noise.getNoise(stripToTry, detNoiseRange);
      if (count < printdebug_) {
        edm::LogPrint(k_Name_) << "WARNING: found "
                               << " detid: " << it.first << " strip: " << stripToTry << " noise:" << theNoise;
      }
      count++;
    } catch (cms::Exception& e) {
      LogDebug(k_Name) << "I have caught";
    }
  }  // loop on the detids
  edm::LogPrint(k_Name_) << "Found " << count << " modules with a valid Noise for strip = "
                         << ((stripToTry_ > 0) ? std::to_string(stripToTry_) : "(nAPVs*128)+1");
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void SiStripNoisesBoundaryChecker::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;

  desc.setComment(
      "Given a certain Global Tag, checks that the all the unmasked strips, do have a noise within the payload range");
  desc.addUntracked<edm::FileInPath>("file", edm::FileInPath(SiStripDetInfoFileReader::kDefaultFile));
  desc.addUntracked<int32_t>("stripToTest", -1);
  desc.addUntracked<uint32_t>("printDebug", std::numeric_limits<unsigned int>::max());
  descriptions.addWithDefaultLabel(desc);
}

DEFINE_FWK_MODULE(SiStripNoisesBoundaryChecker);
