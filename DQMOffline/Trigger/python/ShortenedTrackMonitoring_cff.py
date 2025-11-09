import FWCore.ParameterSet.Config as cms
from DQMServices.Core.DQMEDAnalyzer import DQMEDAnalyzer

from RecoTracker.FinalTrackSelectors.SingleLongTrackProducer_cfi import *
hltSingleLongTrackProducer = singleLongTrackProducer.clone(
    allTracks = "hltMergedTracks",
    matchMuons = "hltIterL3MuonsNoID",
    requiredDr= 0.01,
    minNumberOfLayers = 10,
    onlyValidHits = True,
    debug = False,
    minPt = 15.0,
    maxEta = 2.2,
    maxDxy = 0.02,
    maxDz = 0.5,
    PrimaryVertex = "hltPixelVertices")

from RecoTracker.FinalTrackSelectors.trackerTrackHitFilter_cfi import trackerTrackHitFilter as _trackerTrackHitFilter
hltShortTrackCandidates = _trackerTrackHitFilter.clone(src = "hltSingleLongTrackProducer",                                                       
                                                       truncateTracks = True,
                                                       replaceWithInactiveHits = True,
                                                       rejectBadStoNHits = True,
                                                       usePixelQualityFlag = True)

from Configuration.Eras.Modifier_phase2_tracker_cff import phase2_tracker
phase2_tracker.toModify(hltShortTrackCandidates,
                        isPhase2 = True)

hltShortTrackCandidates3 = hltShortTrackCandidates.clone(minimumHits = 3,
                                                         layersRemaining = 3)

hltShortTrackCandidates4 = hltShortTrackCandidates.clone(minimumHits = 4,
                                                         layersRemaining = 4)

hltShortTrackCandidates5 = hltShortTrackCandidates.clone(minimumHits = 5,
                                                         layersRemaining = 5)

hltShortTrackCandidates6 = hltShortTrackCandidates.clone(minimumHits = 6,
                                                         layersRemaining = 6)

hltShortTrackCandidates7 = hltShortTrackCandidates.clone(minimumHits = 7,
                                                         layersRemaining = 7)

hltShortTrackCandidates8 = hltShortTrackCandidates.clone(minimumHits = 8,
                                                         layersRemaining = 8)

import RecoTracker.TrackProducer.CTFFinalFitWithMaterial_cff
hltRefittedShortTracks = RecoTracker.TrackProducer.CTFFinalFitWithMaterial_cff.ctfWithMaterialTracks.clone(src = 'hltShortTrackCandidates')

hltRefittedShortTracks3 = hltRefittedShortTracks.clone(src = 'hltShortTrackCandidates3')
hltRefittedShortTracks4 = hltRefittedShortTracks.clone(src = 'hltShortTrackCandidates4')
hltRefittedShortTracks5 = hltRefittedShortTracks.clone(src = 'hltShortTrackCandidates5')
hltRefittedShortTracks6 = hltRefittedShortTracks.clone(src = 'hltShortTrackCandidates6')
hltRefittedShortTracks7 = hltRefittedShortTracks.clone(src = 'hltShortTrackCandidates7')
hltRefittedShortTracks8 = hltRefittedShortTracks.clone(src = 'hltShortTrackCandidates8')

from DQM.TrackingMonitorSource.shortenedTrackResolution_cfi import shortenedTrackResolution as _shortenedTrackResolution
hltTrackingResolution = _shortenedTrackResolution.clone(folderName           = "HLT/Tracking/ShortTrackResolution",
                                                        hitsRemainInput      = ["3","4","5","6","7","8"],
                                                        minTracksEtaInput    = 0.0,
                                                        maxTracksEtaInput    = 2.2,
                                                        minTracksPtInput     = 15.0,
                                                        maxTracksPtInput     = 99999.9,
                                                        maxDrInput           = 0.01,
                                                        tracksInputTag       = "hltSingleLongTrackProducer",
                                                        tracksRerecoInputTag = ["hltRefittedShortTracks3",
                                                                                "hltRefittedShortTracks4",
                                                                                "hltRefittedShortTracks5",
                                                                                "hltRefittedShortTracks6",
                                                                                "hltRefittedShortTracks7",
                                                                                "hltRefittedShortTracks8"])

hltShortTrackResolution3to8 = cms.Sequence(hltSingleLongTrackProducer *
                                           hltShortTrackCandidates3 *
                                           hltShortTrackCandidates4 *
                                           hltShortTrackCandidates5 *
                                           hltShortTrackCandidates6 *
                                           hltShortTrackCandidates7 *
                                           hltShortTrackCandidates8 *
                                           hltRefittedShortTracks3 *
                                           hltRefittedShortTracks4 *
                                           hltRefittedShortTracks5 *
                                           hltRefittedShortTracks6 *
                                           hltRefittedShortTracks7 *
                                           hltRefittedShortTracks8 *
                                           hltTrackingResolution)
