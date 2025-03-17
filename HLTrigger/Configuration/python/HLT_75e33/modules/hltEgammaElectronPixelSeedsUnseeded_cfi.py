import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaElectronProducers.ElectronNHitSeedProducer import ElectronNHitSeedProducer as _ElectronNHitSeedProducer

hltEgammaElectronPixelSeedsUnseeded = _ElectronNHitSeedProducer(
    beamSpot = ("hltOnlineBeamSpot"),
    initialSeeds = ("hltElePixelSeedsCombinedUnseeded"),
    matcherConfig = dict(
        detLayerGeom = ("","GlobalDetLayerGeometry"),
        enableHitSkipping = True,
        matchingCuts = [
            dict(
                dPhiMaxHighEt = cms.vdouble(0.05),
                dPhiMaxHighEtThres = cms.vdouble(20.0),
                dPhiMaxLowEtGrad = cms.vdouble(-0.002),
                dRZMaxHighEt = cms.vdouble(9999.0),
                dRZMaxHighEtThres = cms.vdouble(0.0),
                dRZMaxLowEtGrad = cms.vdouble(0.0),
                version = 2
            ),
            dict(
                dPhiMaxHighEt = cms.vdouble(0.003),
                dPhiMaxHighEtThres = cms.vdouble(0.0),
                dPhiMaxLowEtGrad = cms.vdouble(0.0),
                dRZMaxHighEt = cms.vdouble(0.05),
                dRZMaxHighEtThres = cms.vdouble(30.0),
                dRZMaxLowEtGrad = cms.vdouble(-0.002),
                etaBins = cms.vdouble(),
                version = 2
            ),
            dict(
                dPhiMaxHighEt = cms.vdouble(0.003),
                dPhiMaxHighEtThres = cms.vdouble(0.0),
                dPhiMaxLowEtGrad = cms.vdouble(0.0),
                dRZMaxHighEt = cms.vdouble(0.05),
                dRZMaxHighEtThres = cms.vdouble(30.0),
                dRZMaxLowEtGrad = cms.vdouble(-0.002),
                etaBins = cms.vdouble(),
                version = 2
            )
        ],
        minNrHits = [2, 3],
        minNrHitsValidLayerBins = [4],
        navSchool = ("","SimpleNavigationSchool"),
        requireExactMatchCount = False,
        useParamMagFieldIfDefined = True,
        useRecoVertex = False
    ),
    measTkEvt = ("hltMeasurementTrackerEvent"),
    superClusters = ["hltEgammaSuperClustersToPixelMatchUnseeded"],
    vertices = ("")
)
