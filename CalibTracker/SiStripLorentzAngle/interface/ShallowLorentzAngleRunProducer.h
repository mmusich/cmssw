#ifndef CALIBTRACKER_SISTRIPLORENTZANGLE_SHALLOWLORENTZANGLERUNPRODUCER
#define CALIBTRACKER_SISTRIPLORENTZANGLE_SHALLOWLORENTZANGLERUNPRODUCER

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/one/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include <ext/hash_map>


class ShallowLorentzAngleRunProducer : public edm::one::EDProducer< edm::BeginRunProducer,
								    edm::one::WatchRuns> 
{
   public:
      explicit ShallowLorentzAngleRunProducer(const edm::ParameterSet&);
      virtual ~ShallowLorentzAngleRunProducer();
   private:
      std::string Suffix;
      std::string Prefix;

      virtual void produce(edm::Event& iEvent, const edm::EventSetup& iSetup)override final;
      virtual void beginRunProduce(edm::Run & iRun, const edm::EventSetup& iSetup)override final;
      virtual void beginRun(edm::Run const& iRun, const edm::EventSetup& iSetup)override final;
      virtual void endRun(edm::Run const& iRun, const edm::EventSetup& iSetup)override final;

};
#endif



