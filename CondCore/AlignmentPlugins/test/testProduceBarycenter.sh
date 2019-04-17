#!/bin/bash

# Save current working dir so img can be outputted there later
W_DIR=$(pwd);

# Set SCRAM architecture var
SCRAM_ARCH=slc6_amd64_gcc530; 
export SCRAM_ARCH;

cd $W_DIR;
source /afs/cern.ch/cms/cmsset_default.sh;
eval `scram run -sh`;

mkdir -p $W_DIR/results_alignments

#*************************************************************************#
elements=(X Y Z)

for i in "${elements[@]}"
do
    echo "Processing: $i partition"
    
    getPayloadData.py  \
 	--plugin pluginTrackerAlignment_PayloadInspector \
 	--plot plot_${i}_BPixBarycenterHistory \
 	--tag Alignments \
 	--time_type Run \
	--iovs '{"start_iov": "297049", "end_iov": "307082"}' \
  	--db sqlite_file:/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/um0001/jobData/jobm/um0001.db  \
 	--test >& $W_DIR/results_alignments/plot_${i}_BPixBarycenterHistory.json & \

    getPayloadData.py  \
 	--plugin pluginTrackerAlignment_PayloadInspector \
 	--plot plot_${i}_BPixBarycenterHistory \
 	--tag TrackerAlignment_v24_offline \
 	--time_type Run \
	--iovs '{"start_iov": "297049", "end_iov": "307082"}' \
  	--db frontier://FrontierProd/CMS_CONDITIONS  \
 	--test >& $W_DIR/results_alignments/plot_${i}_BPixBarycenterHistoryOld.json & \
    
done   




