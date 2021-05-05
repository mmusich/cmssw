#!/bin/bash

eval `scramv1 runtime -sh`
CMSSW_DIR=${CMSSW_BASE}/src/Alignment/OfflineValidation/test
cd $CMSSW_DIR

if [ -d $CMSSW_DIR/outfiles ]; then
    echo "$CMSSW_DIR/outfiles already exists, skipping"
else
    mkdir $CMSSW_DIR/outfiles
fi

condor_submit par1=113X_mc2017_realistic_v4 par2=: par3=RealisticV2 par4=${CMSSW_DIR} submit.sub
condor_submit par1=113X_mc2017_realistic_v4 par2=TrackerAlignmentRcd:TrackerAlignment_Upgrade2017_design_v4,TrackerAlignmentErrorExtendedRcd:TrackerAlignmentErrorsExtended_Upgrade2017_design_v0 par3=Ideal par4=${CMSSW_DIR} submit.sub
condor_submit par1=113X_mc2017_realistic_v4 par2=TrackerAlignmentRcd:TrackerAlignment_2017_ultralegacymc_v1,TrackerAlignmentErrorExtendedRcd:TrackerAlignmentExtendedErrors_2017_ultralegacymc_v1 par3=RealisticV1 par4=${CMSSW_DIR} submit.sub

#count=0
#while read line; do
#  echo "i $count $line"
#  ((count=$count+1))
#  condor_submit par1=$line par2=${count} par3=113X_mc2017_realistic_v4 submit.sub par4=${CMSSW_DIR}
#done < files.txt


