/*!
  \file SiPixelQulity_PayloadInspector
  \Payload Inspector Plugin for SiPixelQuality
  \author M. Musich
  \version $Revision: 1.0 $
  \date $Date: 2018/10/18 14:48:00 $
*/

#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "CondCore/Utilities/interface/PayloadInspectorModule.h"
#include "CondCore/Utilities/interface/PayloadInspector.h"
#include "CondCore/CondDB/interface/Time.h"
#include "FWCore/ParameterSet/interface/FileInPath.h"
#include "CalibTracker/StandaloneTrackerTopology/interface/StandaloneTrackerTopology.h"

// the data format of the condition to be inspected
#include "CondFormats/SiPixelObjects/interface/SiPixelQuality.h"
#include "DataFormats/SiPixelDetId/interface/PixelSubdetector.h"
#include "DataFormats/DetId/interface/DetId.h"

#include <memory>
#include <sstream>
#include <iostream>

// include ROOT 
#include "TH2F.h"
#include "TLegend.h"
#include "TCanvas.h"
#include "TLine.h"
#include "TGraph.h"
#include "TStyle.h"
#include "TLatex.h"
#include "TPave.h"
#include "TPaveStats.h"

namespace {

  /************************************************
    test class
  *************************************************/

  class SiPixelQualityTest : public cond::payloadInspector::Histogram1D<SiPixelQuality> {
    
  public:
    SiPixelQualityTest() : cond::payloadInspector::Histogram1D<SiPixelQuality>("SiPixelQuality test",
									       "SiPixelQuality test", 10,0.0,10.0){
      Base::setSingleIov( true );
    }
    
    bool fill( const std::vector<std::tuple<cond::Time_t,cond::Hash> >& iovs ) override{
      for ( auto const & iov: iovs) {
	std::shared_ptr<SiPixelQuality> payload = Base::fetchPayload( std::get<1>(iov) );
	if( payload.get() ){
	 
	  fillWithValue(1.);
	 
	  auto theDisabledModules = payload->getBadComponentList();
	  for (const auto &mod : theDisabledModules){
	    int BadRocCount(0);
	    for (unsigned short n = 0; n < 16; n++){
	      unsigned short mask = 1 << n;  // 1 << n = 2^{n} using bitwise shift
	      if (mod.BadRocs & mask) BadRocCount++;
	    }
	    std::cout<<"detId:" <<  mod.DetID << " error type:" << mod.errorType << " BadRocs:"  << BadRocCount <<  std::endl;
	  }
	}// payload
      }// iovs
      return true;
    }// fill
  };
  
  /************************************************
    summary class
  *************************************************/

  class SiPixelQualityBadRocsSummary : public cond::payloadInspector::PlotImage<SiPixelQuality> {

  public:
    SiPixelQualityBadRocsSummary() : cond::payloadInspector::PlotImage<SiPixelQuality>("SiPixel Quality Summary"){
      setSingleIov( false );
    }

    bool fill( const std::vector<std::tuple<cond::Time_t,cond::Hash> >& iovs ) override{

      std::vector<std::tuple<cond::Time_t,cond::Hash> > sorted_iovs = iovs;

      for(const auto &iov: iovs){
	std::shared_ptr<SiPixelQuality> payload = fetchPayload( std::get<1>(iov) );
	auto unpacked = unpack(std::get<0>(iov));

	std::cout<<"======================= " << unpacked.first <<" : "<< unpacked.second  << std::endl;
	auto theDisabledModules = payload->getBadComponentList();
	  for (const auto &mod : theDisabledModules){
	    std::cout<<"detId: " <<  mod.DetID << " |error type: " << mod.errorType << " |BadRocs: "  <<  mod.BadRocs <<  std::endl;
	  }
      }

      //=========================
      TCanvas canvas("Partion summary","partition summary",1200,1000);
      canvas.cd();
      canvas.SetBottomMargin(0.11);
      canvas.SetLeftMargin(0.13);
      canvas.SetRightMargin(0.05);
      canvas.Modified();

      std::string fileName(m_imageFileName);
      canvas.SaveAs(fileName.c_str());

      return true;

    }

    std::pair<unsigned int,unsigned int> unpack(cond::Time_t since){
      auto kLowMask = 0XFFFFFFFF;
      auto run  = (since >> 32);
      auto lumi = (since & kLowMask);
      return std::make_pair(run,lumi);
    }

  };

  /************************************************
    time history class
  *************************************************/

  class SiPixelQualityBadRocsTimeHistory : public cond::payloadInspector::TimeHistoryPlot<SiPixelQuality,std::pair<double,double> > {
    
  public:
    SiPixelQualityBadRocsTimeHistory() : cond::payloadInspector::TimeHistoryPlot<SiPixelQuality,std::pair<double,double> >("bad ROCs count vs time","bad ROCs count"){}

    std::pair<double,double> getFromPayload(SiPixelQuality& payload ) override{
      return std::make_pair(extractBadRocCount(payload),0.);
    }

    unsigned int extractBadRocCount(SiPixelQuality& payload){
      unsigned int BadRocCount(0);
      auto theDisabledModules = payload.getBadComponentList();
      for (const auto &mod : theDisabledModules){
	for (unsigned short n = 0; n < 16; n++){
	  unsigned short mask = 1 << n;  // 1 << n = 2^{n} using bitwise shift
	  if (mod.BadRocs & mask) BadRocCount++;
	}
      }
      return BadRocCount;
    }
  };

  /************************************************
   occupancy style map
  *************************************************/
 
  class SiPixelQualityMap : public cond::payloadInspector::PlotImage<SiPixelQuality> {
  public:
    SiPixelQualityMap () : cond::payloadInspector::PlotImage<SiPixelQuality>("SiPixelQuality Map"),
			   m_trackerTopo{StandaloneTrackerTopology::fromTrackerParametersXMLFile(edm::FileInPath("Geometry/TrackerCommonData/data/PhaseI/trackerParameters.xml").fullPath())}
    {
      setSingleIov( true );
    }

    bool fill( const std::vector<std::tuple<cond::Time_t,cond::Hash> >& iovs ) override{
      auto iov = iovs.front();
      std::shared_ptr<SiPixelQuality> payload = fetchPayload( std::get<1>(iov));

      static const int n_layers = 4;
      int nlad_list[n_layers] = {6, 14, 22, 32};
      int divide_roc = 1;

      // ---------------------    BOOK HISTOGRAMS                                                                        
      std::array<TH2D*,n_layers> h_bpix_occ;

      for(unsigned int lay=1;lay<=4;lay++){
	int nlad = nlad_list[lay-1];

	std::string name = "occ_Layer_"+std::to_string(lay);
	std::string title = "; Module # ; Ladder #";
	h_bpix_occ[lay-1] = new TH2D(name.c_str(), title.c_str(),
				     72*divide_roc,-4.5,4.5,
				     (nlad*4+2)*divide_roc,-nlad-0.5,nlad+0.5);
      }
      
      auto theDisabledModules = payload->getBadComponentList();
      for (const auto &mod : theDisabledModules){
	int coded_badRocs = mod.BadRocs;
	if(payload->IsModuleBad(mod.DetID)){
	  int subid = DetId(mod.DetID).subdetId();
	  if(subid==PixelSubdetector::PixelBarrel){
	    auto layer  = m_trackerTopo.pxbLayer(DetId(mod.DetID));
	    auto ladder = m_trackerTopo.pxbLadder(DetId(mod.DetID));
	    auto module = m_trackerTopo.pxbModule(DetId(mod.DetID));
	    std::cout << layer << " " << ladder << " " << module << std::endl;

	    std::vector<std::pair<int,int> > rocsToMask = maskedBarrelRocsToBins(layer,ladder,module);
	    for(const auto& bin : rocsToMask ){
	      h_bpix_occ[layer-1]->SetBinContent(bin.first,bin.second,1);
	    }
	  }
	}
	std::bitset<16> bad_rocs(coded_badRocs);	  
      }
   
      gStyle->SetOptStat(0);
      //=========================
      TCanvas canvas("Summary","Summary",1200,1200);
      canvas.Divide(2,2);
      canvas.SetBottomMargin(0.11);
      canvas.SetLeftMargin(0.13);
      canvas.SetRightMargin(0.05);
      canvas.Modified();
  
      for(unsigned int lay=1;lay<=4;lay++){
	dress_occ_plot_bpix(canvas,h_bpix_occ[lay-1],lay);
      }

      std::string fileName(m_imageFileName);
      canvas.SaveAs(fileName.c_str());

      return true;

    }

    // #============================================================================     
    std::vector<std::pair<int,int> > maskedBarrelRocsToBins(int layer, int ladder, int module){

      std::vector<std::pair<int,int> > rocsToMask;

      int nlad_list[4] = {6, 14, 22, 32};
      int nlad = nlad_list[layer-1];

      int start_x = module<=4 ? ((module-1)*8)+1 : ((module-1)*8)+9;
      int start_y = ladder<nlad/2 ? ((ladder-1)*2)+1 : ((ladder-1)*2)+3 ;
      int end_x   = start_y+8;
      int end_y   = start_y+1;

      for(int bin_x=1;bin_x<=72;bin_x++){
	for(int bin_y=1;bin_y<= (nlad*4+2);bin_y++){
	  if(bin_x >= start_x && bin_x<=end_x && bin_y >= start_y && bin_y <=end_y){
	    rocsToMask.push_back(std::make_pair(bin_x,bin_y));
	  }
	}
      }
      
      return rocsToMask;

    }

    // #============================================================================     
    void dress_occ_plot_bpix(TCanvas& canv,TH2D *h,int lay){

      canv.cd(lay);
      gStyle->SetPadRightMargin(0.125);

      h->Draw("zcol");
      int phase      = 1;
      int half_shift = 1;
      unsigned int n_ladder[4] = {6, 14, 22, 32};
      unsigned int n_lad = n_ladder[lay-1];

      std::vector<TLine*> lines;
      std::vector signs = {-1,1}; 

      for(const auto x_sign : signs ){
	for(const auto y_sign : signs ){
	  float x_low  = x_sign * (half_shift*0.5);
          float x_high = x_sign * (half_shift*0.5 + 4 );
          float y_low  = y_sign * (half_shift*0.5);
          float y_high = y_sign * (half_shift*0.5 + n_lad);
	  //# Outside box                                  
	  
	  lines.push_back(draw_line(x_low,x_high,y_low,y_low,1));   // # bottom
	  lines.push_back(draw_line(x_low,x_high,y_high,y_high,1)); // # top
	  lines.push_back(draw_line(x_low,x_low,y_low,y_high,1));   // # left 
	  lines.push_back(draw_line(x_high,x_high,y_low,y_high,1)); // # right

	  //# Inner Horizontal lines                                        
	  for(unsigned int lad=1;lad<n_lad;lad++){
	    float y = y_sign * (lad + half_shift*0.5);
	    lines.push_back(draw_line(x_low,x_high,y,y,1));
	  }

	  for(unsigned int lad=1;lad<n_lad+1;lad++){
	    float y = y_sign * (lad + half_shift*0.5 - 0.5);
	    lines.push_back(draw_line(x_low, x_high,y,y,1, 3));
	  }
	  
	  //# Inner Vertical lines                                                                                             
	  for(unsigned int mod=1;mod<=4;mod++){
	    float x = x_sign * (mod + half_shift*0.5);
	    lines.push_back(draw_line(x, x, y_low,  y_high, 1));  
	  }
          
	  for(unsigned int mod=1;mod<=4;mod++){
	    for(unsigned int lad=1;lad<n_lad+1;lad++){

	      bool flipped = y_sign==1 ? lad%2==0 : lad%2==1;
	      if (phase==1)  flipped = !flipped;
	      int roc0_orientation = flipped ? -1 : 1;
	      if (x_sign==-1) roc0_orientation *= -1;
	      if (y_sign==-1) roc0_orientation *= -1;
	      float x1 = x_sign * (mod+half_shift*0.5);
	      float x2 = x_sign * (mod+half_shift*0.5 - 1./8);
	      float y1 = y_sign * (lad+half_shift*0.5-0.5);
	      float y2 = y_sign * (lad+half_shift*0.5-0.5 + roc0_orientation*1./2);

	      lines.push_back(draw_line(x1, x2, y1, y1, 1));
	      lines.push_back(draw_line(x2, x2, y1, y2, 1));
	    }
	  }
	}
      }

      auto ltx = TLatex();
      ltx.SetTextFont(62);
      ltx.SetTextColor(1);
      ltx.SetTextSize(0.06);
      ltx.SetTextAlign(31);
      ltx.DrawLatexNDC(1-gPad->GetRightMargin(),
		       1-gPad->GetTopMargin()+0.01,("Layer"+std::to_string(lay)).c_str());
      
      for (auto& l : lines){
	l->Draw("same");
      }
    }

    //============================================================================                     
    TLine* draw_line(float x1, float x2,float y1,float y2,int width=2,int style=1,int color=1){
      
      TLine* l = new TLine(x1, y1, x2, y2);
      l->SetLineWidth(width);
      l->SetLineStyle(style);
      l->SetLineColor(color);
      return l;
    }

  private:
    TrackerTopology m_trackerTopo;
  };
} // namespace

// Register the classes as boost python plugin
PAYLOAD_INSPECTOR_MODULE(SiPixelQuality){
  PAYLOAD_INSPECTOR_CLASS(SiPixelQualityTest);
  PAYLOAD_INSPECTOR_CLASS(SiPixelQualityBadRocsSummary);
  PAYLOAD_INSPECTOR_CLASS(SiPixelQualityBadRocsTimeHistory);
  PAYLOAD_INSPECTOR_CLASS(SiPixelQualityMap);
}
