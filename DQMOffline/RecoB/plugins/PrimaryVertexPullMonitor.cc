#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "DQMServices/Core/interface/DQMOneEDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DQMServices/Core/interface/DQMStore.h"
#include "DQMServices/Core/interface/MonitorElement.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include <vector>
#include <cmath>

class PrimaryVertexPullMonitor : public DQMOneEDAnalyzer<> {
public:
  explicit PrimaryVertexPullMonitor(const edm::ParameterSet&);
  ~PrimaryVertexPullMonitor() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void bookHistograms(DQMStore::IBooker&, edm::Run const&, edm::EventSetup const&) override;
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void pvTracksPlots(const reco::Vertex& v);
  void endJob() override;

  // data members
  std::string dqmLabel;
  std::string TopFolderName_;
  std::string AlignmentLabel_;

  const edm::EDGetTokenT<reco::VertexCollection> vertexToken_;

  MonitorElement* dxyPullVsEta_;
  MonitorElement* dxyPullVsPhi_;

  MonitorElement* dzPullVsEta_;
  MonitorElement* dzPullVsPhi_;

  // Storage to collect dxy/dxyError values for each bin
  std::vector<std::vector<double>> dxyPullsEta_;
  std::vector<std::vector<double>> dxyPullsPhi_;
  std::vector<std::vector<double>> dzPullsEta_;
  std::vector<std::vector<double>> dzPullsPhi_;

  static constexpr int cmToUm = 10000;

  const int nEtaBins = 50;
  const int nPhiBins = 50;
  const double etaMin = -2.5;
  const double etaMax = 2.5;
  const double phiMin = -3.14;
  const double phiMax = 3.14;
};

PrimaryVertexPullMonitor::PrimaryVertexPullMonitor(const edm::ParameterSet& iConfig)
    : TopFolderName_(iConfig.getParameter<std::string>("TopFolderName")),
      AlignmentLabel_(iConfig.getParameter<std::string>("AlignmentLabel")),
      vertexToken_(consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("vertices"))),
      dxyPullVsEta_(nullptr),
      dxyPullVsPhi_(nullptr),
      dzPullVsEta_(nullptr),
      dzPullVsPhi_(nullptr) {
  dxyPullsEta_.resize(nEtaBins);  // Prepare for eta bins
  dxyPullsPhi_.resize(nPhiBins);  // Prepare for phi bins
  dzPullsEta_.resize(nEtaBins);   // Prepare for eta bins
  dzPullsPhi_.resize(nPhiBins);   // Prepare for phi bins
}

void PrimaryVertexPullMonitor::bookHistograms(DQMStore::IBooker& iBooker, edm::Run const&, edm::EventSetup const&) {
  dqmLabel = TopFolderName_ + "/" + AlignmentLabel_;
  iBooker.setCurrentFolder(dqmLabel);

  // Book histograms that will eventually store the RMS of dxy/dxyError in bins of eta and phi
  dxyPullVsEta_ = iBooker.book1D(
      "dxyPullVsEta", "RMS of dxy Pull vs Eta;Track #eta;Pull RMS (dxy/dxyError)", nEtaBins, etaMin, etaMax);
  dxyPullVsPhi_ = iBooker.book1D(
      "dxyPullVsPhi", "RMS of dxy Pull vs Phi;Track #phi;Pull RMS (dxy/dxyError)", nPhiBins, phiMin, phiMax);

  // Book histograms that will eventually store the RMS of dz/dzError in bins of eta and phi
  dzPullVsEta_ =
      iBooker.book1D("dzPullVsEta", "RMS of dz Pull vs Eta;Track #eta;Pull RMS (dz/dzError)", nEtaBins, etaMin, etaMax);
  dzPullVsPhi_ =
      iBooker.book1D("dzPullVsPhi", "RMS of dz Pull vs Phi;Track #phi;Pull RMS (dz/dzError)", nPhiBins, phiMin, phiMax);
}

void PrimaryVertexPullMonitor::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  edm::Handle<reco::VertexCollection> vertices;
  iEvent.getByToken(vertexToken_, vertices);

  if (vertices->empty())
    return;  // Skip if no primary vertex
  const reco::Vertex& primaryVertex = vertices->front();
  pvTracksPlots(primaryVertex);
}

void PrimaryVertexPullMonitor::pvTracksPlots(const reco::Vertex& v) {
  if (!v.isValid())
    return;
  if (v.isFake())
    return;

  if (v.tracksSize() == 0) {
    return;
  }

  const math::XYZPoint myVertex(v.position().x(), v.position().y(), v.position().z());

  for (reco::Vertex::trackRef_iterator t = v.tracks_begin(); t != v.tracks_end(); t++) {
    bool isHighPurity = (**t).quality(reco::TrackBase::highPurity);
    if (!isHighPurity)
      continue;

    float pt = (**t).pt();
    if (pt < 1.)
      continue;

    float eta = (**t).eta();
    float phi = (**t).phi();

    float Dxy = (**t).dxy(myVertex) * cmToUm;
    float Dz = (**t).dz(myVertex) * cmToUm;
    float DxyErr = (**t).dxyError() * cmToUm;
    float DzErr = (**t).dzError() * cmToUm;

    // Determine the eta and phi bin for the track
    int etaBin = dxyPullVsEta_->getTH1()->FindBin(eta) - 1;  // Bins start from 1 in ROOT, but we use 0-based indexing
    int phiBin = dxyPullVsPhi_->getTH1()->FindBin(phi) - 1;

    // Add dxyPull to the corresponding eta and phi bin
    if (etaBin >= 0 && etaBin < nEtaBins) {
      dxyPullsEta_[etaBin].push_back(Dxy / DxyErr);
      dzPullsEta_[etaBin].push_back(Dz / DzErr);
    }

    if (phiBin >= 0 && phiBin < nPhiBins) {
      dxyPullsPhi_[phiBin].push_back(Dxy / DxyErr);
      dzPullsPhi_[phiBin].push_back(Dz / DzErr);
    }
  }
}

void PrimaryVertexPullMonitor::endJob() {
  // Lambda to calculate RMS and fill histogram bin
  auto fillRMS = [](const std::vector<std::vector<double>>& pullsPerBin, MonitorElement* me) {
    for (size_t i = 0; i < pullsPerBin.size(); ++i) {
      const std::vector<double>& pulls = pullsPerBin[i];
      if (pulls.empty())
        continue;  // Skip if no entries in the bin

      // Calculate RMS
      double sum = 0;
      for (double pull : pulls) {
        sum += pull * pull;
      }
      double rms = std::sqrt(sum / pulls.size());
      me->setBinContent(i + 1, rms);  // Bin content starts from 1 in ROOT
    }
  };

  // Use the lambda to fill both eta and phi histograms
  fillRMS(dxyPullsEta_, dxyPullVsEta_);
  fillRMS(dxyPullsPhi_, dxyPullVsPhi_);

  fillRMS(dzPullsEta_, dzPullVsEta_);
  fillRMS(dzPullsPhi_, dzPullVsPhi_);
}

void PrimaryVertexPullMonitor::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<std::string>("TopFolderName", "OfflinePV");
  desc.add<std::string>("AlignmentLabel", "AlignmentPulls");
  desc.add<edm::InputTag>("vertices", edm::InputTag("offlinePrimaryVertices"));
  descriptions.addWithDefaultLabel(desc);
}

// Define this as a plug-in
DEFINE_FWK_MODULE(PrimaryVertexPullMonitor);
