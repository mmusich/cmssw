import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTPixelMatchElectronProducers import EgammaHLTPixelMatchElectronProducers as _EgammaHLTPixelMatchElectronProducers

hltEgammaGsfElectronsL1Seeded = _EgammaHLTPixelMatchElectronProducers(
    BSProducer = ("hltOnlineBeamSpot"),
    GsfTrackProducer = ("hltEgammaGsfTracksL1Seeded"),
    TrackProducer = (""),
    UseGsfTracks = True
)
