#!/bin/bash
display_usage() { 
    echo "This script must be run giving the following arguments." 
    echo -e "./testCompare.sh <name of tag 1> <name of tag 2> <first IOV> <last IOV> <sqlite file> \n\n"
    echo -e "example: \n ./testCompare.sh SiStripApvGain_FromParticles_GR10_v1_express SiStripApvGain_FromParticles_GR10_v1_express 300577 302322 toCompare.db \n" 
} 

# if less than two arguments supplied, display usage 
	if [  $# -le 3 ] 
	then 
		display_usage
		exit 1
	fi 
 
# check whether user had supplied -h or --help . If yes display usage 
	if [[ ( $# == "--help") ||  $# == "-h" ]] 
	then 
		display_usage
		exit 0
	fi 

# Save current working dir so img can be outputted there later
W_DIR=$(pwd);
# Set SCRAM architecture var
SCRAM_ARCH=slc6_amd64_gcc630;
STARTIOV=$3
ENDIOV=$4

export SCRAM_ARCH;
source /afs/cern.ch/cms/cmsset_default.sh;
eval `scram run -sh`;
# Go back to original working directory
cd $W_DIR;

plotTypes=(SiStripApvGainsComparatorTwoTags SiStripApvGainsValuesComparatorTwoTags SiStripApvGainsComparatorByRegionTwoTags SiStripApvGainsRatioComparatorByRegionTwoTags)

mkdir -p $W_DIR/results_$3-$4

if [ -f *.png ]; then    
    rm *.png
fi

for i in "${plotTypes[@]}" 
do

# Run get payload data script
    getPayloadData.py \
	--plugin pluginSiStripApvGain_PayloadInspector \
	--plot plot_${i} \
	--tag $1 \
	--tagtwo $2 \
	--time_type Run \
	--iovs  '{"start_iov": "'$STARTIOV'", "end_iov": "'$STARTIOV'"}' \
	--iovstwo  '{"start_iov": "'$ENDIOV'", "end_iov": "'$ENDIOV'"}' \
	--db sqlite_file:$5 \
	--test;

    mv *.png $W_DIR/results_$3-$4/${i}_$1-$2_$3-$4.png
done

mapTypes=(SiStripApvGainsAvgDeviationRatioTrackerMapTwoTags SiStripApvGainsMaxDeviationRatioTrackerMapTwoTags)

if [ -f *.png ]; then    
    rm *.png
fi

for i in 1 2 3 4 5
do
    echo "${i} sigmas"
    for j in "${mapTypes[@]}" 
    do

	# Run get payload data script
	getPayloadData.py \
	    --plugin pluginSiStripApvGain_PayloadInspector \
	    --plot plot_${j} \
	    --tag $1 \
	    --tagtwo $2 \
	    --time_type Run \
	    --iovs  '{"start_iov": "'$STARTIOV'", "end_iov": "'$STARTIOV'"}' \
	    --iovstwo  '{"start_iov": "'$ENDIOV'", "end_iov": "'$ENDIOV'"}' \
	    --input_params '{"nsigma":"'$i'"}' \
	    --db sqlite_file:$5 \
	    --test;

	mv *.png $W_DIR/results_$3-$4/${j}_${i}sigma_$1-$2_$3-$4.png
    done
done

