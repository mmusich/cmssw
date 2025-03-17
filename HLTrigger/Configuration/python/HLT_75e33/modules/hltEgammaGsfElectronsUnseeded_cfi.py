import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTPixelMatchElectronProducers import EgammaHLTPixelMatchElectronProducers as _EgammaHLTPixelMatchElectronProducers

hltEgammaGsfElectronsUnseeded = _EgammaHLTPixelMatchElectronProducers(
    BSProducer = cms.InputTag("hltOnlineBeamSpot"),
    GsfTrackProducer = cms.InputTag("hltEgammaGsfTracksUnseeded"),
    TrackProducer = cms.InputTag(""),
    UseGsfTracks = cms.bool(True)
)
