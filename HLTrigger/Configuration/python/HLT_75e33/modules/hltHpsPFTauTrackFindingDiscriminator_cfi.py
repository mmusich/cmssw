import FWCore.ParameterSet.Config as cms

from RecoTauTag.RecoTau.PFRecoTauDiscriminationByLeadingObjectPtCut import PFRecoTauDiscriminationByLeadingObjectPtCut as _PFRecoTauDiscriminationByLeadingObjectPtCut

hltHpsPFTauTrackFindingDiscriminator = _PFRecoTauDiscriminationByLeadingObjectPtCut(
    MinPtLeadingObject = 0.0,
    PFTauProducer = ("hltHpsPFTauProducer"),
    Prediscriminants = dict(
        BooleanOperator = cms.string('and')
    ),
    UseOnlyChargedHadrons = True
)
