#!/bin/bash
CWD=`pwd -P`
cd /tmp/musich/CMSSW_12_0_3_patch1/src
export SCRAM_ARCH=slc7_amd64_gcc900
eval `scramv1 ru -sh`



#create results-directory and copy used configuration there
mkdir -p /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest
cp /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/test/testingBeamTest/usedConfiguration.ini /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest


if [[ $HOSTNAME = lxplus[0-9]*[.a-z0-9]* ]] # check for interactive mode
then
    mkdir -p /tmp/musich/testingBeamTest
    cd /tmp/musich/testingBeamTest
else
    cd $CWD
fi
echo "Working directory: $(pwd -P)"

###############################################################################
# download root files from eos
root_files=$(ls /eos/cms/store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/Test/testingBeamTest              | grep ".root$" | grep -v "result.root$")
#for file in ${root_files}
#do
#    xrdcp -f root://eoscms//eos/cms/store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/Test/testingBeamTest/${file} .
#    echo ${file}
#done


#run

#run comparisons


#make primary vertex validation plots

cp /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/test/testingBeamTest/TkAlPrimaryVertexValidationPlot.C .
root -x -b -q TkAlPrimaryVertexValidationPlot.C++

for PdfOutputFile in $(ls *pdf ); do
    xrdcp -f ${PdfOutputFile}  root://eoscms//eos/cms/store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/Test/testingBeamTest/plots/${PdfOutputFile}
    cp ${PdfOutputFile}  /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation
done

for PngOutputFile in $(ls *png ); do
    xrdcp -f ${PngOutputFile}  root://eoscms//eos/cms/store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/Test/testingBeamTest/plots/${PngOutputFile}
    cp ${PngOutputFile}  /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTest/PrimaryVertexValidation
done



# clean-up
# ls -l *.root
rm -f *.root

#zip stdout and stderr from the farm jobs
cd /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/test/testingBeamTest
find . -name "*.stderr" -exec gzip -f {} \;
find . -name "*.stdout" -exec gzip -f {} \;
