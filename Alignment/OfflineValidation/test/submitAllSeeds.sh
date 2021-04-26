#!/bin/bash

eval `scramv1 runtime -sh`
CMSSW_DIR=${CMSSW_BASE}/src/Alignment/OfflineValidation/test
cd $CMSSW_DIR

if [ -d $CMSSW_DIR/outfiles ]; then
    echo "$CMSSW_DIR/outfiles already exists, skipping"
else
    mkdir $CMSSW_DIR/outfiles
fi

condor_submit par1=113X_mc2017_realistic_v4 par2=${CMSSW_DIR} submit.sub

#count=0
#while read line; do
#  echo "i $count $line"
#  ((count=$count+1))
#  condor_submit par1=$line par2=${count} par3=113X_mc2017_realistic_v4 submit.sub par4=${CMSSW_DIR}
#done < files.txt


