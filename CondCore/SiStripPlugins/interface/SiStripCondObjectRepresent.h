#ifndef CondCore_SiStripPlugins_SiStripCondObjectRepresent_h
#define CondCore_SiStripPlugins_SiStripCondObjectRepresent_h 

#include "FWCore/Utilities/interface/Exception.h"
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include "TH1F.h"
#include "TH2F.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "TROOT.h"
#include "TCanvas.h"
#include "TLegend.h"
#include "TStyle.h"
#include "TColor.h"
#include "TLine.h"
#include "TLatex.h"
#include "TProfile.h"
#include "TPaveLabel.h"
#include "CalibTracker/StandaloneTrackerTopology/interface/StandaloneTrackerTopology.h"

//functions for correct representation of data in summary and plot
namespace SiStripCondObjectRepresent{

  template<class type>
  class SiStripCondDataItem {
  public:
    SiStripCondDataItem() {
      init();
    }

    virtual ~SiStripCondDataItem(){};
    
    void fillAll(unsigned int detid,std::vector<type> store){
      m_info[detid]=store;
      m_cached=true;
      return;
    }
    
    void fillByPushBack(unsigned int detid,type value){
      m_info[detid].push_back(value);
      m_cached=true;
    }

    std::vector<type> get(unsigned int detid){
      return m_info[detid];
    }

    void setGranularity(bool isPerStrip,bool isPerAPV){
      m_servedPerStrip=isPerStrip;
      m_servedPerAPV=isPerAPV;      
    }

    bool isCached(){
      return m_cached;
    }

    std::vector<unsigned int> getDetIds(bool verbose){

      std::vector<unsigned int> v;
      for(const auto & element : m_info){
	if(verbose){
	  std::cout<<element.first << "\n";
	}
	v.push_back(element.first);
      }

      return v;
    }

  private:
    std::map<unsigned int,std::vector<type> > m_info;
    bool m_servedPerStrip;
    bool m_servedPerAPV;
    bool m_cached;

    void init(){
      m_servedPerStrip=false;
      m_servedPerAPV=false;
      m_info.clear();
      m_cached=false;
    }

  };

  //used to produce all display objects for payload inspector
  template<class Item,class type>
  class SiStripDataContainer {

  public : 
    SiStripDataContainer(std::shared_ptr<Item> payload, unsigned int run, std::string hash,bool perStrip,bool perAPV) : payload_(payload), run_(run), hash_(hash), isPerStrip_(perStrip), isPerAPV_(perAPV), m_trackerTopo(StandaloneTrackerTopology::fromTrackerParametersXMLFile(edm::FileInPath("Geometry/TrackerCommonData/data/trackerParameters.xml").fullPath()))
    {
      PlotMode_ = "Map";
      SiStripCondData_.setGranularity(isPerStrip_,isPerAPV_);
    }

    virtual ~SiStripDataContainer(){};

    ///////////////// public Get functions  /////////////////
    unsigned int getRun() {return run_;}   
    std::string getHash() {return hash_;}
    std::string getTopoMode() {return TopoMode_;}

    SiStripCondDataItem<type> SiStripCondData_; 

    ////NOTE to be implemented in PayloadInspector classes
    virtual void getAllValues(std::shared_ptr<Item> payload){throw cms::Exception ("Value definition not found") << "getValue definition not found for ";}; // << payload_->myname();};


    /***********************************************************************/
    void printAll()
    /***********************************************************************/
    {
      getAllValues(payload_);
      auto listOfDetIds = SiStripCondData_.getDetIds(false);
      for(const auto &detId: listOfDetIds ){
	std::cout<< detId << ": ";
	auto values = SiStripCondData_.get(detId);
	for(const auto &value : values){
	  std::cout << value << " ";
	}
	std::cout<<"\n";
      }
    }

    /***********************************************************************/
    void fillSummary(TCanvas &canvas)
    /***********************************************************************/
    {
      if(! SiStripCondData_.isCached()) getAllValues(payload_);
      auto listOfDetIds = SiStripCondData_.getDetIds(false);
      for(const auto &detId: listOfDetIds ){
	auto values = SiStripCondData_.get(detId);
	for(const auto &value : values){
	  summary.add(detId,value);
	}
      }

      std::map<unsigned int, SiStripDetSummary::Values> map = summary.getCounts();
      //=========================
      
      canvas.cd();
      auto h1 = new TH1F("byRegion","SiStrip average by partition;; average SiStrip",map.size(),0.,map.size());
      h1->SetStats(false);
      canvas.SetBottomMargin(0.18);
      canvas.SetLeftMargin(0.17);
      canvas.SetRightMargin(0.05);
      canvas.Modified();

      std::vector<int> boundaries;
      unsigned int iBin=0;

      std::string detector;
      std::string currentDetector;

      for (const auto &element : map){
	iBin++;
	int count   = element.second.count;
	double mean = (element.second.mean)/count;

	if(currentDetector.empty()) currentDetector="TIB";
	
	switch ((element.first)/1000) 
	  {
	  case 1:
	    detector = "TIB";
	    break;
	  case 2:
	    detector = "TOB";
	    break;
	  case 3:
	    detector = "TEC";
	    break;
	  case 4:
	    detector = "TID";
	    break;
	  }

	h1->SetBinContent(iBin,mean);
	h1->GetXaxis()->SetBinLabel(iBin,SiStripPI::regionType(element.first).second);
	h1->GetXaxis()->LabelsOption("v");
	
	if(detector!=currentDetector) {
	  boundaries.push_back(iBin);
	  currentDetector=detector;
	}
      }

      h1->GetYaxis()->SetRangeUser(0.,h1->GetMaximum()*1.30);
      h1->SetMarkerStyle(20);
      h1->SetMarkerSize(1);
      h1->Draw("HIST");
      h1->Draw("Psame");
	    
      canvas.Update();
      
      TLine* l[boundaries.size()];
      unsigned int i=0;
      for (const auto & line : boundaries){
	l[i] = new TLine(h1->GetBinLowEdge(line),canvas.GetUymin(),h1->GetBinLowEdge(line),canvas.GetUymax());
	l[i]->SetLineWidth(1);
	l[i]->SetLineStyle(9);
	l[i]->SetLineColor(2);
	l[i]->Draw("same");
	i++;
      }
      
      TLegend* legend = new TLegend(0.52,0.82,0.95,0.9);
      legend->SetHeader(hash_.c_str(),"C"); // option "C" allows to center the header
      legend->AddEntry(h1,Form("IOV: %i",run_),"PL");
      legend->SetTextSize(0.025);
      legend->Draw("same");

    }
  
    /***********************************************************************/
    void fillByPartition(TCanvas &canvas,int nbins,float min,float max)
    /***********************************************************************/
    {
      std::map<std::string,TH1F*> h_parts;
      std::map<std::string,int> colormap;
      std::map<std::string,int> markermap;
      colormap["TIB"] = kRed;       markermap["TIB"] = kFullCircle;           
      colormap["TOB"] = kGreen;	    markermap["TOB"] = kFullTriangleUp;
      colormap["TID"] = kBlack;	    markermap["TID"] = kFullSquare;
      colormap["TEC"] = kBlue; 	    markermap["TEC"] = kFullTriangleDown; 

      std::vector<std::string> parts = {"TEC","TOB","TIB","TID"};
      
      for ( const auto &part : parts){
	h_parts[part] = new TH1F(Form("h_%s",part.c_str()),Form("IOV: %i",run_),nbins,min,max);
      }

      if(! SiStripCondData_.isCached()) getAllValues(payload_);
      auto listOfDetIds = SiStripCondData_.getDetIds(false);
      for(const auto &detId: listOfDetIds ){
	auto values = SiStripCondData_.get(detId);
	int subid = DetId(detId).subdetId();
	for(const auto &value : values){
	  
	  switch(subid){
	  case StripSubdetector::TIB:
	    h_parts["TIB"]->Fill(value);
	    break;
	  case StripSubdetector::TID:
	    h_parts["TID"]->Fill(value);
	    break;
	  case StripSubdetector::TOB:
	    h_parts["TOB"]->Fill(value);
	    break;
	  case StripSubdetector::TEC:
	    h_parts["TEC"]->Fill(value);
	    break;
	  default:
	    edm::LogError("LogicError") << "Unknown partition: " << subid; 
	    break;
	  }

	}
      }

      canvas.Divide(2,2);
      
      int index=0;
      for (const auto &part : parts){
	index++;
	canvas.cd(index)->SetTopMargin(0.05);
	canvas.cd(index)->SetLeftMargin(0.13);
	canvas.cd(index)->SetRightMargin(0.08);

	SiStripPI::makeNicePlotStyle(h_parts[part]);
	h_parts[part]->SetMinimum(1.);
	h_parts[part]->SetStats(false);
	h_parts[part]->SetLineWidth(2);
	h_parts[part]->SetLineColor(colormap[part]);
	h_parts[part]->Draw();
      }
    }
    

  private:
    std::shared_ptr<Item> payload_;
    unsigned int run_;
    std::string hash_;
    bool isPerStrip_;
    bool isPerAPV_;
    std::string TopoMode_;
    TrackerTopology m_trackerTopo;
    SiStripDetSummary summary{&m_trackerTopo};
    // "Map", "Ratio", or "Diff"
    std::string PlotMode_;
   
    std::map<std::string, std::string> units_ = {
      { "SiStripPedestals", "ADC counts" },
      { "SiStripApVGain",  ""},//dimensionless TODO: verify
      { "SiStripNoises" , "ADC counts"},
      { "SiStripLorentzAngle" , "rad"},
      { "SiStripBackPlaneCorrection" , ""},
      { "SiStripBadStrip" , ""},
      
    };
  };

}

#endif
