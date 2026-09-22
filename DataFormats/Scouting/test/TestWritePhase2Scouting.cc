// -*- C++ -*-
//
// Package:    DataFormats/Scouting
// Class:      TestWritePhase2Scouting
//
/**\class edmtest::TestWritePhase2Scouting
  Description: Used as part of tests that ensure the Phase 2 scouting
  data formats can be persistently written and in a subsequent process
  read. First, this is done using the current release version for writing
  and reading. In addition, the output file of the write process should
  be saved permanently each time a Phase 2 Scouting persistent data
  format changes. In unit tests, we read each of those saved files to verify
  that the current releases can read older versions of the data format.
*/
// Original Author:  W. David Dagenhart
//         Created:  17 May 2023

#include "DataFormats/Scouting/interface/Phase2ScoutingCaloJet.h"
#include "DataFormats/Scouting/interface/Phase2ScoutingElectron.h"
#include "DataFormats/Scouting/interface/Phase2ScoutingHitPatternPOD.h"
#include "DataFormats/Scouting/interface/Phase2ScoutingMuon.h"
#include "DataFormats/Scouting/interface/Phase2ScoutingParticle.h"
#include "DataFormats/Scouting/interface/Phase2ScoutingPFJet.h"
#include "DataFormats/Scouting/interface/Phase2ScoutingPhoton.h"
#include "DataFormats/Scouting/interface/Phase2ScoutingTrack.h"
#include "DataFormats/Scouting/interface/Phase2ScoutingVertex.h"
#include "DataFormats/Scouting/interface/Phase2ScoutingEBRecHit.h"
#include "DataFormats/Scouting/interface/Phase2ScoutingEERecHit.h"
#include "DataFormats/Scouting/interface/Phase2ScoutingHBHERecHit.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/ParameterSetDescription.h"
#include "FWCore/Utilities/interface/EDPutToken.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "FWCore/Utilities/interface/StreamID.h"

#include <memory>
#include <utility>
#include <vector>

namespace edmtest {

  class TestWritePhase2Scouting : public edm::global::EDProducer<> {
  public:
    TestWritePhase2Scouting(edm::ParameterSet const&);
    void produce(edm::StreamID, edm::Event&, edm::EventSetup const&) const override;
    static void fillDescriptions(edm::ConfigurationDescriptions&);

  private:
    void produceCaloJets(edm::Event&) const;
    void produceElectrons(edm::Event&) const;
    void produceMuons(edm::Event&) const;
    void produceParticles(edm::Event&) const;
    void producePFJets(edm::Event&) const;
    void producePhotons(edm::Event&) const;
    void produceTracks(edm::Event&) const;
    void produceVertexes(edm::Event&) const;
    void produceEBRecHits(edm::Event&) const;
    void produceEERecHits(edm::Event&) const;
    void produceHBHERecHits(edm::Event&) const;

    void throwWithMessage(const char*) const;

    const std::vector<double> caloJetsValues_;
    const edm::EDPutTokenT<std::vector<Phase2ScoutingCaloJet>> caloJetsPutToken_;

    const std::vector<double> electronsFloatingPointValues_;
    const std::vector<int> electronsIntegralValues_;
    const edm::EDPutTokenT<std::vector<Phase2ScoutingElectron>> electronsPutToken_;

    const std::vector<double> muonsFloatingPointValues_;
    const std::vector<int> muonsIntegralValues_;
    const edm::EDPutTokenT<std::vector<Phase2ScoutingMuon>> muonsPutToken_;

    const std::vector<double> particlesFloatingPointValues_;
    const std::vector<int> particlesIntegralValues_;
    const edm::EDPutTokenT<std::vector<Phase2ScoutingParticle>> particlesPutToken_;

    const std::vector<double> pfJetsFloatingPointValues_;
    const std::vector<int> pfJetsIntegralValues_;
    const edm::EDPutTokenT<std::vector<Phase2ScoutingPFJet>> pfJetsPutToken_;

    const std::vector<double> photonsFloatingPointValues_;
    const std::vector<int> photonsIntegralValues_;
    const edm::EDPutTokenT<std::vector<Phase2ScoutingPhoton>> photonsPutToken_;

    const std::vector<double> tracksFloatingPointValues_;
    const std::vector<int> tracksIntegralValues_;
    const edm::EDPutTokenT<std::vector<Phase2ScoutingTrack>> tracksPutToken_;

    const std::vector<double> vertexesFloatingPointValues_;
    const std::vector<int> vertexesIntegralValues_;
    const edm::EDPutTokenT<std::vector<Phase2ScoutingVertex>> vertexesPutToken_;

    const std::vector<double> ebRecHitsFloatingPointValues_;
    const std::vector<int> ebRecHitsIntegralValues_;
    const edm::EDPutTokenT<std::vector<Phase2ScoutingEBRecHit>> ebRecHitsPutToken_;

    const std::vector<double> eeRecHitsFloatingPointValues_;
    const std::vector<int> eeRecHitsIntegralValues_;
    const edm::EDPutTokenT<std::vector<Phase2ScoutingEERecHit>> eeRecHitsPutToken_;

    const std::vector<double> hbheRecHitsFloatingPointValues_;
    const std::vector<int> hbheRecHitsIntegralValues_;
    const edm::EDPutTokenT<std::vector<Phase2ScoutingHBHERecHit>> hbheRecHitsPutToken_;
  };

  TestWritePhase2Scouting::TestWritePhase2Scouting(edm::ParameterSet const& iPSet)
      : caloJetsValues_(iPSet.getParameter<std::vector<double>>("caloJetsValues")),
        caloJetsPutToken_(produces()),
        electronsFloatingPointValues_(iPSet.getParameter<std::vector<double>>("electronsFloatingPointValues")),
        electronsIntegralValues_(iPSet.getParameter<std::vector<int>>("electronsIntegralValues")),
        electronsPutToken_(produces()),
        muonsFloatingPointValues_(iPSet.getParameter<std::vector<double>>("muonsFloatingPointValues")),
        muonsIntegralValues_(iPSet.getParameter<std::vector<int>>("muonsIntegralValues")),
        muonsPutToken_(produces()),
        particlesFloatingPointValues_(iPSet.getParameter<std::vector<double>>("particlesFloatingPointValues")),
        particlesIntegralValues_(iPSet.getParameter<std::vector<int>>("particlesIntegralValues")),
        particlesPutToken_(produces()),
        pfJetsFloatingPointValues_(iPSet.getParameter<std::vector<double>>("pfJetsFloatingPointValues")),
        pfJetsIntegralValues_(iPSet.getParameter<std::vector<int>>("pfJetsIntegralValues")),
        pfJetsPutToken_(produces()),
        photonsFloatingPointValues_(iPSet.getParameter<std::vector<double>>("photonsFloatingPointValues")),
        photonsIntegralValues_(iPSet.getParameter<std::vector<int>>("photonsIntegralValues")),
        photonsPutToken_(produces()),
        tracksFloatingPointValues_(iPSet.getParameter<std::vector<double>>("tracksFloatingPointValues")),
        tracksIntegralValues_(iPSet.getParameter<std::vector<int>>("tracksIntegralValues")),
        tracksPutToken_(produces()),
        vertexesFloatingPointValues_(iPSet.getParameter<std::vector<double>>("vertexesFloatingPointValues")),
        vertexesIntegralValues_(iPSet.getParameter<std::vector<int>>("vertexesIntegralValues")),
        vertexesPutToken_(produces()),
        ebRecHitsFloatingPointValues_(iPSet.getParameter<std::vector<double>>("ebRecHitsFloatingPointValues")),
        ebRecHitsIntegralValues_(iPSet.getParameter<std::vector<int>>("ebRecHitsIntegralValues")),
        ebRecHitsPutToken_(produces()),
        eeRecHitsFloatingPointValues_(iPSet.getParameter<std::vector<double>>("eeRecHitsFloatingPointValues")),
        eeRecHitsIntegralValues_(iPSet.getParameter<std::vector<int>>("eeRecHitsIntegralValues")),
        eeRecHitsPutToken_(produces()),
        hbheRecHitsFloatingPointValues_(iPSet.getParameter<std::vector<double>>("hbheRecHitsFloatingPointValues")),
        hbheRecHitsIntegralValues_(iPSet.getParameter<std::vector<int>>("hbheRecHitsIntegralValues")),
        hbheRecHitsPutToken_(produces()) {
    if (caloJetsValues_.size() != 16) {
      throwWithMessage("caloJetsValues must have 16 elements and it does not");
    }
    if (electronsFloatingPointValues_.size() != 33) {
      throwWithMessage("electronsFloatingPointValues must have 33 elements and it does not");
    }
    if (electronsIntegralValues_.size() != 8) {
      throwWithMessage("electronsIntegralValues must have 8 elements and it does not");
    }
    if (muonsFloatingPointValues_.size() != 37) {
      throwWithMessage("muonsFloatingPointValues must have 37 elements and it does not");
    }
    if (muonsIntegralValues_.size() != 26) {
      throwWithMessage("muonsIntegralValues must have 26 elements and it does not");
    }
    if (particlesFloatingPointValues_.size() != 11) {
      throwWithMessage("particlesFloatingPointValues must have 11 elements and it does not");
    }
    if (particlesIntegralValues_.size() != 5) {
      throwWithMessage("particlesIntegralValues must have 5 elements and it does not");
    }
    if (pfJetsFloatingPointValues_.size() != 15) {
      throwWithMessage("pfJetsFloatingPointValues must have 15 elements and it does not");
    }
    if (pfJetsIntegralValues_.size() != 8) {
      throwWithMessage("pfJetsIntegralValues must have 8 elements and it does not");
    }
    if (photonsFloatingPointValues_.size() != 17) {
      throwWithMessage("photonsFloatingPointValues must have 17 elements and it does not");
    }
    if (photonsIntegralValues_.size() != 5) {
      throwWithMessage("photonsIntegralValues must have 5 elements and it does not");
    }
    if (tracksFloatingPointValues_.size() != 29) {
      throwWithMessage("tracksFloatingPointValues must have 29 elements and it does not");
    }
    if (tracksIntegralValues_.size() != 5) {
      throwWithMessage("tracksIntegralValues must have 5 elements and it does not");
    }
    if (vertexesFloatingPointValues_.size() != 10) {
      throwWithMessage("vertexesFloatingPointValues must have 10 elements and it does not");
    }
    if (vertexesIntegralValues_.size() != 3) {
      throwWithMessage("vertexesIntegralValues must have 3 elements and it does not");
    }
    if (ebRecHitsFloatingPointValues_.size() != 2) {
      throwWithMessage("ebRecHitsFloatingPointValues must have 2 elements and it does not");
    }
    if (ebRecHitsIntegralValues_.size() != 2) {
      throwWithMessage("ebRecHitsIntegralValues must have 2 elements and it does not");
    }
    if (eeRecHitsFloatingPointValues_.size() != 2) {
      throwWithMessage("eeRecHitsFloatingPointValues must have 2 elements and it does not");
    }
    if (eeRecHitsIntegralValues_.size() != 1) {
      throwWithMessage("eeRecHitsIntegralValues must have 1 elements and it does not");
    }
    if (hbheRecHitsFloatingPointValues_.size() != 2) {
      throwWithMessage("hbheRecHitsFloatingPointValues must have 2 elements and it does not");
    }
    if (hbheRecHitsIntegralValues_.size() != 1) {
      throwWithMessage("hbheRecHitsIntegralValues must have 1 elements and it does not");
    }
  }

  void TestWritePhase2Scouting::produce(edm::StreamID, edm::Event& iEvent, edm::EventSetup const&) const {
    // Fill Phase2 scouting objects. Make sure all the containers inside
    // of them have something in them (not empty). The values are meaningless.
    // We will later check that after writing these objects to persistent storage
    // and then reading them in a later process we obtain matching values for
    // all this content.

    produceCaloJets(iEvent);
    produceElectrons(iEvent);
    produceMuons(iEvent);
    produceParticles(iEvent);
    producePFJets(iEvent);
    producePhotons(iEvent);
    produceTracks(iEvent);
    produceVertexes(iEvent);
    produceEBRecHits(iEvent);
    produceEERecHits(iEvent);
    produceHBHERecHits(iEvent);
  }

  void TestWritePhase2Scouting::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
    edm::ParameterSetDescription desc;
    desc.add<std::vector<double>>("caloJetsValues");
    desc.add<std::vector<double>>("electronsFloatingPointValues");
    desc.add<std::vector<int>>("electronsIntegralValues");
    desc.add<std::vector<double>>("muonsFloatingPointValues");
    desc.add<std::vector<int>>("muonsIntegralValues");
    desc.add<std::vector<double>>("particlesFloatingPointValues");
    desc.add<std::vector<int>>("particlesIntegralValues");
    desc.add<std::vector<double>>("pfJetsFloatingPointValues");
    desc.add<std::vector<int>>("pfJetsIntegralValues");
    desc.add<std::vector<double>>("photonsFloatingPointValues");
    desc.add<std::vector<int>>("photonsIntegralValues");
    desc.add<std::vector<double>>("tracksFloatingPointValues");
    desc.add<std::vector<int>>("tracksIntegralValues");
    desc.add<std::vector<double>>("vertexesFloatingPointValues");
    desc.add<std::vector<int>>("vertexesIntegralValues");
    desc.add<std::vector<double>>("ebRecHitsFloatingPointValues");
    desc.add<std::vector<int>>("ebRecHitsIntegralValues");
    desc.add<std::vector<double>>("eeRecHitsFloatingPointValues");
    desc.add<std::vector<int>>("eeRecHitsIntegralValues");
    desc.add<std::vector<double>>("hbheRecHitsFloatingPointValues");
    desc.add<std::vector<int>>("hbheRecHitsIntegralValues");
    descriptions.addDefault(desc);
  }

  void TestWritePhase2Scouting::produceCaloJets(edm::Event& iEvent) const {
    auto phase2ScoutingCaloJets = std::make_unique<std::vector<Phase2ScoutingCaloJet>>();
    unsigned int vectorSize = 2 + iEvent.id().event() % 4;
    phase2ScoutingCaloJets->reserve(vectorSize);
    for (unsigned int i = 0; i < vectorSize; ++i) {
      double offset = static_cast<double>(iEvent.id().event() + i);
      phase2ScoutingCaloJets->emplace_back(static_cast<float>(caloJetsValues_[0] + offset),
                                           static_cast<float>(caloJetsValues_[1] + offset),
                                           static_cast<float>(caloJetsValues_[2] + offset),
                                           static_cast<float>(caloJetsValues_[3] + offset),
                                           static_cast<float>(caloJetsValues_[4] + offset),
                                           static_cast<float>(caloJetsValues_[5] + offset),
                                           static_cast<float>(caloJetsValues_[6] + offset),
                                           static_cast<float>(caloJetsValues_[7] + offset),
                                           static_cast<float>(caloJetsValues_[8] + offset),
                                           static_cast<float>(caloJetsValues_[9] + offset),
                                           static_cast<float>(caloJetsValues_[10] + offset),
                                           static_cast<float>(caloJetsValues_[11] + offset),
                                           static_cast<float>(caloJetsValues_[12] + offset),
                                           static_cast<float>(caloJetsValues_[13] + offset),
                                           static_cast<float>(caloJetsValues_[14] + offset),
                                           static_cast<float>(caloJetsValues_[15] + offset));
    }
    iEvent.put(caloJetsPutToken_, std::move(phase2ScoutingCaloJets));
  }

  void TestWritePhase2Scouting::produceElectrons(edm::Event& iEvent) const {
    auto phase2ScoutingElectrons = std::make_unique<std::vector<Phase2ScoutingElectron>>();
    unsigned int vectorSize = 2 + iEvent.id().event() % 4;
    phase2ScoutingElectrons->reserve(vectorSize);
    for (unsigned int i = 0; i < vectorSize; ++i) {
      double offset = static_cast<double>(iEvent.id().event() + i);
      int iOffset = static_cast<int>(iEvent.id().event() + i);

      // Note the first eleven of these vectors use an out of sequence index
      // (starting at 19 or 5) because they are data members added in a format
      // change. In the CMSSW_12_4_0 version, they didn't exist.
      // Also the index values 4 and 5 in electronsFloatingPointValues_
      // and index 1 in electronsIntegralValues_ are not used because
      // those data members were dropped in the same format change.
      std::vector<float> trkd0;
      std::vector<float> trkdz;
      std::vector<float> trkpt;
      std::vector<float> trketa;
      std::vector<float> trkphi;
      std::vector<float> trkpMode;
      std::vector<float> trketaMode;
      std::vector<float> trkphiMode;
      std::vector<float> trkqoverpModeError;
      std::vector<float> trkchi2overndf;
      std::vector<int> trkcharge;
      std::vector<float> energyMatrix;
      std::vector<unsigned int> detIds;
      std::vector<float> timingMatrix;
      trkd0.reserve(vectorSize);
      trkdz.reserve(vectorSize);
      trkpt.reserve(vectorSize);
      trketa.reserve(vectorSize);
      trkphi.reserve(vectorSize);
      trkpMode.reserve(vectorSize);
      trketaMode.reserve(vectorSize);
      trkphiMode.reserve(vectorSize);
      trkqoverpModeError.reserve(vectorSize);
      trkchi2overndf.reserve(vectorSize);
      trkcharge.reserve(vectorSize);
      energyMatrix.reserve(vectorSize);
      detIds.reserve(vectorSize);
      timingMatrix.reserve(vectorSize);
      for (unsigned int j = 0; j < vectorSize; ++j) {
        trkd0.push_back(static_cast<float>(electronsFloatingPointValues_[19] + offset + j * 10));
        trkdz.push_back(static_cast<float>(electronsFloatingPointValues_[20] + offset + j * 10));
        trkpt.push_back(static_cast<float>(electronsFloatingPointValues_[21] + offset + j * 10));
        trketa.push_back(static_cast<float>(electronsFloatingPointValues_[22] + offset + j * 10));
        trkphi.push_back(static_cast<float>(electronsFloatingPointValues_[23] + offset + j * 10));
        trkpMode.push_back(static_cast<float>(electronsFloatingPointValues_[28] + offset + j * 10));
        trketaMode.push_back(static_cast<float>(electronsFloatingPointValues_[29] + offset + j * 10));
        trkphiMode.push_back(static_cast<float>(electronsFloatingPointValues_[30] + offset + j * 10));
        trkqoverpModeError.push_back(static_cast<float>(electronsFloatingPointValues_[31] + offset + j * 10));
        trkchi2overndf.push_back(static_cast<float>(electronsFloatingPointValues_[24] + offset + j * 10));
        trkcharge.push_back(static_cast<int>(electronsIntegralValues_[5] + offset + j * 10));
        energyMatrix.push_back(static_cast<float>(electronsFloatingPointValues_[17] + offset + j * 10));
        detIds.push_back(static_cast<uint32_t>(electronsIntegralValues_[3] + iOffset + j * 10));
        timingMatrix.push_back(static_cast<float>(electronsFloatingPointValues_[18] + offset + j * 10));
      }
      phase2ScoutingElectrons->emplace_back(static_cast<float>(electronsFloatingPointValues_[0] + offset),
                                            static_cast<float>(electronsFloatingPointValues_[1] + offset),
                                            static_cast<float>(electronsFloatingPointValues_[2] + offset),
                                            static_cast<float>(electronsFloatingPointValues_[3] + offset),
                                            static_cast<float>(electronsFloatingPointValues_[25] + offset),
                                            static_cast<float>(electronsFloatingPointValues_[26] + offset),
                                            static_cast<float>(electronsFloatingPointValues_[27] + offset),
                                            std::move(trkd0),
                                            std::move(trkdz),
                                            std::move(trkpt),
                                            std::move(trketa),
                                            std::move(trkphi),
                                            std::move(trkpMode),
                                            std::move(trketaMode),
                                            std::move(trkphiMode),
                                            std::move(trkqoverpModeError),
                                            std::move(trkchi2overndf),
                                            static_cast<float>(electronsFloatingPointValues_[6] + offset),
                                            static_cast<float>(electronsFloatingPointValues_[7] + offset),
                                            static_cast<float>(electronsFloatingPointValues_[8] + offset),
                                            static_cast<float>(electronsFloatingPointValues_[9] + offset),
                                            static_cast<float>(electronsFloatingPointValues_[10] + offset),
                                            electronsIntegralValues_[0] + iOffset,
                                            std::move(trkcharge),
                                            static_cast<float>(electronsFloatingPointValues_[32] + offset),
                                            static_cast<float>(electronsFloatingPointValues_[11] + offset),
                                            static_cast<float>(electronsFloatingPointValues_[12] + offset),
                                            static_cast<float>(electronsFloatingPointValues_[13] + offset),
                                            static_cast<float>(electronsFloatingPointValues_[14] + offset),
                                            static_cast<float>(electronsFloatingPointValues_[15] + offset),
                                            static_cast<float>(electronsFloatingPointValues_[16] + offset),
                                            static_cast<uint32_t>(electronsIntegralValues_[2] + iOffset),
                                            static_cast<uint32_t>(electronsIntegralValues_[6] + iOffset),
                                            static_cast<uint32_t>(electronsIntegralValues_[7] + iOffset),
                                            std::move(energyMatrix),
                                            std::move(detIds),
                                            std::move(timingMatrix),
                                            static_cast<bool>((electronsIntegralValues_[4] + iOffset) % 2));
    }
    iEvent.put(electronsPutToken_, std::move(phase2ScoutingElectrons));
  }

  void TestWritePhase2Scouting::produceMuons(edm::Event& iEvent) const {
    auto phase2ScoutingMuons = std::make_unique<std::vector<Phase2ScoutingMuon>>();
    unsigned int vectorSize = 2 + iEvent.id().event() % 4;
    phase2ScoutingMuons->reserve(vectorSize);
    for (unsigned int i = 0; i < vectorSize; ++i) {
      double offset = static_cast<double>(iEvent.id().event() + i);
      int iOffset = static_cast<int>(iEvent.id().event() + i);

      std::vector<int> vtxIndx;
      std::vector<uint16_t> hitPattern;
      vtxIndx.reserve(vectorSize);
      hitPattern.reserve(vectorSize);
      for (unsigned int j = 0; j < vectorSize; ++j) {
        vtxIndx.push_back(static_cast<int>(muonsIntegralValues_[17] + iOffset + j * 10));
        hitPattern.push_back(static_cast<uint16_t>(muonsIntegralValues_[25] + iOffset + j * 10));
      }

      Phase2ScoutingHitPatternPOD phase2ScoutingHitPatternPOD;
      phase2ScoutingHitPatternPOD.hitCount = static_cast<uint8_t>(muonsIntegralValues_[18] + iOffset);
      phase2ScoutingHitPatternPOD.beginTrackHits = static_cast<uint8_t>(muonsIntegralValues_[19] + iOffset);
      phase2ScoutingHitPatternPOD.endTrackHits = static_cast<uint8_t>(muonsIntegralValues_[20] + iOffset);
      phase2ScoutingHitPatternPOD.beginInner = static_cast<uint8_t>(muonsIntegralValues_[21] + iOffset);
      phase2ScoutingHitPatternPOD.endInner = static_cast<uint8_t>(muonsIntegralValues_[22] + iOffset);
      phase2ScoutingHitPatternPOD.beginOuter = static_cast<uint8_t>(muonsIntegralValues_[23] + iOffset);
      phase2ScoutingHitPatternPOD.endOuter = static_cast<uint8_t>(muonsIntegralValues_[24] + iOffset);
      phase2ScoutingHitPatternPOD.hitPattern = std::move(hitPattern);

      phase2ScoutingMuons->emplace_back(static_cast<float>(muonsFloatingPointValues_[0] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[1] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[2] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[3] + offset),
                                        static_cast<unsigned int>(muonsIntegralValues_[0] + iOffset),
                                        muonsIntegralValues_[1] + iOffset,
                                        static_cast<float>(muonsFloatingPointValues_[4] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[5] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[6] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[7] + offset),
                                        muonsIntegralValues_[2] + iOffset,
                                        muonsIntegralValues_[3] + iOffset,
                                        muonsIntegralValues_[4] + iOffset,
                                        muonsIntegralValues_[5] + iOffset,
                                        muonsIntegralValues_[6] + iOffset,
                                        muonsIntegralValues_[7] + iOffset,
                                        muonsIntegralValues_[8] + iOffset,
                                        static_cast<unsigned int>(muonsIntegralValues_[9] + iOffset),
                                        static_cast<unsigned int>(muonsIntegralValues_[10] + iOffset),
                                        muonsIntegralValues_[11] + iOffset,
                                        static_cast<unsigned int>(muonsIntegralValues_[12] + iOffset),
                                        muonsIntegralValues_[13] + iOffset,
                                        muonsIntegralValues_[14] + iOffset,
                                        muonsIntegralValues_[15] + iOffset,
                                        muonsIntegralValues_[16] + iOffset,
                                        static_cast<float>(muonsFloatingPointValues_[8] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[9] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[10] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[11] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[12] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[13] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[14] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[15] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[16] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[17] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[18] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[19] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[20] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[21] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[22] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[23] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[24] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[25] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[26] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[27] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[28] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[29] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[30] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[31] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[32] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[33] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[34] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[35] + offset),
                                        static_cast<float>(muonsFloatingPointValues_[36] + offset),
                                        std::move(vtxIndx),
                                        std::move(phase2ScoutingHitPatternPOD));
    }
    iEvent.put(muonsPutToken_, std::move(phase2ScoutingMuons));
  }

  void TestWritePhase2Scouting::produceParticles(edm::Event& iEvent) const {
    auto phase2ScoutingParticles = std::make_unique<std::vector<Phase2ScoutingParticle>>();
    unsigned int vectorSize = 2 + iEvent.id().event() % 4;
    phase2ScoutingParticles->reserve(vectorSize);
    for (unsigned int i = 0; i < vectorSize; ++i) {
      double offset = static_cast<double>(iEvent.id().event() + i);
      int iOffset = static_cast<int>(iEvent.id().event() + i);
      phase2ScoutingParticles->emplace_back(static_cast<float>(particlesFloatingPointValues_[0] + offset),
                                            static_cast<float>(particlesFloatingPointValues_[1] + offset),
                                            static_cast<float>(particlesFloatingPointValues_[2] + offset),
                                            particlesIntegralValues_[0] + iOffset,
                                            particlesIntegralValues_[1] + iOffset,
                                            static_cast<float>(particlesFloatingPointValues_[3] + offset),
                                            static_cast<float>(particlesFloatingPointValues_[4] + offset),
                                            static_cast<float>(particlesFloatingPointValues_[5] + offset),
                                            static_cast<float>(particlesFloatingPointValues_[6] + offset),
                                            static_cast<float>(particlesFloatingPointValues_[7] + offset),
                                            static_cast<uint8_t>(particlesIntegralValues_[2] + iOffset),
                                            static_cast<uint8_t>(particlesIntegralValues_[3] + iOffset),
                                            static_cast<float>(particlesFloatingPointValues_[8] + offset),
                                            static_cast<float>(particlesFloatingPointValues_[9] + offset),
                                            static_cast<float>(particlesFloatingPointValues_[10] + offset),
                                            static_cast<bool>((particlesIntegralValues_[4] + iOffset) % 2));
    }
    iEvent.put(particlesPutToken_, std::move(phase2ScoutingParticles));
  }

  void TestWritePhase2Scouting::producePFJets(edm::Event& iEvent) const {
    auto phase2ScoutingPFJets = std::make_unique<std::vector<Phase2ScoutingPFJet>>();
    unsigned int vectorSize = 2 + iEvent.id().event() % 4;
    phase2ScoutingPFJets->reserve(vectorSize);

    for (unsigned int i = 0; i < vectorSize; ++i) {
      double offset = static_cast<double>(iEvent.id().event() + i);
      int iOffset = static_cast<int>(iEvent.id().event() + i);

      std::vector<int> constituents;
      constituents.reserve(vectorSize);
      for (unsigned int j = 0; j < vectorSize; ++j) {
        constituents.push_back(static_cast<int>(pfJetsIntegralValues_[7] + iOffset + j * 10));
      }

      phase2ScoutingPFJets->emplace_back(static_cast<float>(pfJetsFloatingPointValues_[0] + offset),
                                         static_cast<float>(pfJetsFloatingPointValues_[1] + offset),
                                         static_cast<float>(pfJetsFloatingPointValues_[2] + offset),
                                         static_cast<float>(pfJetsFloatingPointValues_[3] + offset),
                                         static_cast<float>(pfJetsFloatingPointValues_[4] + offset),
                                         static_cast<float>(pfJetsFloatingPointValues_[5] + offset),
                                         static_cast<float>(pfJetsFloatingPointValues_[6] + offset),
                                         static_cast<float>(pfJetsFloatingPointValues_[7] + offset),
                                         static_cast<float>(pfJetsFloatingPointValues_[8] + offset),
                                         static_cast<float>(pfJetsFloatingPointValues_[9] + offset),
                                         static_cast<float>(pfJetsFloatingPointValues_[10] + offset),
                                         static_cast<float>(pfJetsFloatingPointValues_[11] + offset),
                                         pfJetsIntegralValues_[0] + iOffset,
                                         pfJetsIntegralValues_[1] + iOffset,
                                         pfJetsIntegralValues_[2] + iOffset,
                                         pfJetsIntegralValues_[3] + iOffset,
                                         pfJetsIntegralValues_[4] + iOffset,
                                         pfJetsIntegralValues_[5] + iOffset,
                                         pfJetsIntegralValues_[6] + iOffset,
                                         static_cast<float>(pfJetsFloatingPointValues_[12] + offset),
                                         static_cast<float>(pfJetsFloatingPointValues_[13] + offset),
                                         static_cast<float>(pfJetsFloatingPointValues_[14] + offset),
                                         std::move(constituents));
    }
    iEvent.put(pfJetsPutToken_, std::move(phase2ScoutingPFJets));
  }

  void TestWritePhase2Scouting::producePhotons(edm::Event& iEvent) const {
    auto phase2ScoutingPhotons = std::make_unique<std::vector<Phase2ScoutingPhoton>>();
    unsigned int vectorSize = 2 + iEvent.id().event() % 4;
    phase2ScoutingPhotons->reserve(vectorSize);
    for (unsigned int i = 0; i < vectorSize; ++i) {
      double offset = static_cast<double>(iEvent.id().event() + i);
      int iOffset = static_cast<int>(iEvent.id().event() + i);

      std::vector<float> energyMatrix;
      std::vector<uint32_t> detIds;
      std::vector<float> timingMatrix;
      energyMatrix.reserve(vectorSize);
      detIds.reserve(vectorSize);
      timingMatrix.reserve(vectorSize);
      for (unsigned int j = 0; j < vectorSize; ++j) {
        energyMatrix.push_back(static_cast<float>(photonsFloatingPointValues_[12] + offset + j * 10));
        detIds.push_back(static_cast<uint32_t>(photonsIntegralValues_[1] + iOffset + j * 10));
        timingMatrix.push_back(static_cast<float>(photonsFloatingPointValues_[13] + offset + j * 10));
      }
      phase2ScoutingPhotons->emplace_back(static_cast<float>(photonsFloatingPointValues_[0] + offset),
                                          static_cast<float>(photonsFloatingPointValues_[1] + offset),
                                          static_cast<float>(photonsFloatingPointValues_[2] + offset),
                                          static_cast<float>(photonsFloatingPointValues_[3] + offset),
                                          static_cast<float>(photonsFloatingPointValues_[14] + offset),
                                          static_cast<float>(photonsFloatingPointValues_[15] + offset),
                                          static_cast<float>(photonsFloatingPointValues_[16] + offset),
                                          static_cast<float>(photonsFloatingPointValues_[4] + offset),
                                          static_cast<float>(photonsFloatingPointValues_[5] + offset),
                                          static_cast<float>(photonsFloatingPointValues_[6] + offset),
                                          static_cast<float>(photonsFloatingPointValues_[7] + offset),
                                          static_cast<float>(photonsFloatingPointValues_[8] + offset),
                                          static_cast<float>(photonsFloatingPointValues_[9] + offset),
                                          static_cast<float>(photonsFloatingPointValues_[10] + offset),
                                          static_cast<float>(photonsFloatingPointValues_[11] + offset),
                                          static_cast<uint32_t>(photonsIntegralValues_[0] + iOffset),
                                          static_cast<uint32_t>(photonsIntegralValues_[3] + iOffset),
                                          static_cast<uint32_t>(photonsIntegralValues_[4] + iOffset),
                                          std::move(energyMatrix),
                                          std::move(detIds),
                                          std::move(timingMatrix),
                                          static_cast<bool>((photonsIntegralValues_[2] + iOffset) % 2));
    }
    iEvent.put(photonsPutToken_, std::move(phase2ScoutingPhotons));
  }

  void TestWritePhase2Scouting::produceTracks(edm::Event& iEvent) const {
    auto phase2ScoutingTracks = std::make_unique<std::vector<Phase2ScoutingTrack>>();
    unsigned int vectorSize = 2 + iEvent.id().event() % 4;
    phase2ScoutingTracks->reserve(vectorSize);

    for (unsigned int i = 0; i < vectorSize; ++i) {
      double offset = static_cast<double>(iEvent.id().event() + i);
      int iOffset = static_cast<int>(iEvent.id().event() + i);

      phase2ScoutingTracks->emplace_back(static_cast<float>(tracksFloatingPointValues_[0] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[1] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[2] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[3] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[4] + offset),
                                         tracksIntegralValues_[0] + iOffset,
                                         static_cast<float>(tracksFloatingPointValues_[5] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[6] + offset),
                                         tracksIntegralValues_[1] + iOffset,
                                         tracksIntegralValues_[2] + iOffset,
                                         tracksIntegralValues_[3] + iOffset,
                                         static_cast<float>(tracksFloatingPointValues_[7] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[8] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[9] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[10] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[11] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[12] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[13] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[14] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[15] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[16] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[17] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[18] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[19] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[20] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[21] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[22] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[23] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[24] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[25] + offset),
                                         tracksIntegralValues_[4] + iOffset,
                                         static_cast<float>(tracksFloatingPointValues_[26] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[27] + offset),
                                         static_cast<float>(tracksFloatingPointValues_[28] + offset));
    }
    iEvent.put(tracksPutToken_, std::move(phase2ScoutingTracks));
  }

  void TestWritePhase2Scouting::produceVertexes(edm::Event& iEvent) const {
    auto phase2ScoutingVertexes = std::make_unique<std::vector<Phase2ScoutingVertex>>();
    unsigned int vectorSize = 2 + iEvent.id().event() % 4;
    phase2ScoutingVertexes->reserve(vectorSize);

    for (unsigned int i = 0; i < vectorSize; ++i) {
      double offset = static_cast<double>(iEvent.id().event() + i);
      int iOffset = static_cast<int>(iEvent.id().event() + i);

      phase2ScoutingVertexes->emplace_back(static_cast<float>(vertexesFloatingPointValues_[0] + offset),
                                           static_cast<float>(vertexesFloatingPointValues_[1] + offset),
                                           static_cast<float>(vertexesFloatingPointValues_[2] + offset),
                                           static_cast<float>(vertexesFloatingPointValues_[3] + offset),
                                           static_cast<float>(vertexesFloatingPointValues_[4] + offset),
                                           static_cast<float>(vertexesFloatingPointValues_[5] + offset),
                                           vertexesIntegralValues_[0] + iOffset,
                                           static_cast<float>(vertexesFloatingPointValues_[6] + offset),
                                           vertexesIntegralValues_[1] + iOffset,
                                           static_cast<bool>((vertexesIntegralValues_[2] + iOffset) % 2),
                                           static_cast<float>(vertexesFloatingPointValues_[7] + offset),
                                           static_cast<float>(vertexesFloatingPointValues_[8] + offset),
                                           static_cast<float>(vertexesFloatingPointValues_[9] + offset));
    }
    iEvent.put(vertexesPutToken_, std::move(phase2ScoutingVertexes));
  }

  void TestWritePhase2Scouting::produceEBRecHits(edm::Event& iEvent) const {
    auto phase2ScoutingEBRecHits = std::make_unique<std::vector<Phase2ScoutingEBRecHit>>();
    unsigned int vectorSize = 2 + iEvent.id().event() % 4;
    phase2ScoutingEBRecHits->reserve(vectorSize);

    for (unsigned int i = 0; i < vectorSize; ++i) {
      double offset = static_cast<double>(iEvent.id().event() + i);
      int iOffset = static_cast<int>(iEvent.id().event() + i);

      phase2ScoutingEBRecHits->emplace_back(static_cast<float>(ebRecHitsFloatingPointValues_[0] + offset),
                                            static_cast<float>(ebRecHitsFloatingPointValues_[1] + offset),
                                            static_cast<unsigned int>(ebRecHitsIntegralValues_[0] + iOffset),
                                            static_cast<uint32_t>(ebRecHitsIntegralValues_[1] + iOffset));
    }
    iEvent.put(ebRecHitsPutToken_, std::move(phase2ScoutingEBRecHits));
  }

  void TestWritePhase2Scouting::produceEERecHits(edm::Event& iEvent) const {
    auto phase2ScoutingEERecHits = std::make_unique<std::vector<Phase2ScoutingEERecHit>>();
    unsigned int vectorSize = 2 + iEvent.id().event() % 4;
    phase2ScoutingEERecHits->reserve(vectorSize);

    for (unsigned int i = 0; i < vectorSize; ++i) {
      double offset = static_cast<double>(iEvent.id().event() + i);
      int iOffset = static_cast<int>(iEvent.id().event() + i);

      phase2ScoutingEERecHits->emplace_back(static_cast<float>(eeRecHitsFloatingPointValues_[0] + offset),
                                            static_cast<float>(eeRecHitsFloatingPointValues_[1] + offset),
                                            static_cast<unsigned int>(eeRecHitsIntegralValues_[0] + iOffset));
    }
    iEvent.put(eeRecHitsPutToken_, std::move(phase2ScoutingEERecHits));
  }

  void TestWritePhase2Scouting::produceHBHERecHits(edm::Event& iEvent) const {
    auto phase2ScoutingHBHERecHits = std::make_unique<std::vector<Phase2ScoutingHBHERecHit>>();
    unsigned int vectorSize = 2 + iEvent.id().event() % 4;
    phase2ScoutingHBHERecHits->reserve(vectorSize);

    for (unsigned int i = 0; i < vectorSize; ++i) {
      double offset = static_cast<double>(iEvent.id().event() + i);
      int iOffset = static_cast<int>(iEvent.id().event() + i);

      phase2ScoutingHBHERecHits->emplace_back(static_cast<float>(hbheRecHitsFloatingPointValues_[0] + offset),
                                              static_cast<float>(hbheRecHitsFloatingPointValues_[1] + offset),
                                              static_cast<unsigned int>(hbheRecHitsIntegralValues_[0] + iOffset));
    }
    iEvent.put(hbheRecHitsPutToken_, std::move(phase2ScoutingHBHERecHits));
  }

  void TestWritePhase2Scouting::throwWithMessage(const char* msg) const {
    throw cms::Exception("TestFailure") << "TestWritePhase2Scouting constructor, test configuration error, " << msg;
  }

}  // namespace edmtest

using edmtest::TestWritePhase2Scouting;
DEFINE_FWK_MODULE(TestWritePhase2Scouting);
