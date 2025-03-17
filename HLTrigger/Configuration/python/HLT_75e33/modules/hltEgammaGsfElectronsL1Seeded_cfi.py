import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTPixelMatchElectronProducers import EgammaHLTPixelMatchElectronProducers as _EgammaHLTPixelMatchElectronProducers

hltEgammaGsfElectronsL1Seeded = _EgammaHLTPixelMatchElectronProducers(
    BSProducer = cms.InputTag("hltOnlineBeamSpot"),
    GsfTrackProducer = cms.InputTag("hltEgammaGsfTracksL1Seeded"),
    TrackProducer = cms.InputTag(""),
    UseGsfTracks = cms.bool(True)
)
