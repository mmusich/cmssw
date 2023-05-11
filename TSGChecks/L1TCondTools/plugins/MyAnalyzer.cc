#include "CondFormats/DataRecord/interface/L1TUtmTriggerMenuRcd.h"
#include "CondFormats/L1TObjects/interface/L1TUtmTriggerMenu.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include <iostream>

class MyAnalyzer : public edm::one::EDAnalyzer<> {
public:
  explicit MyAnalyzer(const edm::ParameterSet&);
  ~MyAnalyzer() = default;
private:
  virtual void analyze(const edm::Event&, const edm::EventSetup&);

  const edm::ESGetToken<L1TUtmTriggerMenu, L1TUtmTriggerMenuRcd> m_l1GtMenuToken;
  long unsigned int cachedMenuHash{0};
};

MyAnalyzer::MyAnalyzer(const edm::ParameterSet&):
  m_l1GtMenuToken(esConsumes<L1TUtmTriggerMenu, L1TUtmTriggerMenuRcd>()){}

void MyAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  
  edm::ESHandle<L1TUtmTriggerMenu> l1GtMenu = iSetup.getHandle(m_l1GtMenuToken);
  const L1TUtmTriggerMenu* utml1GtMenu = l1GtMenu.product();

  if(cachedMenuHash!=utml1GtMenu->getFirmwareUuidHashed()){
    std::cout << "Run number: " << iEvent.id().run()  << " Firmware UUID hashed: " << utml1GtMenu->getFirmwareUuidHashed() << " int-converted: " << static_cast<int>(utml1GtMenu->getFirmwareUuidHashed()) << std::endl;
    cachedMenuHash = utml1GtMenu->getFirmwareUuidHashed();
  }
}

DEFINE_FWK_MODULE(MyAnalyzer);
