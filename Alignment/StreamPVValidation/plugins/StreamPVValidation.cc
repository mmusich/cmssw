#include "Alignment/StreamPVValidation/interface/StreamPVValidation.h"
#include "FWCore/Framework/interface/ConstProductRegistry.h"
#include "FWCore/Framework/interface/ProductSelector.h"
#include "FWCore/Framework/interface/ProductSelectorRules.h"
#include "DataFormats/Provenance/interface/SelectedProducts.h"
#include "Math/LorentzVector.h"
#include "Math/Vector3D.h"

#include<TH1F.h>
#include <map>
#include <algorithm> 
#include <numeric>
#include "boost/foreach.hpp"
#include <TBranch.h>
#include <TLorentzVector.h>

auto getBin = [](int mult, double pitch, double start) -> double { return start + mult*pitch; };

StreamPVValidation::StreamPVValidation(const edm::ParameterSet& ps) {    
  _tagVertices = ps.getUntrackedParameter<edm::InputTag>("tagVertices", edm::InputTag("offlinePrimaryVertices"));
  _tokVertices = consumes<reco::VertexCollection>(_tagVertices);	
}

StreamPVValidation::~StreamPVValidation() {
}

std::unique_ptr<PVValidationStreamData> StreamPVValidation::beginStream(edm::StreamID sid) const {
  //return std::unique_ptr<PVValidation::ChannelHistogramMap>(new StreamPVValidation::ChannelHistogramMap());
  return std::unique_ptr<PVValidationStreamData>(new PVValidationStreamData());
}

std::shared_ptr<PVValidationStreamData> StreamPVValidation::globalBeginRunSummary(edm::Run const& run, edm::EventSetup const& es) const {
  //std::shared_ptr<PVValidation::ChannelHistogramMap> returnValue(new StreamPVValidation::ChannelHistogramMap());
  std::shared_ptr<PVValidationStreamData> returnValue(new PVValidationStreamData());
  
  for(unsigned int ieta=0;ieta<nBins_;ieta++){
    for(unsigned int iphi=0;iphi<nBins_;iphi++){

      char hname[50];
      PhaseSpaceBin did(ieta,iphi);
      
      sprintf(hname, "h_dxy_ieta%d_iphi%d_run%d", did.ieta(), did.iphi(), run.runAuxiliary().run());
      returnValue->_hist_dxy.insert(std::pair<uint32_t, TH1F*>(did.rawId(), new TH1F(hname, hname, 1000, -500., 500.)));
      
      sprintf(hname, "h_dz_ieta%d_iphi%d_run%d", did.ieta(), did.iphi(), run.runAuxiliary().run());
      returnValue->_hist_dz.insert(std::pair<uint32_t, TH1F*>(did.rawId(), new TH1F(hname, hname, 1000, -500., 500.)));  

      did.clear();
    }
  }

  // SumW2 all histograms
  for (auto& it : returnValue->_hist_dxy) {
    it.second->Sumw2();
  }
  for (auto& it : returnValue->_hist_dz)  {
    it.second->Sumw2();
  }
  
  return returnValue;
}

void StreamPVValidation::streamBeginRun(edm::StreamID sid, edm::Run const& run, edm::EventSetup const& es) const {
  
  for(unsigned int ieta=0;ieta<nBins_;ieta++){
    for(unsigned int iphi=0;iphi<nBins_;iphi++){

      char hname[50];
      PhaseSpaceBin did(ieta,iphi);

      sprintf(hname, "h_dxy_ieta%d_iphi%d_run%d", did.ieta(), did.iphi(), run.runAuxiliary().run());
      streamCache(sid)->_hist_dxy.insert(std::pair<uint32_t, TH1F*>(did.rawId(), new TH1F(hname, hname, 1000, -500., 500.)));
      
      sprintf(hname, "h_dz_ieta%d_iphi%d_run%d", did.ieta(), did.iphi(), run.runAuxiliary().run());      
      streamCache(sid)->_hist_dz.insert(std::pair<uint32_t, TH1F*>(did.rawId(), new TH1F(hname, hname, 1000, -500., 500.)));
      
      did.clear();
    }
  }

  char fname[50];
  sprintf(fname, "gaus_%d", sid.value());
  streamCache(sid)->_fgaus = new TF1(fname, "gaus", 0., 500.);
  streamCache(sid)->_nevents = 0;
  
  // Sumw2 all histograms
  for (auto& it : streamCache(sid)->_hist_dxy) {
    it.second->Sumw2();
  }
  for (auto& it : streamCache(sid)->_hist_dz) {
    it.second->Sumw2();
  }
  
}

void StreamPVValidation::beginJob() {
}


std::pair<unsigned int ,unsigned int> 
StreamPVValidation::getiEtaiPhi(float eta,float phi) const{
    
  unsigned int iPhi(9999),iEta(9999);

  std::array<unsigned int, nBins_> multiplier;
  std::iota(multiplier.begin(), multiplier.end(),0);

  for (auto i : multiplier){

    auto etaMin = getBin(i,((etaHig_-etaLow_)/nBins_),etaLow_);
    auto etaMax = getBin(i+1,((etaHig_-etaLow_)/nBins_),etaLow_);

    auto phiMin = getBin(i,((phiHig_-phiLow_)/nBins_),phiLow_);
    auto phiMax = getBin(i+1,((phiHig_-phiLow_)/nBins_),phiLow_);
        
    if(phi>phiMin && phi<=phiMax){
      iPhi = i;
    }

    if(eta>etaMin && eta<=etaMax){
      iEta = i;
    }
  }

  if(iEta==9999 || iPhi==9999){
    std::cout << "[debug] WARNING : eta="<<eta<<"("<<iEta<<")"<<" phi="<<phi<<"("<< iPhi<< ") is not a valid set of coordinates" << std::endl;
  }

  return std::make_pair(iEta,iPhi);
}

void StreamPVValidation::analyze(edm::StreamID sid, const edm::Event& event, const edm::EventSetup& es) const {

  const double cmToum = 10000;
  streamCache(sid)->_nevents += 1;
  
  using namespace edm;

  // edm::ESHandle<TransientTrackBuilder>            theB                ;
  // edm::ESHandle<GlobalTrackingGeometry>           theTrackingGeometry ;
  // es.get<GlobalTrackingGeometryRecord>().get(theTrackingGeometry) ;
  // es.get<TransientTrackRecord>().get("TransientTrackBuilder",theB);

  // load vertices
  edm::Handle<reco::VertexCollection> vertices;
  if(!event.getByToken(_tokVertices, vertices)){
    std::cout << "Collection reco::VertexCollection  isn't available" << _tagVertices.label() << " " << _tagVertices.instance() << std::endl;
    exit(1);
  }
  const reco::VertexCollection pvtx  = *(vertices.product())  ;
  
  for (reco::VertexCollection::const_iterator pvIt = pvtx.begin(); pvIt!=pvtx.end(); pvIt++){
    reco::Vertex iPV = *pvIt;
    if (iPV.isFake()) continue;

    streamCache(sid)->_nvertices += 1;
    const math::XYZPoint pos_(iPV.x(),iPV.y(),iPV.z());

    reco::Vertex::trackRef_iterator trki;

    // vertex selection as in bs code                                                                                
    //if ( iPV.ndof() < minVtxNdf_ || (iPV.ndof()+3.)/iPV.tracksSize()< 2*minVtxWgt_ )  continue;

    //reco::TrackCollection allTracks;
    //reco::TrackCollection groupOne, groupTwo;
    for (trki  = iPV.tracks_begin(); trki != iPV.tracks_end(); ++trki){
      if (trki->isNonnull()){
	
	streamCache(sid)->_ntracks += 1;

	double dxyRes  = (*trki)->dxy(pos_)*cmToum;
	double dzRes   = (*trki)->dz(pos_)*cmToum;
	
	//double dxy_err = (*trki)->dxyError()*cmToum;
	//double dz_err  = (*trki)->dzError()*cmToum;
	
	float trackphi = (*trki)->phi();
	float tracketa = (*trki)->eta();

	auto coords = getiEtaiPhi(tracketa,trackphi);
	PhaseSpaceBin did(coords.first,coords.second);

	if (streamCache(sid)->_hist_dxy.find(did.rawId()) != streamCache(sid)->_hist_dxy.end()) {
	  streamCache(sid)->_hist_dxy.at(did.rawId())->Fill(dxyRes);
	} else {
	  std::cout << "[debug] WARNING : Did " << did << " is not in the streamCache object!" << std::endl;
	}

	if (streamCache(sid)->_hist_dz.find(did.rawId()) != streamCache(sid)->_hist_dz.end()) {
	  streamCache(sid)->_hist_dz.at(did.rawId())->Fill(dzRes);
	} else {
	  std::cout << "[debug] WARNING : Did " << did << " is not in the streamCache object!" << std::endl;
	}

      }// if track reference is not null
    }// loop on tracks
  } // loop on vertices
}

void StreamPVValidation::streamEndRunSummary(edm::StreamID sid, edm::Run const& run, edm::EventSetup const& es, PVValidationStreamData* globalData) const {
  //Add the values seen in this Stream to the total for this Run
  globalData->add(streamCache(sid));
  streamCache(sid)->reset();
}

std::map<TString, double> StreamPVValidation::fitIP(TH1F* hist, TF1** peak_fit, bool debug) const {
  std::map<TString, double> returnMap = {{"gain_est",0.}, {"gain",0.}, {"dgain",0.}};
  std::vector<int> peak_bins;
  TSpectrum* spectrum = new TSpectrum(250);
  int npeaks = spectrum->Search(hist, 1., "", 0.02); // histogram, width, option, threshold (peaks lower than thresh*max are discarded)
  if (npeaks <= 1) {
    std::cerr << "[StreamPVValidation::fitIP] WARNING : npeaks=" << npeaks << " for hist " << hist->GetName() << ". hist integral = " << hist->Integral() << std::endl;
    return returnMap;
  }
  double *peak_x = spectrum->GetPositionX();
  for (int i_peak = 0; i_peak < npeaks; ++i_peak) {
    double this_x = peak_x[i_peak];
    peak_bins.push_back(hist->GetXaxis()->FindBin(this_x));
  }
  std::sort(peak_bins.begin(), peak_bins.end());
  if (debug) {
    std::cout << "[debug] Peak bins:" << std::endl;
    for (auto& it_bin : peak_bins) {
      std::cout << it_bin << " => " << hist->GetBinCenter(it_bin) << std::endl;
    }
  }
  
  double gain_est = hist->GetBinCenter(peak_bins[1]) - hist->GetBinCenter(peak_bins[0]);
  double peak0_mean_est = hist->GetBinCenter(peak_bins[0]);
  double peak1_mean_est = hist->GetBinCenter(peak_bins[1]);
  double peak2_mean_est = hist->GetBinCenter(peak_bins[2]);
  char fitname[100];
  sprintf(fitname, "peakfit_%s", hist->GetName());
  (*peak_fit) = new TF1(fitname, "gaus(0)+gaus(3)+gaus(6)", peak0_mean_est - gain_est / 3., peak2_mean_est + gain_est/3.);
  // Set initial parameters of fit
  // - par0 (constant) = integral (maybe should include the 2s and pis...)
  // - par1 (mean) = bin center of peak, limited to 0.6*gain_est to avoid fitting a neighboring peak
  // - par2 (sigma) = 5.
  (*peak_fit)->SetParameter(0, hist->Integral(hist->GetXaxis()->FindBin(peak0_mean_est - gain_est / 2.), hist->GetXaxis()->FindBin(peak0_mean_est + gain_est / 2.)));
  (*peak_fit)->SetParLimits(0, 0., 100.*hist->Integral(hist->GetXaxis()->FindBin(peak0_mean_est - gain_est / 2.), hist->GetXaxis()->FindBin(peak0_mean_est + gain_est / 2.)));
  (*peak_fit)->SetParameter(1, peak0_mean_est);
  (*peak_fit)->SetParLimits(1, peak0_mean_est - gain_est * 0.25, peak0_mean_est + gain_est * 0.25);
  (*peak_fit)->SetParameter(2, 5.);
  
  (*peak_fit)->SetParameter(3, hist->Integral(hist->GetXaxis()->FindBin(peak1_mean_est - gain_est / 2.), hist->GetXaxis()->FindBin(peak1_mean_est + gain_est / 2.)));
  (*peak_fit)->SetParLimits(3, 0., 100.*hist->Integral(hist->GetXaxis()->FindBin(peak1_mean_est - gain_est / 2.), hist->GetXaxis()->FindBin(peak1_mean_est + gain_est / 2.)));
  (*peak_fit)->SetParameter(4, peak1_mean_est);
  (*peak_fit)->SetParLimits(4, peak1_mean_est - gain_est * 0.25, peak1_mean_est + gain_est * 0.25);
  (*peak_fit)->SetParameter(5, 5.);
  
  (*peak_fit)->SetParameter(6, hist->Integral(hist->GetXaxis()->FindBin(peak2_mean_est - gain_est / 2.), hist->GetXaxis()->FindBin(peak2_mean_est + gain_est / 2.)));
  (*peak_fit)->SetParLimits(6, 0., 100.*hist->Integral(hist->GetXaxis()->FindBin(peak2_mean_est - gain_est / 2.), hist->GetXaxis()->FindBin(peak2_mean_est + gain_est / 2.)));
  (*peak_fit)->SetParameter(7, peak2_mean_est);
  (*peak_fit)->SetParLimits(7, peak2_mean_est - gain_est * 0.25, peak2_mean_est + gain_est * 0.25);
  (*peak_fit)->SetParameter(8, 5.);
  
  if (debug) {
    hist->Fit((*peak_fit), "R0");
  } else {
    hist->Fit((*peak_fit), "QR0");
  }
  
  double gain = (*peak_fit)->GetParameter(4) - (*peak_fit)->GetParameter(1);
  double dgain = TMath::Sqrt(TMath::Power((*peak_fit)->GetParError(1), 2) + TMath::Power((*peak_fit)->GetParError(4), 2));
  
  returnMap["gain_est"] = gain_est;
  returnMap["gain"]     = gain;
  returnMap["dgain"]    = dgain;
  returnMap["const1"] = (*peak_fit)->GetParameter(0);
  returnMap["const2"] = (*peak_fit)->GetParameter(3);
  returnMap["mean1"] = (*peak_fit)->GetParameter(1);
  returnMap["mean2"] = (*peak_fit)->GetParameter(4);
  returnMap["sigma1"] = (*peak_fit)->GetParameter(2);
  returnMap["sigma2"] = (*peak_fit)->GetParameter(5);
  delete spectrum;
  return returnMap;
}


//*************************************************************                                                                                                                                             
// Generic booker function                                                                                                                                                                                  
//*************************************************************                                                                                                                                             
HistogramMap StreamPVValidation::bookResidualsHistogram(unsigned int theNOfBins,
							TString resType,
							TString varType) const{
  TH1F::SetDefaultSumw2(kTRUE);
  
  Double_t up   =  500.;
  Double_t down = -500.;

  if(resType.Contains("norm")){
    up = up*0.01;
    down = down*0.01;
  }

  HistogramMap h;

  const char* auxResType = (resType.ReplaceAll("_","")).Data();

  for(unsigned int i=0; i<theNOfBins;i++){
    h.insert(std::pair<uint32_t,TH1F*>(i,new TH1F(Form("histo_%s_%s_plot%i",resType.Data(),varType.Data(),i),
						  Form("%s vs %s - bin %i;%s;tracks",auxResType,varType.Data(),i,auxResType),
						  1000,down,up)));  
  }
  return h;
}

void StreamPVValidation::globalEndRunSummary(edm::Run const& run, edm::EventSetup const& es, PVValidationStreamData* globalData) const {
  // Test: just print the map
  //std::cout << "[PVValidation::globalEndRunSummary] DEBUG : Printing results" << std::endl;
  int counter = 0;
  int max_histogram_counter = 0; 
  //for (auto& it : (globalData->_hist_fc)) {
  //	std::cout << "[StreamPVValidation::globalEndRunSummary] DEBUG : \t" << HcalDetId(it.first) << " => " << it.second << " , integral " << it.second->Integral() << std::endl; 
  //	//it.second->Print("all");
  //	++counter;
  //	if (counter > 10) break;
  //}
  
  // Do gain fits
  
  // Save all histograms
  _queue.pushAndWait([&]() {

      _fs->file().cd();

      std::cout << "[StreamPVValidation::globalEndRunSummary] DEBUG : \t" 
		<< globalData->_nevents << " have been processed \t" 
		<< globalData->_nvertices << " vertices and " 
		<< globalData->_ntracks   << " tracks in total"
		<< std::endl;

      auto h_dxy_phi_      = bookResidualsHistogram(nBins_,"dxy","phi");
      auto h_dz_phi_       = bookResidualsHistogram(nBins_,"dz","phi");
      auto h_dxy_eta_      = bookResidualsHistogram(nBins_,"dxy","eta");
      auto h_dz_eta_       = bookResidualsHistogram(nBins_,"dz","eta");

      std::string subdir_name = "run" + std::to_string(run.runAuxiliary().run());
      TDirectory* subdir = _fs->file().mkdir(subdir_name.c_str());
      subdir->cd();

      TDirectory* Residuals = subdir->mkdir("Residuals");
      Residuals->cd();

      for (auto& it : globalData->_hist_dxy) {
	TH1F* histdxy = it.second;
	TH1F* histdz  = globalData->_hist_dz.at(it.first);

	PhaseSpaceBin did(it.first);

	std::cout << std::endl << "[debug] *** Doing fit determination for channel " << did << " ***" << std::endl;

	histdxy->Write();
	histdz->Write();
      
	for(unsigned int iBin=0; iBin<nBins_;iBin++){
	  if(did.iphi()==iBin){
	    std::cout << "iPhi:" << iBin << std::endl;
	    h_dxy_phi_.at(iBin)->Add(histdxy);
	    h_dz_phi_.at(iBin)->Add(histdz);
	  }

	  if(did.ieta()==iBin){
	    std::cout << "iEta:" << iBin << std::endl;
	    h_dxy_eta_.at(iBin)->Add(histdxy);
	    h_dz_eta_.at(iBin)->Add(histdz);
	  }
	}
      }
      
      // book residuals vs phi histograms                                                                                     
      
      TDirectory* AbsTransPhiRes = _fs->file().mkdir("Abs_Transv_Phi_Residuals");
      AbsTransPhiRes->cd();
      for (auto& it : h_dxy_phi_) {
      	auto hist = it.second;
      	hist->Write();
      }

      TDirectory* AbsLongPhiRes = _fs->file().mkdir("Abs_Long_Phi_Residuals");
      AbsLongPhiRes->cd();
      for (auto& it : h_dz_phi_) {
      	auto hist = it.second;
      	hist->Write();
      }

      // book residuals vs eta histograms                                                                                     
 
      TDirectory* AbsTransEtaRes = _fs->file().mkdir("Abs_Transv_Eta_Residuals");
      AbsTransEtaRes->cd();

  
      for (auto& it : h_dxy_eta_) {
      	auto hist = it.second;
      	hist->Write();
      }

      TDirectory* AbsLongEtaRes  = _fs->file().mkdir("Abs_Long_Eta_Residuals");
      AbsLongEtaRes->cd();      
      for (auto& it : h_dz_eta_) {
      	auto hist = it.second;
      	hist->Write();
      }

      // fill the trend plots

      TDirectory* MeanTrendsDir   = _fs->file().mkdir("MeanTrends");
      TDirectory* WidthTrendsDir  = _fs->file().mkdir("WidthTrends");

      auto a_dxyPhiMeanTrend  = new TH1F("means_dxy_phi",
					 "#LT d_{xy} #GT vs #phi sector;track #varphi;#LT d_{xy} #GT [#mum]",
					 nBins_,phiLow_,phiHig_); 
  
      auto a_dxyPhiWidthTrend = new TH1F("widths_dxy_phi",
					 "#sigma_{d_{xy}} vs #phi sector;track #varphi;#sigma_{d_{xy}} [#mum]",
					 nBins_,phiLow_,phiHig_);

      auto a_dzPhiMeanTrend   = new TH1F ("means_dz_phi",
					  "#LT d_{z} #GT vs #phi sector;track #varphi;#LT d_{z} #GT [#mum]",
					  nBins_,phiLow_,phiHig_); 
      
      auto a_dzPhiWidthTrend  = new TH1F("widths_dz_phi",
					 "#sigma_{d_{z}} vs #phi sector;track #varphi;#sigma_{d_{z}} [#mum]",
					 nBins_,phiLow_,phiHig_);
      
      auto a_dxyEtaMeanTrend  = new TH1F ("means_dxy_eta",
					  "#LT d_{xy} #GT vs #eta sector;track #eta;#LT d_{xy} #GT [#mum]",
					  nBins_,etaLow_,etaHig_);

      auto a_dxyEtaWidthTrend = new TH1F("widths_dxy_eta",
					 "#sigma_{d_{xy}} vs #eta sector;track #eta;#sigma_{d_{xy}} [#mum]",
					 nBins_,etaLow_,etaHig_);
  
      auto a_dzEtaMeanTrend   = new TH1F ("means_dz_eta",
					  "#LT d_{z} #GT vs #eta sector;track #eta;#LT d_{z} #GT [#mum]",
					  nBins_,etaLow_,etaHig_); 
  
      auto a_dzEtaWidthTrend  = new TH1F("widths_dz_eta",
					 "#sigma_{d_{xy}} vs #eta sector;track #eta;#sigma_{d_{z}} [#mum]",
					 nBins_,etaLow_,etaHig_);

      fillTrendPlotByIndex(a_dxyPhiMeanTrend ,h_dxy_phi_,"mean");  
      fillTrendPlotByIndex(a_dxyPhiWidthTrend,h_dxy_phi_,"width");
      fillTrendPlotByIndex(a_dzPhiMeanTrend  ,h_dz_phi_,"mean");   
      fillTrendPlotByIndex(a_dzPhiWidthTrend ,h_dz_phi_,"width"); 

      fillTrendPlotByIndex(a_dxyEtaMeanTrend ,h_dxy_eta_,"mean");  
      fillTrendPlotByIndex(a_dxyEtaWidthTrend,h_dxy_eta_,"width");
      fillTrendPlotByIndex(a_dzEtaMeanTrend  ,h_dz_eta_,"mean");   
      fillTrendPlotByIndex(a_dzEtaWidthTrend ,h_dz_eta_,"width"); 

      MeanTrendsDir->cd();
      a_dxyPhiMeanTrend->Write();
      a_dzPhiMeanTrend->Write(); 
      a_dxyEtaMeanTrend->Write();
      a_dzEtaMeanTrend->Write();

      WidthTrendsDir->cd();
      a_dxyPhiWidthTrend->Write();
      a_dzPhiWidthTrend->Write();
      a_dxyEtaWidthTrend->Write();
      a_dzEtaWidthTrend->Write();

    });

  // // Bin width of 4 fC to avoid gaps
  //   hist->Rebin(4);
  //   if (counter < 100) {
  //     std::cout << "[debug] Fitting nominal histogram" << std::endl;
  //   }
  //   TF1* peak_fit = 0;
  //   std::map<TString, double> thisGain = fitIP(hist, &peak_fit, (counter<10));
    
  //   _gain_container.run      = run.runAuxiliary().run();
  //   _gain_container.nevents  = globalData->_nevents;
  //   _gain_container.subdet   = _subdet_to_string.at(did.subdet());
  //   _gain_container.ieta     = did.ieta();
  //   _gain_container.iphi     = did.iphi();
  //   _gain_container.depth    = did.depth();
  //   _gain_container.gain     = thisGain["gain"];
  //   _gain_container.gain_est = thisGain["gain_est"];
  //   _gain_container.dgain    = thisGain["dgain"];
  //   _gain_container.mean1    = thisGain["mean1"];
  //   _gain_container.mean2    = thisGain["mean2"];
    
  //   // Do fit for kernel-based histograms too
  //   TH1F* hist_kernel = globalData->_hist_fc_kernel.at(it.first);
  //   // Set the uncertainty in each bin to sqrt(contents)... maybe not rigorous, but at least this gets the total histogram Sumw2 correct...
  //   for (int bin = 0; bin <= hist_kernel->GetNbinsX() + 1; ++bin) {
  //     if (hist_kernel->GetBinContent(bin) > 0) {
  // 	hist_kernel->SetBinError(bin, TMath::Sqrt(hist_kernel->GetBinContent(bin)));
  //     }
  //   }
  //   if (counter < 100) {
  //     std::cout << "[debug] Fitting kernel histogram" << std::endl;
  //   }
  //   TF1* peak_fit_kernel = 0;		
  //   std::map<TString, double> thisGainKernel = fitIP(hist_kernel, &peak_fit_kernel);
  //   _gain_container.gain_kernel     = thisGainKernel["gain"];
  //   _gain_container.gain_est_kernel = thisGainKernel["gain_est"];
  //   _gain_container.dgain_kernel    = thisGainKernel["dgain"];
  //   _gain_container.mean1_kernel    = thisGainKernel["mean1"];
  //   _gain_container.mean2_kernel    = thisGainKernel["mean2"];
    
  //   if ((thisGain["gain"] < 30. || thisGainKernel["gain"] < 30. || counter < 100) && max_histogram_counter < 200) {
  //     char tmpname[100];
      
  //     sprintf(tmpname, "lowgainhist_%s", hist->GetName());
  //     hist->Write(tmpname);
      
  //     sprintf(tmpname, "lowgainhist_%s", hist_kernel->GetName());
  //     hist_kernel->Write(tmpname);
      
  //     sprintf(tmpname, "peak_fit_%s", hist_kernel->GetName());
  //     _fs->cd();
  //     if (peak_fit_kernel) {
  // 	peak_fit_kernel->Write(tmpname);
  //     }
      
  //     sprintf(tmpname, "peak_fit_%s", hist->GetName());
  //     _fs->cd();
  //     if (peak_fit) {
  // 	peak_fit->Write(tmpname);
  //     }
      
  //     ++max_histogram_counter;
  //   }
    
  //   if (thisGain["gain"] != 0 || thisGainKernel["gain"] != 0) {
  //     _fs->cd();
  //     _tree->Fill();
  //   }
    
  //   if (peak_fit) {
  //     delete peak_fit;
  //     peak_fit = 0;
  //   }
  //   if (peak_fit_kernel) {
  //     delete peak_fit_kernel;
  //     peak_fit_kernel = 0;
  //   }
    
}

//*************************************************************
void StreamPVValidation::fillTrendPlotByIndex(TH1F* trendPlot,HistogramMap& h, TString fitPar_) const
//*************************************************************
{  
  for(auto iterator = h.begin(); iterator != h.end(); iterator++) {
    
    unsigned int bin = (iterator->first)+1;
    std::pair<std::pair<Double_t,Double_t>, std::pair<Double_t,Double_t>  > myFit = fitResiduals(iterator->second);
    
    if(fitPar_=="mean"){
      float mean_      = myFit.first.first;
      float meanErr_   = myFit.first.second;
      trendPlot->SetBinContent(bin,mean_);
      trendPlot->SetBinError(bin,meanErr_);
    } else if (fitPar_=="width"){
      float width_     = myFit.second.first;
      float widthErr_  = myFit.second.second;
      trendPlot->SetBinContent(bin,width_);
      trendPlot->SetBinError(bin,widthErr_);
    } else if (fitPar_=="median"){
      float median_    = getMedian(iterator->second).first;
      float medianErr_ = getMedian(iterator->second).second;
      trendPlot->SetBinContent(bin,median_);
      trendPlot->SetBinError(bin,medianErr_);
    } else if (fitPar_=="mad"){
      float mad_       = getMAD(iterator->second).first; 
      float madErr_    = getMAD(iterator->second).second;
      trendPlot->SetBinContent(bin,mad_);
      trendPlot->SetBinError(bin,madErr_);
    } else {
      std::cout<<"PrimaryVertexValidation::fillTrendPlot() "<<fitPar_<<" unknown estimator!"<<std::endl;
    }
  }
}

//*************************************************************
std::pair<std::pair<Double_t,Double_t>, std::pair<Double_t,Double_t>  > StreamPVValidation::fitResiduals(TH1 *hist) const
//*************************************************************
{
  //float fitResult(9999);
  //if (hist->GetEntries() < 20) return ;
  
  float mean  = hist->GetMean();
  float sigma = hist->GetRMS();
  
  TF1 func("tmp", "gaus", mean - 1.5*sigma, mean + 1.5*sigma); 
  if (0 == hist->Fit(&func,"QNR")) { // N: do not blow up file by storing fit!
    mean  = func.GetParameter(1);
    sigma = func.GetParameter(2);
    // second fit: three sigma of first fit around mean of first fit
    func.SetRange(mean - 2*sigma, mean + 2*sigma);
      // I: integral gives more correct results if binning is too wide
      // L: Likelihood can treat empty bins correctly (if hist not weighted...)
    if (0 == hist->Fit(&func, "Q0LR")) {
      if (hist->GetFunction(func.GetName())) { // Take care that it is later on drawn:
	hist->GetFunction(func.GetName())->ResetBit(TF1::kNotDraw);
      }
    }
  }

  float res_mean  = func.GetParameter(1);
  float res_width = func.GetParameter(2);
  
  float res_mean_err  = func.GetParError(1);
  float res_width_err = func.GetParError(2);

  std::pair<Double_t,Double_t> resultM;
  std::pair<Double_t,Double_t> resultW;

  resultM = std::make_pair(res_mean,res_mean_err);
  resultW = std::make_pair(res_width,res_width_err);

  std::pair<std::pair<Double_t,Double_t>, std::pair<Double_t,Double_t>  > result;
  
  result = std::make_pair(resultM,resultW);
  return result;
}

//*************************************************************
std::pair<Double_t,Double_t> StreamPVValidation::getMedian(TH1 *histo) const
//*************************************************************
{
  Double_t median = 999;
  int nbins = histo->GetNbinsX();

  //extract median from histogram
  double *x = new double[nbins];
  double *y = new double[nbins];
  for (int j = 0; j < nbins; j++) {
    x[j] = histo->GetBinCenter(j+1);
    y[j] = histo->GetBinContent(j+1);
  }
  median = TMath::Median(nbins, x, y);
  
  delete[] x; x = 0;
  delete[] y; y = 0;  

  std::pair<Double_t,Double_t> result;
  result = std::make_pair(median,median/TMath::Sqrt(histo->GetEntries()));

  return result;

}

//*************************************************************
std::pair<Double_t,Double_t> StreamPVValidation::getMAD(TH1 *histo) const
//*************************************************************
{

  int nbins = histo->GetNbinsX();
  Double_t median = getMedian(histo).first;
  Double_t x_lastBin = histo->GetBinLowEdge(nbins+1);
  const char *HistoName =histo->GetName();
  TString Finalname = Form("resMed%s",HistoName);
  TH1F *newHisto = new TH1F(Finalname,Finalname,nbins,0.,x_lastBin);
  Double_t *residuals = new Double_t[nbins];
  Double_t *weights = new Double_t[nbins];

  for (int j = 0; j < nbins; j++) {
    residuals[j] = TMath::Abs(median - histo->GetBinCenter(j+1));
    weights[j]=histo->GetBinContent(j+1);
    newHisto->Fill(residuals[j],weights[j]);
  }
  
  Double_t theMAD = (getMedian(newHisto).first)*1.4826;
  
  delete[] residuals; residuals=0;
  delete[] weights; weights=0;
  newHisto->Delete("");
  
  std::pair<Double_t,Double_t> result;
  result = std::make_pair(theMAD,theMAD/histo->GetEntries());

  return result;

}


DEFINE_FWK_MODULE(StreamPVValidation);
