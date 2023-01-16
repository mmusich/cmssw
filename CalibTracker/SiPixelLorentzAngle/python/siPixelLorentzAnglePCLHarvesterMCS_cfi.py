import FWCore.ParameterSet.Config as cms

siPixelLorentzAnglePCLHarvesterMCS = cms.EDProducer(
    'SiPixelLorentzAnglePCLHarvesterMCS',
    dqmDir = cms.string('AlCaReco/SiPixelLorentzAngle'),
    newmodulelist = cms.vstring(),
    fitRange = cms.vdouble(
        -1.5,
        1.5
    ),
    record = cms.string('SiPixelLorentzAngleRcd'),
)
