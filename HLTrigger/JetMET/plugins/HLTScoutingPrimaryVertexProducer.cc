// -*- C++ -*-
//
// Package:    HLTrigger/JetMET
// Class:      HLTScoutingPrimaryVertexProducer
//
// Description: Producer for Run3ScoutingVertex or Phase2ScoutingVertex collections of primary vertices.
//              The family of output data formats is selected via the "scoutingFormat" parameter.
//
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/ParameterSet/interface/allowedValues.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/Scouting/interface/ScoutingFormatTraits.h"
#include "DataFormats/Math/interface/libminifloat.h"

#include <memory>
#include <string>
#include <utility>

class HLTScoutingPrimaryVertexProducer : public edm::global::EDProducer<> {
public:
  explicit HLTScoutingPrimaryVertexProducer(const edm::ParameterSet&);

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void produce(edm::StreamID sid, edm::Event& iEvent, edm::EventSetup const& setup) const final;

  // implementation templated on the family of scouting data formats
  template <typename Format>
  void produceImpl(edm::Event& iEvent) const;

  edm::EDGetTokenT<reco::VertexCollection> const vertexCollToken_;
  int const mantissaPrecision_;
  scouting::Format const format_;
};

HLTScoutingPrimaryVertexProducer::HLTScoutingPrimaryVertexProducer(const edm::ParameterSet& iConfig)
    : vertexCollToken_(consumes(iConfig.getParameter<edm::InputTag>("vertexCollection"))),
      mantissaPrecision_(iConfig.getParameter<int>("mantissaPrecision")),
      format_(scouting::formatFromString(iConfig.getParameter<std::string>(scouting::kFormatParameterName))) {
  switch (format_) {
    case scouting::Format::kRun3:
      produces<scouting::Run3Format::VertexCollection>("primaryVtx");
      break;
    case scouting::Format::kPhase2:
      produces<scouting::Phase2Format::VertexCollection>("primaryVtx");
      break;
  }
}

void HLTScoutingPrimaryVertexProducer::produce(edm::StreamID sid,
                                               edm::Event& iEvent,
                                               edm::EventSetup const& setup) const {
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
void HLTScoutingPrimaryVertexProducer::produceImpl(edm::Event& iEvent) const {
  auto outVertices = std::make_unique<typename Format::VertexCollection>();

  auto const vertexCollHandle = iEvent.getHandle(vertexCollToken_);

  if (vertexCollHandle.isValid()) {
    outVertices->reserve(vertexCollHandle->size());
    for (auto const& vtx : *vertexCollHandle) {
      outVertices->emplace_back(
          MiniFloatConverter::reduceMantissaToNbitsRounding(vtx.x(), mantissaPrecision_),
          MiniFloatConverter::reduceMantissaToNbitsRounding(vtx.y(), mantissaPrecision_),
          MiniFloatConverter::reduceMantissaToNbitsRounding(vtx.z(), mantissaPrecision_),
          MiniFloatConverter::reduceMantissaToNbitsRounding(vtx.zError(), mantissaPrecision_),
          MiniFloatConverter::reduceMantissaToNbitsRounding(vtx.xError(), mantissaPrecision_),
          MiniFloatConverter::reduceMantissaToNbitsRounding(vtx.yError(), mantissaPrecision_),
          vtx.tracksSize(),
          MiniFloatConverter::reduceMantissaToNbitsRounding(vtx.chi2(), mantissaPrecision_),
          vtx.ndof(),
          vtx.isValid(),
          MiniFloatConverter::reduceMantissaToNbitsRounding(vtx.covariance(0, 1), mantissaPrecision_),
          MiniFloatConverter::reduceMantissaToNbitsRounding(vtx.covariance(0, 2), mantissaPrecision_),
          MiniFloatConverter::reduceMantissaToNbitsRounding(vtx.covariance(1, 2), mantissaPrecision_));
    }
  }

  iEvent.put(std::move(outVertices), "primaryVtx");
}

void HLTScoutingPrimaryVertexProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<edm::InputTag>("vertexCollection", edm::InputTag("hltPixelVertices"))
      ->setComment("InputTag of input collection of primary vertices");
  desc.add<int>("mantissaPrecision", 10)->setComment("default float16, change to 23 for float32");
  desc.ifValue(edm::ParameterDescription<std::string>(scouting::kFormatParameterName, scouting::kRun3FormatName, true),
               edm::allowedValues<std::string>(scouting::kRun3FormatName, scouting::kPhase2FormatName))
      ->setComment("family of scouting data formats to produce (\"Run3\" or \"Phase2\")");
  descriptions.addWithDefaultLabel(desc);
}

DEFINE_FWK_MODULE(HLTScoutingPrimaryVertexProducer);
