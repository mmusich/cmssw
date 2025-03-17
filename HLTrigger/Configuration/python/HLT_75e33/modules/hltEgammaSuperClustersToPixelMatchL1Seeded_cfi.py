import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTFilteredSuperClusterProducer import EgammaHLTFilteredSuperClusterProducer as _EgammaHLTFilteredSuperClusterProducer

hltEgammaSuperClustersToPixelMatchL1Seeded = _EgammaHLTFilteredSuperClusterProducer(
    cands = ("hltEgammaCandidatesL1Seeded"),
    cuts = [dict(
        barrelCut = dict(
            cutOverE = 0.2,
            useEt = False
        ),
        endcapCut = dict(
            cutOverE = 0.2,
            useEt = False
        ),
        var = ("hltEgammaHoverEL1Seeded")
    )],
    minEtCutEB = 10.0,
    minEtCutEE = 10.0
)
