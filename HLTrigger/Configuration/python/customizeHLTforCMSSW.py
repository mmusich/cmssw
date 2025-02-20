import FWCore.ParameterSet.Config as cms

# helper functions
from HLTrigger.Configuration.common import *

# add one customisation function per PR
# - put the PR number into the name of the function
# - add a short comment
# for example:

# CCCTF tuning
# def customiseFor12718(process):
#     for pset in process._Process__psets.values():
#         if hasattr(pset,'ComponentType'):
#             if (pset.ComponentType == 'CkfBaseTrajectoryFilter'):
#                 if not hasattr(pset,'minGoodStripCharge'):
#                     pset.minGoodStripCharge = cms.PSet(refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone'))
#     return process



def customiseForOffline(process):
    # For running HLT offline on Run-3 Data, use "(OnlineBeamSpotESProducer).timeThreshold = 1e6",
    # in order to pick the beamspot that was actually used by the HLT (instead of a "fake" beamspot).
    # These same settings can be used offline for Run-3 Data and Run-3 MC alike.
    # Note: the products of the OnlineBeamSpotESProducer are used only
    #       if the configuration uses "(BeamSpotOnlineProducer).useTransientRecord = True".
    # See CMSHLT-2271 and CMSHLT-2300 for further details.
    for prod in esproducers_by_type(process, 'OnlineBeamSpotESProducer'):
        prod.timeThreshold = int(1e6)

    # For running HLT offline and relieve the strain on Frontier so it will no longer inject a
    # transaction id which tells Frontier to add a unique "&freshkey" to many query URLs.
    # That was intended as a feature to only be used by the Online HLT, to guarantee that fresh conditions
    # from the database were loaded at each Lumi section
    # Seee CMSHLT-3123 for further details
    if hasattr(process, 'GlobalTag'):
        # Set ReconnectEachRun and RefreshEachRun to False
        process.GlobalTag.ReconnectEachRun = cms.untracked.bool(False)
        process.GlobalTag.RefreshEachRun = cms.untracked.bool(False)

        if hasattr(process.GlobalTag, 'toGet'):
            # Filter out PSet objects containing only 'record' and 'refreshTime'
            process.GlobalTag.toGet = [
                pset for pset in process.GlobalTag.toGet
                if set(pset.parameterNames_()) != {'record', 'refreshTime'}
            ]

    return process

def customizeHLTfor46935(process):
    """Changes parameter names of EcalUncalibRecHitSoAToLegacy producer"""
    for prod in producers_by_type(process, 'EcalUncalibRecHitSoAToLegacy'):
        if hasattr(prod, 'uncalibRecHitsPortableEB'):
            prod.inputCollectionEB = prod.uncalibRecHitsPortableEB
            delattr(prod, 'uncalibRecHitsPortableEB')
        if hasattr(prod, 'uncalibRecHitsPortableEE'):
            prod.inputCollectionEE = prod.uncalibRecHitsPortableEE
            delattr(prod, 'uncalibRecHitsPortableEE')
        if hasattr(prod, 'recHitsLabelCPUEB'):
            prod.outputLabelEB = prod.recHitsLabelCPUEB
            delattr(prod, 'recHitsLabelCPUEB')
        if hasattr(prod, 'recHitsLabelCPUEE'):
            prod.outputLabelEE = prod.recHitsLabelCPUEE
            delattr(prod, 'recHitsLabelCPUEE')
    return process


def customizeHLTfor47017(process):
    """Remove unneeded parameters from the HLT menu"""
    for prod in producers_by_type(process, 'MaskedMeasurementTrackerEventProducer'):
        if hasattr(prod, 'OnDemand'):
            delattr(prod, 'OnDemand')

    for prod in producers_by_type(process, 'HcalHaloDataProducer'):
        if hasattr(prod, 'HcalMaxMatchingRadiusParam'):
            delattr(prod, 'HcalMaxMatchingRadiusParam')
        if hasattr(prod, 'HcalMinMatchingRadiusParam'):
            delattr(prod, 'HcalMinMatchingRadiusParam')

    for prod in producers_by_type(process, 'SiPixelRecHitConverter'):
        if hasattr(prod, 'VerboseLevel'):
            delattr(prod, 'VerboseLevel')

    return process


def customizeHLTfor47079(process):
    """Remove unneeded parameters from the HLT menu"""
    for filt in filters_by_type(process, 'PrimaryVertexObjectFilter'):
        if hasattr(filt, 'filterParams') and hasattr(filt.filterParams, 'pvSrc'):
            del filt.filterParams.pvSrc  # Remove the pvSrc parameter

    for prod in producers_by_type(process, 'HcalHitReconstructor'):
        # Remove useless parameters
        if hasattr(prod,'setHSCPFlags'):
            delattr(prod,'setHSCPFlags')

        if hasattr(prod,'setPulseShapeFlags'):
            delattr(prod,'setPulseShapeFlags')
                    
    return process

def customizeHLTfor47047(process):
    """Migrates many ESProducers to MoveToDeviceCache"""
    import copy
    if hasattr(process, "ecalMultifitParametersSource"):
        del process.ecalMultifitParametersSource
    esProducer = None
    for prod in esproducers_by_type(process, "EcalMultifitParametersHostESProducer@alpaka"):
        if esProducer is not None:
            raise Exception("Assumption of only one EcalMultifitParametersHostESProducer@alpaka in a process broken")
        esProducer = prod
    if esProducer is not None:
        for prod in producers_by_type(process, "EcalUncalibRecHitProducerPortable@alpaka", "alpaka_serial_sync::EcalUncalibRecHitProducerPortable"):
            for attr in ["EBtimeFitParameters", "EEtimeFitParameters", "EBamplitudeFitParameters", "EEamplitudeFitParameters"]:
                setattr(prod, attr, copy.deepcopy(getattr(esProducer, attr)))
        delattr(process, esProducer.label())

    for prod in producers_by_type(process, "HBHERecHitProducerPortable@alpaka", "alpaka_serial_sync::HBHERecHitProducerPortable"):
        if not hasattr(prod, 'mahiPulseOffSets'):
            continue
        pulseOffsetLabel = prod.mahiPulseOffSets.getModuleLabel()
        if hasattr(process, pulseOffsetLabel):
            esProducer = getattr(process, pulseOffsetLabel)
            prod.pulseOffsets = copy.deepcopy(esProducer.pulseOffsets)
        del prod.mahiPulseOffSets
    for prod in list(esproducers_by_type(process, "HcalMahiPulseOffsetsESProducer@alpaka")):
        delattr(process, prod.label())

    for prod in producers_by_type(process, "PFClusterSoAProducer@alpaka", "alpaka_serial_sync::PFClusterSoAProducer"):
        if not hasattr(prod, 'pfClusterParams'):
            continue
        clusterParamsLabel = prod.pfClusterParams.getModuleLabel()
        if hasattr(process, clusterParamsLabel):
            esProducer = getattr(process, clusterParamsLabel)
            for attr in ["seedFinder", "initialClusteringStep", "pfClusterBuilder"]:
                setattr(prod, attr, copy.deepcopy(getattr(esProducer, attr).copy()))
        del prod.pfClusterParams
    for prod in list(esproducers_by_type(process, "PFClusterParamsESProducer@alpaka")):
        delattr(process, prod.label())

    if hasattr(process, "hltESSJobConfigurationGPURecord"):
        del process.hltESSJobConfigurationGPURecord

    return process
        
def customizeHLTfor47107(process):
    """Remove unneeded parameters from the HLT menu"""

    for prod in producers_by_type(process, 'TrackProducer'):
        if hasattr(prod, 'alias'):
            delattr(prod, 'alias')

    for prod in producers_by_type(process, 'GsfTrackProducer'):
        if hasattr(prod, 'producer'):
            delattr(prod, 'producer')

    return process

def customizeHLTfor47191(process):
    for esprod in esproducers_by_type(process, "PromptTrackCountingESProducer"):
        if hasattr(esprod, 'minimumImpactParameter'):
            delattr(esprod, 'minimumImpactParameter')

        if hasattr(esprod, 'useSignedImpactParameterSig'):
            delattr(esprod, 'useSignedImpactParameterSig')
            
    return process

def customizeHLTfor45063(process):
    """Assigns value of MuonHLTSeedMVAClassifier mva input file, scales and mean values according to the value of isFromL1"""
    for prod in producers_by_type(process, 'MuonHLTSeedMVAClassifier'):
        if hasattr(prod, "isFromL1"):
            if (prod.isFromL1 == True):
                if hasattr(prod, "mvaFileBL1"):
                    prod.mvaFileB = prod.mvaFileBL1
                if hasattr(prod, "mvaFileEL1"):
                    prod.mvaFileE = prod.mvaFileEL1
                if hasattr(prod, "mvaScaleMeanBL1"):
                    prod.mvaScaleMeanB = prod.mvaScaleMeanBL1
                if hasattr(prod, "mvaScaleStdBL1"):
                    prod.mvaScaleStdB = prod.mvaScaleStdBL1
                if hasattr(prod, "mvaScaleMeanEL1"):
                    prod.mvaScaleMeanE = prod.mvaScaleMeanEL1
                if hasattr(prod, "mvaScaleStdEL1"):                    
                    prod.mvaScaleStdE = prod.mvaScaleStdEL1                
            else:
                if hasattr(prod, "mvaFileBL2"):
                    prod.mvaFileB = prod.mvaFileBL2
                if hasattr(prod, "mvaFileEL2"):
                    prod.mvaFileE = prod.mvaFileEL2
                if hasattr(prod, "mvaScaleMeanBL2"):
                    prod.mvaScaleMeanB = prod.mvaScaleMeanBL2
                if hasattr(prod, "mvaScaleStdBL2"):
                    prod.mvaScaleStdB = prod.mvaScaleStdBL2
                if hasattr(prod, "mvaScaleMeanEL2"):
                    prod.mvaScaleMeanE = prod.mvaScaleMeanEL2
                if hasattr(prod, "mvaScaleStdEL2"):
                    prod.mvaScaleStdE = prod.mvaScaleStdEL2
                    
    for prod in producers_by_type(process, 'MuonHLTSeedMVAClassifier'):
        delattr(prod,"mvaFileBL1")
        delattr(prod,"mvaFileEL1")
        delattr(prod,"mvaScaleMeanBL1")
        delattr(prod,"mvaScaleStdBL1")
        delattr(prod,"mvaScaleMeanEL1")
        delattr(prod,"mvaScaleStdEL1")
        delattr(prod,"mvaFileBL2")
        delattr(prod,"mvaFileEL2")
        delattr(prod,"mvaScaleMeanBL2")
        delattr(prod,"mvaScaleStdBL2")
        delattr(prod,"mvaScaleMeanEL2")
        delattr(prod,"mvaScaleStdEL2")       
                    
    return process

def customizeHLTfor46135(process):
    """Remove pfRecHitFractionAllocation from PFClusterSoAProducer config"""
    for producer in producers_by_type(process, "PFClusterSoAProducer@alpaka"):
        if hasattr(producer, 'pfRecHitFractionAllocation'):
            delattr(producer, 'pfRecHitFractionAllocation')
    for producer in producers_by_type(process, "alpaka_serial_sync::PFClusterSoAProducer"):
        if hasattr(producer, 'pfRecHitFractionAllocation'):
            delattr(producer, 'pfRecHitFractionAllocation')
    return process

def customizeHLTfor45206(process):

    dqmPixelRecoPathName = None
    for pathName in process.paths_():
        if pathName.startswith('DQM_PixelReconstruction_v'):
            dqmPixelRecoPathName = pathName
            break

    if dqmPixelRecoPathName == None:
        return process

    import copy
    from DQM.SiPixelPhase1Common.SiPixelPhase1RawData_cfi import SiPixelPhase1RawDataConf,SiPixelPhase1RawDataAnalyzer

    # PixelDigiErrors: monitor of SerialSync product
    SiPixelPhase1RawDataConfForCPU = copy.deepcopy(SiPixelPhase1RawDataConf)
    for pset in SiPixelPhase1RawDataConfForCPU:
        pset.topFolderName =  "SiPixelHeterogeneous/PixelErrorsCPU"

    process.hltPixelPhase1MonitorRawDataACPU = SiPixelPhase1RawDataAnalyzer.clone(
        src = "hltSiPixelDigiErrorsSerialSync",
        histograms = SiPixelPhase1RawDataConfForCPU
    )

    # PixelDigiErrors: monitor of GPU product
    SiPixelPhase1RawDataConfForGPU = copy.deepcopy(SiPixelPhase1RawDataConf)
    for pset in SiPixelPhase1RawDataConfForGPU:
        pset.topFolderName =  "SiPixelHeterogeneous/PixelErrorsGPU"

    process.hltPixelPhase1MonitorRawDataAGPU = SiPixelPhase1RawDataAnalyzer.clone(
        src = "hltSiPixelDigiErrors",
        histograms = SiPixelPhase1RawDataConfForGPU
    )

    # PixelDigiErrors: 'Alpaka' comparison
    process.hltPixelDigiErrorsCompareGPUvsCPU = cms.EDProducer('SiPixelPhase1RawDataErrorComparator',
        pixelErrorSrcCPU = cms.InputTag( 'hltSiPixelDigiErrorsSerialSync' ),
        pixelErrorSrcGPU = cms.InputTag( 'hltSiPixelDigiErrors' ),
        topFolderName = cms.string( 'SiPixelHeterogeneous/PixelErrorsCompareGPUvsCPU' )
    )

    # Comparisons below are to change the names of the modules defined in customizeHLTforAlpaka
    process.hltPixelRecHitsSoACompareGPUvsCPU = cms.EDProducer('SiPixelPhase1CompareRecHits',
        pixelHitsReferenceSoA = cms.InputTag('hltSiPixelRecHitsSoASerialSync'),
        pixelHitsTargetSoA = cms.InputTag('hltSiPixelRecHitsSoA'),
        topFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU'),
        minD2cut = cms.double(1.0e-4)
    )

    process.hltPixelTracksSoACompareGPUvsCPU = cms.EDProducer("SiPixelPhase1CompareTracks",
        deltaR2cut = cms.double(0.04),
        minQuality = cms.string('loose'),
        pixelTrackReferenceSoA = cms.InputTag("hltPixelTracksSoASerialSync"),
        pixelTrackTargetSoA = cms.InputTag("hltPixelTracksSoA"),
        topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU'),
        useQualityCut = cms.bool(True)
    )

    process.hltPixelVertexSoACompareGPUvsCPU = cms.EDProducer("SiPixelCompareVertices",
        beamSpotSrc = cms.InputTag("hltOnlineBeamSpot"),
        dzCut = cms.double(1),
        pixelVertexReferenceSoA = cms.InputTag("hltPixelVerticesSoASerialSync"),
        pixelVertexTargetSoA = cms.InputTag("hltPixelVerticesSoA"),
        topFolderName = cms.string('SiPixelHeterogeneous/PixelVertexCompareGPUvsCPU')
    )

    process.HLTDQMPixelReconstruction = cms.Sequence(
        process.hltPixelPhase1MonitorRawDataACPU
      + process.hltPixelPhase1MonitorRawDataAGPU
      + process.hltPixelDigiErrorsCompareGPUvsCPU
      + process.hltPixelRecHitsSoAMonitorCPU
      + process.hltPixelRecHitsSoAMonitorGPU
      + process.hltPixelRecHitsSoACompareGPUvsCPU
      + process.hltPixelTracksSoAMonitorCPU
      + process.hltPixelTracksSoAMonitorGPU
      + process.hltPixelTracksSoACompareGPUvsCPU
      + process.hltPixelVertexSoAMonitorCPU
      + process.hltPixelVertexSoAMonitorGPU
      + process.hltPixelVertexSoACompareGPUvsCPU
    )

    return process

def customizeHLTfor44576(process):
    """Ensure TrackerAdditionalParametersPerDetRcd ESProducer is run when needed"""
    for esprod in esproducers_by_type(process, 'TrackerGeometricDetESModule'):
        process.load("Geometry.TrackerGeometryBuilder.TrackerAdditionalParametersPerDet_cfi")
        break
    return process

# Adding zdc Topology producer
def customizeHLTfor46033(process):
    """Add topology producer for ZDC"""

    for esprod in esproducers_by_type(process, 'ZdcGeometryFromDBEP'):
        process.load("Geometry.ForwardGeometry.zdcTopologyEP_cfi")
        break

    return process

# CMSSW version specific customizations
def customizeHLTforCMSSW(process, menuType="GRun"):

    process = customiseForOffline(process)

    # add call to action function in proper order: newest last!
    # process = customiseFor12718(process)

    process = customizeHLTfor46935(process)
    process = customizeHLTfor47017(process)
    process = customizeHLTfor47079(process)
    process = customizeHLTfor47047(process)
    process = customizeHLTfor47107(process)
    process = customizeHLTfor47191(process)
    process = customizeHLTfor45063(process)
    process = customizeHLTfor46135(process)
    process = customizeHLTfor45206(process)
    process = customizeHLTfor44576(process)
    process = customizeHLTfor46033(process)
    
    return process
