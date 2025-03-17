import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFProducer.PFBlockProducer import PFBlockProducer as _PFBlockProducer

hltParticleFlowBlock = _PFBlockProducer(
    debug = False,
    elementImporters = [
        dict(
            importerName = 'SuperClusterImporter',
            maximumHoverE = 0.5,
            minPTforBypass = 100.0,
            minSuperClusterPt = 10.0,
            source_eb = ("hltParticleFlowSuperClusterECAL","particleFlowSuperClusterECALBarrel"),
            source_ee = ("hltParticleFlowSuperClusterECAL","particleFlowSuperClusterECALEndcapWithPreshower"),
            hbheRecHitsTag = ("hltHbhereco"),
            maxSeverityHB = 9,
            maxSeverityHE = 9,
            usePFThresholdsFromDB = True,
            superClustersArePF = True
        ),
        dict(
            DPtOverPtCuts_byTrackAlgo = cms.vdouble(
                10.0, 10.0, 10.0, 10.0, 10.0,
                5.0
            ),
            NHitCuts_byTrackAlgo = cms.vuint32(
                3, 3, 3, 3, 3,
                3
            ),
            cleanBadConvertedBrems = True,
            importerName = 'GeneralTracksImporter',
            maxDPtOPt = 1.0,
            muonMaxDPtOPt = 1,
            muonSrc = ("hltPhase2L3Muons"),
            source = ("hltPfTrack"),
            trackQuality = 'highPurity',
            useIterativeTracking = True,
            vetoEndcap = True,
            vetoMode = 2,
            vetoSrc = ("hltPfTICL")
        ),
        dict(
            BCtoPFCMap = ("hltParticleFlowSuperClusterECAL","PFClusterAssociationEBEE"),
            importerName = 'ECALClusterImporter',
            source = ("hltParticleFlowClusterECAL")
        ),
        dict(
            importerName = 'GenericClusterImporter',
            source = ("hltParticleFlowClusterHCAL")
        ),
        dict(
            importerName = 'GenericClusterImporter',
            source = ("hltParticleFlowBadHcalPseudoCluster")
        ),
        dict(
            importerName = 'GenericClusterImporter',
            source = ("hltParticleFlowClusterHO")
        ),
        dict(
            importerName = 'GenericClusterImporter',
            source = ("hltParticleFlowClusterHF")
        )
    ],
    linkDefinitions = [
        dict(
            linkType = 'TRACK:ECAL',
            linkerName = 'TrackAndECALLinker',
            useKDTree = True
        ),
        dict(
            linkType = 'TRACK:HCAL',
            linkerName = 'TrackAndHCALLinker',
            nMaxHcalLinksPerTrack = 1,
            trajectoryLayerEntrance = 'HCALEntrance',
            trajectoryLayerExit = 'HCALExit',
            useKDTree = True
        ),
        dict(
            linkType = 'TRACK:HO',
            linkerName = 'TrackAndHOLinker',
            useKDTree = False
        ),
        dict(
            linkType = 'ECAL:HCAL',
            linkerName = 'ECALAndHCALLinker',
            minAbsEtaEcal = 2.5,
            useKDTree = False
        ),
        dict(
            linkType = 'HCAL:HO',
            linkerName = 'HCALAndHOLinker',
            useKDTree = False
        ),
        dict(
            linkType = 'HFEM:HFHAD',
            linkerName = 'HFEMAndHFHADLinker',
            useKDTree = False
        ),
        dict(
            linkType = 'TRACK:TRACK',
            linkerName = 'TrackAndTrackLinker',
            useKDTree = False
        ),
        dict(
            linkType = 'ECAL:ECAL',
            linkerName = 'ECALAndECALLinker',
            useKDTree = False
        ),
        dict(
            linkType = 'ECAL:BREM',
            linkerName = 'ECALAndBREMLinker',
            useKDTree = False
        ),
        dict(
            linkType = 'HCAL:BREM',
            linkerName = 'HCALAndBREMLinker',
            useKDTree = False
        ),
        dict(
            SuperClusterMatchByRef = True,
            linkType = 'SC:ECAL',
            linkerName = 'SCAndECALLinker',
            useKDTree = False
        ),
        dict(
            linkType = 'TRACK:HFEM',
            linkerName = 'TrackAndHCALLinker',
            nMaxHcalLinksPerTrack = -1,
            trajectoryLayerEntrance = 'VFcalEntrance',
            trajectoryLayerExit = '',
            useKDTree = True
        ),
        dict(
            linkType = 'TRACK:HFHAD',
            linkerName = 'TrackAndHCALLinker',
            nMaxHcalLinksPerTrack = -1,
            trajectoryLayerEntrance = 'VFcalEntrance',
            trajectoryLayerExit = '',
            useKDTree = True
        )
    ],
    verbose = cms.untracked.bool(False)
)
