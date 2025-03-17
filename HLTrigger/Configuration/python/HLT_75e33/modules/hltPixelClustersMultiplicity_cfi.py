import FWCore.ParameterSet.Config as cms

from HLTrigger.JetMET.HLTSiPixelClusterMultiplicityValueProducer import HLTSiPixelClusterMultiplicityValueProducer as _HLTSiPixelClusterMultiplicityValueProducer

hltPixelClustersMultiplicity = _HLTSiPixelClusterMultiplicityValueProducer(
    defaultValue = cms.double(-1.0),
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("hltSiPixelClusters")
)
