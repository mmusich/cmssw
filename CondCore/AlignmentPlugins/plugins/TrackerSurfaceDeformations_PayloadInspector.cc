/*!
  \file TrackerSurfaceDeformations_PayloadInspector
  \Payload Inspector Plugin for Tracker Surface Deformations
  \author M. Musich
  \version $Revision: 1.0 $
  \date $Date: 2018/02/01 15:57:24 $
*/

#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "CondCore/Utilities/interface/PayloadInspectorModule.h"
#include "CondCore/Utilities/interface/PayloadInspector.h"
#include "CondCore/CondDB/interface/Time.h"

// the data format of the condition to be inspected
#include "CondFormats/Alignment/interface/AlignmentSurfaceDeformations.h" 
#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/SiStripDetId/interface/StripSubdetector.h" 
#include "DataFormats/DetId/interface/DetId.h"

#include "Alignment/CommonAlignment/interface/Utilities.h"

// needed for the tracker map
#include "CommonTools/TrackerMap/interface/TrackerMap.h"

// needed for mapping
#include "CondCore/AlignmentPlugins/interface/AlignmentPayloadInspectorHelper.h"
#include "CalibTracker/StandaloneTrackerTopology/interface/StandaloneTrackerTopology.h" 

#include <memory>
#include <sstream>
#include <iostream>

// include ROOT 
#include "TH2F.h"
#include "TLegend.h"
#include "TCanvas.h"
#include "TLine.h"
#include "TStyle.h"
#include "TLatex.h"
#include "TPave.h"
#include "TPaveStats.h"

namespace {

  class TrackerSurfaceDeformationsTest : public cond::payloadInspector::Histogram1D<AlignmentSurfaceDeformations> {
    
  public:
    TrackerSurfaceDeformationsTest () : cond::payloadInspector::Histogram1D<AlignmentSurfaceDeformations>("TrackerSurfaceDeformationsTest",
													  "TrackerSurfaceDeformationsTest",2,0.0,2.0){
      Base::setSingleIov( true );
    }
    
    bool fill( const std::vector<std::tuple<cond::Time_t,cond::Hash> >& iovs ) override{

      for ( auto const & iov: iovs) {
	std::shared_ptr<AlignmentSurfaceDeformations> payload = Base::fetchPayload( std::get<1>(iov) );
	if( payload.get() ){
	  
	  int i=0;
	  auto listOfItems = payload->items();
	  std::cout << "items size:" << listOfItems.size() << std::endl;

	  for (const auto &item : listOfItems){
	    std::cout<< i << " "<< item.m_rawId <<" Det: "<<  DetId(item.m_rawId).subdetId() << " " << item.m_index << std::endl; 
 	    const auto beginEndPair = payload->parameters(i);
	    std::vector<align::Scalar> params(beginEndPair.first, beginEndPair.second);
	    std::cout << "params.size()" << params.size() << std::endl;
	    i++;
	  }

	}// payload
      }// iovs
      return true;
    }// fill
  };
 
} // close namespace

PAYLOAD_INSPECTOR_MODULE(TrackerSurfaceDeformations){
  PAYLOAD_INSPECTOR_CLASS(TrackerSurfaceDeformationsTest);
}
