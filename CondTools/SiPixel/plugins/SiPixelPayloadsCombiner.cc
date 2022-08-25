// -*- C++ -*-
//
// Package:    SiPixelPayloadsCombiner/SiPixelPayloadsCombiner
// Class:      SiPixelPayloadsCombiner
//
/**\class SiPixelPayloadsCombiner SiPixelPayloadsCombiner.cc SiPixelPayloadsCombiner/SiPixelPayloadsCombiner/plugins/SiPixelPayloadsCombiner.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Marco Musich
//         Created:  Wed, 24 Aug 2022 11:20:42 GMT
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
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "CondTools/SiPixel/interface/SiPixelCondDataContainer.h"

//
// class declaration
//

class SiPixelPayloadsCombiner : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit SiPixelPayloadsCombiner(const edm::ParameterSet&);
  ~SiPixelPayloadsCombiner() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void beginJob() override;
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override;

  // ----------member data ---------------------------
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
SiPixelPayloadsCombiner::SiPixelPayloadsCombiner(const edm::ParameterSet& iConfig) {}

//
// member functions
//

// ------------ method called for each event  ------------
void SiPixelPayloadsCombiner::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) { using namespace edm; }

// ------------ method called once each job just before starting event loop  ------------
void SiPixelPayloadsCombiner::beginJob() {
  // please remove this method if not needed
}

// ------------ method called once each job just after ending the event loop  ------------
void SiPixelPayloadsCombiner::endJob() {
  // please remove this method if not needed
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void SiPixelPayloadsCombiner::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
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
DEFINE_FWK_MODULE(SiPixelPayloadsCombiner);
