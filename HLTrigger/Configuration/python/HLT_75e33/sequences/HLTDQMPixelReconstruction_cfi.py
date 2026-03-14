import FWCore.ParameterSet.Config as cms

#from ..modules.hltSiPixelRecHitsSoAMonitorCPU_cfi import *
#from ..modules.hltSiPixelRecHitsSoAMonitorGPU_cfi import *
#from ..modules.hltSiPixelRecHitsSoACompareGPUvsCPU_cfi import *
from ..modules.hltPixelTracksSoAMonitorCPU_cfi import *
from ..modules.hltPixelTracksSoAMonitorGPU_cfi import *
from ..modules.hltPixelTracksSoACompareGPUvsCPU_cfi import *
#from ..modules.hltPixelVerticesSoAMonitorCPU_cfi import *
#from ..modules.hltPixelVerticesSoAMonitorGPU_cfi import *
#from ..modules.hltPixelVerticesSoACompareGPUvsCPU_cfi import *

HLTDQMPixelReconstruction = cms.Sequence(#hltSiPixelRecHitsSoAMonitorCPU +
    #hltSiPixelRecHitsSoAMonitorGPU +
    #hltSiPixelRecHitsSoACompareGPUvsCPU +
    hltPixelTracksSoAMonitorCPU +
    hltPixelTracksSoAMonitorGPU +
    hltPixelTracksSoACompareGPUvsCPU )
#process.hltPixelVerticesSoAMonitorCPU +
#process.hltPixelVerticesSoAMonitorGPU +
#process.hltPixelVerticesSoACompareGPUvsCPU)
