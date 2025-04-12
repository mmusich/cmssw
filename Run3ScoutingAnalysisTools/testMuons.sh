#!/bin/bash -ex

# CMSSW_15_0_4

hltGetConfiguration /users/musich/tests/dev/CMSSW_15_0_0/NGT_DEMONSTRATOR/TestData/online/HLT/V1 \
            --globaltag 150X_dataRun3_Prompt_v1 \
            --data \
            --unprescale \
            --output all \
            --max-events -1 \
            --eras Run3_2024 --l1-emulator uGT --l1 L1Menu_Collisions2025_v1_0_0_xml \
            --input root://xrootd-cms.infn.it//store/data/Run2024I/Muon0/RAW-RECO/ZMu-PromptReco-v1/000/386/679/00000/0ad3b71c-6d7f-4631-bb55-6005a255b228.root \
            > hltData.py

cmsRun hltData.py >& hltData.log

