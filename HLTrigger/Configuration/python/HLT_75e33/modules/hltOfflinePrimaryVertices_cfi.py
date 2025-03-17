import FWCore.ParameterSet.Config as cms

from CommonTools.RecoAlgos.RecoChargedRefCandidatePrimaryVertexSorter import RecoChargedRefCandidatePrimaryVertexSorter as _RecoChargedRefCandidatePrimaryVertexSorter

hltOfflinePrimaryVertices = _RecoChargedRefCandidatePrimaryVertexSorter(
    assignment = dict(
        DzCutForChargedFromPUVtxs = 0.2,
        EtaMinUseDz = -1,
        NumOfPUVtxsForCharged = 0,
        OnlyUseFirstDz = False,
        PtMaxCharged = -1,
        maxDistanceToJetAxis = 0.07,
        maxDtSigForPrimaryAssignment = 4.0,
        maxDxyForJetAxisAssigment = 0.1,
        maxDxyForNotReconstructedPrimary = 0.01,
        maxDxySigForNotReconstructedPrimary = 2,
        maxDzErrorForPrimaryAssignment = 0.05,
        maxDzForJetAxisAssigment = 0.1,
        maxDzForPrimaryAssignment = 0.1,
        maxDzSigForPrimaryAssignment = 5.0,
        maxJetDeltaR = 0.5,
        minJetPt = 25,
        preferHighRanked = False,
        useTiming = False,
        useVertexFit = True
    ),
    jets = ("hltAk4CaloJetsForTrk"),
    particles = ("hltTrackRefsForJetsBeforeSorting"),
    produceAssociationToOriginalVertices = False,
    produceNoPileUpCollection = False,
    producePileUpCollection = False,
    produceSortedVertices = True,
    qualityForPrimary = 3,
    sorting = dict(

    ),
    trackTimeResoTag = (""),
    trackTimeTag = (""),
    usePVMET = True,
    vertices = ("hltUnsortedOfflinePrimaryVertices")
)
