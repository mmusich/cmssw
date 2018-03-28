#include "TROOT.h"
#include "TFile.h"
#include "TCanvas.h"
#include "TH1F.h"
#include "TTree.h"
#include "TBranch.h"
#include "TTree.h"
#include "TChain.h"

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <iostream>
#include <iomanip>      // std::setw

enum TrackerRegion { 
  TIB1  = 1,
  TIB2  = 2,
  TIB3  = 3,
  TIB4  = 4,
  TOB1  = 5,
  TOB2  = 6,
  TOB3  = 7,
  TOB4  = 8,
  TOB5  = 9,
  TOB6  = 10,
  TIDP1 = 11,
  TIDP2 = 12,
  TIDP3 = 13,
  TIDM1 = 14,
  TIDM2 = 15,
  TIDM3 = 16,
  TECP1 = 17,
  TECP2 = 18,
  TECP3 = 19,
  TECP4 = 20,
  TECP5 = 21,
  TECP6 = 22,
  TECP7 = 23,
  TECP8 = 24,
  TECP9 = 25,
  TECM1 = 26,
  TECM2 = 27,
  TECM3 = 28,
  TECM4 = 29,
  TECM5 = 30,
  TECM6 = 31,
  TECM7 = 32,
  TECM8 = 33,
  TECM9 = 34,
  END_OF_REGIONS = 35	
};

TrackerRegion getTheRegionFromTopology(int subdet,int side,int layer){
  int ret(-99);
  switch(subdet){
  case 3: 
    // this is TIB
    ret=layer;
    break;
  case 4:
    // this is TID
    ret = side==1 ? 10+std::abs(layer) : 13+std::abs(layer);
    break;
  case 5:
    // this is TOB 
    ret = layer+4;
    break;
  case 6:
    // this is TEC
    ret = side==1 ? 16+std::abs(layer) : 25+std::abs(layer);
    break;
  default:
    std::cout<<"shall never ever be here!" << std::endl;
    break;
  }
  return static_cast<TrackerRegion>(ret);
}


/*--------------------------------------------------------------------*/
const char * regionType(int index)
/*--------------------------------------------------------------------*/
{  
  auto region = static_cast<std::underlying_type_t<TrackerRegion> >(index);

  switch(region){
  case TIB1: return "TIB L1";
  case TIB2: return "TIB L2";
  case TIB3: return "TIB L3";
  case TIB4: return "TIB L4";
  case TOB1: return "TOB L1";
  case TOB2: return "TOB L2";
  case TOB3: return "TOB L3";
  case TOB4: return "TOB L4";
  case TOB5: return "TOB L5";
  case TOB6: return "TOB L6";
  case TIDP1: return "TID+ D1";
  case TIDP2: return "TID+ D2";
  case TIDP3: return "TID+ D3"; 
  case TIDM1: return "TID- D1";
  case TIDM2: return "TID- D2";
  case TIDM3: return "TID- D3"; 
  case TECP1: return "TEC+ D1";
  case TECP2: return "TEC+ D2";
  case TECP3: return "TEC+ D3";
  case TECP4: return "TEC+ D4";
  case TECP5: return "TEC+ D5";
  case TECP6: return "TEC+ D6";
  case TECP7: return "TEC+ D7";
  case TECP8: return "TEC+ D8";
  case TECP9: return "TEC+ D9";
  case TECM1: return "TEC- D1";
  case TECM2: return "TEC- D2";
  case TECM3: return "TEC- D3";
  case TECM4: return "TEC- D4";
  case TECM5: return "TEC- D5";
  case TECM6: return "TEC- D6";
  case TECM7: return "TEC- D7";
  case TECM8: return "TEC- D8";
  case TECM9: return "TEC- D9";
  case END_OF_REGIONS : return "undefined";
  default : return "should never be here";  
  }
}

void readNSiStripDBTrees(TString fname){
  TChain* tree_ = new TChain("treeDump/StripDBTree"); 
  tree_->Add(fname);

  uint32_t detId_, ring_, istrip_, det_type_; 
  Int_t layer_, side_,subdetId_;
  float noise_, gsim_, g1_, g2_, lenght_; 
  bool isTIB_, isTOB_, isTEC_, isTID_, isBad_; 

  std::map<int, TH1F*> idealNoiseRatioPerLayer;
  std::map<int, TH1F*> NoisePerLayer;
  std::map<int, TH1F*> g1PerLayer;

  tree_->SetBranchAddress("detId"   , &detId_    );
  tree_->SetBranchAddress("detType" , &det_type_ );
  tree_->SetBranchAddress("noise"   , &noise_    ); 
  tree_->SetBranchAddress("istrip"  , &istrip_   );
  tree_->SetBranchAddress("gsim"    , &gsim_     ); 
  tree_->SetBranchAddress("g1"      , &g1_       ); 
  tree_->SetBranchAddress("g2"      , &g2_       ); 
  tree_->SetBranchAddress("layer"   , &layer_    ); 
  tree_->SetBranchAddress("side"    , &side_     ); 
  tree_->SetBranchAddress("subdetId", &subdetId_ ); 
  tree_->SetBranchAddress("ring"    , &ring_     ); 
  tree_->SetBranchAddress("length"  , &lenght_   ); 
  tree_->SetBranchAddress("isBad"   , &isBad_    ); 
  tree_->SetBranchAddress("isTIB"   , &isTIB_    ); 
  tree_->SetBranchAddress("isTOB"   , &isTOB_    ); 
  tree_->SetBranchAddress("isTEC"   , &isTEC_    ); 
  tree_->SetBranchAddress("isTID"   , &isTID_    ); 

  int nentries = tree_->GetEntries();
  std::cout << "Number of entries = " << nentries << std::endl;

  TH1F* h_idealNoiseRatioPerLayer = new TH1F("h_IdealNoise", "Ideal Noise;Ideal Noise ratio;n. strips",500,0.,10.);
  TH1F* h_NoisePerLayer           = new TH1F("h_Noise", "Noise;Noise;n. strips",500,0.,10.);
  TH1F* h_g1PerLayer              = new TH1F("h_g1", "g1 gain;g1 gain;n. strips",200,0.,2.);

  for(int region = TrackerRegion::TIB1; region != TrackerRegion::END_OF_REGIONS; region++ ){
    auto tag = regionType(region);
    std::cout<< "booking region: " << std::setw(3) << region << " -> " << tag << std::endl;
    idealNoiseRatioPerLayer[region] = new TH1F(Form("IdealNoise_%s",tag), Form("Ideal Noise %s;Ideal Noise ratio for %s;n. strips",tag,tag),500,0.,10.);
    NoisePerLayer[region]           = new TH1F(Form("Noise_%s",tag), Form("Noise %s;Noise for %s;n. strips",tag,tag),500,0.,10.);
    g1PerLayer[region]              = new TH1F(Form("g1_%s",tag), Form("g1 %s;g1 for %s;n. strips",tag,tag),200,0.,2.);
  }

  uint32_t cachedDetId=-1;
  for (Int_t stripNo=0; stripNo < nentries; stripNo++){
    Int_t IgetStrip = tree_-> GetEntry(stripNo);  
    auto region =  getTheRegionFromTopology(subdetId_,side_,layer_);

    h_idealNoiseRatioPerLayer->Fill(noise_/g1_); 
    h_NoisePerLayer->Fill(noise_);           
    h_g1PerLayer->Fill(g1_);              

    idealNoiseRatioPerLayer[region]->Fill(noise_/g1_);
    NoisePerLayer[region]->Fill(noise_);
    g1PerLayer[region]->Fill(g1_);
    //std::cout << " strip n."<< stripNo << " detId:"<< detId_ << " strip n.: "<< istrip_ << std::endl;
    if(detId_!=cachedDetId){
      std::cout << " strip n."<< stripNo << " detId:"<< detId_ << " strip n.: "<< istrip_ 
		<< " subdet: " << subdetId_ <<" side: "<< side_ << " layer: "<< layer_ << " (region: " << region << ") =>  " << regionType(region) << std::endl;
      cachedDetId=detId_;
    }
  }

  TFile* outfile = TFile::Open("idealNoise.root","RECREATE");
  outfile->cd();
  h_idealNoiseRatioPerLayer->Write();
  h_NoisePerLayer->Write();          
  h_g1PerLayer->Write();             

  TDirectory *cdIdealNoise = outfile->mkdir("idealNoise");
  cdIdealNoise->cd(); 
  for(int region = TrackerRegion::TIB1; region != TrackerRegion::END_OF_REGIONS; region++ ){
    auto tag = regionType(region);
    idealNoiseRatioPerLayer[region]->Write();
  }

  outfile->cd();
  TDirectory *cdNoise = outfile->mkdir("Noise");
  cdNoise->cd(); 
  for(int region = TrackerRegion::TIB1; region != TrackerRegion::END_OF_REGIONS; region++ ){
    auto tag = regionType(region);
    NoisePerLayer[region]->Write();
  }

  outfile->cd();
  TDirectory *cdG1 = outfile->mkdir("g1");
  cdG1->cd(); 
  for(int region = TrackerRegion::TIB1; region != TrackerRegion::END_OF_REGIONS; region++ ){
    auto tag = regionType(region);
    g1PerLayer[region]->Write();
  }
  
  outfile -> Close();  
  tree_ -> Delete();
  return;
}

