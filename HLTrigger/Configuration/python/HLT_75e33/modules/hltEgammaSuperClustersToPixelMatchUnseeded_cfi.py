import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTFilteredSuperClusterProducer import EgammaHLTFilteredSuperClusterProducer as _EgammaHLTFilteredSuperClusterProducer

hltEgammaSuperClustersToPixelMatchUnseeded = _EgammaHLTFilteredSuperClusterProducer(
    cands = ("hltEgammaCandidatesUnseeded"),
    cuts = [dict(
        barrelCut = dict(
            cutOverE = 0.2,
            useEt = False
        ),
        endcapCut = dict(
            cutOverE = 0.2,
            useEt = False
        ),
        var = ("hltEgammaHoverEUnseeded")
    )],
    minEtCutEB = 10.0,
    minEtCutEE = 10.0
)
