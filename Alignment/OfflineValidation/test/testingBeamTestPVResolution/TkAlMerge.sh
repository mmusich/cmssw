#!/bin/bash
CWD=`pwd -P`
cd /tmp/musich/CMSSW_12_0_3_patch1/src
export SCRAM_ARCH=slc7_amd64_gcc900
eval `scramv1 ru -sh`



#create results-directory and copy used configuration there
mkdir -p /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTestPVResolution
cp /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/test/testingBeamTestPVResolution/usedConfiguration.ini /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTestPVResolution


if [[ $HOSTNAME = lxplus[0-9]*[.a-z0-9]* ]] # check for interactive mode
then
    mkdir -p /tmp/musich/testingBeamTestPVResolution
    cd /tmp/musich/testingBeamTestPVResolution
else
    cd $CWD
fi
echo "Working directory: $(pwd -P)"

###############################################################################
# download root files from eos
root_files=$(ls /eos/cms/store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/Test/testingBeamTestPVResolution              | grep ".root$" | grep -v "result.root$")
#for file in ${root_files}
#do
#    xrdcp -f root://eoscms//eos/cms/store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/Test/testingBeamTestPVResolution/${file} .
#    echo ${file}
#done


#run

#run comparisons


#make primary vertex validation plots

cp /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/test/testingBeamTestPVResolution/TkAlPrimaryVertexResolutionPlot.C .
root -x -b -q TkAlPrimaryVertexResolutionPlot.C++

for PdfOutputFile in $(ls *pdf ); do
    xrdcp -f ${PdfOutputFile}  root://eoscms//eos/cms/store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/Test/testingBeamTestPVResolution/plots/${PdfOutputFile}
    cp ${PdfOutputFile}  /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTestPVResolution/PrimaryVertexResolution
done

for PngOutputFile in $(ls *png ); do
     xrdcp -f ${PngOutputFile}  root://eoscms//eos/cms/store/group/alca_trackeralign/AlignmentValidation/AlignmentValidation/Test/testingBeamTestPVResolution/plots/${PngOutputFile}
    cp ${PngOutputFile}  /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/musich/PVValidationBeamTest/testingBeamTestPVResolution/PrimaryVertexResolution
done



# clean-up
# ls -l *.root
rm -f *.root

#zip stdout and stderr from the farm jobs
cd /tmp/musich/CMSSW_12_0_3_patch1/src/Alignment/OfflineValidation/test/testingBeamTestPVResolution
find . -name "*.stderr" -exec gzip -f {} \;
find . -name "*.stdout" -exec gzip -f {} \;
