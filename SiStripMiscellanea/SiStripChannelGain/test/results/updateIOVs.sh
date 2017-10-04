#!/bin/bash
FILES=$(pwd)/*.db
for f in $FILES 
do
  echo "Processing $f file..."
  # take action on each file. $f store current file name
  echo 'update IOV set SINCE=1 where SINCE=303014;' | sqlite3 $f 
done