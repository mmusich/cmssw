// -*- C++ -*-
//
// Package:    SiPixelTemplateDBObjectESProducer
// Class:      SiPhase2InnerTrackerCPEConditionsESProducer
//
/**\class SiPhase2InnerTrackerCPEConditionsESProducer SiPhase2InnerTrackerCPEConditionsESProducer.cc CalibTracker/SiPixelESProducers/plugin/SiPhase2InnerTrackerCPEConditionsESProducer.cc

 Description: ESProducer for Phase2 IT CPE conditions (geometry dependent)

*/
//
// Original Author:  M. Musich
//         Created:  19 July 2019
//
//

#include <memory>

#include "FWCore/Framework/interface/ESProducer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/EventSetupRecordIntervalFinder.h"

#include "CondFormats/SiPixelObjects/interface/SiPixelTemplateDBObject.h"
#include "CondFormats/DataRecord/interface/SiPixelTemplateDBObjectRcd.h"

#include "CondFormats/SiPixelObjects/interface/SiPixelLorentzAngle.h"
#include "CondFormats/DataRecord/interface/SiPixelLorentzAngleRcd.h"

#include "CondFormats/SiPixelObjects/interface/SiPixelGenErrorDBObject.h"
#include "CondFormats/DataRecord/interface/SiPixelGenErrorDBObjectRcd.h"

using namespace edm;

class SiPhase2InnerTrackerCPEConditionsESProducer : public edm::ESProducer, public edm::EventSetupRecordIntervalFinder {
public:

  SiPhase2InnerTrackerCPEConditionsESProducer(const edm::ParameterSet &);
  ~SiPhase2InnerTrackerCPEConditionsESProducer() override;

  void produce(){};

protected:
  void setIntervalFor(const edm::eventsetup::EventSetupRecordKey &,
                      const edm::IOVSyncValue &,
                      edm::ValidityInterval &) override;
  
  std::unique_ptr<SiPixelLorentzAngle>       produceLorentzAngleOffset(const SiPixelLorentzAngleRcd & rcd);
  std::unique_ptr<SiPixelLorentzAngle>       produceLorentzAngleWidth (const SiPixelLorentzAngleRcd & rcd);
  std::unique_ptr<SiPixelLorentzAngle>       produceSimLorentzAngle(const SiPixelLorentzAngleSimRcd &rcd);
  std::unique_ptr<SiPixelGenErrorDBObject>   produceGenError(const SiPixelGenErrorDBObjectRcd &rcd);
  std::unique_ptr<SiPixelTemplateDBObject>   produceTemplate(const SiPixelTemplateDBObjectRcd &rcd);
  std::unique_ptr<SiPixel2DTemplateDBObject> produce2DTemplateNumerator(const SiPixel2DTemplateDBObjectRcd &rcd);
  std::unique_ptr<SiPixel2DTemplateDBObject> produce2DTemplateDenominator(const SiPixel2DTemplateDBObjectRcd &rcd);
};

DEFINE_FWK_EVENTSETUP_MODULE(SiPhase2InnerTrackerCPEConditionsESProducer);
