The `test/` directory of the `HLTrigger/Configuration` package contains

 - scripts to copy HLT menus from the `ConfDB` database into CMSSW,
   as both `cff` fragments (loadable via `cmsDriver.py`) and standalone `cfg` configurations (usable with `cmsRun`);

 - scripts to run tests with these HLT menus
   (a version of these tests runs in CMSSW integration buils as the so-called "HLT-Validation" tests);

 - a unit test to verify the availability of the EDM input files used in the HLT tests maintained in CMSSW by the Trigger Studies Group
   (see `testAccessToEDMInputsOfHLTTests` below).

_Important_ : when the names of the EDM files hard-coded in
`HLTrigger/Configuration/test/cmsDriver.csh` and/or
`Configuration/HLT/python/addOnTestsHLT.py` are changed, make sure to
(1) commit your local changes, and then
(2) execute the script `HLTrigger/Configuration/test/testAccessToEDMInputsOfHLTTests_update_filelist.sh`
in order to update the file `HLTrigger/Configuration/test/testAccessToEDMInputsOfHLTTests_filelist.txt`.
The latter contains the list of files queried by the unit test `testAccessToEDMInputsOfHLTTests` (see below),
which will then be cached in the IB-EOS area at the CERN T2.

---

Unit test: `testAccessToEDMInputsOfHLTTests`
---

This unit test executes `cmsRun` jobs to verify the availability
of the EDM files listed in `HLTrigger/Configuration/test/testAccessToEDMInputsOfHLTTests_filelist.txt`.

To run the unit test via `scram`, execute
```bash
scram b runtests_testAccessToEDMInputsOfHLTTests
```
To run the unit test locally, execute
```bash
cd "${CMSSW_BASE}"/src/HLTrigger/Configuration/test && \
 SCRAM_TEST_PATH=. ./testAccessToEDMInputsOfHLTTests.sh
```

The unit test does not modify the content of the file `testAccessToEDMInputsOfHLTTests_filelist.txt`.
The latter can be updated by manually executing the script `testAccessToEDMInputsOfHLTTests_update_filelist.sh`.

 - The file `testAccessToEDMInputsOfHLTTests_filelist.txt` lists
   the Logical File Name (LFN) of the EDM files used in HLT tests for
   (1) the main CMSSW development branches (name format: `CMSSW_[0-9]*_[0-9]*_X`), and
   (2) the HEAD of local CMSSW in use.

 - The script `testAccessToEDMInputsOfHLTTests_update_filelist.sh` ignores other branches,
   as well as local modifications which have not been committed yet.

 - The file `testAccessToEDMInputsOfHLTTests_filelist.txt` lists only EDM files which are either
   (1) cached in the IB-EOS area at the CERN T2, or
   (2) accessible remotely via the redirector `cms-xrd-global.cern.ch`.

Here are the steps one normally executes to update the
EDM input files and the unit test `testAccessToEDMInputsOfHLTTests`.

 - Update the input EDM files where needed,
   e.g. `addOnTestsHLT.py` and/or `cmsDriver.csh`.

 - Test, and commit the changes.

 - Run `testAccessToEDMInputsOfHLTTests_update_filelist.sh`
   (this will update `testAccessToEDMInputsOfHLTTests_filelist.txt`, if needed).

 - Run the unit test (e.g. `scram b runtests_testAccessToEDMInputsOfHLTTests`).

 - Commit the changes to `testAccessToEDMInputsOfHLTTests_filelist.txt`, if any.


---

Unit test: `test_OnlineVsDevTablesConsistency.sh`
---

This unit test checks consistency between the **online HLT configuration files** and their corresponding **reference files** in `HLTrigger/Configuration/tables`.

## What it does
- Verifies that all HLT paths listed in each `online_*.txt` file also exist in the matching reference file.
- Ignores comment lines and excludes known technical paths (`HLTAnalyzerEndpath`, `RatesMonitoring`, `DQMHistograms`).
- Fails if any online paths are missing from the reference set.

## Files compared
| Online file                  | Reference file |
|-------------------------------|----------------|
| `online_pion.txt`            | `PIon.txt`     |
| `online_hion.txt`            | `HIon.txt`     |
| `online_pref.txt`            | `PRef.txt`     |
| `online_Circulating.txt`     | `Special.txt`  |
| `online_PPS.txt`             | `Special.txt`  |
| `online_LumiScan.txt`        | `Special.txt`  |
| `online_FirstCollisions.txt` | `Special.txt`  |
| `online_ECAL.txt`            | `Special.txt`  |
| `online_Cosmics.txt`         | `Special.txt`  |
| `online_TrackerVR.txt`       | `Special.txt`  |
| `online_Splashes.txt`        | `Special.txt`  |
| `online_Special.txt`         | `Special.txt`  |
| `online_grun.txt`            | `GRun.txt`     |

## Usage
From a CMSSW environment:
```bash
./test_OnlineVsDevTablesConsistency.sh
```
