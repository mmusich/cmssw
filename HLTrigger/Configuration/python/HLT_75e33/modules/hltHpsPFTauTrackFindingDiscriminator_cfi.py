import FWCore.ParameterSet.Config as cms

from RecoTauTag.RecoTau.PFRecoTauDiscriminationByLeadingObjectPtCut import PFRecoTauDiscriminationByLeadingObjectPtCut as _PFRecoTauDiscriminationByLeadingObjectPtCut

hltHpsPFTauTrackFindingDiscriminator = _PFRecoTauDiscriminationByLeadingObjectPtCut(
    MinPtLeadingObject = cms.double(0.0),
    PFTauProducer = cms.InputTag("hltHpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    UseOnlyChargedHadrons = cms.bool(True)
)
