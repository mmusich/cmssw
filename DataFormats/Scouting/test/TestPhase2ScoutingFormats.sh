#!/bin/bash

function die { echo $1: status $2 ;  exit $2; }

LOCAL_TEST_DIR=${SCRAM_TEST_PATH}

cmsRun ${LOCAL_TEST_DIR}/create_Phase2Scouting_test_file_cfg.py || die 'Failure using create_Phase2Scouting_test_file_cfg.py' $?

cmsRun ${LOCAL_TEST_DIR}/test_readPhase2Scouting_cfg.py || die "Failure using test_readPhase2Scouting_cfg.py" $?

# There are no old Phase 2 Scouting files yet: all Phase2Scouting classes
# were introduced together, starting at ClassVersion 3, and have not
# evolved since.
#
# When a Phase 2 Scouting persistent data format changes, a file written
# with the release *before* the change should be produced by running
# create_Phase2Scouting_test_file_cfg.py, renamed, and added to the
# cms-data DataFormats-Scouting repository (DataFormats/Scouting/data/),
# following the convention used for the Run 3 formats (see
# TestRun3ScoutingFormats.sh). This script should then be extended to
# read each such old file with test_readPhase2Scouting_cfg.py, and
# TestReadPhase2Scouting.cc should gain the corresponding class-version
# parameters to check only the content available in that version.
#
# The versions of the classes are encoded in the filenames
# following the order in which the Phase2Scouting classes appear in
# classes_def.xml. That order is as follows.
#
#  Phase2ScoutingCaloJet
#  Phase2ScoutingElectron
#  Phase2ScoutingHitPatternPOD
#  Phase2ScoutingMuon
#  Phase2ScoutingParticle
#  Phase2ScoutingPFJet
#  Phase2ScoutingPhoton
#  Phase2ScoutingTrack
#  Phase2ScoutingVertex
#  Phase2ScoutingEBRecHit
#  Phase2ScoutingEERecHit
#  Phase2ScoutingHBHERecHit
#
# e.g. testPhase2Scouting_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_v3_CMSSW_X_Y_Z_split_99.root
#
# By default, split level 99 is used (maximum possible splitting).
# If the suffix "_split_0" is near the end of the filename, the
# following was added to the configuration of the output module:
#     "splitLevel = cms.untracked.int32(0)"

exit 0
