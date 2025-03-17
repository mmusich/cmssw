import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTEleL1TrackIsolProducer import EgammaHLTEleL1TrackIsolProducer as _EgammaHLTEleL1TrackIsolProducer

hltEgammaEleL1TrkIsoL1Seeded = _EgammaHLTEleL1TrackIsolProducer(
    ecalCands = ("hltEgammaCandidatesL1Seeded"),
    eles = ("hltEgammaGsfElectronsL1Seeded"),
    isolCfg = dict(
        etaBoundaries = [1.5],
        trkCuts = [
            dict(
                maxDR = 0.3,
                maxDZ = 0.7,
                minDEta = 0.003,
                minDR = 0.01,
                minPt = 2.0
            ),
            dict(
                maxDR = 0.3,
                maxDZ = 0.7,
                minDEta = 0.003,
                minDR = 0.01,
                minPt = 2.0
            )
        ],
        useAbsEta = True
    ),
    l1Tracks = ("l1tTTTracksFromTrackletEmulation","Level1TTTracks")
)
