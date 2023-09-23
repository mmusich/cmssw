// -*- C++ -*-
//
// Package:    DPGAnalysis/PixelClusterCounter
// Class:      PixelClusterCounter
//
/**\class PixelClusterCounter PixelClusterCounter.cc DPGAnalysis/PixelClusterCounter/plugins/PixelClusterCounter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Marco Musich
//         Created:  Fri, 22 Sep 2023 15:11:39 GMT
//
//

// system include files
#include <memory>
#include <iostream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/SiPixelCluster/interface/SiPixelCluster.h"

//
// class declaration
//



class PixelClusterCounter : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit PixelClusterCounter(const edm::ParameterSet&);
  ~PixelClusterCounter() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void analyze(const edm::Event&, const edm::EventSetup&) override;

  // ----------member data ---------------------------
  edm::EDGetTokenT<SiPixelClusterCollectionNew> pixelClusterToken_;  //used to select what tracks to read from configuration file

};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
PixelClusterCounter::PixelClusterCounter(const edm::ParameterSet& iConfig)
  : pixelClusterToken_(consumes<SiPixelClusterCollectionNew>(iConfig.getUntrackedParameter<edm::InputTag>("pixelClusters"))) {
}


//
// member functions
//

// ------------ method called for each event  ------------
void PixelClusterCounter::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;

  unsigned int totalDets = 0;
  unsigned int totalDetSetCounts = 0;
  for (const auto& detSet : iEvent.get(pixelClusterToken_)) {
    totalDets++;
    for (const auto& det : detSet) {
      totalDetSetCounts += det.size();
    }
  }
  std::cout << "totalDets: " << totalDets << " totalDetSetCounts: " << totalDetSetCounts << std::endl;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void PixelClusterCounter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.addUntracked<edm::InputTag>("pixelClusters",edm::InputTag("siPixelClusters"));
  descriptions.addWithDefaultLabel(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PixelClusterCounter);
