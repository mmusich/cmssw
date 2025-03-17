import FWCore.ParameterSet.Config as cms

# RecHits options
from RecoLocalTracker.Phase2TrackerRecHits.Phase2TrackerRecHits import Phase2TrackerRecHits as _Phase2TrackerRecHits

hltSiPhase2RecHits = _Phase2TrackerRecHits(
  src = cms.InputTag("hltSiPhase2Clusters"),
  Phase2StripCPE = cms.ESInputTag("phase2StripCPEESProducer", "Phase2StripCPE")
)
