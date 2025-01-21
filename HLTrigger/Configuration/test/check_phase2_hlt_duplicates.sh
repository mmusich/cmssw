#!/bin/bash

# Directory for the generated files
OUTPUT_DIR="hlt_test_configs"
PYTHON_FILE="$OUTPUT_DIR/Phase2_dump_cfg.py"
DUMP_FILE="$OUTPUT_DIR/Phase2_dump.py"
GROUPS_FILE="hltFindDuplicates_output/groups.txt"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Step 1: Generate the Python file
cat << EOF > "$PYTHON_FILE"
import FWCore.ParameterSet.Config as cms
process = cms.Process("HLT")
process.load("HLTrigger.Configuration.HLT_75e33_cff")
EOF

# Step 2: Run edmConfigDump on the generated Python file
echo "Running edmConfigDump..."
edmConfigDump "$PYTHON_FILE" > "$DUMP_FILE"
if [[ $? -ne 0 ]]; then
  echo "Error: edmConfigDump failed."
  exit 1
fi

# Step 3: Run hltFindDuplicates on the dumped configuration
echo "Running hltFindDuplicates..."
more "$DUMP_FILE" | hltFindDuplicates
if [[ $? -ne 0 ]]; then
  echo "Error: hltFindDuplicates failed."
  exit 1
fi

# Step 4: Check if groups.txt is empty
if [[ ! -f "$GROUPS_FILE" ]]; then
  echo "Error: $GROUPS_FILE not found."
  exit 1
fi

if [[ -s "$GROUPS_FILE" ]]; then
  echo "Duplicates found. Contents of $GROUPS_FILE:"
  cat "$GROUPS_FILE"
  exit 1
else
  echo "No duplicates found. Exiting successfully."
  exit 0
fi
