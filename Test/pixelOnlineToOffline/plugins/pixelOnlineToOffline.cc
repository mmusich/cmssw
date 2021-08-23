// -*- C++ -*-
//
// Package:    Test/pixelOnlineToOffline
// Class:      pixelOnlineToOffline
//
/**\class pixelOnlineToOffline pixelOnlineToOffline.cc Test/pixelOnlineToOffline/plugins/pixelOnlineToOffline.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Marco Musich
//         Created:  Mon, 23 Aug 2021 09:22:05 GMT
//
//

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/TrackerCommon/interface/PixelBarrelName.h"
#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"
#include "Geometry/Records/interface/TrackerTopologyRcd.h"

//
// class declaration
//

class pixelOnlineToOffline : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit pixelOnlineToOffline(const edm::ParameterSet&);
  ~pixelOnlineToOffline();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void beginJob() override;
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override;

  // ----------member data ---------------------------
  
  // esconsumes
  const edm::ESGetToken<TrackerTopology, TrackerTopologyRcd> topoToken_;
  
  // module list
  std::vector<std::string> modulelist_;
};

//
// constructors and destructor
//
pixelOnlineToOffline::pixelOnlineToOffline(const edm::ParameterSet& iConfig):
  topoToken_(esConsumes<TrackerTopology, TrackerTopologyRcd>()),
  modulelist_(iConfig.getParameter<std::vector<std::string>>("modulelist"))
{}

pixelOnlineToOffline::~pixelOnlineToOffline() {}

//
// member functions
//

// ------------ method called for each event  ------------
void pixelOnlineToOffline::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;
  
  const TrackerTopology* const tTopo = &iSetup.getData(topoToken_);
  if (!modulelist_.empty()) {
    for (auto const& mod : modulelist_) {
      PixelBarrelName bn(mod, true); // true is for phase-1
      const auto& detId=bn.getDetId(tTopo);

      edm::LogPrint("pixelOnlineToOffline") << "module name: " << mod << " detId:" << detId.rawId() << std::endl;

    }
  }
}

// ------------ method called once each job just before starting event loop  ------------
void pixelOnlineToOffline::beginJob() {
  // please remove this method if not needed
}

// ------------ method called once each job just after ending the event loop  ------------
void pixelOnlineToOffline::endJob() {
  // please remove this method if not needed
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void pixelOnlineToOffline::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.add<std::vector<std::string>>("modulelist",{"BPix_BmO_SEC3_LYR2_LDR5F_MOD2", "BPix_BpO_SEC1_LYR2_LDR1F_MOD1"});
  descriptions.addWithDefaultLabel(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(pixelOnlineToOffline);
