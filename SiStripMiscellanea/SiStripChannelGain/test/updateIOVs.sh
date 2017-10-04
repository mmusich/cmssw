#!/bin/bash
FILES=/tmp/musich/CMSSW_9_4_X_2017-10-03-0000/src/SiStripMiscellanea/SiStripChannelGain/test/results/*
for f in $FILES
do
  echo "Processing $f file..."
  # take action on each file. $f store current file name
done