import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTGsfTrackVarProducer import EgammaHLTGsfTrackVarProducer as _EgammaHLTGsfTrackVarProducer

hltEgammaGsfTrackVarsL1Seeded = _EgammaHLTGsfTrackVarProducer(
    beamSpotProducer = cms.InputTag("hltOnlineBeamSpot"),
    inputCollection = cms.InputTag("hltEgammaGsfTracksL1Seeded"),
    lowerTrackNrToRemoveCut = cms.int32(-1),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidatesL1Seeded"),
    upperTrackNrToRemoveCut = cms.int32(9999),
    useDefaultValuesForBarrel = cms.bool(False),
    useDefaultValuesForEndcap = cms.bool(False)
)
