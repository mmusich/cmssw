import FWCore.ParameterSet.Config as cms

from RecoHGCal.TICL.PFTICLProducer import PFTICLProducer as _PFTICLProducer

hltPfTICL = _PFTICLProducer(
    mightGet = cms.optional.untracked.vstring,
    muonSrc = ("hltPhase2L3Muons"),
    pfMuonAlgoParameters = dict(
        cosmicRejectionDistance = 1,
        eventFactorForCosmics = 10,
        eventFractionForCleaning = 0.5,
        eventFractionForRejection = 0.8,
        maxDPtOPt = 1,
        metFactorForCleaning = 4,
        metFactorForFakes = 4,
        metFactorForHighEta = 25,
        metFactorForRejection = 4,
        metSignificanceForCleaning = 3,
        metSignificanceForRejection = 4,
        minEnergyForPunchThrough = 100,
        minMomentumForPunchThrough = 100,
        minPtForPostCleaning = 20,
        ptErrorScale = 8,
        ptFactorForHighEta = 2,
        punchThroughFactor = 3,
        punchThroughMETFactor = 4,
        trackQuality = cms.string('highPurity')
    ),
    ticlCandidateSrc = ("hltTiclTrackstersMerge"),
    timingQualityThreshold = 0.5,
    trackTimeErrorMap = ("tofPID","sigmat0"),
    trackTimeQualityMap = ("mtdTrackQualityMVA","mtdQualMVA"),
    trackTimeValueMap = ("tofPID","t0"),
    useMTDTiming = False,
    useTimingAverage = False
)

from Configuration.ProcessModifiers.ticl_v5_cff import ticl_v5
ticl_v5.toModify(hltPfTICL, ticlCandidateSrc = cms.InputTag('hltTiclCandidate'), isTICLv5 = True)
