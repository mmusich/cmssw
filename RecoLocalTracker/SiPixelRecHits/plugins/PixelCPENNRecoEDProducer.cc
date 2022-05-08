#include "RecoLocalTracker/SiPixelRecHits/interface/PixelCPETemplateReco.h"
#include "RecoLocalTracker/Records/interface/TkPixelCPERecord.h"
#include "RecoLocalTracker/ClusterParameterEstimator/interface/PixelClusterParameterEstimator.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/Records/interface/TrackerTopologyRcd.h"
#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"

#include "PhysicsTools/TensorFlow/interface/TensorFlow.h"
#include "RecoLocalTracker/SiPixelRecHits/interface/PixelCPENNReco.h"
#include "FWCore/Framework/interface/stream/EDProducer.h" // note EDProducer instead of Analyzer 

#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/ModuleFactory.h"
#include "FWCore/Framework/interface/ESProducer.h"

#include <string>
#include <memory>

using namespace edm;


struct CacheData {
  CacheData() : graphDef(nullptr) {}
  std::atomic<tensorflow::GraphDef*> graphDef;
};

class PixelCPENNRecoEDProducer : public edm::stream::EDProducer<edm::GlobalCache<CacheData>> {
public:
  PixelCPENNRecoEDProducer(const edm::ParameterSet& p, const CacheData* cacheData);
  ~PixelCPENNRecoEDProducer() override;
  std::unique_ptr<PixelClusterParameterEstimator> produce(const TkPixelCPERecord&);
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

    // two additional static methods for handling the global cache
  static std::unique_ptr<CacheData> initializeGlobalCache(const edm::ParameterSet&);
  static void globalEndJob(const CacheData*);

private:
  edm::ESGetToken<MagneticField, IdealMagneticFieldRecord> magfieldToken_;
  edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> pDDToken_;
  edm::ESGetToken<TrackerTopology, TrackerTopologyRcd> hTTToken_;
  edm::ESGetToken<SiPixelLorentzAngle, SiPixelLorentzAngleRcd> lorentzAngleToken_;
  edm::ESGetToken<SiPixelTemplateDBObject, SiPixelTemplateDBObjectESProducerRcd> templateDBobjectToken_;

  edm::ParameterSet pset_;
  bool doLorentzFromAlignment_;
  bool useLAFromDB_;
  tensorflow::Session* session_x;
};

std::unique_ptr<CacheData> PixelCPENNRecoEDProducer::initializeGlobalCache(const edm::ParameterSet& config) 
{

  // this method is supposed to create, initialize and return a CacheData instance
  CacheData* cacheData = new CacheData();

  // load the graph def and save it
  std::string graphPath_x = config.getParameter<std::string>("graphPath_x");
  cacheData->graphDef = tensorflow::loadGraphDef(graphPath_x);

  // set tensorflow log leven to warning
  tensorflow::setLogging("2");
  //init();

  return std::unique_ptr<CacheData>(cacheData);
}

void PixelCPENNRecoEDProducer::globalEndJob(const CacheData* cacheData) {
  // reset the graphDef
  printf("in global end job\n");
    //tensorflow::closeSession(session_x);    
  if (cacheData->graphDef != nullptr) {
    delete cacheData->graphDef;
  }

}



PixelCPENNRecoEDProducer::PixelCPENNRecoEDProducer(const edm::ParameterSet& p, const CacheData* cacheData ) 
: session_x(tensorflow::createSession(cacheData->graphDef)),{
  std::string myname = p.getParameter<std::string>("ComponentName");

  //useLAFromDB_ = p.getParameter<bool>("useLAFromDB");
  //doLorentzFromAlignment_ = p.getParameter<bool>("doLorentzFromAlignment");

  pset_ = p;
  //auto c = setWhatProduced(this, myname);
  magfieldToken_ = esConsumes<MagneticField, IdealMagneticFieldRecord>();
  pDDToken_ = esConsumes<TrackerGeometry, TrackerDigiGeometryRecord>();
  hTTToken_ = = esConsumes <TrackerTopology, TrackerTopologyRcd>(); // is this the tracker topology token?
  
  //templateDBobjectToken_ = c.consumes();
  //if (useLAFromDB_ || doLorentzFromAlignment_) {
  //  char const* laLabel = doLorentzFromAlignment_ ? "fromAlignment" : "";
  //  lorentzAngleToken_ = c.consumes(edm::ESInputTag("", laLabel));
  //}
}
//===================== how should this communicate with PixelCPENNReco.cc? =========================== 
std::unique_ptr<PixelClusterParameterEstimator> PixelCPENNRecoEDProducer::produce(const edm::EventSetup& setup ) {
  // Normal, default LA is used in case of template failure, load it unless
  // turned off
  // if turned off, null is ok, becomes zero
 // const SiPixelLorentzAngle* lorentzAngleProduct = nullptr;
 // if (useLAFromDB_ || doLorentzFromAlignment_) {
  //  lorentzAngleProduct = &iRecord.get(lorentzAngleToken_);
 // }

  return std::make_unique<PixelCPENNReco>(pset_,
                                                //&iRecord.get(magfieldToken_),
                                                //iRecord.get(pDDToken_),
                                                setup.getHandle(pDDToken_),
                                                //iRecord.get(hTTToken_),
                                                setup.getHandle(hTTToken_),
                                                //lorentzAngleProduct,
                                                //&iRecord.get(templateDBobjectToken_)
                                                );
}
//=================================================================================================

PixelCPENNRecoEDProducer::~PixelCPENNRecoEDProducer() {}

void PixelCPENNRecoEDProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;

  // from PixelCPEBase
  PixelCPEBase::fillPSetDescription(desc);

  // from PixelCPETemplateReco
  PixelCPENNReco::fillPSetDescription(desc);

  // specific to PixelCPENNRecoEDProducer

  desc.add<std::string>("graphPath_x");
  desc.add<std::string>("inputTensorName_x");
  desc.add<std::string>("anglesTensorName_x");
  desc.add<std::string>("outputTensorName");
  //desc.add<bool>("use_det_angles");
  //desc.add<std::string>("cpe");
  desc.add<std::string>("ComponentName", "PixelCPENNReco");
  descriptions.add("_templates_default", desc);
}

DEFINE_FWK_EVENTSETUP_MODULE(PixelCPENNRecoEDProducer);
