import FWCore.ParameterSet.Config as cms

from TrackingTools.KalmanUpdators.KFUpdatorESProducer import KFUpdatorESProducer as _KFUpdatorESProducer

hltESPKFUpdator = _KFUpdatorESProducer(
    ComponentName = cms.string('hltESPKFUpdator')
)
