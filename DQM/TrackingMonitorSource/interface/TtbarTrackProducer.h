#ifndef DQM_TrackingMonitorSource_TtbarTrackProducer_h
#define DQM_TrackingMonitorSource_TtbarTrackProducer_h

#include <memory>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

class TtbarTrackProducer : public edm::EDProducer {
public:
  explicit TtbarTrackProducer(const edm::ParameterSet&);
  ~TtbarTrackProducer() override;

  void produce(edm::Event& iEvent, edm::EventSetup const& iSetup) override;

private:
  // ----------member data ---------------------------

  const edm::InputTag electronTag_;
  const edm::InputTag jetsTag_;
  const edm::InputTag bjetsTag_;
  const edm::InputTag pfmetTag_;
  const edm::InputTag muonTag_;
  const edm::InputTag bsTag_;
  const edm::EDGetTokenT<reco::GsfElectronCollection> electronToken_;
  const edm::EDGetTokenT<reco::PFJetCollection> jetsToken_;
  const edm::EDGetTokenT<reco::JetTagCollection> bjetsToken_;
  const edm::EDGetTokenT<reco::PFMETCollection> pfmetToken_;
  const edm::EDGetTokenT<reco::MuonCollection> muonToken_;
  const edm::EDGetTokenT<reco::BeamSpot> bsToken_;

  const double maxEtaEle_;
  const double maxEtaMu_;
  const double minPt_;
  const double maxDeltaPhiInEB_;
  const double maxDeltaEtaInEB_;
  const double maxHOEEB_;
  const double maxSigmaiEiEEB_;
  const double maxDeltaPhiInEE_;
  const double maxDeltaEtaInEE_;
  const double maxHOEEE_;
  const double maxSigmaiEiEEE_;

  const double minChambers_;
  const double minMatches_;
  const double minMatchedStations_;

  const double minEtaHighest_Jets_;
  const double minEta_Jets_;

  const double btagFactor_;

  const double maxNormChi2_;
  const double maxD0_;
  const double maxDz_;
  const int minPixelHits_;
  const int minStripHits_;
  const double maxIsoEle_;
  const double maxIsoMu_;
  const double minPtHighestMu_;
  const double minPtHighestEle_;
  const double minPtHighest_Jets_;
  const double minPt_Jets_;
  const double minInvMass_;
  const double maxInvMass_;
  const double minMet_;
  const double maxMet_;
  const double minWmass_;
  const double maxWmass_;
};
#endif
