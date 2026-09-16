import FWCore.ParameterSet.Config as cms

# L1 seed for HLT_DoubleMu4_3_LowMass_FromL1TkMuon: OR of the Phase-2 L1 low-mass
# dimuon algorithms (analogue of GRun hltL1sDoubleMuForLowMassInclusive).
# The collection1/collection2 cuts only select which GMTTkMuons are stored in the
# filter product (for downstream L1 matching); the algorithm decision itself
# (SQ quality, opposite sign, dR / mass) is taken from l1tGTAlgoBlockProducer.
# NOTE: check the exact algo names against the L1 menu in
#       L1Trigger/Phase2L1GT/python/l1tGTMenu_*_cff.py
def _tkMu(minPt, maxAbsEta):
    return cms.PSet(
        objectType = cms.string("GMTTkMuons"),
        minPt = cms.double(minPt),
        maxAbsEta = cms.double(maxAbsEta),
    )

hltL1TkDoubleMuForLowMassInclusive = cms.EDFilter("HLTP2GTDoubleObjectFilter",
    saveTags = cms.bool(True),
    l1GTAlgoBlockTag = cms.InputTag("l1tGTAlgoBlockProducer"),
    l1GTAlgos = cms.VPSet(
        cms.PSet(
            name = cms.string("pDoubleTkMuon_4_4er2p0SQ_OS_dR_Max1p2"),
            collection1 = _tkMu(4.0, 2.0),
            collection2 = _tkMu(4.0, 2.0),
            minDR = cms.double(0.0),
            maxDR = cms.double(1.2),
            minDEta = cms.double(-1.0),
            minDPhi = cms.double(-1.0),
            minInvMass = cms.double(0.0),
            maxInvMass = cms.double(1.0e9),
        ),
        cms.PSet(
            name = cms.string("pDoubleTkMuon_4p5er2p0SQ_OS_Mass7to18"),
            collection1 = _tkMu(4.5, 2.0),
            collection2 = _tkMu(4.5, 2.0),
            minDR = cms.double(0.0),
            maxDR = cms.double(1.0e9),
            minDEta = cms.double(-1.0),
            minDPhi = cms.double(-1.0),
            minInvMass = cms.double(7.0),
            maxInvMass = cms.double(18.0),
        ),
        cms.PSet(
            name = cms.string("pDoubleTkMuon0er1p5_SQ_OS_dR_Max1p4"),
            collection1 = _tkMu(0.0, 1.5),
            collection2 = _tkMu(0.0, 1.5),
            minDR = cms.double(0.0),
            maxDR = cms.double(1.4),
            minDEta = cms.double(-1.0),
            minDPhi = cms.double(-1.0),
            minInvMass = cms.double(0.0),
            maxInvMass = cms.double(1.0e9),
        ),
    ),
)
