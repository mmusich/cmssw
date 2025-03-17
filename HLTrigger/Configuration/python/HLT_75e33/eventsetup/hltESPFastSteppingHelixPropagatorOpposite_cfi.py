import FWCore.ParameterSet.Config as cms

from TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorESProducer import SteppingHelixPropagatorESProducer as _SteppingHelixPropagatorESProducer

hltESPFastSteppingHelixPropagatorOpposite = _SteppingHelixPropagatorESProducer(
    ApplyRadX0Correction = True,
    AssumeNoMaterial = False,
    ComponentName = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
    NoErrorPropagation = False,
    PropagationDirection = cms.string('oppositeToMomentum'),
    SetVBFPointer = False,
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = False,
    endcapShiftInZNeg = 0.0,
    endcapShiftInZPos = 0.0,
    returnTangentPlane = True,
    sendLogWarning = False,
    useEndcapShiftsInZ = False,
    useInTeslaFromMagField = False,
    useIsYokeFlag = True,
    useMagVolumes = True,
    useMatVolumes = True,
    useTuningForL2Speed = True
)
