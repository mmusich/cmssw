import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTGsfTrackVarProducer import EgammaHLTGsfTrackVarProducer as _EgammaHLTGsfTrackVarProducer

hltEgammaBestGsfTrackVarsL1Seeded = _EgammaHLTGsfTrackVarProducer(
    beamSpotProducer = ("hltOnlineBeamSpot"),
    inputCollection = ("hltEgammaGsfElectronsL1Seeded"),
    lowerTrackNrToRemoveCut = -1,
    recoEcalCandidateProducer = ("hltEgammaCandidatesL1Seeded"),
    upperTrackNrToRemoveCut = 9999,
    useDefaultValuesForBarrel = False,
    useDefaultValuesForEndcap = False
)
