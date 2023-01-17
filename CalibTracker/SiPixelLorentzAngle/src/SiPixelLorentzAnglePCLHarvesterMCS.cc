// -*- C++ -*-
//
// Package:    CalibTracker/SiPixelLorentzAnglePCLHarvesterMCS
// Class:      SiPixelLorentzAnglePCLHarvesterMCS
//
/**\class SiPixelLorentzAnglePCLHarvesterMCS SiPixelLorentzAnglePCLHarvesterMCS.cc CalibTracker/SiPixelLorentzAngle/src/SiPixelLorentzAnglePCLHarvesterMCS.cc
 Description: reads the intermediate ALCAPROMPT DQMIO-like dataset and performs the fitting of the SiPixel Lorentz Angle in the Prompt Calibration Loop
 Implementation:
 Reads the 16 2D histograms of the cluser size x/y vs cot(alpha/beta) and 16*3 histogrmas of the magnetic field components created by SiPixelLorentzAnglePCLWorker module. The cluser size x/y vs cot(alpha/beta) histograms are used to generate 1D profiles (average cluster size x/y vs cot(alpha/beta)) which are then fit and the values of the cot (alpha/beta) for which the cluser sizes are minimal are determined. The obtained cot(alpha/beta)_min value for z- and z+ side are used to perform fit and the muH for different rings and panels of the Pixel Forward Phase 1 detector using the formulas: 
 cot(alpha)_min = vx/vz  = (muHBy + muH^2*Bz*Bx)/(1+muH^2*Bz^2)
 cot(beta)_min = vy/vz  = -(muHBx - muH^2*Bz*Bx)/(1+muH^2*Bz^2)
  
The extracted value of the muH are stored in an output sqlite file which is then uploaded to the conditions database.
*/
//
// Original Author:  tsusa
//         Created:  Sat, 14 Jan 2021 10:12:21 GMT
//
//

// system includes
#include <fmt/format.h>
#include <fmt/printf.h>
#include <fstream>

// user includes
#include "CalibTracker/SiPixelLorentzAngle/interface/SiPixelLorentzAngleCalibrationStruct.h"
#include "CondCore/DBOutputService/interface/PoolDBOutputService.h"
#include "CondFormats/DataRecord/interface/SiPixelLorentzAngleRcd.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelLorentzAngle.h"
#include "DQMServices/Core/interface/DQMEDHarvester.h"
#include "DataFormats/TrackerCommon/interface/PixelBarrelName.h"
#include "DataFormats/TrackerCommon/interface/PixelEndcapName.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/TrackerGeometryBuilder/interface/PixelTopologyMap.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"

// for ROOT fits
#include "TFitResult.h"
#include "TVirtualFitter.h"
#include "TH1D.h"

namespace SiPixelLAHarvestMCS {
 
  Double_t MCSFitFunction(Double_t *x,Double_t *par){
    Double_t arg;
    
    if(x[0] < par[3]) {
      arg = par[1]*par[1] + par[2]*par[2]*(x[0]-par[3])*(x[0]-par[3]);
    }
    else {
      arg = par[1]*par[1] + par[4]*par[4]*(x[0]-par[3])*(x[0]-par[3]);
    }
    Double_t fitval = par[0]+sqrt(arg);
    return fitval;
  }
  
  struct FPixMuH{
    double bfield[3];
    double shiftx;        // Shift in x direction
    double shifty;        // Shift in y direction
    double shiftx_err;        // Shift in x direction
    double shifty_err;        // Shift in y direction  
  };

  void fcn_func(Int_t& npar, Double_t* deriv, Double_t& f, Double_t *par, Int_t flag);
    
  class FitFPixMuH : public TObject {

  public:
    FitFPixMuH():
      muH(0),
      muHErr(0)
    {}
    
    //-----------------------------------------------------------    
    ~FitFPixMuH() {}
    
    friend void fcn_func(Int_t& npar, Double_t* deriv, Double_t& f, Double_t *par, Int_t flag);

    void Add(const FPixMuH &fmh){
      cmvar.push_back(fmh);
    }
    int Fit(){
      
      minuit = TVirtualFitter::Fitter(this,1);
      minuit->SetFCN(fcn_func);
      double tanlorpertesla = 0.08;
      minuit->SetParameter(0, "muH", tanlorpertesla, 0.1, 0., 0.);
      
      double arglist[100];
      arglist[0] = 3.;
      minuit->ExecuteCommand("SET PRINT", arglist, 0);
      double up = 1.0;
      minuit->SetErrorDef(up);
      arglist[0] = 100000.;
      int retVal = minuit->ExecuteCommand("MIGRAD", arglist, 0);     
      muH = minuit->GetParameter(0);
      muHErr = minuit->GetParError(0);
      
      return retVal;
    }
    
    double GetMuH(){return muH;}
    double GetMuHErr(){return muHErr;}
    unsigned int size(){return cmvar.size();}
  private:
    
    TVirtualFitter* minuit;
    std::vector<FPixMuH> cmvar;
    double muH;
    double muHErr;

    double calcChi2(double par_0){
      double tanlorpertesla = par_0;
      double tlpt2 = tanlorpertesla*tanlorpertesla;
      double v[3], xshift, yshift;
      
      int n = cmvar.size();
      
      double chi2 = 0.0;
      for (int i=0; i<n; i++){
	v[0] = -(tanlorpertesla*cmvar[i].bfield[1]+tlpt2*cmvar[i].bfield[0]*cmvar[i].bfield[2]);
	v[1] = tanlorpertesla*cmvar[i].bfield[0]-tlpt2*cmvar[i].bfield[1]*cmvar[i].bfield[2];
	v[2] = -(1.+tlpt2*cmvar[i].bfield[2]*cmvar[i].bfield[2]);
	
	xshift = v[0]/v[2];
	yshift = v[1]/v[2];
	
	chi2 +=
	  (xshift - cmvar[i].shiftx)*(xshift - cmvar[i].shiftx)/cmvar[i].shiftx_err/cmvar[i].shiftx_err
	  + (yshift - cmvar[i].shifty)*(yshift - cmvar[i].shifty)/cmvar[i].shifty_err/cmvar[i].shifty_err;
	//
      }
      return chi2;
    }
  };
  
  void fcn_func(Int_t& npar, Double_t* deriv, Double_t& f, Double_t *par, Int_t flag){
    
    f=((dynamic_cast<FitFPixMuH*>((TVirtualFitter::GetFitter())->GetObjectFit()))->calcChi2(par[0]));
  }
}  // namespace SiPixelLAHarvesterMCS

//------------------------------------------------------------------------------
class SiPixelLorentzAnglePCLHarvesterMCS : public DQMEDHarvester {
public:
  SiPixelLorentzAnglePCLHarvesterMCS(const edm::ParameterSet&);
  ~SiPixelLorentzAnglePCLHarvesterMCS() override = default;
  using FPixCotAngleFitResults = std::unordered_map<uint32_t, std::pair<double, double>>;
 
  using FpixMuHResults = std::unordered_map<std::string, std::pair<double, double>>;
  
 void beginRun(const edm::Run&, const edm::EventSetup&) override;

  static void fillDescriptions(edm::ConfigurationDescriptions&);

private:
  void dqmEndJob(DQMStore::IBooker&, DQMStore::IGetter&) override;
  void findMean(dqm::reco::MonitorElement* h_2D, dqm::reco::MonitorElement* h_mean, TH1D *h_slice);
  
  // es tokens
  edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> geomEsToken_;
  edm::ESGetToken<TrackerTopology, TrackerTopologyRcd> topoEsTokenBR_, topoEsTokenER_;
  edm::ESGetToken<SiPixelLorentzAngle, SiPixelLorentzAngleRcd> siPixelLAEsToken_;
  edm::ESGetToken<MagneticField, IdealMagneticFieldRecord> magneticFieldToken_;
  
  
  const std::string dqmDir_;
  std::vector<std::string> newmodulelist_; 
  const std::vector<double> fitRange_;
  const std::string recordName_;
  SiPixelLorentzAngleCalibrationHistograms hists_;
  int fitMCSHistogram(dqm::reco::MonitorElement* h_mean);
  std::pair<double, double> theFitRange_{-1.5, 1.5};
  
  std::unique_ptr<TF1> f1_;
  FpixMuHResults fpixMuHResults;

  const SiPixelLorentzAngle* currentLorentzAngle_;
  const TrackerTopology *tTopo;
};

//------------------------------------------------------------------------------
SiPixelLorentzAnglePCLHarvesterMCS::SiPixelLorentzAnglePCLHarvesterMCS(const edm::ParameterSet& iConfig)
  : geomEsToken_(esConsumes<edm::Transition::BeginRun>()),
    topoEsTokenBR_(esConsumes<edm::Transition::BeginRun>()),
    topoEsTokenER_(esConsumes<edm::Transition::EndRun>()),
    siPixelLAEsToken_(esConsumes<edm::Transition::BeginRun>()),    
    dqmDir_(iConfig.getParameter<std::string>("dqmDir")),
    newmodulelist_(iConfig.getParameter<std::vector<std::string>>("newmodulelist")), 
    fitRange_(iConfig.getParameter<std::vector<double>>("fitRange")),
    recordName_(iConfig.getParameter<std::string>("record")){
  
  // initialize the fit range
 
  if (fitRange_.size() == 2) {
    theFitRange_.first = fitRange_[0];
    theFitRange_.second = fitRange_[1];
  } else {
    throw cms::Exception("SiPixelLorentzAnglePCLHarvesterMCS") << "Too many fit range parameters specified";
  }
 
  // first ensure DB output service is available
  edm::Service<cond::service::PoolDBOutputService> poolDbService;
  if (!poolDbService.isAvailable())
    throw cms::Exception("SiPixelLorentzAnglePCLHarvesterMCS") << "PoolDBService required";  
}

//------------------------------------------------------------------------------
void SiPixelLorentzAnglePCLHarvesterMCS::beginRun(const edm::Run& iRun, const edm::EventSetup& iSetup) {
  // geometry
  
  const TrackerGeometry* geom = &iSetup.getData(geomEsToken_);
  //const TrackerTopology* tTopo = &iSetup.getData(topoEsTokenBR_);
  tTopo = &iSetup.getData(topoEsTokenBR_);  
  currentLorentzAngle_ = &iSetup.getData(siPixelLAEsToken_);  
  PixelTopologyMap map = PixelTopologyMap(geom, tTopo);
  hists_.nlay = geom->numberOfLayers(PixelSubdetector::PixelBarrel);
  hists_.nModules_.resize(hists_.nlay);
  hists_.nLadders_.resize(hists_.nlay);
  for (int i = 0; i < hists_.nlay; i++) {
    hists_.nModules_[i] = map.getPXBModules(i + 1);
    hists_.nLadders_[i] = map.getPXBLadders(i + 1);
  }

  // list of modules already filled, then return (we already entered here)
  if (!hists_.BPixnewDetIds_.empty() || !hists_.FPixnewDetIds_.empty())
    return;

  if (!newmodulelist_.empty()) {
    for (auto const& modulename : newmodulelist_) {
      if (modulename.find("BPix_") != std::string::npos) {
        PixelBarrelName bn(modulename, true);
        const auto& detId = bn.getDetId(tTopo);
        hists_.BPixnewmodulename_.push_back(modulename);
        hists_.BPixnewDetIds_.push_back(detId.rawId());
        hists_.BPixnewModule_.push_back(bn.moduleName());
        hists_.BPixnewLayer_.push_back(bn.layerName());
      } else if (modulename.find("FPix_") != std::string::npos) {
        PixelEndcapName en(modulename, true);
        const auto& detId = en.getDetId(tTopo);
        hists_.FPixnewmodulename_.push_back(modulename);
        hists_.FPixnewDetIds_.push_back(detId.rawId());
        hists_.FPixnewDisk_.push_back(en.diskName());
        hists_.FPixnewBlade_.push_back(en.bladeName());
      }
    }
  }

  uint count = 0;
  for (const auto& id : hists_.BPixnewDetIds_) {
    LogDebug("SiPixelLorentzAnglePCLHarvesterMCS") << id;
    count++;
  }
  LogDebug("SiPixelLorentzAnglePCLHarvesterMCS") << "Stored a total of " << count << " new detIds.";

  // list of modules already filled, return (we already entered here)
  if (!hists_.detIdsList.empty())
    return;

  std::vector<uint32_t> treatedIndices;

  for (const auto& det : geom->detsPXB()) {
    const PixelGeomDetUnit* pixelDet = dynamic_cast<const PixelGeomDetUnit*>(det);
    const auto& layer = tTopo->pxbLayer(pixelDet->geographicalId());
    const auto& module = tTopo->pxbModule(pixelDet->geographicalId());
    int i_index = module + (layer - 1) * hists_.nModules_[layer - 1];

    uint32_t rawId = pixelDet->geographicalId().rawId();

    // if the detId is already accounted for in the special class, do not attach it
    if (std::find(hists_.BPixnewDetIds_.begin(), hists_.BPixnewDetIds_.end(), rawId) != hists_.BPixnewDetIds_.end())
      continue;
    if (std::find(treatedIndices.begin(), treatedIndices.end(), i_index) != treatedIndices.end()) {
      hists_.detIdsList[i_index].push_back(rawId);
    } else {
      hists_.detIdsList.insert(std::pair<uint32_t, std::vector<uint32_t>>(i_index, {rawId}));
      treatedIndices.push_back(i_index);
    }
  }

  count = 0;
  for (const auto& i : treatedIndices) {
    for (const auto& id : hists_.detIdsList[i]) {
      LogDebug("SiPixelLorentzAnglePCLHarvesterMCS") << id;
      count++;
    };
  }
  LogDebug("SiPixelLorentzAnglePCLHarvesterMCS") << "Stored a total of " << count << " detIds.";  
}
//------------------------------------------------------------------------------
void SiPixelLorentzAnglePCLHarvesterMCS::dqmEndJob(DQMStore::IBooker& iBooker, DQMStore::IGetter& iGetter) {

  // go in the right directory
  
  iGetter.cd();
  iGetter.setCurrentFolder(dqmDir_);

  const auto& prefix_ = fmt::sprintf("%s/FPix", dqmDir_);

  int nBinsMeanHistsFitSummary  = 2*hists_.nRings_*hists_.nPanels_*hists_.nSides_;
  hists_.h_fpixIsMeanHistoFitValid_ = iBooker.book1D("fpixIsMeanHistoFitValid", "is fit valid by rings/panels/sides; ring/panel/side; is fit valid", nBinsMeanHistsFitSummary, -0.5, nBinsMeanHistsFitSummary-0.5);
  hists_.h_fpixMinClusterSizeCotAngle_ = iBooker.book1D("fpixMinClusterSizeCotAngle", "cot angle of minimal cluster size by rings/panels/sides/angles; ring/panel/side/angle; ", nBinsMeanHistsFitSummary, -0.5, nBinsMeanHistsFitSummary-0.5);
  char binNameAlpha[256];   
  char binNameBeta[256];     
  for (int r=0; r < hists_.nRings_;++r){
    for (int p=0; p < hists_.nPanels_;++p){
      for (int s=0; s < hists_.nSides_;++s){	  
	int idx = hists_.nSides_*hists_.nPanels_*r + hists_.nSides_*p+s;
	int idxBeta = hists_.betaStartIdx_ + hists_.nSides_*hists_.nPanels_*r + hists_.nSides_*p+s;	
	hists_.h_fpixMean_[idx] =
	  iGetter.get(fmt::format("{}/R{}_P{}_z{}_alphaMean", dqmDir_, r+1, p+1, s+1));
	hists_.h_fpixMean_[idxBeta] =
	  iGetter.get(fmt::format("{}/R{}_P{}_z{}_betaMean", dqmDir_, r+1, p+1, s+1));
	hists_.h_fpixAngleSize_[idx] =
	  iGetter.get(fmt::format("{}/R{}_P{}_z{}_alpha", prefix_, r+1, p+1, s+1));
	hists_.h_fpixAngleSize_[idxBeta] =
	  iGetter.get(fmt::format("{}/R{}_P{}_z{}_beta", prefix_, r+1, p+1, s+1));	
	for (int m=0; m<3; ++m){
	  hists_.h_fpixMagField_[m][idx] = 
	    iGetter.get(fmt::format("{}/R{}_P{}_z{}_B{}", prefix_, r+1, p+1, s+1, m));	  
	} 
	int idxLabelAlpha = idx + 1;
	int idxLabelBeta = idxBeta + 1;	
	char sign = s==0? '-': '+';	
	sprintf(binNameAlpha, "#alpha: R%d_P%d_z%c", r+1, p+1, sign);
	sprintf(binNameBeta, "#beta:R%d_P%d_z%c", r+1, p+1, sign);	
	hists_.h_fpixIsMeanHistoFitValid_->setBinLabel(idxLabelAlpha, binNameAlpha);
	hists_.h_fpixIsMeanHistoFitValid_->setBinLabel(idxLabelBeta, binNameBeta);	
	hists_.h_fpixMinClusterSizeCotAngle_->setBinLabel(idxLabelAlpha, binNameAlpha);
	hists_.h_fpixMinClusterSizeCotAngle_->setBinLabel(idxLabelBeta, binNameBeta);	
      }
    }
  } // get histograms

  // Book Histograms   
  iBooker.setCurrentFolder(fmt::format("{}Harvesting", dqmDir_));
  int nBinsMuH = hists_.nRings_*hists_.nPanels_;
  hists_.h_fpixFitStatusMuH_ = iBooker.book1D("fpixFitStatusMuH", "muH fit status by rings/panels; ring/panel; fitStatus", nBinsMuH, -0.5, nBinsMuH-0.5);
  hists_.h_fpixMuH_ = iBooker.book1D("fpixMuH", "muH by rings/panels; ring/panel; #muH [1/T]", nBinsMuH, -0.5, nBinsMuH-0.5);
  hists_.h_fpixDeltaMuH_ = iBooker.book1D("fpixDeltaMuH", "#Delta muH by rings/panels; ring/panel; #Delta #muH [1/T]", nBinsMuH, -0.5, nBinsMuH-0.5);
  hists_.h_fpixRelDeltaMuH_ = iBooker.book1D("fpixRelDeltaMuH", "#Delta #muH/#muH by rings/panels; ring/panel; #Delta #muH/#MuH", nBinsMuH, -0.5, nBinsMuH-0.5);

  char binName[256];   
  for (int r=0; r<hists_.nRings_;++r){
    for (int p=0; p<hists_.nPanels_;++p){
      int idx = r*hists_.nPanels_ + p+1;
      sprintf(binName, "R%d_P%d", r+1, p+1);
      hists_.h_fpixFitStatusMuH_->setBinLabel(idx, binName);
      hists_.h_fpixMuH_->setBinLabel(idx, binName);
      hists_.h_fpixDeltaMuH_->setBinLabel(idx, binName);      
      hists_.h_fpixRelDeltaMuH_->setBinLabel(idx, binName);      
    }
  }
 
  int nSizeBins = hists_.h_fpixAngleSize_[0]->getNbinsY();
  double minSize = hists_.h_fpixAngleSize_[0]->getAxisMin(2);
  double maxSize = hists_.h_fpixAngleSize_[0]->getAxisMax(2);
  
  TH1D* h_slice = new TH1D("h_slice", "slice of cot_angle histogram", nSizeBins, minSize, maxSize);
  f1_ = std::make_unique<TF1>("f1", SiPixelLAHarvestMCS::MCSFitFunction, -3., 3., 5);
  
  f1_->SetParNames("Offset","RMS Constant","SlopeL", "cot(alngle)_min","SlopeR");
  f1_->SetParameters(1., 0.1, -1.6, 0, 1.6);
  
  for (int r=0; r < hists_.nRings_;++r){
    for (int p=0; p < hists_.nPanels_;++p){
      SiPixelLAHarvestMCS::FitFPixMuH fitMuH;
      SiPixelLAHarvestMCS::FPixMuH fmh;
      for (int s=0; s < hists_.nSides_;++s){	  
	int idx = hists_.nSides_*hists_.nPanels_*r + hists_.nSides_*p+s;
	findMean (hists_.h_fpixAngleSize_[idx], hists_.h_fpixMean_[idx], h_slice);
	int retValAlphaFit = fitMCSHistogram(hists_.h_fpixMean_[idx]);
	int idxBeta = hists_.betaStartIdx_ + idx;
	
	
	findMean (hists_.h_fpixAngleSize_[idxBeta], hists_.h_fpixMean_[idxBeta], h_slice);
	int retValBetaFit = fitMCSHistogram(hists_.h_fpixMean_[idxBeta]);
	assert(strcmp(f1_->GetName(), "f1") == 0);	
	double shiftX =  hists_.h_fpixMean_[idx]->getTH1()->GetFunction("f1")->GetParameter(3);
	double errShiftX = hists_.h_fpixMean_[idx]->getTH1()->GetFunction("f1")->GetParError(3);
	double shiftY =  hists_.h_fpixMean_[idxBeta]->getTH1()->GetFunction("f1")->GetParameter(3);
	double errShiftY = hists_.h_fpixMean_[idxBeta]->getTH1()->GetFunction("f1")->GetParError(3);
	

	hists_.h_fpixIsMeanHistoFitValid_->setBinContent(idx+1, retValAlphaFit);
	hists_.h_fpixIsMeanHistoFitValid_->setBinContent(idxBeta+1, retValBetaFit);	
	hists_.h_fpixMinClusterSizeCotAngle_->setBinContent(idx+1, shiftX);
	hists_.h_fpixMinClusterSizeCotAngle_->setBinError(idx+1, errShiftX);
	
	hists_.h_fpixMinClusterSizeCotAngle_->setBinContent(idxBeta+1, shiftY);
	
	hists_.h_fpixMinClusterSizeCotAngle_->setBinError(idxBeta+1, errShiftY);	

	fmh.bfield[0] = hists_.h_fpixMagField_[0][idx]->getMean();
	fmh.bfield[1] = hists_.h_fpixMagField_[1][idx]->getMean();
	fmh.bfield[2] = hists_.h_fpixMagField_[2][idx]->getMean();;
	fmh.shiftx = shiftX;
	fmh.shiftx_err = errShiftX;
	fmh.shifty = shiftY; 
	fmh.shifty_err = errShiftY; 
	fitMuH.Add(fmh);
      } // loop over z sides
      int retVal = fitMuH.Fit();
      int idxMuH = r*hists_.nPanels_ + p + 1;
      hists_.h_fpixFitStatusMuH_->setBinContent(idxMuH, retVal);
      double muH = fitMuH.GetMuH();
      double muHErr = fitMuH.GetMuHErr();
      hists_.h_fpixMuH_->setBinContent(idxMuH, muH);
      hists_.h_fpixMuH_->setBinError(idxMuH, muHErr);
     
      std::string fpixPartNames = "R" + std::to_string(r+1) + "_P" + std::to_string(p+1);
      fpixMuHResults.insert(std::make_pair(fpixPartNames, std::make_pair(muH, muH)));      
    }
  } 
  
  std::shared_ptr<SiPixelLorentzAngle> LorentzAngle = std::make_shared<SiPixelLorentzAngle>();
  
  bool isPayloadChanged{false};
  for (const auto& [id, value] : currentLorentzAngle_->getLorentzAngles()) {
    
    DetId ID = DetId(id);
    
    if (ID.subdetId() == PixelSubdetector::PixelEndcap) {
      PixelEndcapName pen(ID, tTopo, true); // use det-id phaseq      
      int panel = pen.pannelName();
      int ring = pen.ringName();            
      std::string fpixPartNames = "R" + std::to_string(ring) + "_P" + std::to_string(panel);
      if (fpixMuHResults.find(fpixPartNames) != fpixMuHResults.end()){
	double measuredMuH = fpixMuHResults[fpixPartNames].first;
	double  deltaMuH = value - measuredMuH; 
	double  deltaMuHoverMuH = deltaMuH/value; 
	int idxMuH = (ring-1)*hists_.nPanels_ + panel;
	hists_.h_fpixDeltaMuH_->setBinContent(idxMuH, deltaMuH); 
	hists_.h_fpixRelDeltaMuH_->setBinContent(idxMuH, deltaMuHoverMuH);
	float measuredMuHForDB = measuredMuH;
	if (!isPayloadChanged && (deltaMuHoverMuH != 0.f))
	  isPayloadChanged = true;
	
	if (!LorentzAngle->putLorentzAngle(id, measuredMuHForDB)) {
	  edm::LogError("SiPixelLorentzAnglePCLHarvesterMCS") << "[SiPixelLorentzAnglePCLHarvesterMCS::dqmEndJob]: detid ("	   		      				      << id << ") already exists";
	}
      }    
    }
    else {
      float bpixMuH = value;
      if (!LorentzAngle->putLorentzAngle(id, bpixMuH)) {	
	edm::LogError("SiPixelLorentzAnglePCLHarvesterMCS") << "[SiPixelLorentzAnglePCLHarvesterMCS::dqmEndJob]: detid ("	   		      				      << id << ") already exists";
      }
    }
  } // Loop over LA payload entries
  
  if (isPayloadChanged) {
  // fill the DB object record
    edm::Service<cond::service::PoolDBOutputService> mydbservice;
    if (mydbservice.isAvailable()) {
      try {
        mydbservice->writeOneIOV(*LorentzAngle, mydbservice->currentTime(), recordName_);
      } catch (const cond::Exception& er) {
        edm::LogError("SiPixelLorentzAngleDB") << er.what();
      } catch (const std::exception& er) {
        edm::LogError("SiPixelLorentzAngleDB") << "caught std::exception " << er.what();
      }
    } else {
      edm::LogError("SiPixelLorentzAngleDB") << "Service is unavailable";
    }
  } else {
    edm::LogPrint("SiPixelLorentzAngleDB") << __PRETTY_FUNCTION__ << " there is no new valid measurement to append! ";
  } 
}

//------------------------------------------------------------------------------
void SiPixelLorentzAnglePCLHarvesterMCS::findMean(dqm::reco::MonitorElement* h_2D, dqm::reco::MonitorElement* h_mean, TH1D *h_slice){  
  
  int n_x = h_2D->getNbinsX();
  int n_y = h_2D->getNbinsY();
  
  for(int i = 1; i <= n_x; i++){
      h_slice->Reset("ICE");

      //loop over bins in size

      for( int j = 1; j<= n_y; j++){
        h_slice->SetBinContent(j, h_2D->getBinContent(i,j));
      }
      double mean = h_slice->GetMean();
      double error = h_slice->GetMeanError();     
      h_mean->setBinContent(i, mean);
      h_mean->setBinError(i, error);
  } // end loop over bins in depth
}

//------------------------------------------------------------------------------
int SiPixelLorentzAnglePCLHarvesterMCS::fitMCSHistogram(dqm::reco::MonitorElement* h_mean){
  
  int retVal;
  f1_->SetParameters(1., 0.1, -1.6, 0, 1.6);
  int nFits = 0;
  while (nFits < 5){
    nFits++;
    double fitMin = f1_->GetParameter(3) + theFitRange_.first;    
    double fitMax = f1_->GetParameter(3) + theFitRange_.second;
    if (fitMin < -3)
      fitMin = -3;
    if (fitMax > 3)
      fitMax = 3;    
    
    TFitResultPtr r = h_mean->getTH1()->Fit(f1_.get(),"ERSM", "", fitMin, fitMax);
    retVal = r->IsValid();
  }
  return retVal;
}

//------------------------------------------------------------------------------
void SiPixelLorentzAnglePCLHarvesterMCS::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  
  edm::ParameterSetDescription desc;
  desc.setComment("Harvester module of the SiPixel Lorentz Angle PCL monitoring workflow for MinimalClusterSizeMethod");
  desc.add<std::string>("dqmDir", "AlCaReco/SiPixelLorentzAngle")->setComment("the directory of PCL Worker output");
  desc.add<std::vector<std::string>>("newmodulelist", {})->setComment("the list of DetIds for new sensors");
  desc.add<std::vector<double>>("fitRange", {-1.5, 1.5})->setComment("range  to perform the fit");
  desc.add<std::string>("record", "SiPixelLorentzAngleRcd")->setComment("target DB record");
}

DEFINE_FWK_MODULE(SiPixelLorentzAnglePCLHarvesterMCS);
