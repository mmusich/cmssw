// -*- C++ -*-
//
// Module:    CopyAndMoveFED1024
// Class:     CopyAndMoveFED1024
//
// Description: Copies FED 1024 data to FED 1050 and deletes data in FED 1024 in the output FEDRawDataCollection.
//
// Original Author:  Marco Musich (CERN)
//         Created:  26.10.2025 
//
//

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "DataFormats/FEDRawData/interface/FEDRawDataCollection.h"
#include "DataFormats/FEDRawData/interface/FEDRawData.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/FEDRawData/interface/FEDNumbering.h"

class CopyAndMoveFED1024 : public edm::stream::EDProducer<> {
public:
  explicit CopyAndMoveFED1024(const edm::ParameterSet&);
  ~CopyAndMoveFED1024() override {}

  void produce(edm::Event&, const edm::EventSetup&) override;

private:
  edm::EDGetTokenT<FEDRawDataCollection> inputToken_;
};

CopyAndMoveFED1024::CopyAndMoveFED1024(const edm::ParameterSet& iConfig)
    : inputToken_(consumes<FEDRawDataCollection>(iConfig.getParameter<edm::InputTag>("src"))) {
  produces<FEDRawDataCollection>();
}

void CopyAndMoveFED1024::produce(edm::Event& iEvent, const edm::EventSetup&) {
  edm::Handle<FEDRawDataCollection> input;
  iEvent.getByToken(inputToken_, input);

  // Prepare output collection
  std::unique_ptr<FEDRawDataCollection> output(new FEDRawDataCollection());

  // Copy everything as is, except 1024 and 1050
  for (int fedId = 0; fedId <= FEDNumbering::MAXFEDID; ++fedId) {
    if (fedId == 1024 || fedId == 1050) continue;
    const FEDRawData& inData = input->FEDData(fedId);
    if (inData.size() > 0) {
      FEDRawData& outData = output->FEDData(fedId);
      outData.resize(inData.size());
      std::copy(inData.data(), inData.data() + inData.size(), outData.data());
    }
  }

  // Move content from 1024 to 1050 if available
  const FEDRawData& fed1024 = input->FEDData(1024);
  if (fed1024.size() > 0) {
    FEDRawData& fed1050 = output->FEDData(1050);
    fed1050.resize(fed1024.size());
    std::copy(fed1024.data(), fed1024.data() + fed1024.size(), fed1050.data());
  }

  // Zero FED 1024 (no data)
  output->FEDData(1024).resize(0);

  iEvent.put(std::move(output));
}

DEFINE_FWK_MODULE(CopyAndMoveFED1024);
