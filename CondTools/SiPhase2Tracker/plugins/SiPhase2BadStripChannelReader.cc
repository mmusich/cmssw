// user include files
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "CondFormats/SiStripObjects/interface/SiStripBadStrip.h"
#include "CondFormats/DataRecord/interface/SiStripBadStripRcd.h"

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
  const uint32_t printdebug_;
  const std::string label_;
  const edm::ESGetToken<SiStripBadStrip, SiStripBadStripRcd> badStripToken_;
};

SiPhase2BadStripChannelReader::SiPhase2BadStripChannelReader(const edm::ParameterSet& iConfig)
    : printdebug_(iConfig.getUntrackedParameter<uint32_t>("printDebug", 5)),
      label_(iConfig.getUntrackedParameter<std::string>("label", "")),
      badStripToken_(esConsumes(edm::ESInputTag{"", label_})) {}

void SiPhase2BadStripChannelReader::analyze(edm::StreamID,
                                                     edm::Event const& iEvent,
                                                     edm::EventSetup const& iSetup) const {
  const auto& badStrip = iSetup.getData(badStripToken_);
  edm::LogInfo("SiPhase2BadStripChannelReader")
      << "[SiPhase2BadStripChannelReader::analyze] End Reading SiStriBadStrip with label "
      << label_ << std::endl;

  const TrackerTopology* ttopo = nullptr;

  std::stringstream ss;
  badStrip.printDebug(ss,ttopo);
  std:: cout <<  ss.str() << std::endl;

  // const auto& detid_la = lorentzAngles.getLorentzAngles();
  // std::unordered_map<unsigned int, float>::const_iterator it;
  // size_t count = 0;
  // for (it = detid_la.begin(); it != detid_la.end() && count < printdebug_; it++) {
  //   edm::LogInfo("SiPhase2BadStripChannelReader") << "detid " << it->first << " \t"
  //                                                          << " Lorentz angle  " << it->second;
  //   count++;
  // }
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void SiPhase2BadStripChannelReader::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.setComment("Module to read SiStripBadStrip Payloads");
  desc.addUntracked<uint32_t>("printDebug", 5)->setComment("maximum amount of print-outs");
  desc.addUntracked<std::string>("label", "")->setComment("label from which to read the payload");
  descriptions.addWithDefaultLabel(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SiPhase2BadStripChannelReader);
