import FWCore.ParameterSet.Config as cms

##################################################################
# Exact same configuration as TkAlZMuMu
#################################################################
import Alignment.CommonAlignmentProducer.ALCARECOTkAlZMuMu_cff as confALCARECOTkAlZMuMu
ALCARECOTkAlZMuMuAndVertexHLT = confALCARECOTkAlZMuMu.ALCARECOTkAlZMuMuHLT.clone()
ALCARECOTkAlZMuMuAndVertexDCSFilter = confALCARECOTkAlZMuMu.ALCARECOTkAlZMuMuDCSFilter.clone()
ALCARECOTkAlZMuMuAndVertexGoodMuons = confALCARECOTkAlZMuMu.ALCARECOTkAlZMuMuGoodMuons.clone()
ALCARECOTkAlZMuMuAndVertexRelCombIsoMuons = confALCARECOTkAlZMuMu.ALCARECOTkAlZMuMuRelCombIsoMuons.clone(src = 'ALCARECOTkAlZMuMuAndVertexGoodMuons')
ALCARECOTkAlZMuMuAndVertex = confALCARECOTkAlZMuMu.ALCARECOTkAlZMuMu.clone()
ALCARECOTkAlZMuMuAndVertex.GlobalSelector.muonSource = 'ALCARECOTkAlZMuMuAndVertexRelCombIsoMuons'

##################################################################
# Tracks from the selected vertex
#################################################################
import Alignment.CommonAlignmentProducer.AlignmentTracksFromVertexSelector_cfi as TracksFromVertex
ALCARECOTkAlZMuMuVertexTracks = TracksFromVertex.AlignmentTracksFromVertexSelector.clone()

##################################################################
# The sequence
#################################################################
seqALCARECOTkAlZMuMuAndVertex = cms.Sequence(ALCARECOTkAlZMuMuAndVertexHLT+
                                             ALCARECOTkAlZMuMuAndVertexDCSFilter+
                                             ALCARECOTkAlZMuMuAndVertexGoodMuons+
                                             ALCARECOTkAlZMuMuAndVertexRelCombIsoMuons+
                                             ALCARECOTkAlZMuMuAndVertex+
                                             ALCARECOTkAlZMuMuVertexTracks)

## customizations for the pp_on_AA eras
from Configuration.Eras.Modifier_pp_on_XeXe_2017_cff import pp_on_XeXe_2017
from Configuration.ProcessModifiers.pp_on_AA_cff import pp_on_AA
(pp_on_XeXe_2017 | pp_on_AA).toModify(ALCARECOTkAlZMuMuAndVertexHLT,
                                      eventSetupPathsKey='TkAlZMuMuHI'
)
