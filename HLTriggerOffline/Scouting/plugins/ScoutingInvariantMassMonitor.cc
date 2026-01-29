#include "DQMServices/Core/interface/DQMEDAnalyzer.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Scouting/interface/Run3ScoutingElectron.h"
#include "DataFormats/Scouting/interface/Run3ScoutingMuon.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include <vector>
#include <string>

// root libraries
#include "TLorentzVector.h"
#include "Math/VectorUtil.h"

class ScoutingInvariantMassMonitor : public DQMEDAnalyzer {
public:
  explicit ScoutingInvariantMassMonitor(const edm::ParameterSet&);
  ~ScoutingInvariantMassMonitor() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void bookHistograms(DQMStore::IBooker&, edm::Run const&, edm::EventSetup const&) override;
  void analyze(const edm::Event&, const edm::EventSetup&) override;

  // Configuration
  const edm::EDGetTokenT<std::vector<Run3ScoutingMuon>> muonToken_;
  const edm::EDGetTokenT<std::vector<Run3ScoutingElectron>> electronToken_;
  const std::string monitorDir_;

  // Histograms
  MonitorElement* h_muonOSMass_;
  MonitorElement* h_eleOSMass_;
  MonitorElement* h_muonPtSum_;
  MonitorElement* h_elePtSum_;
};

ScoutingInvariantMassMonitor::ScoutingInvariantMassMonitor(const edm::ParameterSet& iConfig)
    : muonToken_(consumes<std::vector<Run3ScoutingMuon>>(iConfig.getParameter<edm::InputTag>("muons"))),
      electronToken_(consumes<std::vector<Run3ScoutingElectron>>(iConfig.getParameter<edm::InputTag>("electrons"))),
      monitorDir_(iConfig.getParameter<std::string>("monitorDir")) {}

void ScoutingInvariantMassMonitor::bookHistograms(DQMStore::IBooker& ibooker, edm::Run const&, edm::EventSetup const&) {
  ibooker.setCurrentFolder(monitorDir_);

  h_muonOSMass_ = ibooker.book1D("muonOSMass", "OS Muon Pair Invariant Mass;Mass [GeV];Events", 100, 0, 150);
  h_muonPtSum_ = ibooker.book1D("muonPtSum", "OS Muon Pair Scalar pT Sum;Sum pT [GeV];Events", 100, 0, 300);

  h_eleOSMass_ = ibooker.book1D("electronOSMass", "OS Electron Pair Invariant Mass;Mass [GeV];Events", 100, 0, 150);
  h_elePtSum_ = ibooker.book1D("electronPtSum", "OS Electron Pair Scalar pT Sum;Sum pT [GeV];Events", 100, 0, 300);
}

void ScoutingInvariantMassMonitor::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  // 1. Process Muons
  auto const& muons = iEvent.get(muonToken_);
  std::vector<const Run3ScoutingMuon*> goodMuons;

  for (auto const& m : muons) {
    // Basic Selection: Kinematics + ID + Isolation
    if (m.pt() < 5.0 || std::abs(m.eta()) > 2.4)
      continue;
    if (m.nValidPixelHits() == 0 || m.nRecoMuonMatchedStations() <= 1)
      continue;

    // Relative Isolation (Track-based)
    float relIso = m.trackIso() / m.pt();
    if (relIso > 0.15)
      continue;

    goodMuons.push_back(&m);
  }

  if (goodMuons.size() >= 2) {
    int bestI = -1, bestJ = -1;
    float maxPtSum = -1.0;

    for (size_t i = 0; i < goodMuons.size(); ++i) {
      for (size_t j = i + 1; j < goodMuons.size(); ++j) {
        if (goodMuons[i]->charge() * goodMuons[j]->charge() < 0) {  // OS
          float ptSum = goodMuons[i]->pt() + goodMuons[j]->pt();
          if (ptSum > maxPtSum) {
            maxPtSum = ptSum;
            bestI = i;
            bestJ = j;
          }
        }
      }
    }

    if (bestI != -1) {
      math::XYZTLorentzVector p1(goodMuons[bestI]->pt() * cos(goodMuons[bestI]->phi()),
                                 goodMuons[bestI]->pt() * sin(goodMuons[bestI]->phi()),
                                 goodMuons[bestI]->pt() * sinh(goodMuons[bestI]->eta()),
                                 0);  // simplified mass calculation or use m.m() if available
      // Note: Scouting objects usually provide pt, eta, phi, m.
      ROOT::Math::PtEtaPhiMVector v1(goodMuons[bestI]->pt(), goodMuons[bestI]->eta(), goodMuons[bestI]->phi(), 0.105);
      ROOT::Math::PtEtaPhiMVector v2(goodMuons[bestJ]->pt(), goodMuons[bestJ]->eta(), goodMuons[bestJ]->phi(), 0.105);

      h_muonOSMass_->Fill((v1 + v2).M());
      h_muonPtSum_->Fill(maxPtSum);
    }
  }

  // 2. Process Electrons
  auto const& electrons = iEvent.get(electronToken_);
  std::vector<const Run3ScoutingElectron*> goodEle;

  for (auto const& e : electrons) {
    if (e.pt() < 10.0 || std::abs(e.eta()) > 2.5)
      continue;
    if (e.hOverE() > 0.1 || std::abs(e.dEtaIn()) > 0.01)
      continue;  // Basic ID bits

    // Scouting Isolation check (e.g., using trackIso or relIso if available)
    // Run3ScoutingElectron usually has sigmaIetaIeta, dEtaIn, dPhiIn, hOverE, relIso
    // if (e.relIso() > 0.15) continue;

    goodEle.push_back(&e);
  }

  if (goodEle.size() >= 2) {
    int bestI = -1, bestJ = -1;
    float maxPtSum = -1.0;

    for (size_t i = 0; i < goodEle.size(); ++i) {
      for (size_t j = i + 1; j < goodEle.size(); ++j) {
        if (goodEle[i]->trkcharge()[0] * goodEle[j]->trkcharge()[0] < 0) {
          float ptSum = goodEle[i]->pt() + goodEle[j]->pt();
          if (ptSum > maxPtSum) {
            maxPtSum = ptSum;
            bestI = i;
            bestJ = j;
          }
        }
      }
    }

    if (bestI != -1) {
      ROOT::Math::PtEtaPhiMVector v1(goodEle[bestI]->pt(), goodEle[bestI]->eta(), goodEle[bestI]->phi(), 0.0005);
      ROOT::Math::PtEtaPhiMVector v2(goodEle[bestJ]->pt(), goodEle[bestJ]->eta(), goodEle[bestJ]->phi(), 0.0005);
      h_eleOSMass_->Fill((v1 + v2).M());
      h_elePtSum_->Fill(maxPtSum);
    }
  }
}

void ScoutingInvariantMassMonitor::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<edm::InputTag>("muons", edm::InputTag("hltScoutingMuonPacker"));
  desc.add<edm::InputTag>("electrons", edm::InputTag("hltScoutingEgammaPacker"));
  desc.add<std::string>("monitorDir", "HLT/Scouting/DiLeptonMass");
  descriptions.add("scoutingInvariantMassMonitor", desc);
}

DEFINE_FWK_MODULE(ScoutingInvariantMassMonitor);
