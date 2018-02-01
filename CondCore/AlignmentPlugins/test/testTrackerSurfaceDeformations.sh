#!/bin/bash

# Save current working dir so img can be outputted there later
W_DIR=$(pwd);

# Set SCRAM architecture var
SCRAM_ARCH=slc6_amd64_gcc530; 
export SCRAM_ARCH;

cd $W_DIR;
source /afs/cern.ch/cms/cmsset_default.sh;
eval `scram run -sh`;

mkdir -p $W_DIR/results_surfaces

getPayloadData.py  \
 	--plugin pluginTrackerSurfaceDeformations_PayloadInspector \
 	--plot plot_TrackerSurfaceDeformationsTest \
 	--tag  TrackerSurafceDeformations_v1_express \
 	--time_type Run \
	--iovs '{"start_iov": "299685", "end_iov": "299685"}' \
  	--db Prod \
 	--test;