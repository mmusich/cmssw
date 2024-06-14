#include "DataFormats/Common/interface/DetSetVector.h"
#include "DataFormats/SiPixelRawData/interface/SiPixelRawDataError.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/ParameterSetDescription.h"
#include "FWCore/Utilities/interface/EDGetToken.h"

#include <random>

class RandomSiPixelErrorProducer : public edm::global::EDProducer<> {
public:
  explicit RandomSiPixelErrorProducer(const edm::ParameterSet&);
  ~RandomSiPixelErrorProducer() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;

  mutable std::mt19937 rng_;
  unsigned int numErrors_;
};


RandomSiPixelErrorProducer::RandomSiPixelErrorProducer(const edm::ParameterSet& iConfig)
    : rng_(std::random_device{}()), numErrors_(iConfig.getParameter<unsigned int>("numErrors")) {
  produces<edm::DetSetVector<SiPixelRawDataError>>();
}

void RandomSiPixelErrorProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup&) const {
  auto errors = std::make_unique<edm::DetSetVector<SiPixelRawDataError>>();

  std::uniform_int_distribution<> fedIdDist(1200,1348);
  std::uniform_int_distribution<> detIdDist(0, 1000);
  std::uniform_int_distribution<> errorTypeDist(25,38);
  std::uniform_int_distribution<> errorWordDist(0, 0xFFFFFF);
  
  for (unsigned int i = 0; i < numErrors_; ++i) {
    int fedId = fedIdDist(rng_);
    uint32_t detId = detIdDist(rng_);
    uint32_t errorType = errorTypeDist(rng_);
    uint32_t errorWord = errorWordDist(rng_);

    SiPixelRawDataError error(errorWord, errorType, fedId);

    // Use find_or_insert to ensure DetSet is available
    auto& detSet = errors->find_or_insert(detId);

    detSet.data.push_back(error);
  }
  
  iEvent.put(std::move(errors));
}

void RandomSiPixelErrorProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<unsigned int>("numErrors", 10)->setComment("Number of random errors to generate");
  descriptions.add("randomSiPixelErrorProducer", desc);
}

// Define this as a plug-in
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(RandomSiPixelErrorProducer);
