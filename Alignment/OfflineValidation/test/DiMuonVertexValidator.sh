#!/bin/bash

mySeed=$1
globalTag=$2
JobName=DiMuonVertexValidator_seed_${mySeed}

echo "Job started at " `date`

CMSSW_DIR=$3
LXBATCH_DIR=$PWD

cd ${CMSSW_DIR}
eval `scramv1 runtime -sh`
cd $LXBATCH_DIR

cp ${CMSSW_DIR}/.user_proxy .
export X509_USER_PROXY=.user_proxy

cp ${CMSSW_DIR}/files.txt .
myFile=`sed "${mySeed}q;d" files.txt`

cp ${CMSSW_DIR}/DiMuonVertexValidator_cfg.py .
echo "cmsRun DiMuonVertexValidator_cfg.py  myfile=${myFile} GlobalTag=${globalTag} >& ${JobName}.out"

cmsRun DiMuonVertexValidator_cfg.py myseed=${mySeed} myfile=${myFile} GlobalTag=${globalTag} >& ${JobName}.out

echo "Content of working directory is: " `ls -lrt`

eos mkdir -p /eos/cms/store/group/alca_trackeralign/$USER/test_out/DiMuonVertexValid/

for payloadOutput in $(ls *root ); do xrdcp -f $payloadOutput root://eoscms.cern.ch//eos/cms/store/group/alca_trackeralign/$USER/test_out/DiMuonVertexValid/DiMuonVertexValidationIdeal_${mySeed}.root ; done

mv ${JobName}.out ${CMSSW_DIR}/outfiles
mv ${JobName}.err ${CMSSW_DIR}/outfiles
mv ${JobName}.log ${CMSSW_DIR}/outfiles

echo  "Job ended at " `date`

exit 0
