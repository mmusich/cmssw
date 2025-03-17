import FWCore.ParameterSet.Config as cms
from ..psets.hgcal_reco_constants_cfi import HGCAL_reco_constants as HGCAL_reco_constants

from RecoLocalCalo.HGCalRecProducers.HGCalUncalibRecHitProducer import HGCalUncalibRecHitProducer as _HGCalUncalibRecHitProducer

hltHGCalUncalibRecHitL1Seeded = _HGCalUncalibRecHitProducer(
    HGCEEConfig = dict(
        adcNbits = 10,
        adcSaturation = 100,
        fCPerMIP = HGCAL_reco_constants.fcPerMip[0:3],
        isSiFE = True,
        tdcNbits = 12,
        tdcOnset = 60,
        tdcSaturation = 10000,
        toaLSB_ns = 0.0244,
        tofDelay = -9
    ),
    HGCEEdigiCollection = ("hltHgcalDigisL1Seeded","EE"),
    HGCEEhitCollection = 'HGCEEUncalibRecHits',
    HGCHEBConfig = dict(
        adcNbits = 10,
        adcSaturation = 68.75,
        fCPerMIP = [1.0, 1.0, 1.0],
        isSiFE = True,
        tdcNbits = 12,
        tdcOnset = 55,
        tdcSaturation = 1000,
        toaLSB_ns = 0.0244,
        tofDelay = -14
    ),
    HGCHEBdigiCollection = ("hltHgcalDigisL1Seeded","HEback"),
    HGCHEBhitCollection = 'HGCHEBUncalibRecHits',
    HGCHEFConfig = dict(
        adcNbits = 10,
        adcSaturation = 100,
        fCPerMIP = HGCAL_reco_constants.fcPerMip[3:6],
        isSiFE = True,
        tdcNbits = 12,
        tdcOnset = 60,
        tdcSaturation = 10000,
        toaLSB_ns = 0.0244,
        tofDelay = -11
    ),
    HGCHEFdigiCollection = ("hltHgcalDigisL1Seeded","HEfront"),
    HGCHEFhitCollection = 'HGCHEFUncalibRecHits',
    HGCHFNoseConfig = dict(
        adcNbits = 10,
        adcSaturation = 100,
        fCPerMIP = [1.25, 2.57, 3.88],
        isSiFE = False,
        tdcNbits = 12,
        tdcOnset = 60,
        tdcSaturation = 10000,
        toaLSB_ns = 0.0244,
        tofDelay = -33
    ),
    HGCHFNosedigiCollection = ("hfnoseDigis","HFNose"),
    HGCHFNosehitCollection = 'HGCHFNoseUncalibRecHits',
    computeLocalTime = False,
    algo = 'HGCalUncalibRecHitWorkerWeights'
)

from Configuration.ProcessModifiers.ticl_v5_cff import ticl_v5
ticl_v5.toModify(hltHGCalUncalibRecHitL1Seeded, computeLocalTime = True)
