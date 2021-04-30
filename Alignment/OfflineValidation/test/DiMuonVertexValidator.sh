#!/bin/bash

mySeed=$1
globalTag=$2
records=$3
objName=$4
CMSSW_DIR=$5

JobName=DiMuonVertexValidation_${objName}_${mySeed}

echo "Job started at " `date`

LXBATCH_DIR=$PWD

cd ${CMSSW_DIR}
eval `scramv1 runtime -sh`
cd $LXBATCH_DIR

cp ${CMSSW_DIR}/.user_proxy .
export X509_USER_PROXY=.user_proxy

cp ${CMSSW_DIR}/files.txt .
myFile=`sed "${mySeed}q;d" files.txt`

cp ${CMSSW_DIR}/DiMuonVertexValidator_cfg.py .
echo "cmsRun DiMuonVertexValidator_cfg.py myseed=${mySeed} myfile=${myFile} GlobalTag=${globalTag} records=${records} outputName=${objName} >& ${JobName}.out"

cmsRun DiMuonVertexValidator_cfg.py myseed=${mySeed} myfile=${myFile} GlobalTag=${globalTag} records=${records} outputName=${objName} >& ${JobName}_cmsRun.out

echo "Content of working directory is: " `ls -lrt`

eos mkdir -p /eos/cms/store/group/alca_trackeralign/$USER/test_out/DiMuonVertexValid2/

for payloadOutput in $(ls *root ); do xrdcp -f $payloadOutput root://eoscms.cern.ch//eos/cms/store/group/alca_trackeralign/$USER/test_out/DiMuonVertexValid2/${JobName}.root ; done

mv ${JobName}_cmsRun.out ${CMSSW_DIR}/outfiles

echo  "Job ended at " `date`

exit 0
