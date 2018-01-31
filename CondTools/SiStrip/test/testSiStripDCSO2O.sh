#!/bin/sh
export TNS_ADMIN=/afs/cern.ch/project/oracle/admin
function die { echo $1: status $2 ; exit $2; }
conddb --yes copy SiStripDetVOff_1hourDelay_v1_Validation --destdb SiStripDetVOff_1hourDelay_O2OTEST.db --o2oTest 
cmsRun ./src/CondTools/SiStrip/python/SiStripDCS_popcon.py destinationConnection=SiStripDetVOff_1hourDelay_O2OTEST.db tag=SiStripDetVOff_1hourDelay_v1_Validation || die "Failure running SiStripDCS_popcon.py" $?
conddb --db  SiStripDetVOff_1hourDelay_O2OTEST.db list SiStripDetVOff_1hourDelay_v1_Validation
