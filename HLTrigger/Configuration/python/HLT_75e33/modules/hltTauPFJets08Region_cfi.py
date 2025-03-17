import FWCore.ParameterSet.Config as cms

from RecoTauTag.RecoTau.RecoTauJetRegionProducer import RecoTauJetRegionProducer as _RecoTauJetRegionProducer

hltTauPFJets08Region = _RecoTauJetRegionProducer(
    deltaR = 0.8,
    maxJetAbsEta = 99.0,
    minJetPt = -1.0,
    pfCandAssocMapSrc = (""),
    pfCandSrc = ("hltParticleFlowTmp"),
    src = ("hltAK4PFJets"),
    verbosity = 0
)
