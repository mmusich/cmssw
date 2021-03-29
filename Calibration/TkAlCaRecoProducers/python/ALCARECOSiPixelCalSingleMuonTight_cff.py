import FWCore.ParameterSet.Config as cms

import copy
from HLTrigger.HLTfilters.hltHighLevel_cfi import *
# AlCaReco for track based calibration using min. bias events
ALCARECOSiPixelCalSingleMuonTightHLTFilter = copy.deepcopy(hltHighLevel)
ALCARECOSiPixelCalSingleMuonTightHLTFilter.andOr = True ## choose logical OR between Triggerbits
ALCARECOSiPixelCalSingleMuonTightHLTFilter.throw = False ## dont throw on unknown path names
#ALCARECOSiPixelCalSingleMuonTightHLTFilter.eventSetupPathsKey = 'SiPixelCalSingleMuonTight'
ALCARECOSiPixelCalSingleMuonTightHLTFilter.HLTPaths = ["HLT_*"]

# Filter on the DCS partitions
import DPGAnalysis.Skims.skim_detstatus_cfi
ALCARECOSiPixelCalSingleMuonTightDCSFilter = DPGAnalysis.Skims.skim_detstatus_cfi.dcsstatus.clone(
    DetectorType = cms.vstring('TIBTID','TOB','TECp','TECm','BPIX','FPIX',
                               'DT0','DTp','DTm','CSCp','CSCm'),
    ApplyFilter  = cms.bool(True),
    AndOr        = cms.bool(True),
    DebugOn      = cms.untracked.bool(False)
)

import Alignment.CommonAlignmentProducer.TkAlMuonSelectors_cfi
ALCARECOSiPixelCalSingleMuonTightGoodMuons = Alignment.CommonAlignmentProducer.TkAlMuonSelectors_cfi.TkAlGoodIdMuonSelector.clone()
ALCARECOSiPixelCalSingleMuonTightRelCombIsoMuons = Alignment.CommonAlignmentProducer.TkAlMuonSelectors_cfi.TkAlRelCombIsoMuonSelector.clone(
    src = 'ALCARECOSiPixelCalSingleMuonTightGoodMuons'
)

import Alignment.CommonAlignmentProducer.AlignmentTrackSelector_cfi
ALCARECOSiPixelCalSingleMuonTight = Alignment.CommonAlignmentProducer.AlignmentTrackSelector_cfi.AlignmentTrackSelector.clone(
    filter = True, ##do not store empty events
    applyBasicCuts = True,
    ptMin = 2.0, ##GeV 
    etaMin = -3.5,
    etaMax = 3.5,
    nHitMin = 0
)

ALCARECOSiPixelCalSingleMuonTight.GlobalSelector.muonSource = 'ALCARECOSiPixelCalSingleMuonTightRelCombIsoMuons'
# Isolation is shifted to the muon preselection, and then applied intrinsically if applyGlobalMuonFilter = True
ALCARECOSiPixelCalSingleMuonTight.GlobalSelector.applyIsolationtest = False
ALCARECOSiPixelCalSingleMuonTight.GlobalSelector.minJetDeltaR = 0.1
ALCARECOSiPixelCalSingleMuonTight.GlobalSelector.applyGlobalMuonFilter = True

ALCARECOSiPixelCalSingleMuonTight.TwoBodyDecaySelector.applyMassrangeFilter = False
ALCARECOSiPixelCalSingleMuonTight.TwoBodyDecaySelector.applyChargeFilter = False
ALCARECOSiPixelCalSingleMuonTight.TwoBodyDecaySelector.applyAcoplanarityFilter = False

# unassociated close-by clusters
from RecoVertex.BeamSpotProducer.BeamSpot_cff import *
from RecoTracker.IterativeTracking.InitialStep_cff import *
from RecoTracker.Configuration.RecoTrackerP5_cff import *
from RecoTracker.TrackProducer.TrackRefitter_cfi import *

ALCARECOSiPixelCalSingleMuonTightTracksRefit = TrackRefitter.clone(src = cms.InputTag("ALCARECOSiPixelCalSingleMuonTight"),
                                                                   NavigationSchool = cms.string("")
                                                                   )

closebyPixelClusters = cms.EDProducer('NearbyPixelClusterProducer',
                                      clusterCollection = cms.InputTag('siPixelClusters'),
                                      trajectoryInput = cms.InputTag('ALCARECOSiPixelCalSingleMuonTightTracksRefit')
                                      )

ALCARECOSiPixelCalSingleMuonTightOffTrackClusters = cms.Sequence(ALCARECOSiPixelCalSingleMuonTightTracksRefit +
                                                                 closebyPixelClusters)

seqALCARECOSiPixelCalSingleMuonTight = cms.Sequence(offlineBeamSpot+
                                                    ALCARECOSiPixelCalSingleMuonTightHLTFilter+
                                                    ALCARECOSiPixelCalSingleMuonTightDCSFilter+
                                                    ALCARECOSiPixelCalSingleMuonTightGoodMuons+
                                                    ALCARECOSiPixelCalSingleMuonTightRelCombIsoMuons+
                                                    ALCARECOSiPixelCalSingleMuonTight+
                                                    ALCARECOSiPixelCalSingleMuonTightOffTrackClusters)


