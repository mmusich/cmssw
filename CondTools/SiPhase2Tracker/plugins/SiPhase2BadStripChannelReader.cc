// user include files
#include "CondFormats/DataRecord/interface/SiPhase2OuterTrackerCondDataRecords.h"
#include "CondFormats/SiStripObjects/interface/SiStripBadStrip.h"
#include "DataFormats/Phase2TrackerDigi/interface/Phase2TrackerDigi.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/global/EDAnalyzer.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

//
//
// class decleration
//
class SiPhase2BadStripChannelReader : public edm::global::EDAnalyzer<> {
public:
  explicit SiPhase2BadStripChannelReader(const edm::ParameterSet&);
  ~SiPhase2BadStripChannelReader() override = default;
  void analyze(edm::StreamID, edm::Event const&, edm::EventSetup const&) const override;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  const bool printdebug_;
  const std::string label_;
  const edm::ESGetToken<SiStripBadStrip, SiPhase2OuterTrackerBadStripRcd> badStripToken_;
};

SiPhase2BadStripChannelReader::SiPhase2BadStripChannelReader(const edm::ParameterSet& iConfig)
    : printdebug_(iConfig.getUntrackedParameter<bool>("printDebug", false)),
      label_(iConfig.getUntrackedParameter<std::string>("label", "")),
      badStripToken_(esConsumes(edm::ESInputTag{"", label_})) {}

void SiPhase2BadStripChannelReader::analyze(edm::StreamID,
                                            edm::Event const& iEvent,
                                            edm::EventSetup const& iSetup) const {
  const auto& payload = &iSetup.getData(badStripToken_);

  edm::LogInfo("SiPhase2BadStripChannelReader")
      << "[SiPhase2BadStripChannelReader::analyze] End Reading SiStriBadStrip with label " << label_ << std::endl;

  const TrackerTopology* ttopo = nullptr;

  std::stringstream ss;
  if (printdebug_) {
    payload->printDebug(ss, ttopo);
  }

  std::vector<uint32_t> detIds;
  payload->getDetIds(detIds);

  for (const auto& d : detIds) {
    SiStripBadStrip::Range range = payload->getRange(d);
    for (std::vector<unsigned int>::const_iterator badChannel = range.first; badChannel != range.second; ++badChannel) {
      const auto& firstStrip = payload->decodePhase2(*badChannel).firstStrip;
      const auto& range = payload->decodePhase2(*badChannel).range;

      if (printdebug_) {
        ss << "DetId=" << d << " Channel=" << payload->decodePhase2(*badChannel).firstStrip << ":"
           << payload->decodePhase2(*badChannel).range << std::endl;
      }

      for (unsigned int index = 0; index < range; index++) {
        std::pair<int, int> badStrip = Phase2TrackerDigi::channelToPixel(firstStrip + index);
        ss << "DetId =" << d << " Channel = " << firstStrip + index << " -> strip (row,col)=(" << badStrip.first << ","
           << badStrip.second << ")" << std::endl;
      }
    }
  }

  std::cout << ss.str() << std::endl;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void SiPhase2BadStripChannelReader::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.setComment("Module to read SiStripBadStrip Payloads");
  desc.addUntracked<bool>("printDebug", false)->setComment("do debug level print-outs");
  desc.addUntracked<std::string>("label", "")->setComment("label from which to read the payload");
  descriptions.addWithDefaultLabel(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SiPhase2BadStripChannelReader);
