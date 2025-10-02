#!/bin/bash -ex

# cmsrel CMSSW_15_0_15
# cd CMSSW_15_0_15/src
# cmsenv
# git cms-checkout-topic mmusich/mm_dev_study_FED1050
# scram b -j 20

# Step 1: Create the FED mover config on the fly
cat <<'@EOF' > fedMove_cfg.py
import FWCore.ParameterSet.Config as cms

process = cms.Process("FEDMove")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/data/Run2025D/EphemeralHLTPhysics0/RAW/v1/000/394/959/00000/02ab3d20-66ba-4372-8f06-5d09e0848408.root'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)  # process all events
)

process.copyAndMoveFED1024 = cms.EDProducer('CopyAndMoveFED1024',
    src = cms.InputTag('rawDataCollector')
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string("modifiedFEDs.root"),
    outputCommands = cms.untracked.vstring(
        'drop FEDRawDataCollection_rawDataCollector_*_LHC',
        "keep *"
    )
)

process.p = cms.Path(process.copyAndMoveFED1024)
process.e = cms.EndPath(process.out)
@EOF

# Step 2: Run it to produce modifiedFEDs.root
cmsRun fedMove_cfg.py >& fedMove.log

# Step 3: Run hltGetConfiguration using the modified file as input
hltGetConfiguration /users/musich/tests/dev/CMSSW_15_0_0/CMSHLT-3643/HLT/V2 \
   --globaltag 150X_dataRun3_HLT_v1 \
   --data \
   --unprescale \
   --output minimal \
   --max-events 100 \
   --eras Run3_2025 --l1-emulator uGT --l1 L1Menu_Collisions2025_v1_3_0_xml \
   --input file:modifiedFEDs.root \
   > hltData.py

# Step 4: Replace rawDataCollector with copyAndMoveFED1024 everywhere
sed -i 's/\brawDataCollector\b/copyAndMoveFED1024/g' hltData.py

# Step 5: Dump config and fix InputTag
edmConfigDump hltData.py > dump.py
cat <<@EOF >> dump.py
process.hltGtStage2Digis.InputLabel = cms.InputTag("rawDataCollector")
@EOF

# Step 6: Run the final HLT config
cmsRun dump.py >& hltData.log
