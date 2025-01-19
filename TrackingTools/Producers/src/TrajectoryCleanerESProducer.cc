#include "FWCore/Framework/interface/ModuleFactory.h"
#include "FWCore/Framework/interface/ESProducer.h"

#include "FWCore/Framework/interface/ESHandle.h"

#include "TrackingTools/Records/interface/TrackingComponentsRecord.h"
#include "TrackingTools/TrajectoryCleaning/interface/TrajectoryCleaner.h"

#include "TrackingTools/TrajectoryCleaning/interface/TrajectoryCleanerFactory.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/ParameterSet/interface/PluginDescription.h"
#include "FWCore/ParameterSet/interface/ParameterSetDescription.h"

class TrajectoryCleanerESProducer : public edm::ESProducer {
public:
  TrajectoryCleanerESProducer(const edm::ParameterSet&);
  ~TrajectoryCleanerESProducer() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

  typedef std::unique_ptr<TrajectoryCleaner> ReturnType;

  ReturnType produce(const TrackingComponentsRecord&);

private:
  std::string theComponentName;
  std::string theComponentType;
  edm::ParameterSet theConfig;
};

TrajectoryCleanerESProducer::TrajectoryCleanerESProducer(const edm::ParameterSet& iConfig) {
  theComponentName = iConfig.getParameter<std::string>("ComponentName");
  theComponentType = iConfig.getParameter<std::string>("ComponentType");

  theConfig = iConfig;
  setWhatProduced(this, theComponentName);
}

void TrajectoryCleanerESProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<std::string>("ComponentName", "TrajectoryCleanerBySharedHits");
  desc.add<std::string>("ComponentType", "TrajectoryCleanerBySharedHits");
  desc.addOptional<double>("fractionShared", 0.19);
  desc.addOptional<double>("ValidHitBonus", 5.0);
  desc.addOptional<double>("MissingHitPenalty", 20.0);
  desc.addOptional<bool>("allowSharedFirstHit", true);
  descriptions.addDefault(desc);
}

// ------------ method called to produce the data  ------------
TrajectoryCleanerESProducer::ReturnType TrajectoryCleanerESProducer::produce(const TrackingComponentsRecord& iRecord) {
  using namespace edm::es;

  return ReturnType(TrajectoryCleanerFactory::get()->create(theComponentType, theConfig));
}

DEFINE_FWK_EVENTSETUP_MODULE(TrajectoryCleanerESProducer);
