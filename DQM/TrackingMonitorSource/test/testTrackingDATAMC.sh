#!/bin/sh

function die { echo $1: status $2 ; exit $2; }

function runTests {

    # local variables
    local testType="$1"
    local inputFiles="$2"
    local sequenceType="$3"
    local isRECO="$4"
    local globalTag="$5"

    echo -e "TESTING step1 ($testType) ...\n\n"

    # optional for the cmsRun sequence
    local sequenceArg=""
    [ -n "$sequenceType" ] && sequenceArg="sequenceType=$sequenceType"
    local globalTagArg=""
    [ -n "$globalTag" ] && globalTagArg="globalTag=$globalTag"

    edmConfigDump ${SCRAM_TEST_PATH}/Tracker_DataMCValidation_cfg.py maxEvents=100 inputFiles="$inputFiles" $sequenceArg isRECO="$isRECO" $globalTagArg > dump.py
    
    cmsRun ${SCRAM_TEST_PATH}/Tracker_DataMCValidation_cfg.py maxEvents=100 inputFiles="$inputFiles" $sequenceArg isRECO="$isRECO" $globalTagArg || die "Failure running Tracker_DataMCValidation_cfg.py sequenceType=$sequenceType" $?

    
    
    mv step1_DQM_1.root "step1_DQM_1_${testType}.root"

    echo -e "TESTING step2 ($testType)...\n\n"
    cmsRun ${SCRAM_TEST_PATH}/Tracker_DataMCValidation_Harvest_cfg.py inputFiles="file:step1_DQM_1_${testType}.root" || die "Failure running Tracker_DataMCValidation_Harvest_cfg.py" $?

    mv DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root "step2_DQM_${testType}.root"

    echo -e "================== Done with testing $testType ==================\n\n"
}

#######################################################
# RECO checks
#######################################################
echo "TESTING Tracking DATA/MC comparison codes on RECO ..."

runTests "electrons" "/store/relval/CMSSW_20_0_0/RelValZEE_14/GEN-SIM-RECO/PU_150X_mcRun4_realistic_v1_STD_D127_RegeneratedGS_PU_16Aug26-v2/2590000/191f20ad-4ff7-4341-aaa4-cddd20732ea5.root" "" "False"
runTests "muons" "/store/relval/CMSSW_20_0_0/RelValZMM_14/GEN-SIM-RECO/PU_150X_mcRun4_realistic_v1_STD_D127_RegeneratedGS_PU_16Aug26-v2/2590000/cb25fd77-e854-4cd1-bf84-8f709e8001ee.root" "muons" "False"
runTests "ttbar" "/store/relval/CMSSW_20_0_0/RelValTTbar_14TeV/GEN-SIM-RECO/PU_150X_mcRun4_realistic_v1_STD_D127_RegeneratedGS_PU_16Aug26-v2/2590000/f7d61e2b-b867-441e-8160-53d5ca60f98c.root" "ttbar" "False"
runTests "minbias" "/store/relval/CMSSW_20_0_0/RelValNuGun/GEN-SIM-RECO/PU_150X_mcRun4_realistic_v1_STD_D127_RegeneratedGS_PU_16Aug26-v2/2590000/d3aa7899-acfe-4bd2-9aa6-c8933a0c4f06.root" "minbias" "False"
runTests "V0s" "/store/relval/CMSSW_20_0_0/RelValNuGun/GEN-SIM-RECO/PU_150X_mcRun4_realistic_v1_STD_D127_RegeneratedGS_PU_16Aug26-v2/2590000/d3aa7899-acfe-4bd2-9aa6-c8933a0c4f06.root" "V0s" "False"

# #######################################################
# # AOD checks
# #######################################################
# echo "TESTING Tracking DATA/MC comparison codes on AOD..."

#runTests "electrons (AOD)" "" "" "False" "130X_mcRun3_2023_realistic_postBPix_v2"
#runTests "muons (AOD)" "" "muons" "False" "130X_mcRun3_2023_realistic_postBPix_v2"
#runTests "ttbar (AOD)" "" "ttbar" "False" "130X_mcRun3_2023_realistic_postBPix_v2"
#runTests "minbias (AOD)" "" "minbias" "False" "130X_mcRun3_2023_realistic_postBPix_v2"
#runTests "V0s (AOD)" "" "V0s" "False" "130X_mcRun3_2023_realistic_postBPix_v2"
