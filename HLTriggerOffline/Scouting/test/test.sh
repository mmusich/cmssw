!/bin/bash -ex                                                                                                                                                                                             

hltGetConfiguration /dev/CMSSW_15_0_0/HLT \
   --globaltag 150X_dataRun3_HLT_v1 \
   --data \
   --unprescale \
   --output minimal \
   --max-events 1000 \
   --eras Run3_2024 --l1-emulator uGT --l1 L1Menu_Collisions2025_v1_0_0_xml \
   --paths HLT_TestData_v*,DST_PFScouting_*,Dataset_TestDataRaw,LocalTestDataRawOutput,Dataset_TestDataScouting,LocalTestDataScoutingOutput \
   --input /store/data/Run2024I/EphemeralHLTPhysics0/RAW/v1/000/386/593/00000/91a08676-199e-404c-9957-f72772ef1354.root \
   > hltData.py

cmsRun hltData.py >& hltData.log
