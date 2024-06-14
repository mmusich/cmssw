#!/bin/bash -ex

# Directory containing .dat files
directory="run380649"

# Check if the directory exists
if [ -d "$directory" ]; then
  echo "Directory '$directory' exists."

  # Remove the directory
  rm -r "$directory"
  
  # Verify removal
  if [ ! -d "$directory" ]; then
    echo "Directory '$directory' has been removed."
  else
    echo "Failed to remove directory '$directory'."
  fi
else
  echo "Directory '$directory' does not exist."
fi

mkdir $directory
cmsRun runRandomSiPixelErrorProducer_cfg.py

# Capture the output of the command into a variable
dat_file=$(ls "$directory" | grep .dat)
json_file=$(ls "$directory" | grep .jsn)

rm -fr $CMSSW_BASE/src/DQM/Integration/data/run380649/*.*
cd run380649
cat run380649_ls0000_streamDQMGPUvsCPU_*.ini $dat_file > $CMSSW_BASE/src/DQM/Integration/data/run380649/$dat_file

# Process the JSON file to remove consecutive zeros
jq '
  .data |= reduce .[] as $val ([];
    if $val == "0" and (.[-1] // null) == "0" then 
      . 
    else 
      . + [$val] 
    end
  )
' "$json_file" > output.jsn

echo "Processed JSON saved to $json_file"

cp output.jsn $CMSSW_BASE/src/DQM/Integration/data/run380649/$json_file
