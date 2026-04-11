// system include files
#include <memory>
#include <cmath>

// user include files
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/Scouting/interface/Run3ScoutingParticle.h"
#include "DataFormats/Common/interface/OrphanHandle.h"

#include "SimGeneral/HepPDTRecord/interface/ParticleDataTable.h"
#include "fastjet/contrib/SoftKiller.hh"

class Run3ScoutingParticleToRecoPFCandidateProducer : public edm::stream::EDProducer<> {
public:
  explicit Run3ScoutingParticleToRecoPFCandidateProducer(const edm::ParameterSet &);
  ~Run3ScoutingParticleToRecoPFCandidateProducer() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions &descriptions);

  void produce(edm::Event &, edm::EventSetup const &) override;

private:
  void createPFCandidates(const edm::Handle<std::vector<Run3ScoutingParticle>> &, reco::PFCandidateCollection &);

  void createPFCandidatesSK(const edm::Handle<std::vector<Run3ScoutingParticle>> &, reco::PFCandidateCollection &);

  reco::PFCandidate createPFCand(const Run3ScoutingParticle &);

  void clearVars();

private:
  const edm::EDGetTokenT<std::vector<Run3ScoutingParticle>> input_token_;
  const edm::ESGetToken<HepPDT::ParticleDataTable, edm::DefaultRecord> pdt_token_;

  bool use_softKiller_;
  bool use_CHS_;

  const HepPDT::ParticleDataTable *pdTable_;

  // cached output vectors
  std::vector<int> vertexIndex_;
  std::vector<float> normchi2_, dz_, dxy_, dzsig_, dxysig_;
  std::vector<int> lostInnerHits_, quality_;
  std::vector<float> trkPt_, trkEta_, trkPhi_;
};

// constructor
Run3ScoutingParticleToRecoPFCandidateProducer::Run3ScoutingParticleToRecoPFCandidateProducer(
    const edm::ParameterSet &iConfig)
    : input_token_(consumes(iConfig.getParameter<edm::InputTag>("scoutingparticle"))),
      pdt_token_(esConsumes()),
      use_softKiller_(iConfig.getParameter<bool>("softKiller")),
      use_CHS_(iConfig.getParameter<bool>("CHS")) {
  produces<reco::PFCandidateCollection>();

  produces<edm::ValueMap<int>>("vertexIndex");
  produces<edm::ValueMap<float>>("normchi2");
  produces<edm::ValueMap<float>>("dz");
  produces<edm::ValueMap<float>>("dxy");
  produces<edm::ValueMap<float>>("dzsig");
  produces<edm::ValueMap<float>>("dxysig");
  produces<edm::ValueMap<int>>("lostInnerHits");
  produces<edm::ValueMap<int>>("quality");
  produces<edm::ValueMap<float>>("trkPt");
  produces<edm::ValueMap<float>>("trkEta");
  produces<edm::ValueMap<float>>("trkPhi");
}

// --- create single candidate ---
reco::PFCandidate Run3ScoutingParticleToRecoPFCandidateProducer::createPFCand(const Run3ScoutingParticle &p) {
  const auto *particle = pdTable_->particle(HepPDT::ParticleID(p.pdgId()));
  if (!particle)
    return reco::PFCandidate();

  const float m = particle->mass();
  const float q = particle->charge();

  const float pt = p.pt();
  const float eta = p.eta();
  const float phi = p.phi();

  const float cosPhi = std::cos(phi);
  const float sinPhi = std::sin(phi);
  const float coshEta = std::cosh(eta);
  const float sinhEta = std::sinh(eta);

  const float px = pt * cosPhi;
  const float py = pt * sinPhi;
  const float pz = pt * sinhEta;
  const float energy = std::sqrt(pt * pt * coshEta * coshEta + m * m);

  reco::Particle::LorentzVector p4(px, py, pz, energy);

  static const reco::PFCandidate dummy;
  reco::PFCandidate cand(q, p4, dummy.translatePdgIdToType(p.pdgId()));

  // store extras
  vertexIndex_.push_back(p.vertex());
  normchi2_.push_back(p.normchi2());
  dz_.push_back(p.dz());
  dxy_.push_back(p.dxy());
  dzsig_.push_back(p.dzsig());
  dxysig_.push_back(p.dxysig());
  lostInnerHits_.push_back(p.lostInnerHits());
  quality_.push_back(p.quality());

  if (p.relative_trk_vars()) {
    trkPt_.push_back(p.trk_pt() + pt);
    trkEta_.push_back(p.trk_eta() + eta);
    trkPhi_.push_back(p.trk_phi() + phi);
  } else {
    trkPt_.push_back(p.trk_pt());
    trkEta_.push_back(p.trk_eta());
    trkPhi_.push_back(p.trk_phi());
  }

  return cand;
}

// --- standard loop ---
void Run3ScoutingParticleToRecoPFCandidateProducer::createPFCandidates(
    const edm::Handle<std::vector<Run3ScoutingParticle>> &handle, reco::PFCandidateCollection &out) {
  if (use_CHS_) {
    for (const auto &p : *handle) {
      if (p.vertex() > 0)
        continue;
      auto cand = createPFCand(p);
      if (cand.energy() != 0)
        out.emplace_back(std::move(cand));
    }
  } else {
    for (const auto &p : *handle) {
      auto cand = createPFCand(p);
      if (cand.energy() != 0)
        out.emplace_back(std::move(cand));
    }
  }
}

// --- soft killer ---
void Run3ScoutingParticleToRecoPFCandidateProducer::createPFCandidatesSK(
    const edm::Handle<std::vector<Run3ScoutingParticle>> &handle, reco::PFCandidateCollection &out) {
  std::vector<fastjet::PseudoJet> fj;
  fj.reserve(handle->size());

  size_t idx = 0;
  for (const auto &p : *handle) {
    const auto *particle = pdTable_->particle(HepPDT::ParticleID(p.pdgId()));
    if (!particle) {
      ++idx;
      continue;
    }

    math::PtEtaPhiMLorentzVector p4(p.pt(), p.eta(), p.phi(), particle->mass());
    fj.emplace_back(p4.px(), p4.py(), p4.pz(), p4.energy());
    fj.back().set_user_index(idx++);
  }

  fastjet::contrib::SoftKiller sk(5, 0.4);
  auto filtered = sk(fj);

  for (const auto &pj : filtered) {
    const auto &p = handle->at(pj.user_index());
    auto cand = createPFCand(p);
    if (cand.energy() != 0)
      out.emplace_back(std::move(cand));
  }
}

// --- produce ---
void Run3ScoutingParticleToRecoPFCandidateProducer::produce(edm::Event &iEvent, edm::EventSetup const &setup) {
  pdTable_ = &setup.getData(pdt_token_);

  edm::Handle<std::vector<Run3ScoutingParticle>> handle;
  iEvent.getByToken(input_token_, handle);

  const size_t n = handle->size();

  // reserve everything
  vertexIndex_.reserve(n);
  normchi2_.reserve(n);
  dz_.reserve(n);
  dxy_.reserve(n);
  dzsig_.reserve(n);
  dxysig_.reserve(n);
  lostInnerHits_.reserve(n);
  quality_.reserve(n);
  trkPt_.reserve(n);
  trkEta_.reserve(n);
  trkPhi_.reserve(n);

  auto out = std::make_unique<reco::PFCandidateCollection>();
  out->reserve(n);

  if (use_softKiller_)
    createPFCandidatesSK(handle, *out);
  else
    createPFCandidates(handle, *out);

  auto oh = iEvent.put(std::move(out));

  auto fillVM = [&](auto &vec, auto label) {
    using T = typename std::decay<decltype(vec[0])>::type;
    auto vm = std::make_unique<edm::ValueMap<T>>();
    typename edm::ValueMap<T>::Filler filler(*vm);
    filler.insert(oh, vec.begin(), vec.end());
    filler.fill();
    iEvent.put(std::move(vm), label);
  };

  fillVM(vertexIndex_, "vertexIndex");
  fillVM(normchi2_, "normchi2");
  fillVM(dz_, "dz");
  fillVM(dxy_, "dxy");
  fillVM(dzsig_, "dzsig");
  fillVM(dxysig_, "dxysig");
  fillVM(lostInnerHits_, "lostInnerHits");
  fillVM(quality_, "quality");
  fillVM(trkPt_, "trkPt");
  fillVM(trkEta_, "trkEta");
  fillVM(trkPhi_, "trkPhi");

  clearVars();
}

// clear
void Run3ScoutingParticleToRecoPFCandidateProducer::clearVars() {
  vertexIndex_.clear();
  normchi2_.clear();
  dz_.clear();
  dxy_.clear();
  dzsig_.clear();
  dxysig_.clear();
  lostInnerHits_.clear();
  quality_.clear();
  trkPt_.clear();
  trkEta_.clear();
  trkPhi_.clear();
}

// descriptions
void Run3ScoutingParticleToRecoPFCandidateProducer::fillDescriptions(edm::ConfigurationDescriptions &descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<edm::InputTag>("scoutingparticle", edm::InputTag("hltScoutingPFPacker"));
  desc.add<bool>("softKiller", false);
  desc.add<bool>("CHS", false);

  descriptions.addWithDefaultLabel(desc);
}

DEFINE_FWK_MODULE(Run3ScoutingParticleToRecoPFCandidateProducer);
