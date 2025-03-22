#!/bin/sh

function die { echo $1: status $2 ; exit $2; }

echo " testing CondCore/ESSources/test/python/load* "

for entry in "${SCRAM_TEST_PATH}/python"/load*
do
  echo "===== Test \"cmsRun $entry \" ===="
  (cmsRun $entry) || die "Failure using cmsRun $entry" $?
done
