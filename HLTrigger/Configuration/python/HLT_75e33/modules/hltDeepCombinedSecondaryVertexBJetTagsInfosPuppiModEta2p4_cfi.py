import FWCore.ParameterSet.Config as cms

from RecoBTag.Combined.DeepNNTagInfoProducer import DeepNNTagInfoProducer as _DeepNNTagInfoProducer

hltDeepCombinedSecondaryVertexBJetTagsInfosPuppiModEta2p4 = _DeepNNTagInfoProducer(
    computer = dict(
        SoftLeptonFlip = False,
        charmCut = 1.5,
        correctVertexMass = True,
        minimumTrackWeight = 0.5,
        pseudoMultiplicityMin = 2,
        pseudoVertexV0Filter = dict(
            k0sMassWindow = 0.05
        ),
        trackFlip = False,
        trackMultiplicityMin = 2,
        trackPairV0Filter = dict(
            k0sMassWindow = 0.03
        ),
        trackPseudoSelection = dict(
            a_dR = -0.001053,
            a_pT = 0.005263,
            b_dR = 0.6263,
            b_pT = 0.3684,
            jetDeltaRMax = 0.3,
            maxDecayLen = 5,
            maxDistToAxis = 0.07,
            max_pT = 500,
            max_pT_dRcut = 0.1,
            max_pT_trackPTcut = 3,
            min_pT = 120,
            min_pT_dRcut = 0.5,
            normChi2Max = 99999.9,
            pixelHitsMin = 0,
            ptMin = 0.0,
            qualityClass = cms.string('any'),
            sip2dSigMax = 99999.9,
            sip2dSigMin = 2.0,
            sip2dValMax = 99999.9,
            sip2dValMin = -99999.9,
            sip3dSigMax = 99999.9,
            sip3dSigMin = -99999.9,
            sip3dValMax = 99999.9,
            sip3dValMin = -99999.9,
            totalHitsMin = 3,
            useVariableJTA = False
        ),
        trackSelection = dict(
            a_dR = -0.001053,
            a_pT = 0.005263,
            b_dR = 0.6263,
            b_pT = 0.3684,
            jetDeltaRMax = 0.3,
            maxDecayLen = 5,
            maxDistToAxis = 0.07,
            max_pT = 500,
            max_pT_dRcut = 0.1,
            max_pT_trackPTcut = 3,
            min_pT = 120,
            min_pT_dRcut = 0.5,
            normChi2Max = 99999.9,
            pixelHitsMin = 2,
            ptMin = 0.0,
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
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = True,
        vertexFlip = False
    ),
    svTagInfos = ("hltDeepSecondaryVertexTagInfosPFPuppiModEta2p4")
)
