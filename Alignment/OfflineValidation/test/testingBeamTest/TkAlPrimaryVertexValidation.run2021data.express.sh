#!/bin/bash
source /afs/cern.ch/cms/caf/setup.sh
export X509_USER_PROXY=/tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/test/testingBeamTest/.user_proxy

echo  -----------------------
echo  Job started at `date`
echo  -----------------------

export theLabel=express
export theDate=10

cwd=`pwd`
cd /tmp/musich/CMSSW_12_0_3_patch1/src
export SCRAM_ARCH=slc7_amd64_gcc900
eval `scram runtime -sh`
cd $cwd

mkdir -p /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest
mkdir -p /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express
mkdir -p /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/test/testingBeamTest
rm -f /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/test/testingBeamTest/*.stdout
rm -f /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/test/testingBeamTest/*.stderr

if [[ $HOSTNAME = lxplus[0-9]*[.a-z0-9]* ]] # check for interactive mode
then
    mkdir -p /tmp/musich/testingBeamTest/777633378
    rm -f /tmp/musich/testingBeamTest/777633378/*
    cd /tmp/musich/testingBeamTest/777633378
else
    mkdir -p $cwd/TkAllInOneTool
    cd $cwd/TkAllInOneTool
fi

#run configfile and post-proccess it
cmsRun /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/test/testingBeamTest/TkAlPrimaryVertexValidation.run2021data.express_cfg.py
 

ls -lh .

eos mkdir -p /store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/Test/testingBeamTest/plots/
for RootOutputFile in $(ls *root )
do
    xrdcp -f ${RootOutputFile} root://eoscms//eos/cms/store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/Test/testingBeamTest/${RootOutputFile}
    cp ${RootOutputFile}  /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express
done

cp /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/macros/FitPVResiduals.C .
cp /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/macros/CMS_lumi.C .
cp /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/macros/CMS_lumi.h .

 if [[ root://eoscms//eos/cms/store/group/alca_trackeralign/validation/PVValidation/Reference/PrimaryVertexValidation_phaseIMC92X_upgrade2017_Ideal.root == *store* ]]; then xrdcp -f root://eoscms//eos/cms/store/group/alca_trackeralign/validation/PVValidation/Reference/PrimaryVertexValidation_phaseIMC92X_upgrade2017_Ideal.root PVValidation_reference.root; else ln -fs root://eoscms//eos/cms/store/group/alca_trackeralign/validation/PVValidation/Reference/PrimaryVertexValidation_phaseIMC92X_upgrade2017_Ideal.root ./PVValidation_reference.root; fi

echo "I am going to produce the comparison with IDEAL geometry of ${RootOutputFile}"
root -b -q "FitPVResiduals.C++g(\"${PWD}/${RootOutputFile}=${theLabel},${PWD}/PVValidation_reference.root=Design simulation\",true,true,\"$theDate\")"

mkdir -p /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots
for PngOutputFile in $(ls *png ); do
    xrdcp -f ${PngOutputFile}  root://eoscms//eos/cms/store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/Test/testingBeamTest/plots/${PngOutputFile}
    cp ${PngOutputFile}  /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots
done

for PdfOutputFile in $(ls *pdf ); do
    xrdcp -f ${PdfOutputFile}  root://eoscms//eos/cms/store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/Test/testingBeamTest/plots/${PdfOutputFile}
    cp ${PdfOutputFile}  /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots
done

mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/Biases/
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/Biases/dzPhi
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/Biases/dxyPhi
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/Biases/dzEta
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/Biases/dxyEta
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/Fit
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dxyVsEta
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dzVsEta
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dxyVsPhi
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dzVsPhi
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dxyVsEtaNorm
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dzVsEtaNorm
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dxyVsPhiNorm
mkdir /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dzVsPhiNorm

mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/BiasesCanvas*     /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/Biases/
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dzPhiBiasCanvas*  /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/Biases/dzPhi
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dxyPhiBiasCanvas* /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/Biases/dxyPhi
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dzEtaBiasCanvas*  /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/Biases/dzEta
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dxyEtaBiasCanvas* /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/Biases/dxyEta
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dzPhiTrendFit*    /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/Fit
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dxyEtaTrendNorm*  /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dxyVsEtaNorm
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dzEtaTrendNorm*   /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dzVsEtaNorm
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dxyPhiTrendNorm*  /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dxyVsPhiNorm
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dzPhiTrendNorm*   /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dzVsPhiNorm
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dxyEtaTrend*      /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dxyVsEta
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dzEtaTrend*       /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dzVsEta
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dxyPhiTrend*      /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dxyVsPhi
mv /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dzPhiTrend*       /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dzVsPhi

wget https://raw.githubusercontent.com/mmusich/PVToolScripts/master/PolishedScripts/index.php

cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/Biases/
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/Biases/dzPhi
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/Biases/dxyPhi
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/Biases/dzEta
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/Biases/dxyEta
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/Fit
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dxyVsEta
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dzVsEta
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dxyVsPhi
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dzVsPhi
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dxyVsEtaNorm
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dzVsEtaNorm
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dxyVsPhiNorm
cp index.php /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation/run2021data/express/plots/dzVsPhiNorm


echo  -----------------------
echo  Job ended at `date`
echo  -----------------------

