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
#include "DQM/TrackerRemapper/interface/Phase1PixelMaps.h"
#include "DQM/TrackerRemapper/interface/Phase1PixelSummaryMap.h"
#include "DQM/TrackerRemapper/interface/Phase1PixelROCMaps.h"

//
// class declaration
//

class pixelOnlineToOffline : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit pixelOnlineToOffline(const edm::ParameterSet&);
  ~pixelOnlineToOffline() override;

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
  std::unique_ptr<Phase1PixelMaps> pixelmap;
  std::unique_ptr<Phase1PixelSummaryMap> summarymap;
};

//
// constructors and destructor
//
pixelOnlineToOffline::pixelOnlineToOffline(const edm::ParameterSet& iConfig)
    : topoToken_(esConsumes<TrackerTopology, TrackerTopologyRcd>()),
      modulelist_(iConfig.getParameter<std::vector<std::string>>("modulelist")) {
  pixelmap = std::make_unique<Phase1PixelMaps>("COLZ0 L");
  summarymap = std::make_unique<Phase1PixelSummaryMap>("COLZ0 L", "New Modules", "new modules");
}

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
      PixelBarrelName bn(mod, true);  // true is for phase-1
      const auto& detId = bn.getDetId(tTopo);
      pixelmap->fill("NewModules", detId.rawId(), 1.);
      summarymap->fillTrackerMap(detId.rawId(), 1.);
      edm::LogPrint("pixelOnlineToOffline") << "module name: " << mod << " detId:" << detId.rawId() << std::endl;
    }
  }
}

// ------------ method called once each job just before starting event loop  ------------
void pixelOnlineToOffline::beginJob() {
  pixelmap->book("NewModules", "New Modules", "New Modules");
  summarymap->createTrackerBaseMap();
}

// ------------ method called once each job just after ending the event loop  ------------
void pixelOnlineToOffline::endJob() {
  gStyle->SetPalette(1);
  pixelmap->beautifyAllHistograms();

  TCanvas cBPix("CanvBarrel", "CanvBarrel", 1200, 1000);
  pixelmap->drawBarrelMaps("NewModules", cBPix);
  cBPix.SaveAs("NewModules_Barrel.png");

  TCanvas cFPix("CanvForward", "CanvForward", 1200, 800);
  pixelmap->drawForwardMaps("NewModules", cFPix);
  cFPix.SaveAs("NewModules_Forward.png");

  TCanvas cAll("CanvAll", "CanvAll", 1200, 800);
  pixelmap->drawSummaryMaps("NewModules", cAll);
  cAll.SaveAs("NewModules_All.png");

  TCanvas cSummary("CanvSummary", "CanvSummary", 1200, 800);
  summarymap->printTrackerMap(cSummary);
  cSummary.SaveAs("NewModules_Summary.png");
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void pixelOnlineToOffline::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<std::vector<std::string>>("modulelist", {"BPix_BmO_SEC3_LYR2_LDR5F_MOD2", "BPix_BpO_SEC1_LYR2_LDR1F_MOD1"});
  descriptions.addWithDefaultLabel(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(pixelOnlineToOffline);
