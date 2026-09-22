#  DataFormats/Scouting

## Scouting Data Formats

Any changes to the Scouting data formats must be backwards compatible. In order to ensure the Scouting formats can be read by all future CMSSW releases, there is a `TestRun3ScoutingDataFormats` unit test, which makes use of the `TestReadRun3Scouting` analyzer and the `TestWriteRun3Scouting` producer. The unit test checks that the objects can be read properly from

* a file written by the same release
* files written by (some) earlier releases

If the persistent format of any Scouting data format gets changed in the future, please adjust the `TestReadRun3Scouting` and `TestWriteRun3Scouting` modules accordingly. It is important that every member container has some content in this test. Please also add new files to the [https://github.com/cms-data/DataFormats-Scouting/](https://github.com/cms-data/DataFormats-Scouting/) repository, and update the `TestRun3ScoutingDataFormats` unit test to read the newly created files. There should be one file written with split level 0 and one with split level 99. The file name should contain the version numbers of the data format classes (from classes_def.xml) in alphabetical order (they are in this alphabetical order already in classes_def.xml), the release or pre-release with which it was written and the split level. If the latest file of Run 3 scouting before the update has not been used in data taking, the file can be deleted.

There are analogous tests for Run 2. It is unlikely those formats will change anymore.

## Phase 2 Scouting Data Formats

The `Phase2Scouting*` classes are the data formats for HLT scouting in Phase 2. They were introduced as exact copies of the `Run3Scouting*` classes (all starting at `ClassVersion="3"`), so that they can evolve independently of the Run 3 formats, which are frozen by the requirement of backward compatibility with the data already taken. The same rules apply to them: any change must be backwards compatible, and the `TestPhase2ScoutingDataFormats` unit test (based on the `TestReadPhase2Scouting` and `TestWritePhase2Scouting` modules) must be kept up to date. At the moment the test only checks a file written by the same release; once the Phase 2 formats have been used to write data that needs to stay readable, old files should be added to the cms-data repository and to the test, following the Run 3 convention described above.

## Scouting format traits

`ScoutingFormatTraits.h` defines the `scouting::Run3Format` and `scouting::Phase2Format` trait structs, mapping each kind of scouting object (`CaloJet`, `Electron`, `Muon`, `Vertex`, ...) and collection to the corresponding `Run3Scouting*` or `Phase2Scouting*` class. The HLT scouting packer producers (`HLTScoutingCaloProducer`, `HLTScoutingPFProducer`, `HLTScoutingPrimaryVertexProducer`, `HLTScoutingEgammaProducer`, `HLTScoutingMuonProducer`, `HLTScoutingTrackProducer`) are written against these traits, and select the family of data formats to produce at configuration time via the `scoutingFormat` parameter (`"Run3"`, the default, or `"Phase2"`).
