#!/bin/bash 
W_DIR=$(pwd); 

# Set SCRAM architecture var
SCRAM_ARCH=slc6_amd64_gcc530; 
export SCRAM_ARCH;

cd $W_DIR;
source /afs/cern.ch/cms/cmsset_default.sh;
eval `scram run -sh`;

mkdir -p $W_DIR/results

scales=(1.03 1.02 1.01 1.00 0.99 0.98 0.97)
smears=(0.05 0.04 0.03 0.02 0.01)

for i in "${scales[@]}"
do
    echo "Processing: $i scale"
    cmsRun $W_DIR/ConfFile_cfg.py scaleFactor=${i}
    mv *.db $W_DIR/results
done


for i in "${smears[@]}"
do
    echo "Processing: $i smear"
    cmsRun $W_DIR/ConfFile_cfg.py smearFactor=${i}
    mv *.db $W_DIR/results
done