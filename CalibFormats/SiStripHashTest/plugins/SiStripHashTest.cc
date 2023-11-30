// -*- C++ -*-
//
// Package:    CalibFormats/SiStripHashTest
// Class:      SiStripHashTest
//
/**\class SiStripHashTest SiStripHashTest.cc CalibFormats/SiStripHashTest/plugins/SiStripHashTest.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Marco Musich
//         Created:  Thu, 30 Nov 2023 15:22:27 GMT
//
//

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "CalibFormats/SiStripObjects/interface/SiStripHashedDetId.h"
#include "CalibTracker/Records/interface/SiStripDependentRecords.h"
#include "CalibTracker/SiStripCommon/interface/ShallowTools.h"
#include "DataFormats/SiStripDetId/interface/SiStripDetId.h"
#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/TrackerGeometryBuilder/interface/StripGeomDetUnit.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"

//
// class declaration
//
class SiStripHashTest : public edm::one::EDAnalyzer<edm::one::WatchRuns> {
public:
  explicit SiStripHashTest(const edm::ParameterSet&);
  ~SiStripHashTest() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void beginRun(edm::Run const& iRun, edm::EventSetup const&) override;
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endRun(edm::Run const& iRun, edm::EventSetup const&) override {}
 
  // ----------member data ---------------------------
  const edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> m_tkGeomTokenBR;
  SiStripHashedDetId m_hash;
};

//
// constructors and destructor
//
SiStripHashTest::SiStripHashTest(const edm::ParameterSet& iConfig)
  : m_tkGeomTokenBR{esConsumes<edm::Transition::BeginRun>()}{}

//
// member functions
//

// ------------ method called for run transition  ------------
void SiStripHashTest::beginRun(edm::Run const& iRun, edm::EventSetup const& iSetup) {
const auto& tkGeom = iSetup.getData(m_tkGeomTokenBR);

 std::vector<uint32_t> c_rawid;

 auto dets = tkGeom.detsTIB();
 //dets.insert(dets.end(), tkGeom.detsTID().begin(), tkGeom.detsTID().end()); // no LA in endcaps
 dets.insert(dets.end(), tkGeom.detsTOB().begin(), tkGeom.detsTOB().end());
 //dets.insert(dets.end(), tkGeom.detsTEC().begin(), tkGeom.detsTEC().end()); // no LA in endcaps
 
 for (auto det : dets) {
   auto detid = det->geographicalId().rawId();
   const StripGeomDetUnit* stripDet = dynamic_cast<const StripGeomDetUnit*>(tkGeom.idToDet(det->geographicalId()));
   if (stripDet) {
     c_rawid.push_back(detid);
   }
 }
 
 /*
 std::vector<uint32_t> c_rawid = {369120278,
				  369120277,
				  369120282,
				  369120281,
				  369120286,
				  369120285,
				  369120294,
				  369120293,
				  369120298};
 */

 // Sorted DetId list gives max performance, anything else is worse
 std::sort(c_rawid.begin(), c_rawid.end());
 
 // initialize the hash map
 m_hash = SiStripHashedDetId{c_rawid};

 std::cout << c_rawid.size() << std::endl;

 SiStripHashedDetId::const_iterator iter = m_hash.begin();
 for (; iter != m_hash.end(); ++iter) {
   std::cout << "detId: " << (*iter) << " hashed index: " << m_hash.hashedIndex((*iter)) << std::endl;
 }
}

// ------------ method called for each event  ------------
void SiStripHashTest::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void SiStripHashTest::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);

  //Specify that only 'tracks' is allowed
  //To use, remove the default given above and uncomment below
  //edm::ParameterSetDescription desc;
  //desc.addUntracked<edm::InputTag>("tracks", edm::InputTag("ctfWithMaterialTracks"));
  //descriptions.addWithDefaultLabel(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SiStripHashTest);
