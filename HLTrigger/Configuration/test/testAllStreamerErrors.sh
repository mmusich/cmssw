#!/bin/bash

# Exit the script immediately if any command fails
set -e

# Enable pipefail to propagate the exit status of the entire pipeline
set -o pipefail

# input variables
hlt_menu="/online/collisions/2025/2e34/v1.1/HLT/V2"
l1t_menu="L1Menu_Collisions2025_v1_1_1_xml"
era="Run3_2025"
base_dir="/store/group/tsg/FOG/error_stream_root/run"
global_tag="150X_dataRun3_HLT_v1"
eos_cmd="eos"

# List of run numbers
runs=(
    ## corrupt L1T data
    
    #377893 # The GlobalAlgBlk unpacker result vector is empty, but is not receiving the first expected header ID!
    #378039 # The GlobalAlgBlk unpacker result vector is empty, but is not receiving the first expected header ID!
    #378113 # The GlobalAlgBlk unpacker result vector is empty, but is not receiving the first expected header ID!

    ### pp Data
    #378366 # see https://github.com/cms-sw/cmssw/issues/44541
    #378369 # see https://github.com/cms-sw/cmssw/issues/44541
    378906
    378940 # see https://github.com/cms-sw/cmssw/issues/44634
    378981 # see https://github.com/cms-sw/cmssw/issues/44639
    378985 # see https://github.com/cms-sw/cmssw/issues/44643
    378993 
    378994
    379154
    379174 # see https://github.com/cms-sw/cmssw/issues/44668
    380115 # see https://github.com/cms-sw/cmssw/issues/44940
    380360
    380399 # see https://github.com/cms-sw/cmssw/issues/44923
    380466 # see https://github.com/cms-sw/cmssw/issues/44940
    380513 
    380531 # see https://github.com/cms-sw/cmssw/issues/44940
    380624 # see https://github.com/cms-sw/cmssw/issues/44923
    381067 # see https://github.com/cms-sw/cmssw/issues/44923
    381147 # see https://github.com/cms-sw/cmssw/issues/44940
    381443 # see https://github.com/cms-sw/cmssw/issues/44923
    381479 # see https://github.com/cms-sw/cmssw/issues/44923
    381543 # see https://github.com/cms-sw/cmssw/issues/45136
    381544 # see https://github.com/cms-sw/cmssw/issues/45136
    381549 # see https://github.com/cms-sw/cmssw/issues/45834
    382250 # see https://github.com/cms-sw/cmssw/issues/44923
    382461 # see https://github.com/cms-sw/cmssw/issues/45312
    382580 # see https://github.com/cms-sw/cmssw/issues/44923
    382594 # see https://github.com/cms-sw/cmssw/issues/44923
    382617 # see https://github.com/cms-sw/cmssw/issues/45834
    382654 # see https://github.com/cms-sw/cmssw/issues/44923
    383034 # see https://github.com/cms-sw/cmssw/issues/45834
    383155 # see https://github.com/cms-sw/cmssw/issues/45834 
    383162 # see https://github.com/cms-sw/cmssw/issues/45834
    383219 # see https://github.com/cms-sw/cmssw/issues/45477
    383254  
    383255 
    383363 # see https://github.com/cms-sw/cmssw/issues/45834
    383368 # see https://github.com/cms-sw/cmssw/issues/45512
    383377 # see https://github.com/cms-sw/cmssw/issues/45834
    383468 
    383485 
    383631 
    383669 
    383812 
    383814
    383830 # see https://github.com/cms-sw/cmssw/issues/45595
    383834 
    384069 # see https://github.com/cms-sw/cmssw/issues/45639
    386614 # see https://github.com/cms-sw/cmssw/issues/45555
    386872 # see https://github.com/cms-sw/cmssw/issues/45555
    386951 # see https://github.com/cms-sw/cmssw/issues/45555
    392441 # see https://github.com/cms-sw/cmssw/issues/48157
    392669 # see https://github.com/cms-sw/cmssw/issues/48205
)

runsHI=(
    ## HION data
    388037 # see https://github.com/cms-sw/cmssw/issues/46656
    388317 # see https://github.com/cms-sw/cmssw/issues/43078
    388390 # see https://github.com/cms-sw/cmssw/issues/43078
    388401 # see https://github.com/cms-sw/cmssw/issues/43078
    388402 # see https://github.com/cms-sw/cmssw/issues/43078
    388419 # see https://github.com/cms-sw/cmssw/issues/43078
    388769 # see https://github.com/cms-sw/cmssw/issues/46783
    388770 # see https://github.com/cms-sw/cmssw/issues/46783
)

# Generate base config only once
base_config="hlt_base.py"
hltGetConfiguration ${hlt_menu} \
  --globaltag ${global_tag} \
  --data \
  --no-prescale \
  --no-output \
  --max-events -1 \
  --eras ${era} --l1-emulator uGT --l1 ${l1t_menu} \
  --input dummy.root > ${base_config}

# Append constant options
cat <<@EOF >> ${base_config}
del process.MessageLogger
process.load('FWCore.MessageService.MessageLogger_cfi')  
process.options.wantSummary = True
process.options.numberOfThreads = 8
process.options.numberOfStreams = 8
@EOF

# Loop over runs
for run in "${runsHI[@]}"; do
  export MALLOC_CONF=junk:true

  input_dir="${base_dir}${run}"
  root_files=$(${eos_cmd} find -f "/eos/cms${input_dir}" -name "*.root" | awk '{print "root://eoscms.cern.ch/" $0}' | paste -sd, -)

  if [ -z "${root_files}" ]; then
    echo "No root files found for run ${run} in directory ${input_dir}."
    continue
  fi

  # Copy base config and create a run-specific config
  run_config="hlt_run${run}.py"
  cp ${base_config} ${run_config}

  # Overwrite the fileNames block by appending a new assignment at the end
  echo "process.source.fileNames = cms.untracked.vstring(" >> ${run_config}
  IFS=',' read -ra FILE_ARRAY <<< "$root_files"
  for f in "${FILE_ARRAY[@]}"; do
      echo "    '${f}'," >> ${run_config}
  done
  echo ")" >> ${run_config}

  # Run cmsRun
  log_file="hlt_run${run}.log"
  echo "Starting cmsRun for run ${run}"

  cmsRun ${run_config} &> ${log_file} || {
      echo "Run ${run} failed. See log: ${log_file}"
      exit 1
  }
  echo "Run ${run} finished successfully."

  #if cmsRun ${run_config} &> ${log_file}; then
  #  echo "Run ${run} finished successfully."
  #else
  #  echo "Run ${run} failed. See log: ${log_file}"
  #fi
done
