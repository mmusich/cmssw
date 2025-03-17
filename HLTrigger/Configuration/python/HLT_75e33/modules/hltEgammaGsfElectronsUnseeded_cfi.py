import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTPixelMatchElectronProducers import EgammaHLTPixelMatchElectronProducers as _EgammaHLTPixelMatchElectronProducers

hltEgammaGsfElectronsUnseeded = _EgammaHLTPixelMatchElectronProducers(
    BSProducer = ("hltOnlineBeamSpot"),
    GsfTrackProducer = ("hltEgammaGsfTracksUnseeded"),
    TrackProducer = (""),
    UseGsfTracks = True
)
