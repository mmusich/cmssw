import FWCore.ParameterSet.Config as cms

from CalibTracker.SiStripCommon.ShallowClustersProducer_cfi import *
from CalibTracker.SiStripCommon.ShallowTrackClustersProducer_cfi import *

LorentzAngleOutputCommands =  [ 'keep *_shallowClusters_clusterdetid_*',
                                'keep *_shallowClusters_clusterwidth_*',
                                'keep *_shallowClusters_clustervariance_*',
                                'keep *_shallowTrackClusters_tsostrackmulti_*',
                                'keep *_shallowTrackClusters_tsosdriftx_*',
                                'keep *_shallowTrackClusters_tsosdriftz_*',
                                'keep *_shallowTrackClusters_tsoslocaltheta_*',
                                'keep *_shallowTrackClusters_tsoslocalphi_*',
                                'keep *_shallowTrackClusters_tsosBdotY_*',
                                #'keep *_shallowTrackClusters_tsoslocaly_*',
                                'keep *_shallowTrackClusters_tsosglobalZofunitlocalY_*']

laCalibrationTree = cms.EDAnalyzer("ShallowTree", outputCommands = cms.untracked.vstring('drop *'))
laCalibrationTree.outputCommands += LorentzAngleOutputCommands

# ESProducer
LorentzAngleNtuple = cms.Sequence( (shallowClusters +
                                    shallowTrackClusters) *
                                   laCalibrationTree
                                   )

from CalibTracker.SiStripLorentzAngle.ShallowLorentzAngleRunProducer_cfi import *

LorentzAngleOutputCommands =  [ 'keep *_shallowLorentzAngleRunProducer_*_*',]

lorentzAngleRunTree = cms.EDAnalyzer("ShallowTree", 
                                     isRunBased = cms.untracked.bool(True),
                                     outputCommands = cms.untracked.vstring('drop *')
                                     )

lorentzAngleRunTree.outputCommands += LorentzAngleOutputCommands

LorentzAngleRunNtuple = cms.Sequence( shallowLorentzAngleRunProducer *  lorentzAngleRunTree)
