import FWCore.ParameterSet.Config as cms

from ..modules.hltScoutingTrackPacker_cfi import *
from ..modules.hltScoutingPrimaryVertexPacker_cfi import *
from ..modules.hltScoutingPFPacker_cfi import *
from ..modules.hltScoutingMuonPacker_cfi import *
from ..modules.hltScoutingEgammaPacker_cfi import *
from ..modules.hltScoutingRecHitPacker_cfi import *

from ..modules.hltIterL3MuonTracks_cfi import *
from ..modules.hltL3MuonsIterL3Links_cfi import *
from ..modules.hltPFMuonMerging_cfi import *
from ..modules.hltDisplacedmumuVtxProducer_cfi import *

HLTPFScoutingPackingSequence = cms.Sequence( hltIterL3MuonTracks +
                                             hltPFMuonMerging +
                                             hltScoutingTrackPacker +
                                             hltScoutingPrimaryVertexPacker +
                                             hltScoutingPFPacker +
                                             hltL3MuonsIterL3Links +
                                             hltDisplacedmumuVtxProducer +
                                             hltScoutingMuonPacker +
                                             hltScoutingEgammaPacker +
                                             hltScoutingRecHitPacker )

