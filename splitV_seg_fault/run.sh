#!/bin/bash
cd $CMSSW_BASE/src
source /cvmfs/cms.cern.ch/cmsset_default.sh
export X509_USER_PROXY=/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/alignmentObjects/hpeterse/ReReco_2024_CDE/SplitV_validation/2024_CDE_ReReco_mp3949_splitV_379525/SplitV/single/compare2024/GT/379525/.user_proxy
eval `scram runtime -sh`
cd /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/alignmentObjects/hpeterse/ReReco_2024_CDE/SplitV_validation/2024_CDE_ReReco_mp3949_splitV_379525/SplitV/single/compare2024/GT/379525
./cmsRun validation_cfg.py config=validation.json
