#!/bin/bash
# Save current working dir so img can be outputted there later
W_DIR=$(pwd);
# Set SCRAM architecture var
SCRAM_ARCH=slc6_amd64_gcc630;
export SCRAM_ARCH;
source /afs/cern.ch/cms/cmsset_default.sh;
eval `scram run -sh`;
# Go back to original working directory
cd $W_DIR;
# Run get payload data script

rm *.png
mkdir $W_DIR/results/


/afs/cern.ch/user/m/musich/public/forStripDBcontacts/getPayloadDataFromLocalDB.py \
    --plugin pluginSiStripApvGain_PayloadInspector \
    --plot plot_SiStripApvGainsComparator \
    --tag modifiedGains \
    --time_type Run \
    --iovs '{"start_iov": "1", "end_iov": "303014"}' \
    --db sqlite_file:Fantasticc.db \
    --test;


    
/afs/cern.ch/user/m/musich/public/forStripDBcontacts/getPayloadDataFromLocalDB.py \
    --plugin pluginSiStripApvGain_PayloadInspector \
    --plot plot_SiStripApvGainsComparatorByPartition \
    --tag modifiedGains \
    --time_type Run \
    --iovs '{"start_iov": "1", "end_iov": "303014"}' \
    --db sqlite_file:Fantasticc.db \
    --test;


    
/afs/cern.ch/user/m/musich/public/forStripDBcontacts/getPayloadDataFromLocalDB.py \
    --plugin pluginSiStripApvGain_PayloadInspector \
    --plot plot_SiStripApvGainsRatioWithPreviousIOVTrackerMap \
    --tag modifiedGains \
    --time_type Run \
    --iovs '{"start_iov": "1", "end_iov": "303014"}' \
    --db sqlite_file:Fantasticc.db \
    --test;
    