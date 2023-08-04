#!/bin/bash
eval `scramv1 runtime -sh`
CMSSW_DIR=${CMSSW_BASE}/src/DQMOffline/Alignment/test

if [ -d $CMSSW_DIR/outfiles ]; then
    echo "$CMSSW_DIR/outfiles already exists, skipping"
else
    mkdir $CMSSW_DIR/outfiles
fi

# Define an array
scenarios=("baseline" "g4refitter")

# Loop over the array and print each element
for scenario in "${scenarios[@]}"
do
  echo "$scenario"
  condor_submit par1=${scenario} par2=${CMSSW_DIR} submitData.sub
done
