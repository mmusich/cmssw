#include <memory>
#include <iostream>
#include <vector>

#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/Common/interface/View.h"

#include "TProfile2D.h"
#include "TH2F.h"
#include "TFile.h"

class MuonAnalyzer : public edm::one::EDAnalyzer<> {
public:
  explicit MuonAnalyzer(const edm::ParameterSet&);
  ~MuonAnalyzer() override {}

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void analyze(const edm::Event&, const edm::EventSetup&) override;

  edm::Service<TFileService> fs;
  const edm::EDGetTokenT<edm::View<reco::Muon>> muonToken_;

  // Histograms
  TH2F* hIsGlobalMuon;
  TH2F* hIsTrackerMuon;
  TH2F* hNumberOfMatches;
  TH2F* hNumberOfValidMuonHits;
  TH2F* hNormalizedChi2;

  TH2F* hIsoSumPtOverPt;
  TH2F* hIsoEmEtOverPt;
  TH2F* hIsoHadEtOverPt;

  TProfile2D* relIsoVsEtaPhi;
  
  TH1F* hTkIso;
  TH1F* hCombIso;
  
  template <typename T, typename... Args>
  T* book(const Args &...args) const {
    T *t = fs->make<T>(args...);
    return t;
  }
};

MuonAnalyzer::MuonAnalyzer(const edm::ParameterSet& iConfig)
  : muonToken_(consumes<edm::View<reco::Muon>>(iConfig.getParameter<edm::InputTag>("muonCollection")))
{
  // Create histograms
  hIsGlobalMuon = book<TH2F>("hIsGlobalMuon", "IsGlobalMuon vs Muon #eta;Muon #eta;IsGlobalMuon", 100, -2.8, 2.8, 2, -0.5, 1.5);
  hIsTrackerMuon = book<TH2F>("hIsTrackerMuon", "IsTrackerMuon vs Muon #eta;Muon #eta;IsTrackerMuon", 100, -2.8, 2.8, 2, -0.5, 1.5);
  hNumberOfMatches = book<TH2F>("hNumberOfMatches", "NumberOfMatches vs Muon #eta;Muon #eta;NumberOfMatches", 100, -2.8, 2.8, 10, -0.5, 9.5);
  hNumberOfValidMuonHits = book<TH2F>("hNumberOfValidMuonHits", "NumberOfValidMuonHits vs Muon #eta;Muon #eta;NumberOfValidMuonHits", 100, -2.8, 2.8, 50, -0.5, 49.5);
  hNormalizedChi2 = book<TH2F>("hNormalizedChi2", "Normalized #chi^{2} vs Muon #eta;Muon #eta;Normalized #chi^{2}", 100, -2.8, 2.8, 100, 0, 10);

  hIsoSumPtOverPt = book<TH2F>("hIsoSumPtOverPt", "Isolation SumPt/Pt vs Muon #phi;Muon #phi;Isolation SumPt/Pt", 100, -M_PI, M_PI, 100, 0, 0.2);
  hIsoEmEtOverPt = book<TH2F>("hIsoEmEtOverPt", "Isolation EmEt/Pt vs Muon #phi;Muon #phi;Isolation EmEt/Pt", 100, -M_PI, M_PI, 100, 0, 0.2);
  hIsoHadEtOverPt = book<TH2F>("hIsoHadEtOverPt", "Isolation HadEt/Pt vs Muon #phi;Muon #phi;Isolation HadEt/Pt", 100, -M_PI, M_PI, 100, 0, 0.2);

  hTkIso = book<TH1F>("hTkIso","Tracker Isolation SumPt/Pt;Isolation SumPt/Pt;n. muons",100,0,0.5);
  hCombIso = book<TH1F>("hCombIso","Combined Isolation;Combined Isolation;n. muons",100,0,0.5);

  relIsoVsEtaPhi = book<TProfile2D>("RelIsoVsEtaPhi","Relvative Isolation vs muon #eta/#phi;Muon #eta;Muon #phi;relative Isolation",100,-2.8,2.8,100,M_PI,M_PI);  
}

void MuonAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  edm::Handle<edm::View<reco::Muon>> muons;
  iEvent.getByToken(muonToken_, muons);

  for (const auto& muon : *muons) {
    // Fill histograms for the specified variables
    hIsGlobalMuon->Fill(muon.eta(), muon.isGlobalMuon());
    hIsTrackerMuon->Fill(muon.eta(), muon.isTrackerMuon());
    hNumberOfMatches->Fill(muon.eta(), muon.numberOfMatches());

    if(muon.isGlobalMuon()){
      hNumberOfValidMuonHits->Fill(muon.eta(), muon.globalTrack()->hitPattern().numberOfValidMuonHits());
      hNormalizedChi2->Fill(muon.eta(), muon.globalTrack()->normalizedChi2());
    }
      
    hIsoSumPtOverPt->Fill(muon.phi(), muon.isolationR03().sumPt / muon.pt());
    hIsoEmEtOverPt->Fill(muon.phi(), muon.isolationR03().emEt / muon.pt());
    hIsoHadEtOverPt->Fill(muon.phi(), muon.isolationR03().hadEt / muon.pt());

    hTkIso->Fill( muon.isolationR03().sumPt / muon.pt() );
    hCombIso->Fill( (muon.isolationR03().sumPt + muon.isolationR03().emEt + muon.isolationR03().hadEt)/muon.pt());

    relIsoVsEtaPhi->Fill(muon.eta(),muon.phi(),(muon.isolationR03().sumPt + muon.isolationR03().emEt + muon.isolationR03().hadEt)/muon.pt());    
  }
}

void MuonAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<edm::InputTag>("muonCollection", edm::InputTag("muons"))->setComment("Input collection of muons");
  descriptions.add("MuonAnalyzer", desc);
}

DEFINE_FWK_MODULE(MuonAnalyzer);
