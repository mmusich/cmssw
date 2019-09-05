// -*- C++ -*-
//
// Package:    CondTools/SiStrip
// Class:      SiStripApvSimulationParametersBuilder
//
/**\class SiStripApvSimulationParametersBuilder SiStripApvSimulationParametersBuilder.cc CondTools/SiStrip/plugins/SiStripApvSimulationParametersBuilder.cc
 Description: class to build SiStripApvSimulationParameters payloads
*/
//
// Original Author:  Marco Musich
//         Created:  Wed, 4 Sept 2019 17:22:00 GMT
//
//

// system include files
#include <memory>
#include <fstream>

// user include files
#include "CondCore/DBOutputService/interface/PoolDBOutputService.h"
#include "CondFormats/DataRecord/interface/SiStripCondDataRecords.h"
#include "CondFormats/SiStripObjects/interface/SiStripApvSimulationParameters.h"
 #include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/ESProducer.h"
#include "FWCore/Framework/interface/ESWatcher.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include <boost/range/adaptor/indexed.hpp>

//
// class declaration
//

class SiStripApvSimulationParametersBuilder : public edm::one::EDAnalyzer<> {
public:
  explicit SiStripApvSimulationParametersBuilder(const edm::ParameterSet&);
  ~SiStripApvSimulationParametersBuilder();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  virtual void beginJob() override;
  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
  virtual void endJob() override;

  SiStripApvSimulationParameters::LayerParameters makeLayerParameters(const std::string& apvBaselinesFileName) const;

  // ----------member data ---------------------------
  std::vector<edm::FileInPath> baselineFiles_TOB_;
  std::vector<edm::FileInPath> baselineFiles_TIB_;
  const unsigned int baseline_nBins_;
  const float baseline_min_;
  const float baseline_max_;
  std::vector<float> puBinEdges_;
  std::vector<float> zBinEdges_;

  SiStripApvSimulationParameters* myAPVSimulationParameters;
};

//
// constructors and destructor
//
SiStripApvSimulationParametersBuilder::SiStripApvSimulationParametersBuilder(const edm::ParameterSet& iConfig)
  : baseline_nBins_(iConfig.getParameter<unsigned int>("apvBaselines_nBinsPerBaseline")),
    baseline_min_(iConfig.getParameter<double>("apvBaselines_minBaseline")),
    baseline_max_(iConfig.getParameter<double>("apvBaselines_maxBaseline")) { 
  
  for (const auto x : iConfig.getParameter<std::vector<double>>("apvBaselines_puBinEdges")) {
    puBinEdges_.push_back(x);
  }
  for (const auto x : iConfig.getParameter<std::vector<double>>("apvBaselines_zBinEdges")) {
    zBinEdges_.push_back(x);
  }

  baselineFiles_TIB_ = {iConfig.getParameter<edm::FileInPath>("apvBaselinesFile_tib1"),
                        iConfig.getParameter<edm::FileInPath>("apvBaselinesFile_tib2"),
                        iConfig.getParameter<edm::FileInPath>("apvBaselinesFile_tib3"),
                        iConfig.getParameter<edm::FileInPath>("apvBaselinesFile_tib4")};

  baselineFiles_TOB_ = {iConfig.getParameter<edm::FileInPath>("apvBaselinesFile_tob1"),
                        iConfig.getParameter<edm::FileInPath>("apvBaselinesFile_tob2"),
                        iConfig.getParameter<edm::FileInPath>("apvBaselinesFile_tob3"),
                        iConfig.getParameter<edm::FileInPath>("apvBaselinesFile_tob4"),
                        iConfig.getParameter<edm::FileInPath>("apvBaselinesFile_tob5"),
                        iConfig.getParameter<edm::FileInPath>("apvBaselinesFile_tob6")};
  //now do what ever initialization is needed
  myAPVSimulationParameters = new SiStripApvSimulationParameters();
}

SiStripApvSimulationParametersBuilder::~SiStripApvSimulationParametersBuilder() { delete  myAPVSimulationParameters; }

//
// member functions
//

SiStripApvSimulationParameters::LayerParameters SiStripApvSimulationParametersBuilder::makeLayerParameters(const std::string& apvBaselinesFileName) const 
{
  // Prepare histograms
  unsigned int nZBins = zBinEdges_.size();
  unsigned int nPUBins = puBinEdges_.size();

  if (nPUBins == 0 || nZBins == 0 || baseline_nBins_ == 0) {
    throw cms::Exception("MissingInput") << "The parameters for the APV simulation are not correctly configured\n";
  }
  std::vector<float> baselineBinEdges{};
  auto baseline_binWidth = (baseline_max_ - baseline_min_) / baseline_nBins_;
  for (unsigned i{0}; i != baseline_nBins_; ++i) {
    baselineBinEdges.push_back(baseline_min_ + i * baseline_binWidth);
  }
  baselineBinEdges.push_back(baseline_max_);

  SiStripApvSimulationParameters::LayerParameters layerParams{zBinEdges_, puBinEdges_, baselineBinEdges};

  // Read apv baselines from text files
  std::vector<double> theAPVBaselines;
  std::ifstream apvBaselineFile(apvBaselinesFileName.c_str());
  if (!apvBaselineFile.good()) {
    throw cms::Exception("FileError") << "Problem opening APV baselines file: " << apvBaselinesFileName;
  }
  std::string line;
  while (std::getline(apvBaselineFile, line)) {
    if (!line.empty()) {
      std::istringstream lStr{line};
      double value;
      while (lStr >> value) {
        theAPVBaselines.push_back(value);
      }
    }
  }
  if (theAPVBaselines.empty()) {
    throw cms::Exception("WrongAPVBaselines")
        << "Problem reading from APV baselines file " << apvBaselinesFileName << ": no values read in";
  }
  
  if (theAPVBaselines.size() != nZBins * nPUBins * baseline_nBins_) {
    throw cms::Exception("WrongAPVBaselines") << "Problem reading from APV baselines file " << apvBaselinesFileName
                                              << ": number of baselines read different to that expected i.e. nZBins * "
                                                 "nPUBins * apvBaselines_nBinsPerBaseline_";
  }

  // Put baselines into histograms
  for (auto const& apvBaseline : theAPVBaselines | boost::adaptors::indexed(0)) {
    unsigned int binInCurrentHistogram = apvBaseline.index() % baseline_nBins_ + 1;
    unsigned int binInZ = int(apvBaseline.index()) / (nPUBins * baseline_nBins_) +1;
    unsigned int binInPU = int(apvBaseline.index() - binInZ * (nPUBins)*baseline_nBins_) / baseline_nBins_ +1;

    layerParams.setBinContent(binInZ, binInPU, binInCurrentHistogram, apvBaseline.value());
  }
  return layerParams;
}



// ------------ method called for each event  ------------
void SiStripApvSimulationParametersBuilder::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  
  for (unsigned int i{0}; i != baselineFiles_TIB_.size(); ++i) {

    if ( ! myAPVSimulationParameters->putTIB(i + 1, makeLayerParameters(baselineFiles_TIB_[i].fullPath())) ) {
      throw cms::Exception("SiStripApvSimulationParameters") << "Could not add parameters for TIB layer " << (i+1);
    } else {
      LogDebug("SiStripApvSimulationParameters") << "Added parameters for TIB layer " << (i+1);
    }
  }

  for (unsigned int i{0}; i != baselineFiles_TOB_.size(); ++i) {
    if ( ! myAPVSimulationParameters->putTOB(i + 1, makeLayerParameters(baselineFiles_TOB_[i].fullPath())) ) {
      throw cms::Exception("SiStripApvSimulationParameters") << "Could not add parameters for TOB layer " << (i+1);
    } else {
      LogDebug("SiStripApvSimulationParameters") << "Added parameters for TOB layer " << (i+1);
    }
  }

}

// ------------ method called once each job just before starting event loop  ------------
void SiStripApvSimulationParametersBuilder::beginJob() {}

// ------------ method called once each job just after ending the event loop  ------------
void SiStripApvSimulationParametersBuilder::endJob() {

  // Form the data here
  edm::Service<cond::service::PoolDBOutputService> poolDbService;
  if (poolDbService.isAvailable()) {
    cond::Time_t valid_time = poolDbService->currentTime();
    // this writes the payload to begin in current run defined in cfg
    poolDbService->writeOne(myAPVSimulationParameters, valid_time,"SiStripApvSimulationParametersRcd");
  }
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void SiStripApvSimulationParametersBuilder::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<unsigned int>("apvBaselines_nBinsPerBaseline",82);
  desc.add<double>("apvBaselines_minBaseline",0.);
  desc.add<double>("apvBaselines_maxBaseline",738.);
  desc.add<std::vector<double>>("apvBaselines_puBinEdges",{0});
  desc.add<std::vector<double>>("apvBaselines_zBinEdges",{0});
  desc.add<edm::FileInPath>("apvBaselinesFile_tib1",edm::FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TIB1_12us.txt"));
  desc.add<edm::FileInPath>("apvBaselinesFile_tib2",edm::FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TIB2_15us.txt"));
  desc.add<edm::FileInPath>("apvBaselinesFile_tib3",edm::FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TIB3_16us.txt"));
  desc.add<edm::FileInPath>("apvBaselinesFile_tib4",edm::FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TIB4_17us.txt"));
  desc.add<edm::FileInPath>("apvBaselinesFile_tob1",edm::FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TOB1_10us.txt"));
  desc.add<edm::FileInPath>("apvBaselinesFile_tob2",edm::FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TOB2_13us.txt"));
  desc.add<edm::FileInPath>("apvBaselinesFile_tob3",edm::FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TOB3_16us.txt"));
  desc.add<edm::FileInPath>("apvBaselinesFile_tob4",edm::FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TOB4_17us.txt"));
  desc.add<edm::FileInPath>("apvBaselinesFile_tob5",edm::FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TOB5_17us.txt"));
  desc.add<edm::FileInPath>("apvBaselinesFile_tob6",edm::FileInPath("SimTracker/SiStripDigitizer/data/APVBaselines_TOB6_18us.txt"));
  descriptions.add("SiStripApvSimulationParametersBuilder",desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(SiStripApvSimulationParametersBuilder);
