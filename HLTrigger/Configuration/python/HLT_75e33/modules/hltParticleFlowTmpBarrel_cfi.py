import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFProducer.PFProducer import PFProducer as _PFProducer

hltParticleFlowTmpBarrel = _PFProducer(
    GedElectronValueMap = ("gedGsfElectronValueMapsTmp"),
    GedPhotonValueMap = ("gedPhotonsTmp","valMapPFEgammaCandToPhoton"),
    PFEGammaCandidates = ("particleFlowEGamma"),
    PFEGammaFiltersParameters = dict(
        electronDnnBkgThresholds = dict(
            electronDnnBkgHighPtBarrelThr = 0.8,
            electronDnnBkgHighPtEndcapThr = 0.75,
            electronDnnBkgLowPtThr = 0.75
        ),
        electronDnnThresholds = dict(
            electronDnnHighPtBarrelThr = 0.068,
            electronDnnHighPtEndcapThr = 0.056,
            electronDnnLowPtThr = 0.075
        ),
        electron_ecalDrivenHademPreselCut = 0.15,
        electron_iso_combIso_barrel = 10,
        electron_iso_combIso_endcap = 10,
        electron_iso_mva_barrel = -0.1875,
        electron_iso_mva_endcap = -0.1075,
        electron_iso_pt = 10,
        electron_maxElePtForOnlyMVAPresel = 50,
        electron_missinghits = 1,
        electron_noniso_mvaCut = -0.1,
        electron_protectionsForBadHcal = dict(
            dEta = [0.0064, 0.01264],
            dPhi = [0.0547, 0.0394],
            eInvPInv = [0.184, 0.0721],
            enableProtections = False,
            full5x5_sigmaIetaIeta = [0.0106, 0.0387]
        ),
        electron_protectionsForJetMET = dict(
            maxDPhiIN = 0.1,
            maxE = 50,
            maxEcalEOverPRes = 0.2,
            maxEcalEOverP_1 = 0.5,
            maxEcalEOverP_2 = 0.2,
            maxEeleOverPout = 0.2,
            maxEeleOverPoutRes = 0.5,
            maxEleHcalEOverEcalE = 0.1,
            maxHcalE = 10,
            maxHcalEOverEcalE = 0.1,
            maxHcalEOverP = 1,
            maxNtracks = 3,
            maxTrackPOverEele = 1
        ),
        photonDnnThresholds = dict(
            photonDnnBarrelThr = 0.22,
            photonDnnEndcapThr = 0.35
        ),
        photon_HoE = 0.05,
        photon_MinEt = 10,
        photon_SigmaiEtaiEta_barrel = 0.0125,
        photon_SigmaiEtaiEta_endcap = 0.034,
        photon_combIso = 10,
        photon_protectionsForBadHcal = dict(
            enableProtections = False,
            solidConeTrkIsoOffset = 10,
            solidConeTrkIsoSlope = 0.3
        ),
        photon_protectionsForJetMET = dict(
            sumPtTrackIso = 4,
            sumPtTrackIsoSlope = 0.001
        ),
        useEBModelInGap = True,
        useElePFidDnn = False,
        usePhotonPFidDnn = False
    ),
    PFHFCleaningParameters = dict(
        maxDeltaPhiPt = 7,
        maxSignificance = 2.5,
        minDeltaMet = 0.4,
        minHFCleaningPt = 5,
        minSignificance = 2.5,
        minSignificanceReduction = 1.4
    ),
    PFMuonAlgoParameters = dict(
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
    blocks = ("hltParticleFlowBlock"),
    calibHF_a_EMHAD = cms.vdouble(
        1, 1, 1, 1, 1,
        1, 1, 1, 1, 1
    ),
    calibHF_a_EMonly = cms.vdouble(
        1, 1, 1, 1, 1,
        1, 1, 1, 1, 1
    ),
    calibHF_b_EMHAD = cms.vdouble(
        1, 1, 1, 1, 1,
        1, 1, 1, 1, 1
    ),
    calibHF_b_HADonly = cms.vdouble(
        1, 1, 1, 1, 1,
        1, 1, 1, 1, 1
    ),
    calibHF_eta_step = cms.vdouble(
        0, 2.9, 3, 3.2, 4.2,
        4.4, 4.6, 4.8, 5.2, 5.4
    ),
    calibHF_use = False,
    calibrationsLabel = cms.string(''),
    cleanedHF = cms.VInputTag("hltParticleFlowRecHitHF:Cleaned", "hltParticleFlowClusterHF:Cleaned"),
    debug = cms.untracked.bool(False),
    dptRel_DispVtx = 10,
    egammaElectrons = ("mvaElectrons"),
    factors_45 = [10, 100],
    goodPixelTrackDeadHcal_chi2n = 2,
    goodPixelTrackDeadHcal_dxy = 0.02,
    goodPixelTrackDeadHcal_dz = 0.05,
    goodPixelTrackDeadHcal_maxLost3Hit = 0,
    goodPixelTrackDeadHcal_maxLost4Hit = 1,
    goodPixelTrackDeadHcal_maxPt = 50,
    goodPixelTrackDeadHcal_minEta = 2.3,
    goodPixelTrackDeadHcal_ptErrRel = 1,
    goodTrackDeadHcal_chi2n = 5,
    goodTrackDeadHcal_dxy = 0.5,
    goodTrackDeadHcal_layers = 4,
    goodTrackDeadHcal_ptErrRel = 0.2,
    goodTrackDeadHcal_validFr = 0.5,
    iCfgCandConnector = dict(
        bCalibPrimary = True,
        bCorrect = True,
        dptRel_MergedTrack = 5,
        dptRel_PrimaryTrack = 10,
        nuclCalibFactors = [0.8, 0.15, 0.5, 0.5, 0.05],
        ptErrorSecondary = 1
    ),
    mightGet = cms.optional.untracked.vstring,
    muon_ECAL = [0.5, 0.5],
    muon_HCAL = [3, 3],
    muon_HO = [0.9, 0.9],
    muons = ("hltPhase2L3Muons"),
    nsigma_TRACK = 1,
    pf_nsigma_ECAL = 0,
    pf_nsigma_HCAL = 1,
    pf_nsigma_HFEM = 1,
    pf_nsigma_HFHAD = 1,
    postHFCleaning = False,
    postMuonCleaning = True,
    pt_Error = 1,
    rejectTracks_Bad = True,
    rejectTracks_Step45 = True,
    resolHF_square = [7.834401, 0.012996, 0],
    useCalibrationsFromDB = True,
    useEGammaElectrons = False,
    useEGammaFilters = False,
    useHO = True,
    usePFConversions = False,
    usePFDecays = False,
    usePFNuclearInteractions = False,
    useProtectionsForJetMET = False,
    useVerticesForNeutral = True,
    verbose = cms.untracked.bool(False),
    vertexCollection = ("hltOfflinePrimaryVertices"),
    vetoEndcap = True,
    vetoes = cms.InputTag({"hltPfTICL"})
)
