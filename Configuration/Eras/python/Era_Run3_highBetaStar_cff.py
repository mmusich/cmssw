import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3
from Configuration.Eras.Modifier_highBetaStar_2018_cff import highBetaStar_2018

Run3_highBetaStar = cms.ModifierChain(Run3, highBetaStar_2018)
