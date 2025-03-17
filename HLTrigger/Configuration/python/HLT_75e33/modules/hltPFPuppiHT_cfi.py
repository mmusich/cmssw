import FWCore.ParameterSet.Config as cms

from HLTrigger.JetMET.HLTHtMhtProducer import HLTHtMhtProducer as _HLTHtMhtProducer

hltPFPuppiHT = _HLTHtMhtProducer(
    excludePFMuons = False,
    jetsLabel = ("hltAK4PFPuppiJetsCorrected"),
    maxEtaJetHt = 2.4,
    maxEtaJetMht = 2.4,
    minNJetHt = 0,
    minNJetMht = 0,
    minPtJetHt = 30.0,
    minPtJetMht = 30.0,
    pfCandidatesLabel = (""),
    usePt = True
)
