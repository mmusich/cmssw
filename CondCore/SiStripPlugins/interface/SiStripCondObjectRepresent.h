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

// needed for the tracker map
#include "CommonTools/TrackerMap/interface/TrackerMap.h"

//functions for correct representation of data in summary and plot
namespace SiStripCondObjectRepresent{

  enum plotType { STANDARD, COMPARISON, DIFF, RATIO, MAP, END_OF_TYPES };
  enum granularity { PERSTRIP, PERAPV, PERMODULE };

  template<class type>
  class SiStripCondDataItem {
  public:
    SiStripCondDataItem() {
      init();
    }

    virtual ~SiStripCondDataItem(){};
    
    void fillAll(unsigned int detid,const std::vector<type>& store){
      m_info[detid]=store;
      m_cached=true;
      return;
    }
    
    void fillByPushBack(unsigned int detid,const type& value){
      m_info[detid].push_back(value);
      m_cached=true;
    }

    void divide(unsigned int detid,const std::vector<type>& denominator){
      
      if(m_info[detid].size() != denominator.size()){
	throw cms::Exception ("Unaligned Conditions") << "data size of numerator mismatched the data size of denominator";
      }
  
      unsigned int counter=0;
      for (const auto &den : denominator){
	m_info[detid].at(counter)/=den;
	counter++;
      }
    }

    void subtract(unsigned int detid,const std::vector<type>& subtractor){
      
      if(m_info[detid].size() != subtractor.size()){
	throw cms::Exception ("Unaligned Conditions") << "data size of numerator mismatched the data size of denominator";
      }
  
      unsigned int counter=0;
      for (const auto &sub : subtractor){
	m_info[detid].at(counter)-=sub;
	counter++;
      }
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
    SiStripDataContainer(std::shared_ptr<Item> payload, unsigned int run, std::string hash) : payload_(payload), run_(run), hash_(hash),  m_trackerTopo(StandaloneTrackerTopology::fromTrackerParametersXMLFile(edm::FileInPath("Geometry/TrackerCommonData/data/trackerParameters.xml").fullPath()))
    {
      granularity_ = PERSTRIP;
      PlotMode_ = STANDARD;
      additionalIOV_ = std::make_pair(-1,"");
    }

    virtual ~SiStripDataContainer(){};

    ///////////////// public Get functions  /////////////////
    unsigned int getRun() {return run_;}   
    std::string getHash() {return hash_;}
    std::string getTopoMode() {return TopoMode_;}
    plotType    getPlotType() {return PlotMode_;}
    void        setPlotType(plotType myType) {PlotMode_ = myType;}
    void        setPayloadType(std::string myPayloadType){payloadType_ = myPayloadType;}
    void        setGranularity(granularity myGranularity){

      granularity_ = myGranularity;
      
      switch(myGranularity){
      case PERSTRIP:
	SiStripCondData_.setGranularity(true,false);
	break;
      case PERAPV:
	SiStripCondData_.setGranularity(false,true);
	break;
      case PERMODULE:
	SiStripCondData_.setGranularity(false,false);
	break;
      default: 
	edm::LogError("LogicError") << "Unknown granularity type: " << myGranularity; 	
      }
    }

    void        setAdditionalIOV(unsigned int run, std::string hash){ 
      additionalIOV_.first  = run;   
      additionalIOV_.second = hash;
    };


    ////NOTE to be implemented in PayloadInspector classes
    virtual void getAllValues(){throw cms::Exception ("Value definition not found") << "getValue definition not found for ";}; // << payload_->myname();};

    SiStripCondDataItem<type> getSiStripCondData() {return SiStripCondData_; }
    
    /***********************************************************************/
    const char* getPlotDescriptor()
    /***********************************************************************/
    {
      
      const char* thePlotType="";
      switch(PlotMode_){
      case STANDARD:
	thePlotType = Form("Display - IOV: %i",run_);
	break;
      case COMPARISON:
	thePlotType = "Display";
	break;
      case DIFF:
	thePlotType = Form("#Delta (%i-%i)",run_,additionalIOV_.first);
	break;
      case RATIO:
	thePlotType = Form("Ratio (%i/%i)",run_,additionalIOV_.first);
	break;
      case MAP:
	thePlotType = Form("TrackerMap - %s",hash_.c_str());
	break;
      case END_OF_TYPES:
	edm::LogError("LogicError") << "Unknown plot type: " << PlotMode_; 
	break;
      default:
	edm::LogError("LogicError") << "Unknown plot type: " << PlotMode_; 
	break;
      }

      return thePlotType;

    }

    // all methods needed for comparison of 2 IOVs

    /***********************************************************************/
    void Compare(SiStripDataContainer* dataCont2) 
    /***********************************************************************/
    {
      PlotMode_ = COMPARISON;
      dataCont2->setPlotType(COMPARISON);

      setAdditionalIOV(dataCont2->getRun(),dataCont2->getHash());

      if(! SiStripCondData_.isCached()) getAllValues();
      dataCont2->getAllValues();
      auto SiStripCondData2_ = dataCont2->getSiStripCondData();
      
      auto listOfDetIds = SiStripCondData_.getDetIds(false);
      for(const auto &detId: listOfDetIds ){
	auto entriesToAdd =  SiStripCondData2_.get(detId);
	for (const auto &entry : entriesToAdd){
	  SiStripCondData_.fillByPushBack(detId,entry);
	}
      }
    }


    /***********************************************************************/
    void Divide(SiStripDataContainer* dataCont2) 
    /***********************************************************************/
    {
      PlotMode_ = RATIO;
      dataCont2->setPlotType(RATIO);

      setAdditionalIOV(dataCont2->getRun(),dataCont2->getHash());

      if(! SiStripCondData_.isCached()) getAllValues();
      dataCont2->getAllValues();
      auto SiStripCondData2_ = dataCont2->getSiStripCondData();

      auto listOfDetIds = SiStripCondData_.getDetIds(false);
      for(const auto &detId: listOfDetIds ){
	SiStripCondData_.divide(detId,SiStripCondData2_.get(detId));
      }

    }

    /***********************************************************************/
    void Subtract(SiStripDataContainer* dataCont2) 
    /***********************************************************************/
    {
      PlotMode_ = DIFF;
      dataCont2->setPlotType(DIFF);

      setAdditionalIOV(dataCont2->getRun(),dataCont2->getHash());

      if(! SiStripCondData_.isCached()) getAllValues();
      dataCont2->getAllValues();
      auto SiStripCondData2_ = dataCont2->getSiStripCondData();

      auto listOfDetIds = SiStripCondData_.getDetIds(false);
      for(const auto &detId: listOfDetIds ){
	SiStripCondData_.subtract(detId,SiStripCondData2_.get(detId));
      }

    }


    /***********************************************************************/
    void printAll()
    /***********************************************************************/
    {
      if(! SiStripCondData_.isCached()) getAllValues();
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
    void fillTrackerMap(TrackerMap* &tmap, std::pair<float,float>& range, const SiStripPI::estimator& est,const int nsigmas_of_saturation)
    /***********************************************************************/
    {

      std::string titleMap; 
      if(PlotMode_!=DIFF && PlotMode_ !=RATIO){
	titleMap = "Tracker Map of "+payloadType_+" "+estimatorType(est)+" per module (payload : "+hash_+")";
      } else {
	titleMap = "Tracker Map of "+payloadType_+" "+Form("%s",getPlotDescriptor())+" "+estimatorType(est)+" per module";
      }

      tmap = new TrackerMap(payloadType_.c_str());
      tmap->setTitle(titleMap);
      tmap->setPalette(1);

      // storage of info
      std::map<unsigned int,float> info_per_detid;

      if(! SiStripCondData_.isCached()) getAllValues();
      auto listOfDetIds = SiStripCondData_.getDetIds(false);
      for(const auto &detId: listOfDetIds ){
	auto values = SiStripCondData_.get(detId);

	unsigned int nElements = values.size();
	double mean(0.),rms(0.),min(10000.), max(0.);
	
	for(const auto &value : values){
	  mean+=value;
	  rms+=value*value;
	  if(value<min) min=value;
	  if(value>max) max=value;
	}
	
	mean/=nElements;
	if((rms/nElements-mean*mean)>0.){
	  rms = sqrt(rms/nElements-mean*mean);
	} else {
	  rms=0.;
	}       

	switch(est){
	case SiStripPI::min:
	  info_per_detid[detId]=min;
	  break;
	case SiStripPI::max:
	  info_per_detid[detId]=max;
	  break;
	case SiStripPI::mean:
	  info_per_detid[detId]=mean;
	  break;
	case SiStripPI::rms:
	  info_per_detid[detId]=rms;
	  break;
	default:
	  edm::LogWarning("LogicError") << "Unknown estimator: " <<  est; 
	  break;
	}	
      }
      
      // loop on the map
      for (const auto &item : info_per_detid){
	tmap->fill(item.first,item.second);
      }
      
      range = SiStripPI::getTheRange(info_per_detid,nsigmas_of_saturation);
    }

    /***********************************************************************/
    void fillValuePlot(TCanvas &canvas,const SiStripPI::OpMode& op_mode_,int nbins,float min,float max)
    /***********************************************************************/
    {

      auto myMode = op_mode_;
      // check the consistency first

      if(granularity_ == PERAPV ){
	switch(op_mode_){
	case SiStripPI::STRIP_BASED:
	  edm::LogError("LogicError") <<" Cannot display average per "<< opType(op_mode_).c_str() << " in a conditions served per APV";
	  return;
	case SiStripPI::APV_BASED:
	  myMode = SiStripPI::STRIP_BASED;
	  break;
	default:
	  break;
	}
      } else if (granularity_ == PERMODULE) {
	if (op_mode_==SiStripPI::STRIP_BASED || op_mode_==SiStripPI::APV_BASED) {
	  edm::LogError("LogicError") <<" Cannot display average per "<< opType(op_mode_).c_str() << " in a conditions served per module";
	  return;
	}
      }
      
      SiStripPI::Monitor1D *f_mon = NULL;
      SiStripPI::Monitor1D *l_mon = NULL;

      f_mon = new SiStripPI::Monitor1D(myMode,
				       "first",
				       Form("#LT %s #GT per %s;#LT%s per %s#GT %s;n. %ss",
					    payloadType_.c_str(),opType(op_mode_).c_str(),payloadType_.c_str(),opType(op_mode_).c_str(),(units_[payloadType_]).c_str(),opType(op_mode_).c_str())
				       ,nbins,min,max);
      
      if(PlotMode_ == COMPARISON){
	l_mon = new SiStripPI::Monitor1D(myMode,
					 "last",
					 Form("#LT %s #GT per %s;#LT%s per %s#GT %s;n. %ss",
					      payloadType_.c_str(),opType(op_mode_).c_str(),payloadType_.c_str(),opType(op_mode_).c_str(),(units_[payloadType_]).c_str(),opType(op_mode_).c_str())
					 ,nbins,min,max);
	
      }
      
      // retrieve the data
      if(! SiStripCondData_.isCached()) getAllValues();
      auto listOfDetIds = SiStripCondData_.getDetIds(false);

      unsigned int prev_det=0, prev_apv=0;
      SiStripPI::Entry f_entryContainer;
      SiStripPI::Entry l_entryContainer;

      std::cout<<"mode:" << opType(myMode) << " granularity: "<< granularity_ 
	       <<" listOfDetIds.size(): "<< listOfDetIds.size() << std::endl;

      for(const auto &detId: listOfDetIds ){
	auto values = SiStripCondData_.get(detId);
	
	unsigned int istrip=0;
	for(const auto &value : values){
	  
	  bool flush = false;
	  switch(myMode) {
	  case (SiStripPI::APV_BASED):
	    flush = (prev_det != 0 && prev_apv != istrip/128);
	    break;
	  case (SiStripPI::MODULE_BASED):
	    flush = (prev_det != 0 && prev_det != detId);
	    break;
	  case (SiStripPI::STRIP_BASED):
	    flush = (istrip != 0);
	    break;
	  }
	  
	  if(flush){
	    f_mon->Fill(prev_apv,prev_det,f_entryContainer.mean());
	    f_entryContainer.reset();
	    
	    if( (PlotMode_== COMPARISON) && (istrip > values.size()/2)){
	      l_mon->Fill(prev_apv,prev_det,l_entryContainer.mean());
	      l_entryContainer.reset();
	    }

	  }

	  if( (PlotMode_== COMPARISON) && (istrip > values.size()/2) ){
	    l_entryContainer.add(value);
	  } else { 
	    f_entryContainer.add(value);
	  }

	  prev_apv = (istrip/128);
	  istrip++;
	}	
	prev_det = detId;
      }

      TH1F* h_first = (TH1F*)(f_mon->getHist()).Clone("h_first");
      h_first->SetStats(kFALSE);
      SiStripPI::makeNicePlotStyle(h_first);
      h_first->GetYaxis()->CenterTitle(true);
      h_first->GetXaxis()->CenterTitle(true);
      h_first->SetLineWidth(2);
      h_first->SetLineColor(kBlack);

      //=========================
      canvas.cd();
      canvas.SetBottomMargin(0.11);
      canvas.SetLeftMargin(0.13);
      canvas.SetRightMargin(0.05);
      //canvas.Modified();

      TLegend* legend = new TLegend(0.52,0.82,0.95,0.9);
      legend->SetTextSize(0.025);

      if(PlotMode_ != COMPARISON){
	float theMax = h_first->GetMaximum();
	h_first->SetMaximum(theMax*1.30);
	h_first->Draw();

	legend->AddEntry(h_first,Form("IOV: %i",run_),"L");

      } else {

	TH1F* h_last  = (TH1F*)(l_mon->getHist()).Clone("h_last");
	h_last->SetStats(kFALSE);
	SiStripPI::makeNicePlotStyle(h_last);
	h_last->GetYaxis()->CenterTitle(true);
	h_last->GetXaxis()->CenterTitle(true);
	h_last->SetLineWidth(2);
	h_last->SetLineColor(kBlue);

	std::cout << h_first->GetEntries() << " ---- "<< h_last->GetEntries() << std::endl;


	float theMax = (h_first->GetMaximum() > h_last->GetMaximum()) ? h_first->GetMaximum() : h_last->GetMaximum();

	h_first->SetMaximum(theMax*1.30);
	h_last->SetMaximum(theMax*1.30);

	h_first->Draw();
	h_last->Draw("same");

	legend->SetHeader(Form("%s comparison",payloadType_.c_str()),"C"); // option "C" allows to center the header
	legend->AddEntry(h_first,Form("IOV: %i",run_),"F");
	legend->AddEntry(h_last, Form("IOV: %i",(additionalIOV_.first)),"F");
      }

      legend->Draw("same");

    }
  
    /***********************************************************************/
    void fillSummary(TCanvas &canvas)
    /***********************************************************************/
    {
      if(! SiStripCondData_.isCached()) getAllValues();
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
      auto h1 = new TH1F("byRegion",Form("SiStrip %s average by partition;; average SiStrip %s",payloadType_.c_str(),payloadType_.c_str()),map.size(),0.,map.size());
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
      std::map<std::string,TH1F* > h_parts;
      std::map<std::string,TH1F* > h_parts2;

      std::map<std::string,int> colormap;
      std::map<std::string,int> markermap;
      colormap["TIB"] = kRed;       markermap["TIB"] = kFullCircle;           
      colormap["TOB"] = kGreen;	    markermap["TOB"] = kFullTriangleUp;
      colormap["TID"] = kBlack;	    markermap["TID"] = kFullSquare;
      colormap["TEC"] = kBlue; 	    markermap["TEC"] = kFullTriangleDown; 

      std::vector<std::string> parts = {"TEC","TOB","TIB","TID"};

      const char* device;
      switch(granularity_){
      case PERSTRIP:
	device = "strips";
	break;
      case PERAPV:
	device = "APVs";
	break;
      case PERMODULE:
	device = "modules";
	break;
      default:
	device = "unrecognized device";
	break;
      }

      for ( const auto &part : parts){

	TString globalTitle = Form("%s - %s %s;%s %s;n. %s",getPlotDescriptor(),payloadType_.c_str(),part.c_str(),payloadType_.c_str(),(units_[payloadType_]).c_str(),device);

	h_parts[part] = new TH1F(Form("h_%s",part.c_str()),globalTitle,nbins,min,max);
	
	if(PlotMode_ == COMPARISON){
	  h_parts2[part] = new TH1F(Form("h2_%s",part.c_str()),globalTitle,nbins,min,max);
	}
      }

      if(! SiStripCondData_.isCached()) getAllValues();
      auto listOfDetIds = SiStripCondData_.getDetIds(false);
      for(const auto &detId: listOfDetIds ){
	auto values = SiStripCondData_.get(detId);
	int subid = DetId(detId).subdetId();
	unsigned int counter=0;
	for(const auto &value : values){
	  counter++;
	  switch(subid){
	  case StripSubdetector::TIB:
	    if((PlotMode_ == COMPARISON) && (counter>(values.size()/2)) ){
	      h_parts2["TIB"]->Fill(value);
	    } else {
	      h_parts["TIB"]->Fill(value);
	    }
	    break;
	  case StripSubdetector::TID:
	    if((PlotMode_ == COMPARISON) && (counter>(values.size()/2))){
	      h_parts2["TID"]->Fill(value);
	    } else {
	      h_parts["TID"]->Fill(value);
	    }
	    break;
	  case StripSubdetector::TOB:
	    if((PlotMode_ == COMPARISON) && (counter>(values.size()/2))){
	      h_parts2["TOB"]->Fill(value);
	    } else {
	      h_parts["TOB"]->Fill(value);
	    }
	    break;
	  case StripSubdetector::TEC:
	    if((PlotMode_ == COMPARISON) && (counter>(values.size()/2))){
	      h_parts2["TEC"]->Fill(value);
	    } else {
	      h_parts["TEC"]->Fill(value);
	    }
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
	canvas.cd(index)->SetTopMargin(0.07);
	canvas.cd(index)->SetLeftMargin(0.13);
	canvas.cd(index)->SetRightMargin(0.08);
	
	SiStripPI::makeNicePlotStyle(h_parts[part]);
	h_parts[part]->SetMinimum(1.);
	h_parts[part]->SetStats(false);
	h_parts[part]->SetLineWidth(2);
	 
	if(PlotMode_ != COMPARISON){
	  h_parts[part]->SetLineColor(colormap[part]);
	  float theMax = h_parts[part]->GetMaximum();
	  h_parts[part]->SetMaximum(theMax*1.30);
	} else {
	  h_parts[part]->SetLineColor(kBlack);

	  SiStripPI::makeNicePlotStyle(h_parts2[part]);
	  h_parts2[part]->SetMinimum(1.);
	  h_parts2[part]->SetStats(false);
	  h_parts2[part]->SetLineWidth(2);
	  h_parts2[part]->SetLineColor(kBlue);

	  float theMax = (h_parts[part]->GetMaximum() > h_parts2[part]->GetMaximum()) ? h_parts[part]->GetMaximum() : h_parts2[part]->GetMaximum();

	  h_parts[part]->SetMaximum(theMax*1.30);
	  h_parts2[part]->SetMaximum(theMax*1.30);

	}

	h_parts[part]->Draw();
	if(PlotMode_ == COMPARISON){
	  h_parts2[part]->Draw("same");
	}

	TLegend* leg = new TLegend(.60,0.8,0.92,0.93);
	if(PlotMode_ != COMPARISON){
	  leg->SetTextSize(0.035);
	  leg->SetHeader(part.c_str(),"C"); // option "C" allows to center the header
	  leg->AddEntry(h_parts[part],Form("#splitline{#mu = %.2f}{r.m.s. = %.2f}",h_parts[part]->GetMean(),h_parts[part]->GetRMS()),"L");
	  leg->Draw("same");
	} else {
	  leg->AddEntry(h_parts[part],Form("IOV: %i",run_),"L");
	  leg->AddEntry(h_parts2[part],Form("IOV: %i",(additionalIOV_.first)),"L");
	  leg->Draw("same");
	}
      } 
    }

  protected:
    std::shared_ptr<Item> payload_;
    std::string payloadType_;
    SiStripCondDataItem<type> SiStripCondData_;     

  private:
    unsigned int run_;
    std::string hash_;
    granularity granularity_;
    std::string TopoMode_;
    TrackerTopology m_trackerTopo;
    SiStripDetSummary summary{&m_trackerTopo};
    // "Map", "Ratio", or "Diff"
    plotType PlotMode_;
    std::pair<int,std::string> additionalIOV_;

    std::map<std::string, std::string> units_ = {
      { "SiStripPedestals", "[ADC counts]" },
      { "SiStripApvGain",  ""},//dimensionless TODO: verify
      { "SiStripNoises" , "[ADC counts]"},
      { "SiStripLorentzAngle" , "[rad]"},
      { "SiStripBackPlaneCorrection" , ""},
      { "SiStripBadStrip" , ""},
      { "SiStripDetVOff" , ""}
    };

    std::string opType(SiStripPI::OpMode mode) {
      std::string types[3] = {"Strip","APV","Module"};
      return types[mode];
    }

  };

}

#endif
