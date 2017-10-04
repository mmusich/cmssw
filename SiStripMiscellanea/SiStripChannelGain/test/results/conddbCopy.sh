#!/bin/bash
FILES=$(pwd)/*smear*.db
COUNTER=2
for f in $FILES 
do
  echo "Processing $f file... $COUNTER"
  # take action on each file. $f store current file name
  conddb_import -c sqlite_file:toInspect.db -f sqlite_file:$f -i modifiedGains -t g2_for_testMatrix -b $COUNTER
  COUNTER=$[$COUNTER +1]
done