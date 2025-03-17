import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTGsfTrackVarProducer import EgammaHLTGsfTrackVarProducer as _EgammaHLTGsfTrackVarProducer

hltEgammaBestGsfTrackVarsUnseeded = _EgammaHLTGsfTrackVarProducer(
    beamSpotProducer = ("hltOnlineBeamSpot"),
    inputCollection = ("hltEgammaGsfElectronsUnseeded"),
    lowerTrackNrToRemoveCut = -1,
    recoEcalCandidateProducer = ("hltEgammaCandidatesUnseeded"),
    upperTrackNrToRemoveCut = 9999,
    useDefaultValuesForBarrel = False,
    useDefaultValuesForEndcap = False
)
