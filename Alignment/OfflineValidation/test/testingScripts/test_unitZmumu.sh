#! /bin/bash

function die { echo $1: status $2 ; exit $2; }

echo "TESTING Alignment/Zmumu single configuration with json..."
pushd test_yaml/Zmumu/single/testSingleZmumu/unitTestZmumuMC/1/
./cmsRun validation_cfg.py config=validation.json || die "Failure running Zmumu single configuration with json" $?

echo "TESTING Alignment/Zmumu single configuration standalone..."
./cmsRun validation_cfg.py || die "Failure running Zmumu single configuration standalone" $?
popd

echo "TESTING Zmumu merge step"
pushd test_yaml/Zmumu/merge/testSingleZmumu/1/
./Zmumumerge validation.json --verbose || die "Failure running Zmumu merge step" $?
popd
