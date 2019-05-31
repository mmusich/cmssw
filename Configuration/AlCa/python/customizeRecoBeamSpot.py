import FWCore.ParameterSet.Config as cms

# customize reco BS for GaussSigmaZ4cmRealistic
def customGaussBSRealistic(process):

    if not hasattr(process.GlobalTag,'toGet'):
        process.GlobalTag.toGet=cms.VPSet()

    process.GlobalTag.toGet.extend(cms.VPSet(cms.PSet(record = cms.string('BeamSpotObjectsRcd'),
                                                      tag = cms.string('GaussBSRealistic'),
                                                      connect = cms.string('sqlite_file:/afs/cern.ch/user/m/musich/public/forErichS/GaussBSRealistic.db'))
                                             )
                                   )            
    return process

# customize reco BS for GaussSigmaZ4cmDisplaced
def customGaussBSDisplaced(process):

    if not hasattr(process.GlobalTag,'toGet'):
        process.GlobalTag.toGet=cms.VPSet()

    process.GlobalTag.toGet.extend(cms.VPSet(cms.PSet(record = cms.string('BeamSpotObjectsRcd'),
                                                      tag = cms.string('GaussBSDisplaced'),
                                                      connect = cms.string('sqlite_file:/afs/cern.ch/user/m/musich/public/forErichS/GaussBSDisplaced.db'))
                                             )
                                   )            
    return process

# customize reco BS for Realistic25ns13TeVEarly2018CollisionCentered
def customRealistic2018BSCentered(process):

    if not hasattr(process.GlobalTag,'toGet'):
        process.GlobalTag.toGet=cms.VPSet()

    process.GlobalTag.toGet.extend(cms.VPSet(cms.PSet(record = cms.string('BeamSpotObjectsRcd'),
                                                      tag = cms.string('Realistic2018BSCentered'),
                                                      connect = cms.string('sqlite_file:/afs/cern.ch/user/m/musich/public/forErichS/Realistic2018BSCentered.db'))
                                             )
                                   )            
    return process

# customize reco BS for Realistic25ns13TeVEarly2018CollisionDisplaced
def customRealistic2018BSDisplaced(process):

    if not hasattr(process.GlobalTag,'toGet'):
        process.GlobalTag.toGet=cms.VPSet()

    process.GlobalTag.toGet.extend(cms.VPSet(cms.PSet(record = cms.string('BeamSpotObjectsRcd'),
                                                      tag = cms.string('Realistic2018BDisplaced'),
                                                      connect = cms.string('sqlite_file:/afs/cern.ch/user/m/musich/public/forErichS/Realistic2018BDisplaced.db'))
                                             )
                                   )            
    return process
