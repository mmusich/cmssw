import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTElectronTrackIsolationProducers import EgammaHLTElectronTrackIsolationProducers as _EgammaHLTElectronTrackIsolationProducers

hltEgammaEleGsfTrackIsoL1Seeded = _EgammaHLTElectronTrackIsolationProducers(
    beamSpotProducer = ("hltOnlineBeamSpot"),
    egTrkIsoConeSize = 0.3,
    egTrkIsoPtMin = 1.0,
    egTrkIsoRSpan = 999999.0,
    egTrkIsoStripBarrel = 0.01,
    egTrkIsoStripEndcap = 0.01,
    egTrkIsoVetoConeSizeBarrel = 0.01,
    egTrkIsoVetoConeSizeEndcap = 0.01,
    egTrkIsoZSpan = 0.15,
    electronProducer = ("hltEgammaGsfElectronsL1Seeded"),
    recoEcalCandidateProducer = ("hltEgammaCandidatesL1Seeded"),
    trackProducer = ("hltGeneralTracks"),
    useGsfTrack = True,
    useSCRefs = True
)
