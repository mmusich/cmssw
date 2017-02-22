// -*- C++ -*-
//
// Package:    Calibration/TkAlCaRecoProducers
// Class:      AlignPCLThresholdsWriter
// 
/**\class AlignPCLThresholdsWriter AlignPCLThresholdsWriter.cc CondFormats/PCLConfig/plugins/AlignPCLThresholdsWriter.cc

 Description: class to build the SiPixelAli PCL thresholds

*/
//
// Original Author:  Marco Musich
//         Created:  Wed, 22 Feb 2017 12:04:36 GMT
//
//

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "CondFormats/PCLConfig/interface/AlignPCLThresholds.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CondCore/DBOutputService/interface/PoolDBOutputService.h"
//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class AlignPCLThresholdsWriter : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit AlignPCLThresholdsWriter(const edm::ParameterSet&);
      ~AlignPCLThresholdsWriter();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      // ----------member data ---------------------------
      std::string m_record;
      std::vector<unsigned int> m_alignableid;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
AlignPCLThresholdsWriter::AlignPCLThresholdsWriter(const edm::ParameterSet& iConfig):
  m_record(iConfig.getParameter<std::string>("record")),
  m_alignableid(iConfig.getParameter<std::vector<unsigned int>>("AlignableIDVec"))
{
   //now do what ever initialization is needed
   usesResource("TFileService");

}


AlignPCLThresholdsWriter::~AlignPCLThresholdsWriter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
AlignPCLThresholdsWriter::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   if (m_alignableid.size()!=0){
     /////// set from a pair of vectors (rpids and rpdistances) --> from xml
     
     AlignPCLThresholds* myThresholds = new AlignPCLThresholds();
     std::cout<<"Size of myThresholds obj  "<< myThresholds->size() <<std::endl<<std::endl;
     
     for(unsigned int i=0;i<m_alignableid.size();i++){

       AlignPCLThreshold a(5.0,30.0,10.0,30.0,15.0,30.0,200.0,10.0);
       myThresholds->setAlignPCLThreshold(m_alignableid[i],a);
       
     }
     
     std::cout<<"Size of myThresholds obj  "<<myThresholds->size() <<std::endl;
     const AlignPCLThresholds::threshold_map & mymap = myThresholds->getThreshold_Map();
     
     std::cout<<"Content of myThresholds "<<std::endl;
     for(AlignPCLThresholds::threshold_map::const_iterator it = mymap.begin(); it != mymap.end() ; ++it)
       std::cout<<"keys : " << it->first <<std::endl
		<<"- Xcut      : " << (it->second).getXcut()       <<" um"     << std::endl
		<<"- thetaXcut : " << (it->second).getThetaXcut()  <<" urad"   << std::endl
		<<"- Ycut      : " << (it->second).getYcut()       <<" um"     << std::endl
		<<"- thetaYcut : " << (it->second).getThetaYcut()  <<" urad"   << std::endl
		<<"- Zcut      : " << (it->second).getZcut()       <<" um"     << std::endl
		<<"- thetaZcut : " << (it->second).getThetaZcut()  <<" urad"   << std::endl
		<<"- MaxMove   : " << (it->second).getMaxMoveCut() <<" um/rad" << std::endl
		<<"- MaxError  : " << (it->second).getMaxErrorCut()<<" um/rad" << std::endl
		<<std::endl;
     
     // Form the data here
     edm::Service<cond::service::PoolDBOutputService> poolDbService;
     if( poolDbService.isAvailable() ){
       cond::Time_t valid_time = poolDbService->currentTime(); 
       // this writes the payload to begin in current run defined in cfg
       poolDbService->writeOne(myThresholds,valid_time, m_record  );
     }
   }
}
   
// ------------ method called once each job just before starting event loop  ------------
void 
AlignPCLThresholdsWriter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
AlignPCLThresholdsWriter::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
AlignPCLThresholdsWriter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(AlignPCLThresholdsWriter);
