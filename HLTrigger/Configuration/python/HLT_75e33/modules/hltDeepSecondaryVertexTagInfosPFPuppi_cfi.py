import FWCore.ParameterSet.Config as cms

from RecoBTag.SecondaryVertex.CandSecondaryVertexProducer import CandSecondaryVertexProducer as _CandSecondaryVertexProducer

hltDeepSecondaryVertexTagInfosPFPuppi = _CandSecondaryVertexProducer(
    beamSpotTag = ("hltOnlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = ("hltDeepInclusiveMergedVerticesPF"),
    extSVDeltaRToJet = 0.3,
    minimumTrackWeight = 0.5,
    trackIPTagInfos = ("hltDeepBLifetimeTagInfosPFPuppi"),
    trackSelection = dict(
        a_dR = -0.001053,
        a_pT = 0.005263,
        b_dR = 0.6263,
        b_pT = 0.3684,
        jetDeltaRMax = 0.3,
        maxDecayLen = 99999.9,
        maxDistToAxis = 0.2,
        max_pT = 500,
        max_pT_dRcut = 0.1,
        max_pT_trackPTcut = 3,
        min_pT = 120,
        min_pT_dRcut = 0.5,
        normChi2Max = 99999.9,
        pixelHitsMin = 2,
        ptMin = 1.0,
        qualityClass = cms.string('any'),
        sip2dSigMax = 99999.9,
        sip2dSigMin = -99999.9,
        sip2dValMax = 99999.9,
        sip2dValMin = -99999.9,
        sip3dSigMax = 99999.9,
        sip3dSigMin = -99999.9,
        sip3dValMax = 99999.9,
        sip3dValMin = -99999.9,
        totalHitsMin = 3,
        useVariableJTA = False
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = True,
    usePVError = True,
    vertexCuts = dict(
        distSig2dMax = 99999.9,
        distSig2dMin = 2.0,
        distSig3dMax = 99999.9,
        distSig3dMin = -99999.9,
        distVal2dMax = 2.5,
        distVal2dMin = 0.01,
        distVal3dMax = 99999.9,
        distVal3dMin = -99999.9,
        fracPV = 0.79,
        massMax = 6.5,
        maxDeltaRToJetAxis = 0.4,
        minimumTrackWeight = 0.5,
        multiplicityMin = 2,
        useTrackWeights = True,
        v0Filter = dict(
            k0sMassWindow = 0.05
        )
    ),
    vertexReco = dict(
        finder = cms.string('avr'),
        minweight = 0.5,
        primcut = 1.8,
        seccut = 6.0,
        smoothing = False,
        weightthreshold = 0.001
    ),
    vertexSelection = dict(
        sortCriterium = cms.string('dist3dError')
    ),
    weights = ("hltPFPuppi")
)
