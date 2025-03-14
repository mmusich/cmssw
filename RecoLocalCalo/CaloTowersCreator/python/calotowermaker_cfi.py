import FWCore.ParameterSet.Config as cms

from RecoLocalCalo.CaloTowersCreator.modules import *
calotowermaker = CaloTowersCreator(
    usePFThresholdsFromDB = False
)

from Configuration.Eras.Modifier_run2_HE_2018_cff import run2_HE_2018
run2_HE_2018.toModify(calotowermaker, 
                      HcalPhase = 1,
                      HESThreshold1 = 0.1,
                      HESThreshold  = 0.2,
                      HEDThreshold1 = 0.1,
                      HEDThreshold  = 0.2
)

# needed to handle inner/outer assignment
from Configuration.ProcessModifiers.run2_HECollapse_2018_cff import run2_HECollapse_2018
run2_HECollapse_2018.toModify(calotowermaker,
    HcalPhase = 0,
    HESThreshold1 = 0.8,
    HESThreshold  = 0.8,
    HEDThreshold1 = 0.8,
    HEDThreshold  = 0.8
)

from Configuration.Eras.Modifier_run3_HB_cff import run3_HB
run3_HB.toModify(calotowermaker,
    HBThreshold1 = 0.1,
    HBThreshold2 = 0.2,
    HBThreshold = 0.3,
)

#--- Use DB conditions for HBHE thresholds for Run3 and phase2
from Configuration.Eras.Modifier_hcalPfCutsFromDB_cff import hcalPfCutsFromDB
hcalPfCutsFromDB.toModify( calotowermaker,
                           usePFThresholdsFromDB = True)
