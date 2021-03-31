// -*- C++ -*-
//
// Package:    Geometry/TrackerTopologyCollector
// Class:      TrackerTopologyCollector
//
/**\class TrackerTopologyCollector TrackerTopologyCollector.cc Geometry/TrackerTopologyCollector/plugins/TrackerTopologyCollector.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Marco Musich
//         Created:  Wed, 31 Mar 2021 11:01:16 GMT
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

#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"
#include "Geometry/Records/interface/TrackerTopologyRcd.h"
#include "Geometry/CommonDetUnit/interface/PixelGeomDetUnit.h"

//
// Ancillary struct
//

struct barrelTopologyMap {
  std::map<unsigned, std::pair<unsigned, unsigned>> myMap_;
public:
  void print(){
    for(const auto element: myMap_){
      std::cout << "layer:" << element.first << " has: " << element.second.first << " ladders and "<< element.second.second << " modules" << std::endl;
    }
  }
};

//
// class declaration
//

class TrackerTopologyCollector : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit TrackerTopologyCollector(const edm::ParameterSet&);
  ~TrackerTopologyCollector() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void beginJob() override;
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override;

  // ----------member data ---------------------------
  const edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> geomEsToken_;
  const edm::ESGetToken<TrackerTopology, TrackerTopologyRcd> topoToken_;

  barrelTopologyMap myTopoMap;
};


//
// constructors and destructor
//
TrackerTopologyCollector::TrackerTopologyCollector(const edm::ParameterSet& iConfig)
  : geomEsToken_(esConsumes()),
    topoToken_(esConsumes()){}

//
// member functions
//

// ------------ method called for each event  ------------
void TrackerTopologyCollector::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;

  // get the Tracker geometry from event setup
  const TrackerGeometry* trackerGeometry_ = &iSetup.getData(geomEsToken_);
  const TrackerTopology* tTopo_ = &iSetup.getData(topoToken_);

  const auto& nlay = trackerGeometry_->numberOfLayers(1);
  std::vector<unsigned> maxLadder, maxModule;
  maxLadder.resize(nlay);
  maxModule.resize(nlay);
  for(unsigned int i =0; i < nlay; i++){
    maxLadder.push_back(0);
    maxModule.push_back(0);
  }

  for (auto det : trackerGeometry_->detsPXB()) {
    const PixelGeomDetUnit* pixelDet = dynamic_cast<const PixelGeomDetUnit*>(det);
    const auto layer = tTopo_->pxbLayer(pixelDet->geographicalId());
    const auto ladder = tTopo_->pxbLadder(pixelDet->geographicalId());
    const auto module = tTopo_->pxbModule(pixelDet->geographicalId());
    if(ladder > maxLadder[layer]){
      maxLadder[layer] = ladder;
    }
    if(module > maxModule[layer]){
      maxModule[layer] = module;
    }
  }

  for(unsigned int i=1; i<= nlay; i++){
    myTopoMap.myMap_[i] = std::make_pair(maxLadder[i],maxModule[i]);
  }

  myTopoMap.print();
}

// ------------ method called once each job just before starting event loop  ------------
void TrackerTopologyCollector::beginJob() {
  // please remove this method if not needed
}

// ------------ method called once each job just after ending the event loop  ------------
void TrackerTopologyCollector::endJob() {
  // please remove this method if not needed
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void TrackerTopologyCollector::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);

  //Specify that only 'tracks' is allowed
  //To use, remove the default given above and uncomment below
  //ParameterSetDescription desc;
  //desc.addUntracked<edm::InputTag>("tracks","ctfWithMaterialTracks");
  //descriptions.addWithDefaultLabel(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TrackerTopologyCollector);
