// -*- C++ -*-
//
// Package:    HLTrigger/JetMET
// Class:      HLTScoutingCaloProducer
//
/**\class HLTScoutingCaloProducer HLTScoutingCaloProducer.cc HLTrigger/JetMET/plugins/HLTScoutingCaloProducer.cc

Description: Producer for Run3ScoutingCaloJets or Phase2ScoutingCaloJets from reco::CaloJet objects.
             The family of output data formats is selected via the "scoutingFormat" parameter.

*/
//
// Original Author:  Dustin James Anderson
//         Created:  Fri, 12 Jun 2015 15:49:20 GMT
//
//

// system include files
#include <memory>
#include <string>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/allowedValues.h"

#include "DataFormats/JetReco/interface/CaloJet.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/METReco/interface/CaloMETCollection.h"
#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/BTauReco/interface/JetTag.h"

#include "DataFormats/Scouting/interface/ScoutingFormatTraits.h"

#include "DataFormats/Math/interface/deltaR.h"

class HLTScoutingCaloProducer : public edm::global::EDProducer<> {
public:
  explicit HLTScoutingCaloProducer(const edm::ParameterSet&);
  ~HLTScoutingCaloProducer() override;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void produce(edm::StreamID sid, edm::Event& iEvent, edm::EventSetup const& setup) const final;

  // implementation templated on the family of scouting data formats
  template <typename Format>
  void produceImpl(edm::Event& iEvent) const;

  const edm::EDGetTokenT<reco::CaloJetCollection> caloJetCollection_;
  const edm::EDGetTokenT<reco::JetTagCollection> caloJetBTagCollection_;
  const edm::EDGetTokenT<reco::JetTagCollection> caloJetIDTagCollection_;
  const edm::EDGetTokenT<reco::VertexCollection> vertexCollection_;
  const edm::EDGetTokenT<reco::CaloMETCollection> metCollection_;
  const edm::EDGetTokenT<double> rho_;

  const double caloJetPtCut;
  const double caloJetEtaCut;

  const bool doMet;
  const bool doJetBTags;
  const bool doJetIDTags;

  const scouting::Format format_;
};

//
// constructors and destructor
//
HLTScoutingCaloProducer::HLTScoutingCaloProducer(const edm::ParameterSet& iConfig)
    : caloJetCollection_(consumes<reco::CaloJetCollection>(iConfig.getParameter<edm::InputTag>("caloJetCollection"))),
      caloJetBTagCollection_(
          consumes<reco::JetTagCollection>(iConfig.getParameter<edm::InputTag>("caloJetBTagCollection"))),
      caloJetIDTagCollection_(
          consumes<reco::JetTagCollection>(iConfig.getParameter<edm::InputTag>("caloJetIDTagCollection"))),
      vertexCollection_(consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("vertexCollection"))),
      metCollection_(consumes<reco::CaloMETCollection>(iConfig.getParameter<edm::InputTag>("metCollection"))),
      rho_(consumes<double>(iConfig.getParameter<edm::InputTag>("rho"))),
      caloJetPtCut(iConfig.getParameter<double>("caloJetPtCut")),
      caloJetEtaCut(iConfig.getParameter<double>("caloJetEtaCut")),
      doMet(iConfig.getParameter<bool>("doMet")),
      doJetBTags(iConfig.getParameter<bool>("doJetBTags")),
      doJetIDTags(iConfig.getParameter<bool>("doJetIDTags")),
      format_(scouting::formatFromString(iConfig.getParameter<std::string>(scouting::kFormatParameterName))) {
  //register products
  switch (format_) {
    case scouting::Format::kRun3:
      produces<scouting::Run3Format::CaloJetCollection>();
      break;
    case scouting::Format::kPhase2:
      produces<scouting::Phase2Format::CaloJetCollection>();
      break;
  }
  produces<double>("rho");
  produces<double>("caloMetPt");
  produces<double>("caloMetPhi");
}

HLTScoutingCaloProducer::~HLTScoutingCaloProducer() = default;

// ------------ method called to produce the data  ------------
void HLTScoutingCaloProducer::produce(edm::StreamID sid, edm::Event& iEvent, edm::EventSetup const& setup) const {
  switch (format_) {
    case scouting::Format::kRun3:
      produceImpl<scouting::Run3Format>(iEvent);
      break;
    case scouting::Format::kPhase2:
      produceImpl<scouting::Phase2Format>(iEvent);
      break;
  }
}

template <typename Format>
void HLTScoutingCaloProducer::produceImpl(edm::Event& iEvent) const {
  using namespace edm;

  //get calo jets
  Handle<reco::CaloJetCollection> caloJetCollection;
  auto outCaloJets = std::make_unique<typename Format::CaloJetCollection>();
  if (iEvent.getByToken(caloJetCollection_, caloJetCollection)) {
    //get jet tags
    Handle<reco::JetTagCollection> caloJetBTagCollection;
    bool haveJetBTags = false;
    if (doJetBTags && iEvent.getByToken(caloJetBTagCollection_, caloJetBTagCollection)) {
      haveJetBTags = true;
    }
    Handle<reco::JetTagCollection> caloJetIDTagCollection;
    bool haveJetIDTags = false;
    if (doJetIDTags && iEvent.getByToken(caloJetIDTagCollection_, caloJetIDTagCollection)) {
      haveJetIDTags = true;
    }

    for (auto& jet : *caloJetCollection) {
      if (jet.pt() > caloJetPtCut && fabs(jet.eta()) < caloJetEtaCut) {
        //find the jet tag(s) corresponding to the jet
        float bTagValue = -20;
        float bTagMinDR2 = 0.01;
        if (haveJetBTags) {
          for (auto& tag : *caloJetBTagCollection) {
            float dR2 = reco::deltaR2(jet, *(tag.first));
            if (dR2 < bTagMinDR2) {
              bTagMinDR2 = dR2;
              bTagValue = tag.second;
            }
          }
        }
        float idTagValue = -20;
        float idTagMinDR2 = 0.01;
        if (haveJetIDTags) {
          for (auto& tag : *caloJetIDTagCollection) {
            float dR2 = reco::deltaR2(jet, *(tag.first));
            if (dR2 < idTagMinDR2) {
              idTagMinDR2 = dR2;
              idTagValue = tag.second;
            }
          }
        }
        outCaloJets->emplace_back(jet.pt(),
                                  jet.eta(),
                                  jet.phi(),
                                  jet.mass(),
                                  jet.jetArea(),
                                  jet.maxEInEmTowers(),
                                  jet.maxEInHadTowers(),
                                  jet.hadEnergyInHB(),
                                  jet.hadEnergyInHE(),
                                  jet.hadEnergyInHF(),
                                  jet.emEnergyInEB(),
                                  jet.emEnergyInEE(),
                                  jet.emEnergyInHF(),
                                  jet.towersArea(),
                                  idTagValue,
                                  bTagValue);
      }
    }
  }

  //get rho
  Handle<double> rho;
  std::unique_ptr<double> outRho(new double(-999));
  if (iEvent.getByToken(rho_, rho)) {
    outRho = std::make_unique<double>(*rho);
  }

  //get MET
  Handle<reco::CaloMETCollection> metCollection;
  std::unique_ptr<double> outMetPt(new double(-999));
  std::unique_ptr<double> outMetPhi(new double(-999));
  if (doMet && iEvent.getByToken(metCollection_, metCollection)) {
    outMetPt = std::make_unique<double>(metCollection->front().pt());
    outMetPhi = std::make_unique<double>(metCollection->front().phi());
  }

  //put output
  iEvent.put(std::move(outCaloJets));
  //    iEvent.put(std::move(outVertices));
  iEvent.put(std::move(outRho), "rho");
  iEvent.put(std::move(outMetPt), "caloMetPt");
  iEvent.put(std::move(outMetPhi), "caloMetPhi");
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void HLTScoutingCaloProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<edm::InputTag>("caloJetCollection", edm::InputTag("hltAK4CaloJets"));
  desc.add<edm::InputTag>("caloJetBTagCollection", edm::InputTag("hltCombinedSecondaryVertexBJetTagsCalo"));
  desc.add<edm::InputTag>("caloJetIDTagCollection", edm::InputTag("hltCaloJetFromPV"));
  desc.add<edm::InputTag>("vertexCollection", edm::InputTag("hltPixelVertices"));
  desc.add<edm::InputTag>("metCollection", edm::InputTag("hltMet"));
  desc.add<edm::InputTag>("rho", edm::InputTag("hltFixedGridRhoFastjetAllCalo"));
  desc.add<double>("caloJetPtCut", 20.0);
  desc.add<double>("caloJetEtaCut", 3.0);
  desc.add<bool>("doMet", true);
  desc.add<bool>("doJetBTags", false);
  desc.add<bool>("doJetIDTags", false);
  desc.ifValue(edm::ParameterDescription<std::string>(scouting::kFormatParameterName, scouting::kRun3FormatName, true),
               edm::allowedValues<std::string>(scouting::kRun3FormatName, scouting::kPhase2FormatName))
      ->setComment("family of scouting data formats to produce (\"Run3\" or \"Phase2\")");
  descriptions.add("hltScoutingCaloProducer", desc);
}

// declare this class as a framework plugin
DEFINE_FWK_MODULE(HLTScoutingCaloProducer);
