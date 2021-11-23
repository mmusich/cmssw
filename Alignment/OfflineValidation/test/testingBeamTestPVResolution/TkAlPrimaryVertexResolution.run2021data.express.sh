#!/bin/bash
source /afs/cern.ch/cms/caf/setup.sh
export X509_USER_PROXY=/tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/test/testingBeamTestPVResolution/.user_proxy

source /afs/cern.ch/cms/caf/setup.sh

echo  -----------------------
echo  Job started at `date`
echo  -----------------------

export theLabel=express
export theDate=1

cwd=`pwd`
cd /tmp/musich/CMSSW_12_0_3_patch1/src
export SCRAM_ARCH=slc7_amd64_gcc900
eval `scram runtime -sh`
cd $cwd

mkdir -p /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTestPVResolution
mkdir -p /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTestPVResolution/PrimaryVertexResolution/run2021data/express
mkdir -p /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/test/testingBeamTestPVResolution
rm -f /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/test/testingBeamTestPVResolution/*.stdout
rm -f /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/test/testingBeamTestPVResolution/*.stderr

if [[ $HOSTNAME = lxplus[0-9]*[.a-z0-9]* ]] # check for interactive mode
then
    mkdir -p /tmp/musich/testingBeamTestPVResolution/6264293120
    rm -f /tmp/musich/testingBeamTestPVResolution/6264293120/*
    cd /tmp/musich/testingBeamTestPVResolution/6264293120
else
    mkdir -p $cwd/TkAllInOneTool
    cd $cwd/TkAllInOneTool
fi

#run configfile and post-proccess it
cmsRun /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/test/testingBeamTestPVResolution/TkAlPrimaryVertexResolution.run2021data.express_cfg.py
 

ls -lh .

eos mkdir -p /store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/Test/testingBeamTestPVResolution/plots/

for RootOutputFile in $(ls *root )
do
    xrdcp -f ${RootOutputFile} root://eoscms//eos/cms/store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/Test/testingBeamTestPVResolution/${RootOutputFile}
    cp ${RootOutputFile}  /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTestPVResolution/PrimaryVertexResolution/run2021data/express
done

cp /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/macros/FitPVResolution.C .
cp /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/macros/CMS_lumi.C .
cp /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/macros/CMS_lumi.h .

 if [[ root://eoscms//eos/cms/store/group/alca_trackeralign/validation/PVResolution/Reference/PrimaryVertexResolution_phaseIMC92X_upgrade2017_Ideal.root == *store* ]]; then xrdcp -f root://eoscms//eos/cms/store/group/alca_trackeralign/validation/PVResolution/Reference/PrimaryVertexResolution_phaseIMC92X_upgrade2017_Ideal.root PVValidation_reference.root; else ln -fs root://eoscms//eos/cms/store/group/alca_trackeralign/validation/PVResolution/Reference/PrimaryVertexResolution_phaseIMC92X_upgrade2017_Ideal.root ./PVResolution_reference.root; fi

root -b -q "FitPVResolution.C(\"${PWD}/${RootOutputFile}=${theLabel},${PWD}/PVValidation_reference.root=Design simulation\",\"$theDate\")"

mkdir -p /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTestPVResolution/PrimaryVertexResolution/run2021data/express/plots
for PngOutputFile in $(ls *png ); do
    xrdcp -f ${PngOutputFile}  root://eoscms//eos/cms/store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/Test/testingBeamTestPVResolution/plots/${PngOutputFile}
    cp ${PngOutputFile}  /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTestPVResolution/PrimaryVertexResolution/run2021data/express/plots
done

for PdfOutputFile in $(ls *pdf ); do
    xrdcp -f ${PdfOutputFile}  root://eoscms//eos/cms/store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/Test/testingBeamTestPVResolution/plots/${PdfOutputFile}
    cp ${PdfOutputFile}  /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTestPVResolution/PrimaryVertexResolution/run2021data/express/plots
done

echo  -----------------------
echo  Job ended at `date`
echo  -----------------------

