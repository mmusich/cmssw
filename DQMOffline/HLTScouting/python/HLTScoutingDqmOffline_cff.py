'''
Scouting DQM sequences for offline DQM developed for 2025 pp data-taking
and used by DQM GUI (DQMOffline/Configuration):
currently running EGM and MUO monitoring modules.
'''

import FWCore.ParameterSet.Config as cms
from DQMServices.Core.DQMEDHarvester import DQMEDHarvester                                

from HLTriggerOffline.Scouting.ScoutingMuonTriggerAnalyzer_cfi import *
from HLTriggerOffline.Scouting.ScoutingMuonTagProbeAnalyzer_cfi import *
from HLTriggerOffline.Scouting.ScoutingMuonMonitoring_Client_cff import *


from HLTriggerOffline.Scouting.HLTScoutingEGammaDqmOffline_cff import *
from HLTriggerOffline.Scouting.ScoutingDQMMakerRun3_cfi import *


from DQMOffline.JetMET.jetMETDQMOfflineSource_cff import *

hltScoutingMuonDqmOffline = cms.Sequence(scoutingMonitoringTagProbeMuonNoVtx
                                         * scoutingMonitoringTagProbeMuonVtx                                                         
                                         * scoutingMonitoringTriggerMuon                                                              
)

hltScoutingJetDqmOffline = cms.Sequence(jetMETDQMOfflineSourceScouting)

hltScoutingnewDqmOffline = cms.Sequence(scoutingDQMMakerRun3)


hltScoutingDqmOffline = cms.Sequence(hltScoutingMuonDqmOffline + hltScoutingEGammaDqmOffline + hltScoutingJetDqmOffline + hltScoutingnewDqmOffline)
