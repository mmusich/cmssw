/*!
  \file SiStripFedCabling_PayloadInspector
  \Payload Inspector Plugin for SiStrip Fed Cabling
  \author M. Musich
  \version $Revision: 1.0 $
  \date $Date: 2018/11/02 17:05:56 $
*/

#include "CondCore/Utilities/interface/PayloadInspectorModule.h"
#include "CondCore/Utilities/interface/PayloadInspector.h"
#include "CondCore/CondDB/interface/Time.h"

#include "CondFormats/SiStripObjects/interface/SiStripDetSummary.h"
#include "CondFormats/SiStripObjects/interface/SiStripFedCabling.h"
#include "CalibFormats/SiStripObjects/interface/SiStripDetCabling.h"

#include "CommonTools/TrackerMap/interface/TrackerMap.h"
#include "CondCore/SiStripPlugins/interface/SiStripPayloadInspectorHelper.h"
#include "CalibTracker/StandaloneTrackerTopology/interface/StandaloneTrackerTopology.h"
#include "CalibTracker/SiStripCommon/interface/SiStripDetInfoFileReader.h"

#include <memory>
#include <sstream>
#include <TCanvas.h>
#include <TH2D.h>
#include <TLatex.h>

namespace {

  /************************************************
    TrackerMap of SiStrip FED Cabling
  *************************************************/
  class SiStripFedCabling_TrackerMap : public cond::payloadInspector::PlotImage<SiStripFedCabling> {
  public:
    SiStripFedCabling_TrackerMap() : cond::payloadInspector::PlotImage<SiStripFedCabling>( "Tracker Map SiStrip Fed Cabling" ){
      setSingleIov( true );
    }

    bool fill( const std::vector<std::tuple<cond::Time_t,cond::Hash> >& iovs ) override{
      auto iov = iovs.front();
      std::shared_ptr<SiStripFedCabling> payload = fetchPayload( std::get<1>(iov) );

      std::unique_ptr<TrackerMap> tmap = std::unique_ptr<TrackerMap>(new TrackerMap("SiStripFedCabling"));
      tmap->setPalette(1);
      std::string titleMap = "TrackerMap of SiStrip Fed Cabling per module, IOV : "+std::to_string(std::get<0>(iov));
      tmap->setTitle(titleMap);

      TrackerTopology tTopo = StandaloneTrackerTopology::fromTrackerParametersXMLFile(edm::FileInPath("Geometry/TrackerCommonData/data/trackerParameters.xml").fullPath());
      std::unique_ptr<SiStripDetCabling> detCabling_ =std::unique_ptr<SiStripDetCabling>(new SiStripDetCabling(*(payload.get()),&tTopo));

      std::vector<uint32_t> activeDetIds;
      detCabling_->addActiveDetectorsRawIds(activeDetIds);
      //detCabling_->addAllDetectorsRawIds(activeDetIds);

      for(const auto &detId : activeDetIds){
      	int32_t n_conn = 0;																      
      	for(uint32_t connDet_i=0; connDet_i<detCabling_->getConnections(detId).size(); connDet_i++){						      
      	  if(detCabling_->getConnections(detId)[connDet_i]!=nullptr && detCabling_->getConnections(detId)[connDet_i]->isConnected()!=0) n_conn++;     
      	}																		      
      	if(n_conn!=0){																	      
      	  tmap->fill(detId,n_conn*2);														      
      	}                                                                                                                                                     
      }

      //edm::FileInPath fp_ = edm::FileInPath("CalibTracker/SiStripCommon/data/SiStripDetInfo.dat");
      //SiStripDetInfoFileReader* reader = new SiStripDetInfoFileReader(fp_.fullPath());

      // auto DetInfos  = reader->getAllData(); 
      // for(std::map<uint32_t, SiStripDetInfoFileReader::DetInfo >::const_iterator it = DetInfos.begin(); it != DetInfos.end(); it++){    
      // 	// check if det id is correct and if it is actually cabled in the detector
      // 	if( it->first==0 || it->first==0xFFFFFFFF ) {
      // 	  edm::LogError("DetIdNotGood") << "@SUB=analyze" << "Wrong det id: " << it->first 
      // 					<< "  ... neglecting!" << std::endl;
      // 	  continue;
      // 	}

      // 	// uint16_t nAPVs = 0;
      // 	// const std::vector<const FedChannelConnection*> connection = detCabling_->getConnections(it->first);
      // 	// for (unsigned int ca = 0; ca<connection.size(); ca++) {
      // 	//   if ( connection[ca]!=0 )  {
      // 	//     nAPVs+=( connection[ca] )->nApvs();
      // 	//     break;
      // 	//   }
      // 	// }

      // 	int32_t n_conn = 0;
      // 	for(uint32_t connDet_i=0; connDet_i<detCabling_->getConnections(it->first).size(); connDet_i++){
      // 	  if(detCabling_->getConnections(it->first)[connDet_i]!=nullptr && detCabling_->getConnections(it->first)[connDet_i]->isConnected()!=0) n_conn++;
      // 	}
      // 	if(n_conn!=0){
      // 	  tmap->fill(it->first,n_conn*2);
      // 	}                                                                                                                                                     
      // }

      // auto feds = payload->fedIds();
      // for ( auto ifed = feds.begin(); ifed != feds.end(); ifed++ ) { // iterate over active feds, get all their FedChannelConnection-s
      // 	SiStripFedCabling::ConnsConstIterRange conns = payload->fedConnections( *ifed );
      // 	for ( auto iconn = conns.begin(); iconn != conns.end(); iconn++ ) { // loop over FedChannelConnection objects
      // 	  bool have_fed_id = iconn->fedId();
      // 	  std::vector<int> vector_of_connected_apvs;
      // 	  if(have_fed_id){ // these apvpairs are seen from the readout
      // 	    // there can be at most 6 APVs on one DetId: 0,1,2,3,4,5
      // 	    int which_apv_pair = iconn->apvPairNumber(); // APVPair (0,1) for 512 strips and (0,1,2) for 768 strips
	
      // 	    // patch needed to take into account invalid detids or apvPairs
      // 	    if( iconn->detId()==0 ||  
      // 		iconn->detId() == sistrip::invalid32_ ||  
      // 		iconn->apvPairNumber() == sistrip::invalid_  ||
      // 		iconn->nApvPairs() == sistrip::invalid_ ) {
      // 	      continue;
      // 	    } 

      // 	    if(iconn->i2cAddr(0)) vector_of_connected_apvs.push_back(2*which_apv_pair + 0); // first apv of the pair
      // 	    if(iconn->i2cAddr(1)) vector_of_connected_apvs.push_back(2*which_apv_pair + 1); // second apv of the pair
      // 	  }

      // 	  if(!vector_of_connected_apvs.empty()){ // add only is smth. there, obviously
      // 	    std::cout << iconn->detId();
      // 	    for (const auto &element : vector_of_connected_apvs){
      // 	      std::cout << " "<< element;
      // 	    }
      // 	     std::cout << std::endl;
      // 	  }
      // 	} // loop on fedchannel connections
      // } // loop on feds

      // // for(const auto & element : map_of_connected_apvs){
      // // 	std::cout<<" detid" << element.first << " n. APVs:" << element.second << std::endl;
      // // 	tmap->fill(element.first,element.second);
      // // }

      std::string fileName(m_imageFileName);
      tmap->save(true,0.,6.,fileName);

      return true;
    }
  };

  /************************************************
    Summary Plot of SiStrip FED Cabling
  *************************************************/
  class SiStripFedCabling_Summary : public cond::payloadInspector::PlotImage<SiStripFedCabling> {
  public:
    SiStripFedCabling_Summary() : cond::payloadInspector::PlotImage<SiStripFedCabling>( "SiStrip Fed Cabling Summary" ){
      setSingleIov( true );
    }

    bool fill( const std::vector<std::tuple<cond::Time_t,cond::Hash> >& iovs ) override{
      auto iov = iovs.front();
      std::shared_ptr<SiStripFedCabling> payload = fetchPayload( std::get<1>(iov) );
      int IOV = std::get<0>(iov);
      std::vector<uint32_t> activeDetIds;

      TrackerTopology tTopo = StandaloneTrackerTopology::fromTrackerParametersXMLFile(edm::FileInPath("Geometry/TrackerCommonData/data/trackerParameters.xml").fullPath());
      std::unique_ptr<SiStripDetCabling> detCabling_ =std::unique_ptr<SiStripDetCabling>(new SiStripDetCabling(*(payload.get()),&tTopo));

      detCabling_->addActiveDetectorsRawIds(activeDetIds);
      //detCabling_->addAllDetectorsRawIds(activeDetIds);

      containers myCont;
      containers allCounts;

      edm::FileInPath fp_ = edm::FileInPath("CalibTracker/SiStripCommon/data/SiStripDetInfo.dat");
      SiStripDetInfoFileReader* reader = new SiStripDetInfoFileReader(fp_.fullPath());
      auto DetInfos  = reader->getAllData(); 
      for(std::map<uint32_t, SiStripDetInfoFileReader::DetInfo >::const_iterator it = DetInfos.begin(); it != DetInfos.end(); it++){    
      	// check if det id is correct and if it is actually cabled in the detector
      	if( it->first==0 || it->first==0xFFFFFFFF ) {
      	  edm::LogError("DetIdNotGood") << "@SUB=analyze" << "Wrong det id: " << it->first 
      					<< "  ... neglecting!" << std::endl;
      	  continue;
      	}
	updateCounters(it->first,allCounts,tTopo);
      }

      for(const auto &detId : activeDetIds){
	updateCounters(detId,myCont,tTopo);
      }

      TH2D* ME = new TH2D("SummaryOfCabling","SummaryOfCabling",6,0.5,6.5,9,0.5,9.5);
      ME->GetXaxis()->SetTitle("Sub Det");
      ME->GetYaxis()->SetTitle("Layer");

      ME->SetTitle(0);

      ME->GetXaxis()->SetBinLabel(1,"TIB");
      ME->GetXaxis()->SetBinLabel(2,"TID F");
      ME->GetXaxis()->SetBinLabel(3,"TID B");
      ME->GetXaxis()->SetBinLabel(4,"TOB");
      ME->GetXaxis()->SetBinLabel(5,"TEC F");
      ME->GetXaxis()->SetBinLabel(6,"TEC B");

      for(int i=0;i<4;i++){
	ME->Fill(1,i+1,float(myCont.counterTIB[i])/allCounts.counterTIB[i]);
      }
  
      for(int i=0;i<2;i++){
	for(int j=0;j<3;j++){
	  ME->Fill(i+2,j+1,float(myCont.counterTID[i][j])/allCounts.counterTID[i][j]);
	}
      }

      for(int i=0;i<6;i++){
	ME->Fill(4,i+1,float(myCont.counterTOB[i])/allCounts.counterTOB[i]);
      }
  
      for(int i=0;i<2;i++){
	for(int j=0;j<9;j++){
	  ME->Fill(i+5,j+1,float(myCont.counterTEC[i][j])/allCounts.counterTEC[i][j]);
	}
      }
      
      TCanvas c1("SiStrip FED cabling summary","SiStrip FED cabling summary",800,600);
      c1.SetTopMargin(0.07);
      c1.SetBottomMargin(0.10);
      c1.SetLeftMargin(0.07);
      c1.SetRightMargin(0.10);

      ME->Draw("colz");
      ME->Draw("TEXTsame");
      ME->SetStats(kFALSE);
      
      TLatex t1;
      t1.SetNDC();
      t1.SetTextAlign(26);
      t1.SetTextSize(0.05);
      t1.DrawLatex(0.5, 0.96, Form("SiStrip FedCabling, IOV %i", IOV));

      std::string fileName(m_imageFileName);
      c1.SaveAs(fileName.c_str());

      return true;
    }

  private:
    struct containers{
    public:
      int counterTIB[4]={0};	    
      int counterTID[2][3]={{0}};
      int counterTOB[6]={0};	    
      int counterTEC[2][9]={{0}};
    };

    void updateCounters(int detId,containers &cont,const TrackerTopology& tTopo){
      
      StripSubdetector subdet(detId);

      switch (subdet.subdetId()) {
      case StripSubdetector::TIB:
	{
	  int i = tTopo.tibLayer(detId) - 1;
	  cont.counterTIB[i]++;
	  break;       
	}
      case StripSubdetector::TID:
	{
	  int j = tTopo.tidWheel(detId) - 1;
	  int side = tTopo.tidSide(detId);
	  if (side == 2) {
	    cont.counterTID[0][j]++;
	  } else if (side == 1) {
	    cont.counterTID[1][j]++;
	  }
	  break;       
	}
      case StripSubdetector::TOB:
	{
	  int i = tTopo.tobLayer(detId) - 1;
	  cont.counterTOB[i]++;
	  break;       
	}
      case StripSubdetector::TEC:
	{
	  int j = tTopo.tecWheel(detId) - 1;
	  int side = tTopo.tecSide(detId);
	  if (side == 2) {
	    cont.counterTEC[0][j]++;
	  } else if (side == 1) {
	    cont.counterTEC[1][j]++;
	  }
	  break;       
	}
      }
    }
  };

}

PAYLOAD_INSPECTOR_MODULE( SiStripFedCabling ){
  PAYLOAD_INSPECTOR_CLASS( SiStripFedCabling_TrackerMap );
  PAYLOAD_INSPECTOR_CLASS( SiStripFedCabling_Summary );
}
