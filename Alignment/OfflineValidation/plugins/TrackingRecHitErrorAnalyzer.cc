#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripRecHit2D.h"
#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHit.h"
#include "DataFormats/TrackingRecHit/interface/TrackingRecHit.h"
#include "DataFormats/GeometrySurface/interface/Surface.h"
#include "Geometry/CommonDetUnit/interface/GeomDet.h"
#include "Geometry/CommonTopologies/interface/TrackerGeomDet.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/SiPixelDetId/interface/PixelSubdetector.h"
#include "DataFormats/TrackerCommon/interface/PixelBarrelName.h"
#include "DataFormats/TrackerCommon/interface/PixelEndcapName.h"
#include "TrackingTools/TrajectoryState/interface/TrajectoryStateOnSurface.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TFile.h"

class TrackingRecHitErrorAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit TrackingRecHitErrorAnalyzer(const edm::ParameterSet&);
  ~TrackingRecHitErrorAnalyzer() override;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void beginJob() override;
  void endJob() override;

  edm::EDGetTokenT<reco::TrackCollection> tracksToken_;
  std::map<std::string, TH2F*> histos_;
  std::map<std::string, std::map<std::string, TH2F*>> layerHistos_;
  std::string outputFile_;
  TFile* outFile_;
};

TrackingRecHitErrorAnalyzer::TrackingRecHitErrorAnalyzer(const edm::ParameterSet& iConfig)
    : tracksToken_(consumes<reco::TrackCollection>(iConfig.getParameter<edm::InputTag>("tracks"))),
      outputFile_(iConfig.getParameter<std::string>("outputFile")) {}

TrackingRecHitErrorAnalyzer::~TrackingRecHitErrorAnalyzer() {}

void TrackingRecHitErrorAnalyzer::beginJob() {
  outFile_ = new TFile(outputFile_.c_str(), "RECREATE");

  std::vector<std::string> layers = {
      "BPix1", "BPix2", "BPix3", "BPix4", "FPix1+", "FPix1-", "FPix2+", "FPix2-", "FPix3+", "FPix3-"};

  for (const auto& layer : layers) {
    layerHistos_[layer]["rechitError_withAPE_vs_pt"] =
        new TH2F(("rechitError_withAPE_vs_pt_" + layer).c_str(),
                 ("Rechit Error with APE vs pT in " + layer + "; pT [GeV]; Error").c_str(),
                 100,
                 0,
                 100,
                 100,
                 0,
                 0.05);
    layerHistos_[layer]["rechitError_withoutAPE_vs_pt"] =
        new TH2F(("rechitError_withoutAPE_vs_pt_" + layer).c_str(),
                 ("Rechit Error without APE vs pT in " + layer + "; pT [GeV]; Error").c_str(),
                 100,
                 0,
                 100,
                 100,
                 0,
                 0.05);
    layerHistos_[layer]["rechitError_withAPE_vs_eta"] =
        new TH2F(("rechitError_withAPE_vs_eta_" + layer).c_str(),
                 ("Rechit Error with APE vs eta in " + layer + "; eta; Error").c_str(),
                 100,
                 -3,
                 3,
                 100,
                 0,
                 0.05);
    layerHistos_[layer]["rechitError_withoutAPE_vs_eta"] =
        new TH2F(("rechitError_withoutAPE_vs_eta_" + layer).c_str(),
                 ("Rechit Error without APE vs eta in " + layer + "; eta; Error").c_str(),
                 100,
                 -3,
                 3,
                 100,
                 0,
                 0.05);
  }
}

void TrackingRecHitErrorAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  edm::Handle<reco::TrackCollection> tracks;
  iEvent.getByToken(tracksToken_, tracks);

  for (const auto& track : *tracks) {
    for (auto hit = track.recHitsBegin(); hit != track.recHitsEnd(); ++hit) {
      if (!(*hit)->isValid())
        continue;
      const auto& localError = (*hit)->localPositionError();

      double errorWithAPE = sqrt(localError.xx());
      double errorWithoutAPE = errorWithAPE;

      const auto* trackerDet = dynamic_cast<const TrackerGeomDet*>((*hit)->det());
      if (trackerDet) {
        LocalError lape = trackerDet->localAlignmentError();
        if (lape.valid()) {
          errorWithoutAPE = sqrt(localError.xx() - lape.xx());
        }
      }

      DetId detId = (*hit)->geographicalId();
      std::string layer;
      if (detId.subdetId() == PixelSubdetector::PixelBarrel) {
        int layerNumber = PixelBarrelName(detId).layerName();
        layer = "BPix" + std::to_string(layerNumber);
      } else if (detId.subdetId() == PixelSubdetector::PixelEndcap) {
        PixelEndcapName pixelEndcap(detId);
        int disk = pixelEndcap.diskName();
        std::string sign =
            (pixelEndcap.halfCylinder() == PixelEndcapName::pO || pixelEndcap.halfCylinder() == PixelEndcapName::pI)
                ? "+"
                : "-";
        layer = "FPix" + std::to_string(disk) + sign;
      }

      layerHistos_[layer]["rechitError_withAPE_vs_pt"]->Fill(track.pt(), errorWithAPE);
      layerHistos_[layer]["rechitError_withoutAPE_vs_pt"]->Fill(track.pt(), errorWithoutAPE);
      layerHistos_[layer]["rechitError_withAPE_vs_eta"]->Fill(track.eta(), errorWithAPE);
      layerHistos_[layer]["rechitError_withoutAPE_vs_eta"]->Fill(track.eta(), errorWithoutAPE);
    }
  }
}

void TrackingRecHitErrorAnalyzer::endJob() {
  outFile_->cd();
  for (const auto& layer : layerHistos_) {
    for (const auto& histo : layer.second) {
      histo.second->Write();
    }
  }
  outFile_->Close();
}

void TrackingRecHitErrorAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<edm::InputTag>("tracks", edm::InputTag("generalTracks"));
  desc.add<std::string>("outputFile", "rechitErrors.root");
  descriptions.add("trackingRecHitErrorAnalyzer", desc);
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(TrackingRecHitErrorAnalyzer);
