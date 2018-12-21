#include "Alignment/StreamPVValidation/interface/StreamPVValidation.h"
#include "FWCore/Framework/interface/ConstProductRegistry.h"
#include "FWCore/Framework/interface/ProductSelector.h"
#include "FWCore/Framework/interface/ProductSelectorRules.h"
#include "DataFormats/Provenance/interface/SelectedProducts.h"
#include "Math/LorentzVector.h"
#include "Math/Vector3D.h"

#include <map>
#include "boost/foreach.hpp"
#include <TBranch.h>
#include <TLorentzVector.h>

StreamPVValidation::StreamPVValidation(const edm::ParameterSet& ps) {
  _tagHE = ps.getUntrackedParameter<edm::InputTag>("tagHE", edm::InputTag("hcalDigis"));
  _tokHE = consumes<QIE11DigiCollection>(_tagHE);	
  _subdet_to_string[HcalBarrel]  = "HB";
  _subdet_to_string[HcalEndcap]  = "HE";
  _subdet_to_string[HcalForward] = "HF";
  _subdet_to_string[HcalOuter]   = "HO";
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
  edm::ESHandle<HcalDbService> dbs;
  es.get<HcalDbRecord>().get(dbs);
  const HcalElectronicsMap * emap = dbs->getHcalMapping();
  
  for (auto& it_gdid : emap->allPrecisionId()) {
    if (!it_gdid.isHcalDetId()) {
      continue;
    }
    HcalDetId did(it_gdid.rawId());
    if (did.subdet() == HcalEndcap) {
      char hname[50];
      sprintf(hname, "h_fc_HE_ieta%d_iphi%d_depth%d_run%d", did.ieta(), did.iphi(), did.depth(), run.runAuxiliary().run());
      returnValue->_hist_fc.insert(std::pair<uint32_t, TH1F*>(did.rawId(), new TH1F(hname, hname, 500, 0., 500.)));
      
      sprintf(hname, "h_fc_kernel_HE_ieta%d_iphi%d_depth%d_run%d", did.ieta(), did.iphi(), did.depth(), run.runAuxiliary().run());
      returnValue->_hist_fc_kernel.insert(std::pair<uint32_t, TH1F*>(did.rawId(), new TH1F(hname, hname, 500, 0., 500.)));
      
      sprintf(hname, "h_adc_HE_ieta%d_iphi%d_depth%d_run%d", did.ieta(), did.iphi(), did.depth(), run.runAuxiliary().run());
      returnValue->_hist_adc.insert(std::pair<uint32_t, TH1F*>(did.rawId(), new TH1F(hname, hname, 256, -0.5, 255.5)));
    }
  }
  
  // SumW2 all histograms
  for (auto& it : returnValue->_hist_fc) {
    it.second->Sumw2();
	}
  for (auto& it : returnValue->_hist_fc_kernel) {
    it.second->Sumw2();
  }
  for (auto& it : returnValue->_hist_adc) {
    it.second->Sumw2();
  }
  
  return returnValue;
}

void StreamPVValidation::streamBeginRun(edm::StreamID sid, edm::Run const& run, edm::EventSetup const& es) const {
  // Book stream histograms and TF1
  edm::ESHandle<HcalDbService> dbs;
  es.get<HcalDbRecord>().get(dbs);
  const HcalElectronicsMap * emap = dbs->getHcalMapping();
  
  for (auto& it_gdid : emap->allPrecisionId()) {
    if (!it_gdid.isHcalDetId()) {
      continue;
    }
    HcalDetId did(it_gdid.rawId());
    if (did.subdet() == HcalEndcap) {
      char hname[50];
      sprintf(hname, "h_fc_HE_ieta%d_iphi%d_depth%d_run%d", did.ieta(), did.iphi(), did.depth(), run.runAuxiliary().run());
      streamCache(sid)->_hist_fc.insert(std::pair<uint32_t, TH1F*>(did.rawId(), new TH1F(hname, hname, 500, 0., 500.)));
      
      sprintf(hname, "h_fc_kernel_HE_ieta%d_iphi%d_depth%d_run%d", did.ieta(), did.iphi(), did.depth(), run.runAuxiliary().run());
      streamCache(sid)->_hist_fc_kernel.insert(std::pair<uint32_t, TH1F*>(did.rawId(), new TH1F(hname, hname, 500, 0., 500.)));
      
      sprintf(hname, "h_adc_HE_ieta%d_iphi%d_depth%d_run%d", did.ieta(), did.iphi(), did.depth(), run.runAuxiliary().run());
      streamCache(sid)->_hist_adc.insert(std::pair<uint32_t, TH1F*>(did.rawId(), new TH1F(hname, hname, 256, -0.5, 255.5)));
    }
  }
  char fname[50];
  sprintf(fname, "gaus_%d", sid.value());
  streamCache(sid)->_fgaus = new TF1(fname, "gaus", 0., 500.);
  
  streamCache(sid)->_nevents = 0;
  
  // Sumw2 all histograms
  for (auto& it : streamCache(sid)->_hist_fc) {
    it.second->Sumw2();
  }
  for (auto& it : streamCache(sid)->_hist_fc_kernel) {
    it.second->Sumw2();
  }
  for (auto& it : streamCache(sid)->_hist_adc) {
    it.second->Sumw2();
  }
  
}

void StreamPVValidation::beginJob() {
  _tree = _fs->make<TTree>("gains", "gains");
  _tree->Branch("run", &(_gain_container.run));
  _tree->Branch("nevents", &(_gain_container.nevents));
  _tree->Branch("subdet", &(_gain_container.subdet));
  _tree->Branch("ieta", &(_gain_container.ieta));
  _tree->Branch("iphi", &(_gain_container.iphi));
  _tree->Branch("depth", &(_gain_container.depth));
  _tree->Branch("gain", &(_gain_container.gain));
  _tree->Branch("gain_est", &(_gain_container.gain_est));
  _tree->Branch("dgain", &(_gain_container.dgain));
  _tree->Branch("mean1", &(_gain_container.mean1));
  _tree->Branch("mean2", &(_gain_container.mean2));
  
  _tree->Branch("gain_kernel", &(_gain_container.gain_kernel));
  _tree->Branch("gain_est_kernel", &(_gain_container.gain_est_kernel));
  _tree->Branch("dgain_kernel", &(_gain_container.dgain_kernel));
  _tree->Branch("mean1_kernel", &(_gain_container.mean1_kernel));
  _tree->Branch("mean2_kernel", &(_gain_container.mean2_kernel));
}

void StreamPVValidation::analyze(edm::StreamID sid, const edm::Event& event, const edm::EventSetup& es) const {
  streamCache(sid)->_nevents += 1;
  
  // Load digis
  edm::Handle<QIE11DigiCollection> che_qie11;
  if (!event.getByToken(_tokHE, che_qie11)) {
    std::cout << "Collection QIE11DigiCollection isn't available" << _tagHE.label() << " " << _tagHE.instance() << std::endl;
    exit(1);
  }
  
  edm::ESHandle<HcalDbService> dbs;
  es.get<HcalDbRecord>().get(dbs);
  
  for (QIE11DigiCollection::const_iterator it=che_qie11->begin(); it!=che_qie11->end();
       ++it)
    {
      const QIE11DataFrame digi = static_cast<const QIE11DataFrame>(*it);
      HcalDetId const& did = digi.detid();
      if (did.subdet() != HcalEndcap) {
	continue;
      }
      //CaloSamples digi_fC = hcaldqm::utilities::loadADC2fCDB<QIE11DataFrame>(dbs, did, digi);
      double sumq = 0.;
      double dsumq2 = 0.;
      for (int i=0; i<digi.samples(); i++) {
	//double q = hcaldqm::utilities::adc2fCDBMinusPedestal<QIE11DataFrame>(dbs, digi_fC, did, digi, i); // This is pedestal subtracted, don't want
	//double q = digi_fC[i]; // Database apparently doesn't have GSel0?
	double q = adc2fC[digi[i].adc()];
	double delta_q = 0.;
	if (digi[i].adc() == 0) {
	  delta_q = adc2fC[digi[i].adc()] / 2.;
	} else if (digi[i].adc() == 255) {
	  delta_q = (adc2fC[digi[i].adc()] - adc2fC[digi[i].adc() - 1]) / 2.;
	} else {
	  delta_q = (adc2fC[digi[i].adc() + 1] - adc2fC[digi[i].adc() - 1]) / 2.;
	}
	delta_q = delta_q / TMath::Sqrt(12);
	sumq += q;
	dsumq2 += TMath::Power(delta_q, 2);
	if (streamCache(sid)->_hist_adc.find(did.rawId()) != streamCache(sid)->_hist_adc.end()) {
	  streamCache(sid)->_hist_adc.at(did.rawId())->Fill(digi[i].adc());
	} else {
	  //std::cout << "[debug] WARNING : Did " << did << " is not in the streamCache object!" << std::endl;
	}
	
      }
      double dsumq = TMath::Sqrt(dsumq2);
      
      // For high-charge events, print the pulse shape
      //if (sumq > 100) {
      //std::cout << "[StreamPVValidation::analyze] INFO : Printing high-charge pulse ADC => q" << std::endl;
      //for (int i = 0; i < digi.samples(); ++i) {
      //	std::cout << "[StreamPVValidation::analyze] INFO : \t" << digi[i].adc() << "\t=>\t" << digi_fC[i] << std::endl;
      //}
      //}
      if (streamCache(sid)->_hist_fc.find(did.rawId()) != streamCache(sid)->_hist_fc.end()) {
	streamCache(sid)->_hist_fc.at(did.rawId())->Fill(sumq);
      }
      ChannelHistogramMap::iterator it_hist_fc_kernel = streamCache(sid)->_hist_fc_kernel.find(did.rawId());
      TF1* fgaus = streamCache(sid)->_fgaus;
      if (it_hist_fc_kernel != streamCache(sid)->_hist_fc_kernel.end()) {
	TH1F* this_hist_fc_kernel = it_hist_fc_kernel->second;
	//std::cout << "[debug] Making gaussian with width " << dsumq << " / mean " << sumq << " / constant " << 1. / TMath::Sqrt(2*TMath::Pi()*dsumq*dsumq) << std::endl;
	fgaus->SetParameter(1, sumq);
	fgaus->SetParameter(2, dsumq);
	fgaus->SetParameter(0, 1. / TMath::Sqrt(2*TMath::Pi()*dsumq*dsumq));
	for (int bin = 1; bin <= this_hist_fc_kernel->GetNbinsX(); ++bin) {
	  this_hist_fc_kernel->Fill(this_hist_fc_kernel->GetXaxis()->GetBinCenter(bin), fgaus->Integral(this_hist_fc_kernel->GetXaxis()->GetBinLowEdge(bin), this_hist_fc_kernel->GetXaxis()->GetBinUpEdge(bin)));
	}
      }
    }
}

void StreamPVValidation::streamEndRunSummary(edm::StreamID sid, edm::Run const& run, edm::EventSetup const& es, PVValidationStreamData* globalData) const {
  //Add the values seen in this Stream to the total for this Run
  globalData->add(streamCache(sid));
  streamCache(sid)->reset();
}

std::map<TString, double> StreamPVValidation::fitGain(TH1F* hist, TF1** peak_fit, bool debug) const {
  std::map<TString, double> returnMap = {{"gain_est",0.}, {"gain",0.}, {"dgain",0.}};
  std::vector<int> peak_bins;
  TSpectrum* spectrum = new TSpectrum(250);
  int npeaks = spectrum->Search(hist, 1., "", 0.02); // histogram, width, option, threshold (peaks lower than thresh*max are discarded)
  if (npeaks <= 1) {
    std::cerr << "[StreamPVValidation::fitGain] WARNING : npeaks=" << npeaks << " for hist " << hist->GetName() << ". hist integral = " << hist->Integral() << std::endl;
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
  
  for (auto& it : globalData->_hist_fc) {
    HcalDetId did(it.first);
    TH1F* hist = it.second;
    
    // Write out a few histograms
    if (hist->Integral() > 0 && counter < 100) {
      _fs->cd();
      hist->Write();
      globalData->_hist_fc_kernel.at(it.first)->Write();
      globalData->_hist_adc.at(it.first)->Write();
    }

    // Skip histograms with low integral. 
    if (hist->Integral() < 100) {
      ++counter;
      continue;
    }
    if (counter < 100) {
      std::cout << std::endl << "[debug] *** Doing gain determination for channel " << did << " ***" << std::endl;
    }
    
    
    // Bin width of 4 fC to avoid gaps
    hist->Rebin(4);
    if (counter < 100) {
      std::cout << "[debug] Fitting nominal histogram" << std::endl;
    }
    TF1* peak_fit = 0;
    std::map<TString, double> thisGain = fitGain(hist, &peak_fit, (counter<10));
    
    _gain_container.run      = run.runAuxiliary().run();
    _gain_container.nevents  = globalData->_nevents;
    _gain_container.subdet   = _subdet_to_string.at(did.subdet());
    _gain_container.ieta     = did.ieta();
    _gain_container.iphi     = did.iphi();
    _gain_container.depth    = did.depth();
    _gain_container.gain     = thisGain["gain"];
    _gain_container.gain_est = thisGain["gain_est"];
    _gain_container.dgain    = thisGain["dgain"];
    _gain_container.mean1    = thisGain["mean1"];
    _gain_container.mean2    = thisGain["mean2"];
    
    // Do fit for kernel-based histograms too
    TH1F* hist_kernel = globalData->_hist_fc_kernel.at(it.first);
    // Set the uncertainty in each bin to sqrt(contents)... maybe not rigorous, but at least this gets the total histogram Sumw2 correct...
    for (int bin = 0; bin <= hist_kernel->GetNbinsX() + 1; ++bin) {
      if (hist_kernel->GetBinContent(bin) > 0) {
	hist_kernel->SetBinError(bin, TMath::Sqrt(hist_kernel->GetBinContent(bin)));
      }
    }
    if (counter < 100) {
      std::cout << "[debug] Fitting kernel histogram" << std::endl;
    }
    TF1* peak_fit_kernel = 0;		
    std::map<TString, double> thisGainKernel = fitGain(hist_kernel, &peak_fit_kernel);
    _gain_container.gain_kernel     = thisGainKernel["gain"];
    _gain_container.gain_est_kernel = thisGainKernel["gain_est"];
    _gain_container.dgain_kernel    = thisGainKernel["dgain"];
    _gain_container.mean1_kernel    = thisGainKernel["mean1"];
    _gain_container.mean2_kernel    = thisGainKernel["mean2"];
    
    if ((thisGain["gain"] < 30. || thisGainKernel["gain"] < 30. || counter < 100) && max_histogram_counter < 200) {
      char tmpname[100];
      
      sprintf(tmpname, "lowgainhist_%s", hist->GetName());
      hist->Write(tmpname);
      
      sprintf(tmpname, "lowgainhist_%s", hist_kernel->GetName());
      hist_kernel->Write(tmpname);
      
      sprintf(tmpname, "peak_fit_%s", hist_kernel->GetName());
      _fs->cd();
      if (peak_fit_kernel) {
	peak_fit_kernel->Write(tmpname);
      }
      
      sprintf(tmpname, "peak_fit_%s", hist->GetName());
      _fs->cd();
      if (peak_fit) {
	peak_fit->Write(tmpname);
      }
      
      ++max_histogram_counter;
    }
    
    if (thisGain["gain"] != 0 || thisGainKernel["gain"] != 0) {
      _fs->cd();
      _tree->Fill();
    }
    
    if (peak_fit) {
      delete peak_fit;
      peak_fit = 0;
    }
    if (peak_fit_kernel) {
      delete peak_fit_kernel;
      peak_fit_kernel = 0;
    }
    
    ++counter;
  }
}
