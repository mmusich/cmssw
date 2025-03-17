import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.EgammaHLTHcalVarProducerFromRecHit import EgammaHLTHcalVarProducerFromRecHit as _EgammaHLTHcalVarProducerFromRecHit

hltEgammaHoverEL1Seeded = _EgammaHLTHcalVarProducerFromRecHit(
    absEtaLowEdges = [0.0, 1.479],
    depth = 0,
    doEtSum = False,
    doRhoCorrection = False,
    effectiveAreas = [0.105, 0.17],
    innerCone = 0.0,
    outerCone = 0.14,
    recoEcalCandidateProducer = ("hltEgammaCandidatesL1Seeded"),
    rhoMax = 99999999.0,
    rhoProducer = ("hltFixedGridRhoFastjetAllCaloForEGamma"),
    rhoScale = 1.0,
    useSingleTower = False,
    hbheRecHitsTag = cms.InputTag( "hltHbhereco" ),
    eThresHB = [ 0.1, 0.2, 0.3, 0.3 ], #Run3 thresholds. Will be overwritten with valid aging customisation
    etThresHB = [ 0.0, 0.0, 0.0, 0.0 ],
    eThresHE = [ 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2 ],
    etThresHE = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ],
    usePFThresholdsFromDB = True,
    maxSeverityHB =  9 ,
    maxSeverityHE =  9 
)
