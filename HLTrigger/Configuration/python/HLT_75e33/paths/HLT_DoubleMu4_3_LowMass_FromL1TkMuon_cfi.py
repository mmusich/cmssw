import FWCore.ParameterSet.Config as cms

from ..modules.hltDoubleTkMuon43LowMassL1TkMuonFilter_cfi import *
from ..modules.hltDoubleMu43LowMassL3Filtered_cfi import *
from ..modules.hltDisplacedmumuVtxProducerDoubleMu43LowMass_cfi import *
from ..modules.hltDisplacedmumuFilterDoubleMu43LowMass_cfi import *
from ..modules.hltPhase2L3MuonCandidates_cfi import *
from ..modules.hltPhase2PixelFitterByHelixProjections_cfi import *
from ..modules.hltPhase2PixelTrackFilterByKinematics_cfi import *
from ..sequences.HLTBeginSequence_cfi import *
from ..sequences.HLTEndSequence_cfi import *
from ..sequences.HLTMuonsSequence_cfi import *
from ..sequences.HLTItLocalRecoSequence_cfi import *
from ..sequences.HLTMuonlocalrecoSequence_cfi import *
from ..sequences.HLTOtLocalRecoSequence_cfi import *

HLT_DoubleMu4_3_LowMass_FromL1TkMuon = cms.Path(
    HLTBeginSequence
    + hltL1TkDoubleMuForLowMassInclusive
    + HLTMuonlocalrecoSequence
    + HLTItLocalRecoSequence
    + HLTOtLocalRecoSequence
    + hltPhase2PixelFitterByHelixProjections
    + hltPhase2PixelTrackFilterByKinematics
    + HLTMuonsSequence
    + hltPhase2L3MuonCandidates
    + hltDoubleMu43LowMassL3Filtered
    + hltDisplacedmumuVtxProducerDoubleMu43LowMass
    + hltDisplacedmumuFilterDoubleMu43LowMass
    + HLTEndSequence
)
