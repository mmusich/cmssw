#include "TFile.h"
#include "TKey.h"
#include "TH1.h"
#include "TH2.h"
#include "TLatex.h"
#include "TDirectory.h"
#include "TObject.h"
#include <iostream>
#include "TLegend.h"
#include "TClass.h"
#include "TRatioPlot.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TGaxis.h"
#include <vector>

std::vector<TFile*> sourceFiles;
Int_t def_colors[9]  = {kBlack,kBlue,kRed,kMagenta,kGreen,kCyan,kViolet,kOrange,kGreen+2};
Int_t def_markers[9] = {kFullCross,kFullSquare,kFullCircle,kOpenSquare,kOpenCircle,kFullTriangleDown,kFullTriangleUp,kOpenTriangleDown,kOpenTriangleDown};

std::pair<Double_t,Double_t> getExtrema(TObjArray *array);
template<typename T> void MakeNicePlotStyle(T *hist);

//void MakeNicePlotStyle(TH1 *hist);
void plotHistograms(std::vector<TH1*>, const std::vector<TString>& labels,bool isNormalized);
void recurseOverKeys( TDirectory *target1, const std::vector<TString>& labels,bool isNorm);
void cmsPrel(TPad* pad,size_t ipads=1);

/*--------------------------------------------------------------------*/
void cmsPrel(TPad* pad,size_t ipads) {
/*--------------------------------------------------------------------*/
  
  float H = pad->GetWh();
  float W = pad->GetWw();
  float l = pad->GetLeftMargin();
  float t = pad->GetTopMargin();
  float r = pad->GetRightMargin();
  float b = pad->GetBottomMargin();
  float relPosX = 0.009;
  float relPosY = 0.045;
  float lumiTextOffset = 0.8;

  TLatex *latex = new TLatex();
  latex->SetNDC();
  latex->SetTextSize(0.045);

  float posX_    = 1-(r/ipads)-0.02;
  float posY_    = 1-t - 0.03; /// - relPosY*(1-t-b);
  float factor   = 1./0.82;

  latex->SetTextAlign(33);
  latex->SetTextSize(0.045);
  latex->SetTextFont(42); //22
  latex->DrawLatex(posX_,posY_,"Internal (13 TeV)");

  UInt_t w;
  UInt_t h;
  latex->GetTextExtent(w,h,"Internal (13 TeV)");
  float size = w/(W/ipads);
  //std::cout<<w<<" "<<" "<<W<<" "<<size<<std::endl;
  float posXCMS_ = posX_- size*(1+0.025*ipads);

  latex->SetTextAlign(33);
  latex->SetTextFont(61);
  latex->SetTextSize(0.045*factor);
  latex->DrawLatex(posXCMS_,posY_+0.004,"CMS");

  //latex->DrawLatex(posX_,posY_,"CMS Preliminary (13 TeV)");
  //latex->DrawLatex(posX_,posY_,"CMS 2017 Work in progress (13 TeV)");
  
}

/************************************************/
void multi_loopAndPlot(TString namesandlabels,bool doNormalize=false)
/************************************************/
{

  std::vector<TString> labels;

  namesandlabels.Remove(TString::kTrailing, ',');
  TObjArray *nameandlabelpairs = namesandlabels.Tokenize(",");
  for (Int_t i = 0; i < nameandlabelpairs->GetEntries(); ++i) {
    TObjArray *aFileLegPair = TString(nameandlabelpairs->At(i)->GetName()).Tokenize("=");
    if(aFileLegPair->GetEntries() == 2) {
      sourceFiles.push_back(TFile::Open(aFileLegPair->At(0)->GetName(),"READ")); 
      TObjString* s_label = (TObjString*)aFileLegPair->At(1);
      labels.push_back(s_label->String());
    }
    else {
      std::cout << "Please give file name and legend entry in the following form:\n" 
		<< " filename1=legendentry1,filename2=legendentry2\n";
    }    
  }
  
  recurseOverKeys(sourceFiles[0],labels,doNormalize);

  for(const auto &file : sourceFiles){
    file->Close();
  } 

}


/************************************************/
void recurseOverKeys(TDirectory *target1,const std::vector<TString>& labels,bool isNorm) 
/************************************************/
{
  // Figure out where we are
  TString path( (char*)strstr( target1->GetPath(), ":" ) );
  path.Remove( 0, 2 );

  //TString path = "DQMData/Run 1/SiStrip/Run summary/Mechanical view/";

  sourceFiles[0]->cd( path );
  
  std::cout<<path<<std::endl;
  
  TDirectory *current_sourcedir = gDirectory;

  TKey *key;
  TIter nextkey(current_sourcedir->GetListOfKeys());

  while ( (key = (TKey*)nextkey()) ) {

    auto obj = key->ReadObj();

    // Check if this is a 1D histogram or a directory
    if (obj->IsA()->InheritsFrom("TH1")) {

      if (obj->IsA()->InheritsFrom("TH2")) continue;
      if ( (TString(obj->GetName())).Contains("_per_LumiBlock")) continue; 

      // **************************
      // Plot & Save this Histogram
      std::vector<TH1*> histos;

      TH1* htemp1 = (TH1*)obj;
      TString histName = htemp1->GetName();

      for(const auto &file : sourceFiles){
	TH1* htemp;
	if (path != "") {
	  file->GetObject(path+"/"+histName, htemp);
	} else {
	  file->GetObject(histName, htemp);
	}
	histos.push_back(htemp);
      }

      //outputFilename=histName;
      //plot2Histograms(htemp1, htemp2, outputFolder+path+"/"+outputFilename+"."+imageType);
      plotHistograms(histos,labels,isNorm);
      
    } else if ( obj->IsA()->InheritsFrom( "TDirectory" ) ) {
      // it's a subdirectory

      cout << "Found subdirectory " << obj->GetName() <<" " << ((TDirectory*)(obj))->GetPath() << endl;
      //gSystem->MakeDirectory(outputFolder+path+"/"+obj->GetName());

      // obj is now the starting point of another round of merging
      // obj still knows its depth within the target file via
      // GetPath(), so we can still figure out where we are in the recursion

      if(TString(((TDirectory*)(obj))->GetPath()).Contains("Residuals") ){
	continue;
      } else {
	recurseOverKeys( (TDirectory*)obj ,labels,isNorm);
      }
    
    } // end of IF a TDriectory 
  }
}

/************************************************/
void plotHistograms(std::vector<TH1*> histos, const std::vector<TString>& labels, bool isNormalized) {
/************************************************/

  TGaxis::SetMaxDigits(3);

  auto c1 = new TCanvas(Form("c1_%s",histos[0]->GetName()), "A ratio example",1000,800);
  c1->SetTicks(0, 1);
  gStyle->SetOptStat(0);

  TObjArray *array = new TObjArray(histos.size()); 
  int index=0;
  for(const auto &histo : histos){
    MakeNicePlotStyle<TH1>(histo);

    if(isNormalized){
      if(histo->Integral()>0.){
	Double_t scale = 1./histo->Integral();
	histo->Scale(scale);
      }
    }
    
    histo->SetLineColor(def_colors[index]);
    histo->SetMarkerColor(def_colors[index]);
    histo->SetMarkerStyle(def_markers[index]);
    histo->SetMarkerSize(1.5);
    array->Add(histo);
    index++;
  }

  std::pair<Double_t,Double_t> extrema =  getExtrema(array);
  delete array;
  float min = (extrema.first>0) ? (extrema.first)*0.7 : (extrema.first)*1.3;
  histos[0]->GetYaxis()->SetRangeUser(min,extrema.second*1.3);
  
  TRatioPlot* rp;

  for(unsigned int i=1;i<histos.size();i++){

    if(i==1){
      rp  = new TRatioPlot(histos[0],histos[i]);
      rp->SetLeftMargin(0.15); 
      rp->SetRightMargin(0.05);
      rp->SetSeparationMargin(0.01);
      rp->SetLowBottomMargin(0.35); 
      rp->Draw("");
    } else {
      rp->GetUpperPad()->cd();
      histos[i]->Draw("PE1same");
    }
  }

  rp->GetUpperPad()->cd();
  // if( ((TString)(histos[0]->GetName())).Contains("seedCharge") ){
  //  gPad->SetLogy();
  // }
  // Draw the legend
  TLegend *infoBox = new TLegend(0.15,0.75,0.60,0.90, "");
  infoBox->SetShadowColor(0);  // 0 = transparent
  infoBox->SetFillColor(kWhite); 
  infoBox->SetTextSize(0.04);

  for(unsigned int i=0;i<histos.size();i++){
    
    TString mean = histos[i]->GetMean() < 1000 ? Form("%.1f",histos[i]->GetMean()) : Form("%.1fk",histos[i]->GetMean()/1000.);
    TString rms  = histos[i]->GetRMS()  < 1000 ? Form("%.1f",histos[i]->GetRMS())  : Form("%.1fk",histos[i]->GetRMS()/1000.);

    if(i==0){
      infoBox->AddEntry(histos[i],labels[i]+Form(" #mu: %s, rms: %s",mean.Data(),rms.Data()),"L");
    } else {
      infoBox->AddEntry(histos[i],labels[i]+Form(" #mu: %s, rms: %s",mean.Data(),rms.Data()),"P");
    }
  }
  infoBox->Draw("same");
  
  auto current_pad = static_cast<TPad*>(gPad);
  cmsPrel(current_pad);

  MakeNicePlotStyle<TGraph>(rp->GetLowerRefGraph());
  rp->GetLowerRefGraph()->GetYaxis()->SetTitle("ratio");
  rp->GetLowerRefGraph()->SetMinimum(0.);
  rp->GetLowerRefGraph()->SetMaximum(2.);
  rp->GetLowerRefGraph()->SetLineColor(def_colors[0]);
  rp->GetLowerRefGraph()->SetMarkerColor(def_colors[0]);
  rp->GetLowerRefGraph()->SetMarkerStyle(def_markers[0]);
  rp->GetLowerRefGraph()->SetMarkerSize(1.5);
  //c1->Update();
  
  for(unsigned int i=1;i<histos.size();i++){
    auto c2 = new TCanvas(Form("c2_%s_%i",histos[i]->GetName(),i), "A ratio example 2",800,800);
    c2->cd();
    auto rp2 = new TRatioPlot(histos[0],histos[i]);
    rp2->Draw();
    TGraph *g = rp2->GetLowerRefGraph();
    // if(g) 
    MakeNicePlotStyle<TGraph>(g);
    g->SetLineColor(def_colors[i]);
    g->SetMarkerColor(def_colors[i]);
    g->SetMarkerStyle(def_markers[i]);
    g->SetMarkerSize(1.5);

    c1->cd();
    rp->GetLowerPad()->cd();
    if(g) g->Draw("Psame");
    c1->Update();
    delete c2;
  }

  //rp->GetLowerPad()->cd();
  //c1->Update();
  
  c1->SaveAs(TString(histos[0]->GetName())+".png");
  delete c1;
}

/*--------------------------------------------------------------------*/
template<typename T>
void MakeNicePlotStyle(T *hist)
/*--------------------------------------------------------------------*/
{ 

  gStyle->SetTitleX(0.7);
  gStyle->SetTitleAlign(23); 
  gStyle->SetTitleSize(0.1);

  //hist->SetStats(kFALSE);  
  hist->SetLineWidth(2);
  hist->GetXaxis()->SetNdivisions(505);
  hist->GetXaxis()->CenterTitle(true);
  hist->GetYaxis()->CenterTitle(true);
  hist->GetXaxis()->SetTitleFont(42); 
  hist->GetYaxis()->SetTitleFont(42);  
  hist->GetXaxis()->SetTitleSize(0.05);
  hist->GetYaxis()->SetTitleSize(0.05);
  hist->GetXaxis()->SetTitleOffset(0.9);
  hist->GetYaxis()->SetTitleOffset(1.4);
  hist->GetXaxis()->SetLabelFont(42);
  hist->GetYaxis()->SetLabelFont(42);
  if( ((TObject*)hist)->IsA()->InheritsFrom("TGraph") ){
    hist->GetYaxis()->SetLabelSize(.025);
    //hist->GetYaxis()->SetNdivisions(505);
  } else {
    hist->GetYaxis()->SetLabelSize(.05);
    ((TH1*)hist)->SetTitleFont(42);  
    ((TH1*)hist)->SetTitle(TString(hist->GetTitle()).ReplaceAll("Summary","").ReplaceAll("_"," "));  
  }
  hist->GetXaxis()->SetLabelSize(.05);
}

//*****************************************************//
std::pair<Double_t,Double_t> getExtrema(TObjArray *array)
//*****************************************************//
{
  Double_t theMaximum = (static_cast<TH1*>(array->At(0)))->GetMaximum();
  Double_t theMinimum = (static_cast<TH1*>(array->At(0)))->GetMinimum();
  for(Int_t i = 0; i< array->GetSize(); i++){
    if( (static_cast<TH1*>(array->At(i)))->GetMaximum() > theMaximum){
      theMaximum = (static_cast<TH1*>(array->At(i)))->GetMaximum();
    }
    if ( (static_cast<TH1*>(array->At(i)))->GetMinimum() < theMinimum){
      theMinimum = (static_cast<TH1*>(array->At(i)))->GetMinimum();
    }
  }
  return std::make_pair(theMinimum,theMaximum);
}
