import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTGsfTrackVarProducer import EgammaHLTGsfTrackVarProducer as _EgammaHLTGsfTrackVarProducer

hltEgammaGsfTrackVarsL1Seeded = _EgammaHLTGsfTrackVarProducer(
    beamSpotProducer = ("hltOnlineBeamSpot"),
    inputCollection = ("hltEgammaGsfTracksL1Seeded"),
    lowerTrackNrToRemoveCut = -1,
    recoEcalCandidateProducer = ("hltEgammaCandidatesL1Seeded"),
    upperTrackNrToRemoveCut = 9999,
    useDefaultValuesForBarrel = False,
    useDefaultValuesForEndcap = False
)
