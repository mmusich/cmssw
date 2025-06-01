#include "RecoVertex/PrimaryVertexProducer/interface/TrackFilterForPVFinding.h"
#include <cmath>

TrackFilterForPVFinding::TrackFilterForPVFinding(const edm::ParameterSet& conf) {
  maxD0Sig_ = conf.getParameter<double>("maxD0Significance");
  maxD0Error_ = conf.getParameter<double>("maxD0Error");
  maxDzError_ = conf.getParameter<double>("maxDzError");
  minPt_ = conf.getParameter<double>("minPt");
  maxEta_ = conf.getParameter<double>("maxEta");
  maxNormChi2_ = conf.getParameter<double>("maxNormalizedChi2");
  minSiLayers_ = conf.getParameter<int>("minSiliconLayersWithHits");
  minPxLayers_ = conf.getParameter<int>("minPixelLayersWithHits");
  minStripHits_ = conf.getParameter<int>("minValidStripHits");

  // the next few lines are taken from RecoBTag/SecondaryVertex/interface/TrackSelector.h"
  std::string qualityClass = conf.getParameter<std::string>("trackQuality");
  if (qualityClass == "any" || qualityClass == "Any" || qualityClass == "ANY" || qualityClass.empty()) {
    quality_ = reco::TrackBase::undefQuality;
  } else {
    quality_ = reco::TrackBase::qualityByName(qualityClass);
  }
}

// select a single track
/*
bool TrackFilterForPVFinding::operator()(const reco::TransientTrack& tk) const {
  if (!tk.stateAtBeamLine().isValid())
    return false;
  bool IPSigCut = (tk.stateAtBeamLine().transverseImpactParameter().significance() < maxD0Sig_) &&
                  (tk.stateAtBeamLine().transverseImpactParameter().error() < maxD0Error_) &&
                  (tk.track().dzError() < maxDzError_);
  bool pTCut = tk.impactPointState().globalMomentum().transverse() > minPt_;
  bool etaCut = std::fabs(tk.impactPointState().globalMomentum().eta()) < maxEta_;
  bool normChi2Cut = tk.normalizedChi2() < maxNormChi2_;
  bool nPxLayCut = tk.hitPattern().pixelLayersWithMeasurement() >= minPxLayers_;
  bool nSiLayCut = tk.hitPattern().trackerLayersWithMeasurement() >= minSiLayers_;
  bool trackQualityCut = (quality_ == reco::TrackBase::undefQuality) || tk.track().quality(quality_);
  bool nStripHitsCut = tk.hitPattern().numberOfValidStripHits() >= minStripHits_;

  return IPSigCut && pTCut && etaCut && normChi2Cut && nPxLayCut && nSiLayCut && trackQualityCut && nStripHitsCut;
}
*/

#include <iostream>  // for std::cout
#include <iomanip>   // for std::setprecision

bool TrackFilterForPVFinding::operator()(const reco::TransientTrack& tk) const {
  if (!tk.stateAtBeamLine().isValid()) {
    std::cout << "[TrackFilter] Invalid beamline state" << std::endl;
    return false;
  }

  bool passed = true;

  auto d0sig = tk.stateAtBeamLine().transverseImpactParameter().significance();
  auto d0err = tk.stateAtBeamLine().transverseImpactParameter().error();
  auto dzerr = tk.track().dzError();

  if (d0sig >= maxD0Sig_) {
    std::cout << "[TrackFilter] Failed d0 significance cut: " << d0sig << " >= " << maxD0Sig_ << std::endl;
    passed = false;
  }

  if (d0err >= maxD0Error_) {
    std::cout << "[TrackFilter] Failed d0 error cut: " << d0err << " >= " << maxD0Error_ << std::endl;
    passed = false;
  }

  if (dzerr >= maxDzError_) {
    std::cout << "[TrackFilter] Failed dz error cut: " << dzerr << " >= " << maxDzError_ << std::endl;
    passed = false;
  }

  auto pt = tk.impactPointState().globalMomentum().transverse();
  if (pt <= minPt_) {
    std::cout << "[TrackFilter] Failed pT cut: " << pt << " <= " << minPt_ << std::endl;
    passed = false;
  }

  auto eta = tk.impactPointState().globalMomentum().eta();
  if (std::fabs(eta) >= maxEta_) {
    std::cout << "[TrackFilter] Failed eta cut: |" << eta << "| >= " << maxEta_ << std::endl;
    passed = false;
  }

  auto chi2 = tk.normalizedChi2();
  if (chi2 >= maxNormChi2_) {
    std::cout << "[TrackFilter] Failed normalized chi2 cut: " << chi2 << " >= " << maxNormChi2_ << std::endl;
    passed = false;
  }

  auto pxLayers = tk.hitPattern().pixelLayersWithMeasurement();
  if (pxLayers < minPxLayers_) {
    std::cout << "[TrackFilter] Failed pixel layers cut: " << pxLayers << " < " << minPxLayers_ << std::endl;
    passed = false;
  }

  auto siLayers = tk.hitPattern().trackerLayersWithMeasurement();
  if (siLayers < minSiLayers_) {
    std::cout << "[TrackFilter] Failed silicon layers cut: " << siLayers << " < " << minSiLayers_ << std::endl;
    passed = false;
  }

  auto nStripHits = tk.hitPattern().numberOfValidStripHits();
  if (nStripHits < minStripHits_) {
    std::cout << "[TrackFilter] Failed strip hits cut: " << nStripHits << " < " << minStripHits_ << std::endl;
    passed = false;
  }

  bool qualityPass = (quality_ == reco::TrackBase::undefQuality) || tk.track().quality(quality_);
  if (!qualityPass) {
    std::cout << "[TrackFilter] Failed quality flag check: required " << quality_ << std::endl;
    passed = false;
  }

  if (passed)
    std::cout << "[TrackFilter] Track passed all cuts" << std::endl;

  return passed;
}

// select the vector of tracks that pass the filter cuts
std::vector<reco::TransientTrack> TrackFilterForPVFinding::select(
    const std::vector<reco::TransientTrack>& tracks) const {
  std::vector<reco::TransientTrack> seltks;
  for (std::vector<reco::TransientTrack>::const_iterator itk = tracks.begin(); itk != tracks.end(); itk++) {
    if (operator()(*itk))
      seltks.push_back(*itk);  //  calls the filter function for single tracks
  }
  return seltks;
}

// select the vector of tracks that pass the filter cuts with a tighter pt selection
std::vector<reco::TransientTrack> TrackFilterForPVFinding::selectTight(const std::vector<reco::TransientTrack>& tracks,
                                                                       double minPtTight) const {
  std::vector<reco::TransientTrack> seltks;
  for (std::vector<reco::TransientTrack>::const_iterator itk = tracks.begin(); itk != tracks.end(); itk++) {
    if (itk->impactPointState().globalMomentum().transverse() < minPtTight)
      continue;
    if (operator()(*itk))
      seltks.push_back(*itk);  //  calls the filter function for single tracks
  }
  return seltks;
}

void TrackFilterForPVFinding::fillPSetDescription(edm::ParameterSetDescription& desc) {
  desc.add<double>("maxNormalizedChi2", 10.0);
  desc.add<double>("minPt", 0.0);
  desc.add<std::string>("algorithm", "filter");
  desc.add<double>("maxEta", 2.4);
  desc.add<double>("maxD0Significance", 4.0);
  desc.add<double>("maxD0Error", 1.0);
  desc.add<double>("maxDzError", 1.0);
  desc.add<std::string>("trackQuality", "any");
  desc.add<int>("minPixelLayersWithHits", 2);
  desc.add<int>("minSiliconLayersWithHits", 5);
  desc.add<int>("minValidStripHits", 0);
}
