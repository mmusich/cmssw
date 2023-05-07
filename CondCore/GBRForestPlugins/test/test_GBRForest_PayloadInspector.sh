#!/bin/bash
# Save current working dir so img can be outputted there later
W_DIR=$(pwd);
source /afs/cern.ch/cms/cmsset_default.sh;
eval `scram run -sh`;
# Go back to original working directory
cd $W_DIR;
# Run get payload data script

mkdir -p $W_DIR/results

if [ -f *.png ]; then
    rm *.png
fi

####################
# Test GBRForest
####################
getPayloadData.py \
    --plugin pluginGBRForest_PayloadInspector \
    --plot plot_GBRForest_Test \
    --tag GBRForest_PFResolution_v0_offline  \
    --time_type Run \
    --iovs '{"start_iov": "1", "end_iov": "1"}' \
    --db Prod \
    --test;

mv *.png $W_DIR/results/GBRForest_Test.png
