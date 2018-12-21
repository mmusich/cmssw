#ifndef StreamPVValidation_h
#define StreamPVValidation_h

#include "FWCore/Framework/interface/global/EDAnalyzer.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Utilities/interface/StreamID.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include <string>
#include <map>
#include <vector>
#include <TTree.h>
#include <TSpectrum.h>
#include <TF1.h>
#include <TMath.h>

typedef std::map<uint32_t, TH1F*> HistogramMap;

class PVValidationStreamData {
public:
  HistogramMap _hist; // Filled
  TF1* _fgaus;
  int _nevents;
  inline void add(const PVValidationStreamData* data) {
    for (auto& it : _hist) {
      if (data->_hist.find(it.first) != data->_hist.end()) {
	it.second->Add(data->_hist.at(it.first));
      }
    }
    _nevents += data->_nevents;
  }
  
  inline void reset() {
    this->_hist.clear();
    if (_fgaus) {
      delete _fgaus;
      _fgaus = 0;
    }
  }
};

class StreamPVValidation :  
  public edm::global::EDAnalyzer<edm::StreamCache<PVValidationStreamData>, edm::RunSummaryCache<PVValidationStreamData>> {
 public:
  edm::EDGetTokenT<TrackCollection> tracksToken_;  //used to select what tracks to read from configuration file  

 public:
  explicit StreamPVValidation(const edm::ParameterSet& ps);// : pset(iConfig) {}
  ~StreamPVValidation();

 private:
	
  void beginJob();
  void beginRun(edm::Run const&, edm::EventSetup const&) {}
  std::shared_ptr<PVValidationStreamData> globalBeginRunSummary(edm::Run const&, edm::EventSetup const&) const;
  std::unique_ptr<PVValidationStreamData> beginStream(edm::StreamID) const;
  void streamBeginRun(edm::StreamID, edm::Run const&, edm::EventSetup const&) const;
  void analyze(edm::StreamID, const edm::Event&, const edm::EventSetup&) const;
  void streamEndRunSummary(edm::StreamID, edm::Run const&, edm::EventSetup const&, PVValidationStreamData*) const;
  void globalEndRunSummary(edm::Run const&, edm::EventSetup const&, PVValidationStreamData*) const;
  
  void endJob(){}
  void endRun(edm::Run const&, edm::EventSetup const&){}
  
  std::map<TString, double> fitIP(TH1F* hist, TF1** peak_fit, bool debug=false) const;
  
  edm::Service<TFileService> _fs;
  
 protected:
  
 public:

};

#endif
