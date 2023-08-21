// system includes
#include <iostream>
#include <fstream>
#include <map>

// user includes
#include "CondFormats/DataRecord/interface/SiPixelFedCablingMapRcd.h"
#include "CondFormats/SiPixelObjects/interface/PixelFEDLink.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFedCablingMap.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFedCablingTree.h"
#include "DataFormats/SiPixelDetId/interface/PXBDetId.h"
#include "DataFormats/SiPixelDetId/interface/PXFDetId.h"
#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/ESTransientHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"

//
// class declaration
//
class SiPixelPhase1CablingAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit SiPixelPhase1CablingAnalyzer(const edm::ParameterSet&);
  ~SiPixelPhase1CablingAnalyzer() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;

  // ----------member data ---------------------------
  const edm::ESGetToken<SiPixelFedCablingMap, SiPixelFedCablingMapRcd> mapToken_;
  const edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> geomToken_;
};

using namespace std;

SiPixelPhase1CablingAnalyzer::SiPixelPhase1CablingAnalyzer(const edm::ParameterSet& iConfig)
    : mapToken_{esConsumes()}, geomToken_{esConsumes()} {
  //now do what ever initialization is needed
  // usesResource("TFileService");
}

void SiPixelPhase1CablingAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;

  const TrackerGeometry* theTrackerGeometry = &iSetup.getData(geomToken_);
  const SiPixelFedCablingMap* pixelFEDCablingMap = &iSetup.getData(mapToken_);

  // cout << pixelFEDCablingMap->version();
  // edm::ESHandle<TrackerTopology> trackerTopologyHandle;
  // iSetup.get<TrackerTopologyRcd>().get(trackerTopologyHandle);
  // const TrackerTopology* tt = trackerTopologyHandle.operator->();

  auto pxb = theTrackerGeometry->detsPXB();

  auto cablingTree = pixelFEDCablingMap->cablingTree();

  // for (auto &i: pxb)
  // {
  // const GeomDet *det = i;
  // PXBDetId id = det->geographicalId();
  // unsigned rawid = id.rawId();

  // auto pixelFEDCab = cablingTree->fed(rawid);

  // // pixelFEDCab->print();
  // }

  std::vector<const SiPixelFedCablingTree::PixelFEDCabling*> fedCabling = cablingTree->fedList();
  // cout << "FED list size: " << fedCabling.size() << endl;

  std::map<unsigned, std::vector<unsigned> > dataDic;

  for (auto& fed : fedCabling)  // through all feds
  {
    // cout << "FED id: " << fed->id() << endl;

    unsigned i = 1;
    const sipixelobjects::PixelFEDLink* link = nullptr;
    while ((link = fed->link(i))) {
      // cout << "\tLNK id: " << link->id() << endl;

      if (link->numberOfROCs()) {
        unsigned rawId = link->roc(1)->rawId();
        // cout << "\t\tRAWID: " << rawId << endl;

        auto& dataRef = dataDic[rawId];

        if (dataRef.size() == 0) {
          dataRef.push_back(fed->id());
        }
        dataRef.push_back(link->id());
      }

      ++i;
    }
  }
  // ofstream file("dbCablData.dat");
  for (auto& elem : dataDic) {
    unsigned fed = elem.second[0];
    cout << elem.first << " " << fed << " ";
    for (unsigned i = 1; i < elem.second.size(); ++i) {
      cout << elem.second[i] << "/";
    }
    cout << endl;
  }
  // file.close();
  // cout << cablingTree->print(34) << endl;

  // # MIN FED NUMBER: phase0 = 0 (FEDNumbering::MINSiPixelFEDID), phase1 = 1200 (FEDNumbering::MINSiPixeluTCAFEDID)
}

void SiPixelPhase1CablingAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SiPixelPhase1CablingAnalyzer);
