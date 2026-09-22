#ifndef DataFormats_Scouting_ScoutingFormatTraits_h
#define DataFormats_Scouting_ScoutingFormatTraits_h

// Traits describing the two families of HLT-Scouting data formats
// (Run 3 and Phase 2). The HLT scouting "packer" producers are written
// against these traits, so that the same producer can emit either family
// of collections, selected at configuration time.

#include <string>
#include <string_view>
#include <utility>

#include "FWCore/Utilities/interface/Exception.h"

#include "DataFormats/Scouting/interface/Run3ScoutingCaloJet.h"
#include "DataFormats/Scouting/interface/Run3ScoutingEBRecHit.h"
#include "DataFormats/Scouting/interface/Run3ScoutingEERecHit.h"
#include "DataFormats/Scouting/interface/Run3ScoutingElectron.h"
#include "DataFormats/Scouting/interface/Run3ScoutingHBHERecHit.h"
#include "DataFormats/Scouting/interface/Run3ScoutingHitPatternPOD.h"
#include "DataFormats/Scouting/interface/Run3ScoutingMuon.h"
#include "DataFormats/Scouting/interface/Run3ScoutingPFJet.h"
#include "DataFormats/Scouting/interface/Run3ScoutingParticle.h"
#include "DataFormats/Scouting/interface/Run3ScoutingPhoton.h"
#include "DataFormats/Scouting/interface/Run3ScoutingTrack.h"
#include "DataFormats/Scouting/interface/Run3ScoutingVertex.h"

#include "DataFormats/Scouting/interface/Phase2ScoutingCaloJet.h"
#include "DataFormats/Scouting/interface/Phase2ScoutingEBRecHit.h"
#include "DataFormats/Scouting/interface/Phase2ScoutingEERecHit.h"
#include "DataFormats/Scouting/interface/Phase2ScoutingElectron.h"
#include "DataFormats/Scouting/interface/Phase2ScoutingHBHERecHit.h"
#include "DataFormats/Scouting/interface/Phase2ScoutingHitPatternPOD.h"
#include "DataFormats/Scouting/interface/Phase2ScoutingMuon.h"
#include "DataFormats/Scouting/interface/Phase2ScoutingPFJet.h"
#include "DataFormats/Scouting/interface/Phase2ScoutingParticle.h"
#include "DataFormats/Scouting/interface/Phase2ScoutingPhoton.h"
#include "DataFormats/Scouting/interface/Phase2ScoutingTrack.h"
#include "DataFormats/Scouting/interface/Phase2ScoutingVertex.h"

namespace scouting {

  // Identifier of the data-format family, as selected in the configuration
  enum class Format { kRun3, kPhase2 };

  // Name of the configuration parameter used by the packers to select the family
  inline constexpr char const* kFormatParameterName = "scoutingFormat";
  inline constexpr char const* kRun3FormatName = "Run3";
  inline constexpr char const* kPhase2FormatName = "Phase2";

  inline Format formatFromString(std::string_view name) {
    if (name == kRun3FormatName)
      return Format::kRun3;
    if (name == kPhase2FormatName)
      return Format::kPhase2;
    throw cms::Exception("Configuration")
        << "invalid value \"" << name << "\" for parameter \"" << kFormatParameterName << "\": allowed values are \""
        << kRun3FormatName << "\" and \"" << kPhase2FormatName << "\"";
  }

  // Run 3 scouting data formats
  struct Run3Format {
    static constexpr Format format = Format::kRun3;
    using CaloJet = Run3ScoutingCaloJet;
    using EBRecHit = Run3ScoutingEBRecHit;
    using EERecHit = Run3ScoutingEERecHit;
    using Electron = Run3ScoutingElectron;
    using HBHERecHit = Run3ScoutingHBHERecHit;
    using HitPatternPOD = Run3ScoutingHitPatternPOD;
    using Muon = Run3ScoutingMuon;
    using PFJet = Run3ScoutingPFJet;
    using Particle = Run3ScoutingParticle;
    using Photon = Run3ScoutingPhoton;
    using Track = Run3ScoutingTrack;
    using Vertex = Run3ScoutingVertex;

    using CaloJetCollection = Run3ScoutingCaloJetCollection;
    using EBRecHitCollection = Run3ScoutingEBRecHitCollection;
    using EERecHitCollection = Run3ScoutingEERecHitCollection;
    using ElectronCollection = Run3ScoutingElectronCollection;
    using HBHERecHitCollection = Run3ScoutingHBHERecHitCollection;
    using MuonCollection = Run3ScoutingMuonCollection;
    using PFJetCollection = Run3ScoutingPFJetCollection;
    using ParticleCollection = Run3ScoutingParticleCollection;
    using PhotonCollection = Run3ScoutingPhotonCollection;
    using TrackCollection = Run3ScoutingTrackCollection;
    using VertexCollection = Run3ScoutingVertexCollection;

    // reco::HitPattern natively provides the Run 3 POD
    static HitPatternPOD hitPatternPOD(Run3ScoutingHitPatternPOD hp) { return hp; }
  };

  // Phase 2 scouting data formats
  struct Phase2Format {
    static constexpr Format format = Format::kPhase2;
    using CaloJet = Phase2ScoutingCaloJet;
    using EBRecHit = Phase2ScoutingEBRecHit;
    using EERecHit = Phase2ScoutingEERecHit;
    using Electron = Phase2ScoutingElectron;
    using HBHERecHit = Phase2ScoutingHBHERecHit;
    using HitPatternPOD = Phase2ScoutingHitPatternPOD;
    using Muon = Phase2ScoutingMuon;
    using PFJet = Phase2ScoutingPFJet;
    using Particle = Phase2ScoutingParticle;
    using Photon = Phase2ScoutingPhoton;
    using Track = Phase2ScoutingTrack;
    using Vertex = Phase2ScoutingVertex;

    using CaloJetCollection = Phase2ScoutingCaloJetCollection;
    using EBRecHitCollection = Phase2ScoutingEBRecHitCollection;
    using EERecHitCollection = Phase2ScoutingEERecHitCollection;
    using ElectronCollection = Phase2ScoutingElectronCollection;
    using HBHERecHitCollection = Phase2ScoutingHBHERecHitCollection;
    using MuonCollection = Phase2ScoutingMuonCollection;
    using PFJetCollection = Phase2ScoutingPFJetCollection;
    using ParticleCollection = Phase2ScoutingParticleCollection;
    using PhotonCollection = Phase2ScoutingPhotonCollection;
    using TrackCollection = Phase2ScoutingTrackCollection;
    using VertexCollection = Phase2ScoutingVertexCollection;

    // convert the POD provided by reco::HitPattern into the Phase 2 one (same layout)
    static HitPatternPOD hitPatternPOD(Run3ScoutingHitPatternPOD hp) {
      return HitPatternPOD{hp.hitCount,
                           hp.beginTrackHits,
                           hp.endTrackHits,
                           hp.beginInner,
                           hp.endInner,
                           hp.beginOuter,
                           hp.endOuter,
                           std::move(hp.hitPattern)};
    }
  };

}  // namespace scouting

#endif
