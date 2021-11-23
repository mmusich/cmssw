#!/bin/bash
source /afs/cern.ch/cms/caf/setup.sh
export X509_USER_PROXY=/tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/test/testingBeamTest/.user_proxy

echo  -----------------------
echo  Job started at `date`
echo  -----------------------

export theLabel=PCL
export theDate=10

cwd=`pwd`
cd /tmp/musich/CMSSW_12_0_3_patch1/src
export SCRAM_ARCH=slc7_amd64_gcc900
eval `scram runtime -sh`
cd $cwd

mkdir -p /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest
mkdir -p /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL
mkdir -p /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/test/testingBeamTest
rm -f /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/test/testingBeamTest/*.stdout
rm -f /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/test/testingBeamTest/*.stderr

if [[ $HOSTNAME = lxplus[0-9]*[.a-z0-9]* ]] # check for interactive mode
then
    mkdir -p /tmp/musich/testingBeamTest/629875846
    rm -f /tmp/musich/testingBeamTest/629875846/*
    cd /tmp/musich/testingBeamTest/629875846
else
    mkdir -p $cwd/TkAllInOneTool
    cd $cwd/TkAllInOneTool
fi

#run configfile and post-proccess it
cmsRun /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/test/testingBeamTest/TkAlPrimaryVertexValidation.run2021data.PCL_cfg.py
 

ls -lh .

eos mkdir -p /store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/Test/testingBeamTest/plots/
for RootOutputFile in $(ls *root )
do
    xrdcp -f ${RootOutputFile} root://eoscms//eos/cms/store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/Test/testingBeamTest/${RootOutputFile}
    cp ${RootOutputFile}  /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL
done

cp /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/macros/FitPVResiduals.C .
cp /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/macros/CMS_lumi.C .
cp /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/macros/CMS_lumi.h .

 if [[ root://eoscms//eos/cms/store/group/alca_trackeralign/validation/PVValidation/Reference/PrimaryVertexValidation_phaseIMC92X_upgrade2017_Ideal.root == *store* ]]; then xrdcp -f root://eoscms//eos/cms/store/group/alca_trackeralign/validation/PVValidation/Reference/PrimaryVertexValidation_phaseIMC92X_upgrade2017_Ideal.root PVValidation_reference.root; else ln -fs root://eoscms//eos/cms/store/group/alca_trackeralign/validation/PVValidation/Reference/PrimaryVertexValidation_phaseIMC92X_upgrade2017_Ideal.root ./PVValidation_reference.root; fi

echo "I am going to produce the comparison with IDEAL geometry of ${RootOutputFile}"
root -b -q "FitPVResiduals.C++g(\"${PWD}/${RootOutputFile}=${theLabel},${PWD}/PVValidation_reference.root=Design simulation\",true,true,\"$theDate\")"

mkdir -p /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots
for PngOutputFile in $(ls *png ); do
    xrdcp -f ${PngOutputFile}  root://eoscms//eos/cms/store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/Test/testingBeamTest/plots/${PngOutputFile}
    cp ${PngOutputFile}  /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots
done

for PdfOutputFile in $(ls *pdf ); do
    xrdcp -f ${PdfOutputFile}  root://eoscms//eos/cms/store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/Test/testingBeamTest/plots/${PdfOutputFile}
    cp ${PdfOutputFile}  /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots
done

mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/Biases/
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/Biases/dzPhi
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/Biases/dxyPhi
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/Biases/dzEta
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/Biases/dxyEta
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/Fit
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dxyVsEta
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dzVsEta
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dxyVsPhi
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dzVsPhi
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dxyVsEtaNorm
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dzVsEtaNorm
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dxyVsPhiNorm
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dzVsPhiNorm

mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/BiasesCanvas*     /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/Biases/
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dzPhiBiasCanvas*  /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/Biases/dzPhi
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dxyPhiBiasCanvas* /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/Biases/dxyPhi
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dzEtaBiasCanvas*  /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/Biases/dzEta
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dxyEtaBiasCanvas* /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/Biases/dxyEta
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dzPhiTrendFit*    /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/Fit
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dxyEtaTrendNorm*  /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dxyVsEtaNorm
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dzEtaTrendNorm*   /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dzVsEtaNorm
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dxyPhiTrendNorm*  /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dxyVsPhiNorm
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dzPhiTrendNorm*   /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dzVsPhiNorm
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dxyEtaTrend*      /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dxyVsEta
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dzEtaTrend*       /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dzVsEta
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dxyPhiTrend*      /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dxyVsPhi
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dzPhiTrend*       /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dzVsPhi

wget https://raw.githubusercontent.com/mmusich/PVToolScripts/master/PolishedScripts/index.php

cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/Biases/
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/Biases/dzPhi
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/Biases/dxyPhi
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/Biases/dzEta
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/Biases/dxyEta
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/Fit
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dxyVsEta
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dzVsEta
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dxyVsPhi
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dzVsPhi
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dxyVsEtaNorm
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dzVsEtaNorm
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dxyVsPhiNorm
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/PCL/plots/dzVsPhiNorm


echo  -----------------------
echo  Job ended at `date`
echo  -----------------------

