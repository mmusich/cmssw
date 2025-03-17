import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTGsfTrackVarProducer import EgammaHLTGsfTrackVarProducer as _EgammaHLTGsfTrackVarProducer

hltEgammaGsfTrackVarsUnseeded = _EgammaHLTGsfTrackVarProducer(
    beamSpotProducer = ("hltOnlineBeamSpot"),
    inputCollection = ("hltEgammaGsfTracksUnseeded"),
    lowerTrackNrToRemoveCut = -1,
    recoEcalCandidateProducer = ("hltEgammaCandidatesUnseeded"),
    upperTrackNrToRemoveCut = 9999,
    useDefaultValuesForBarrel = False,
    useDefaultValuesForEndcap = False
)
