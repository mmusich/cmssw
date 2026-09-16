import FWCore.ParameterSet.Config as cms

# Port of GRun hltDoubleMu43LowMassL3Filtered to the Phase-2 muon collections.
# Parameter list matches the fillDescriptions of HLTMuonDimuonL3Filter.
# Physics cuts are identical to GRun; only CandTag / PreviousCandTag / L1CandTag /
# InputLinks / PreviousCandIsL2 / ChargeOpt are changed.
hltDoubleMu43LowMassL3Filtered = cms.EDFilter("HLTMuonDimuonL3Filter",
    saveTags = cms.bool(True),
    BeamSpotTag = cms.InputTag("hltOnlineBeamSpot"),
    CandTag = cms.InputTag("hltPhase2L3MuonCandidates"),
    PreviousCandTag = cms.InputTag("hltDoubleTkMuon43LowMassL1TkMuonFilter"),
    L1CandTag = cms.InputTag("hltDoubleTkMuon43LowMassL1TkMuonFilter"),
    inputMuonCollection = cms.InputTag(""),
    PreviousCandIsL2 = cms.bool(False),
    FastAccept = cms.bool(False),
    MinN = cms.int32(1),
    MaxEta = cms.double(2.5),
    MinNhits = cms.int32(0),
    MaxDr = cms.double(2.0),
    MaxDz = cms.double(9999.0),
    ChargeOpt = cms.int32(-1),                # GRun uses 0 because L1 already requires OS
    MinPtPair = cms.vdouble(4.9),
    MaxPtPair = cms.vdouble(1.0E125),
    MinPtMax = cms.vdouble(4.0),
    MinPtMin = cms.vdouble(3.0),
    MaxPtMin = cms.vdouble(1.0E125),
    MinInvMass = cms.vdouble(0.2),
    MaxInvMass = cms.vdouble(8.5),
    MinDiMuonDeltaR = cms.double(-1.0),
    MinAcop = cms.double(-999.0),
    MaxAcop = cms.double(999.0),
    MinPtBalance = cms.double(-1.0),
    MaxPtBalance = cms.double(999999.0),
    NSigmaPt = cms.double(0.0),
    MaxDCAMuMu = cms.double(0.5),
    MaxRapidityPair = cms.double(999999.0),
    CutCowboys = cms.bool(False),
    InputLinks = cms.InputTag(""),            # as in hltL3fL1DoubleMu155fPreFiltered27
    L1MatchingdR = cms.double(0.3),
    MatchToPreviousCand = cms.bool(True),
    # L1 propagation settings (defaults; same as the Phase-2 HLTMuonL3PreFilter modules)
    useSimpleGeometry = cms.bool(True),
    useStation2 = cms.bool(True),
    fallbackToME1 = cms.bool(False),
    cosmicPropagationHypothesis = cms.bool(False),
    useMB2InOverlap = cms.bool(False),
    useTrack = cms.string("tracker"),
    useState = cms.string("atVertex"),
    propagatorAlong = cms.ESInputTag("", "hltESPSteppingHelixPropagatorAlong"),
    propagatorAny = cms.ESInputTag("", "SteppingHelixPropagatorAny"),
    propagatorOpposite = cms.ESInputTag("", "hltESPSteppingHelixPropagatorOpposite"),
)
