#!/bin/bash

# Save current working dir so img can be outputted there later
W_DIR=$(pwd);

# Set SCRAM architecture var
SCRAM_ARCH=slc6_amd64_gcc530; 
export SCRAM_ARCH;

cd $W_DIR;
source /afs/cern.ch/cms/cmsset_default.sh;
eval `scram run -sh`;

# Run get payload data script
$W_DIR/getPayloadData.py  \
    --plugin pluginSiStripApvGain_PayloadInspector \
    --plot plot_SiStripApvGainsRatioWithPreviousIOVTrackerMap \
    --tag SiStripApvGain_FromParticles_GR10_v10_offline \
    --time_type Run \
    --iovs '{"start_iov": "132440", "end_iov": "285368"}' \
    --db Prod \
    --image_plot True \
    --test;

$W_DIR/getPayloadData.py  \
    --plugin pluginSiStripApvGain_PayloadInspector \
    --plot plot_SiStripApvGainsAverageTrackerMap \
    --tag SiStripApvGain_FromParticles_GR10_v10_offline \
    --time_type Run \
    --iovs '{"start_iov": "132440", "end_iov": "132440"}' \
    --db Prod \
    --image_plot True \
    --test;

$W_DIR/getPayloadData.py  \
    --plugin pluginSiStripApvGain_PayloadInspector \
    --plot plot_SiStripApvGainsMaximumTrackerMap \
    --tag SiStripApvGain_FromParticles_GR10_v10_offline \
    --time_type Run \
    --iovs '{"start_iov": "132440", "end_iov": "132440"}' \
    --db Prod \
    --image_plot True \
    --test;

$W_DIR/getPayloadData.py  \
    --plugin pluginSiStripApvGain_PayloadInspector \
    --plot plot_SiStripApvGainsMinimumTrackerMap \
    --tag SiStripApvGain_FromParticles_GR10_v10_offline \
    --time_type Run \
    --iovs '{"start_iov": "132440", "end_iov": "132440"}' \
    --db Prod \
    --image_plot True \
    --test;