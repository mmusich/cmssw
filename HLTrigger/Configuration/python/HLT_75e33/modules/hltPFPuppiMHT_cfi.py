import FWCore.ParameterSet.Config as cms

from HLTrigger.JetMET.HLTHtMhtProducer import HLTHtMhtProducer as _HLTHtMhtProducer

hltPFPuppiMHT = _HLTHtMhtProducer(
    excludePFMuons = False,
    jetsLabel = ("hltAK4PFPuppiJetsCorrected"),
    maxEtaJetHt = 5.0,
    maxEtaJetMht = 5.0,
    minNJetHt = 0,
    minNJetMht = 0,
    minPtJetHt = 30.0,
    minPtJetMht = 30.0,
    pfCandidatesLabel = (""),
    usePt = False
)
