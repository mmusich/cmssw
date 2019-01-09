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
#include "FWCore/Concurrency/interface/SerialTaskQueue.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

#include <string>
#include <map>
#include <vector>
#include <TTree.h>
#include <TSpectrum.h>
#include <TF1.h>
#include <TMath.h>

typedef std::map<uint32_t, TH1F*> HistogramMap;

// auxilliary class to store phase-space info
struct PhaseSpaceBin {

  PhaseSpaceBin(unsigned int iEta,unsigned int iPhi): 
    mEta(iEta),mPhi(iPhi){
    mRawId=100*iEta+iPhi;
  }
  
  PhaseSpaceBin(unsigned int rawId): 
    mRawId(rawId){
    mEta=mRawId/100;
    mPhi=mRawId%100;
  }
  
public:
  void clear() {
    mEta=0;
    mPhi=0;
    mRawId=0;
  }

  void print(std::ostream & os) const {
    os<< "phi :"<< mPhi << " eta:" << mEta <<" rawID:" << mRawId << "  \n ";
  }

  unsigned int rawId(){return mRawId;}
  unsigned int iphi(){return mPhi;}
  unsigned int ieta(){return mEta;}

private:
  unsigned int mEta;
  unsigned int mPhi;
  unsigned int mRawId;
};

std::ostream & operator<<( std::ostream & os, PhaseSpaceBin bin) {
  std::stringstream ss;
  bin.print( ss );
  os << ss.str();
  return os;
}

class PVValidationStreamData {
public:
  HistogramMap _hist_dxy; // Filled with transverse impact parameter
  HistogramMap _hist_dz;  // Filled with longitudinal impact parameter
  TF1* _fgaus;
  int _nevents;
  int _nvertices;
  int _ntracks;
  inline void add(const PVValidationStreamData* data) {
    for (auto& it : _hist_dxy) {
      if (data->_hist_dxy.find(it.first) != data->_hist_dxy.end()) {
	it.second->Add(data->_hist_dxy.at(it.first));
      }
    }

    for (auto& it : _hist_dz) {
      if (data->_hist_dz.find(it.first) != data->_hist_dz.end()) {
	it.second->Add(data->_hist_dz.at(it.first));
      }
    }

    _nevents    += data->_nevents;
    _nvertices  += data->_nvertices;
    _ntracks    += data->_ntracks;
  }
  
  inline void reset() {
    this->_hist_dxy.clear();
    this->_hist_dz.clear();
    if (_fgaus) {
      delete _fgaus;
      _fgaus = 0;
    }
  }
};

class StreamPVValidation :  
  public edm::global::EDAnalyzer<edm::StreamCache<PVValidationStreamData>, edm::RunSummaryCache<PVValidationStreamData>> {
 public:
  edm::InputTag		                   _tagVertices;
  edm::EDGetTokenT<reco::VertexCollection> _tokVertices;

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
  std::pair<unsigned int ,unsigned int> getiEtaiPhi(float eta,float phi) const;
  
  HistogramMap bookResidualsHistogram(unsigned int theNOfBins,
				      TString resType,
				      TString varType) const ;
    

  void fillTrendPlotByIndex(TH1F* trendPlot,HistogramMap& h, TString fitPar_) const;
  std::pair<std::pair<Double_t,Double_t>, std::pair<Double_t,Double_t>  > fitResiduals(TH1 *hist) const;
  std::pair<Double_t,Double_t> getMedian(TH1 *histo) const;
  std::pair<Double_t,Double_t> getMAD(TH1 *histo) const;

  edm::Service<TFileService> _fs;
  mutable edm::SerialTaskQueue _queue; //queue is used to serialize access to output file

 protected:
  static const unsigned int nBins_ = 48;
  static constexpr double phiLow_ = -TMath::Pi();
  static constexpr double phiHig_ =  TMath::Pi();
  static constexpr double etaLow_ = -2.5;
  static constexpr double etaHig_ = 2.5;

 public:

};

#endif
