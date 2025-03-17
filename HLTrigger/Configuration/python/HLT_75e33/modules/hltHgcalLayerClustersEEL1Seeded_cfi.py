import FWCore.ParameterSet.Config as cms
from ..psets.hgcal_reco_constants_cfi import HGCAL_reco_constants as HGCAL_reco_constants

from RecoLocalCalo.HGCalRecProducers.HGCalLayerClusterProducer import HGCalLayerClusterProducer as _HGCalLayerClusterProducer

hltHgcalLayerClustersEEL1Seeded = _HGCalLayerClusterProducer(
    detector = cms.string('EE'),
    mightGet = cms.optional.untracked.vstring,
    nHitsTime = 3,
    plugin = dict(
        dEdXweights = HGCAL_reco_constants.dEdXweights,
        deltac = cms.vdouble(
            1.3,
            1.3,
            1.3,
            0.0315
        ),
        deltasi_index_regemfac = 3,
        dependSensor = True,
        ecut = 3,
        fcPerEle = HGCAL_reco_constants.fcPerEle,
        fcPerMip = HGCAL_reco_constants.fcPerMip,
        kappa = 9,
        maxNumberOfThickIndices = HGCAL_reco_constants.maxNumberOfThickIndices,
        noiseMip = HGCAL_reco_constants.noiseMip,
        noises = HGCAL_reco_constants.noises,
        positionDeltaRho2 = HGCAL_reco_constants.positionDeltaRho2,
        sciThicknessCorrection = HGCAL_reco_constants.sciThicknessCorrection,
        thicknessCorrection = HGCAL_reco_constants.thicknessCorrection,
        thresholdW0 = HGCAL_reco_constants.thresholdW0,
        type = cms.string('SiCLUE'),
        use2x2 = True,
        verbosity = cms.untracked.uint32(3)
    ),
    recHits = ("hltRechitInRegionsHGCAL","HGCEERecHits"),
    timeClname = cms.string('timeLayerCluster')
)

