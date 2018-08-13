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
#include "TStyle.h"
#include "TColor.h"
#include "TLine.h"
#include "TLatex.h"
#include "TProfile.h"
#include "TPaveLabel.h"

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
      return;
    }
    
    void fillByPushBack(unsigned int detid,type value){
      m_info[detid].push_back(value);
    }

    std::vector<type> get(unsigned int detid){
      return m_info[detid];
    }

    void setGranularity(bool isPerStrip,bool isPerAPV){
      m_servedPerStrip=isPerStrip;
      m_servedPerAPV=isPerAPV;      
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

    void init(){
      m_servedPerStrip=false;
      m_servedPerAPV=false;
      m_info.clear();
    }

  };

  //used to produce all display objects for payload inspector
  template<class Item,class type>
  class SiStripDataContainer {

  public : 
    SiStripDataContainer(std::shared_ptr<Item> payload, unsigned int run,bool perStrip,bool perAPV) : payload_(payload), run_(run), isPerStrip_(perStrip), isPerAPV_(perAPV) {
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

    void printAll(){
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


  private:
    std::shared_ptr<Item> payload_;
    unsigned int run_;
    std::string hash_;
    bool isPerStrip_;
    bool isPerAPV_;
    std::string TopoMode_;
    // "Map", "Ratio", or "Diff"
    std::string PlotMode_;
   
    std::map<std::string, std::string> units_ = {
      { "SiStripPedestals", "ADC" },
      { "SiStripApVGain",  ""},//dimensionless TODO: verify
      { "SiStripNoises" , ""},
      { "SiStripLorentzAngle" , ""},
      { "SiStripBackPlaneCorrection" , ""},
      { "SiStripBadStrip" , ""},
      
    };
  };

}

#endif
