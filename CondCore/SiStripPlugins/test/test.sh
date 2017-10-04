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

for i in `seq 2 12`;
do
    echo $i
    mkdir $W_DIR/results/Comparison_1_$i

    /afs/cern.ch/user/m/musich/public/forStripDBcontacts/getPayloadDataFromLocalDB.py \
	--plugin pluginSiStripApvGain_PayloadInspector \
	--plot plot_SiStripApvGainsComparator \
	--tag g2_for_testMatrix \
	--time_type Run \
	--iovs '{"start_iov": "1", "end_iov": "'$i'"}' \
	--db sqlite_file:toInspect.db \
	--test;

    mv *.png  $W_DIR/results/Comparison_1_$i/SiStripApvGainsComparator.png
    
    /afs/cern.ch/user/m/musich/public/forStripDBcontacts/getPayloadDataFromLocalDB.py \
	--plugin pluginSiStripApvGain_PayloadInspector \
	--plot plot_SiStripApvGainsComparatorByPartition \
	--tag g2_for_testMatrix \
	--time_type Run \
	--iovs '{"start_iov": "1", "end_iov": "'$i'"}' \
	--db sqlite_file:toInspect.db \
	--test;

    mv *.png  $W_DIR/results/Comparison_1_$i/SiStripApvGainsComparatorByPartition.png
    
    /afs/cern.ch/user/m/musich/public/forStripDBcontacts/getPayloadDataFromLocalDB.py \
	--plugin pluginSiStripApvGain_PayloadInspector \
	--plot plot_SiStripApvGainsRatioWithPreviousIOVTrackerMap \
	--tag g2_for_testMatrix \
	--time_type Run \
	--iovs '{"start_iov": "1", "end_iov": "'$i'"}' \
	--db sqlite_file:toInspect.db \
	--test;
    
    mv *.png  $W_DIR/results/Comparison_1_$i/SiStripApvGainsRatioWithPreviousIOVTrackerMap.png
done