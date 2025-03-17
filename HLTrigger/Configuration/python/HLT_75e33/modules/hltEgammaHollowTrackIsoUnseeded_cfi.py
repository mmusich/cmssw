import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTPhotonTrackIsolationProducersRegional import EgammaHLTPhotonTrackIsolationProducersRegional as _EgammaHLTPhotonTrackIsolationProducersRegional

hltEgammaHollowTrackIsoUnseeded = _EgammaHLTPhotonTrackIsolationProducersRegional(
    countTracks = False,
    egTrkIsoConeSize = 0.29,
    egTrkIsoPtMin = 1.0,
    egTrkIsoRSpan = 999999.0,
    egTrkIsoStripBarrel = 0.03,
    egTrkIsoStripEndcap = 0.03,
    egTrkIsoVetoConeSize = 0.06,
    egTrkIsoZSpan = 999999.0,
    recoEcalCandidateProducer = ("hltEgammaCandidatesUnseeded"),
    trackProducer = ("hltGeneralTracks")
)
