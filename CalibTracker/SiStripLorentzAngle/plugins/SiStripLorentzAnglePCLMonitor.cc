// -*- C++ -*-
//
// Package:    CalibTracker/SiStripLorentzAnglePCLMonitor
// Class:      SiStripLorentzAnglePCLMonitor
//
/**\class SiStripLorentzAnglePCLMonitor SiStripLorentzAnglePCLMonitor.cc CalibTracker/SiStripLorentzAnglePCLMonitor/plugins/SiStripLorentzAnglePCLMonitor.cc

 Description: class to book and fill histograms necessary for the online monitoring of the SiStripLorentzAngle

 Implementation:
     Largely taken from https://github.com/robervalwalsh/tracker-la/blob/master/SiStripLAMonitor.cc
*/
//
// Original Author:  musich
//         Created:  Sun, 07 May 2023 16:57:10 GMT
//
//

#include <string>

// user include files
#include "DQMServices/Core/interface/DQMEDAnalyzer.h"
#include "DQMServices/Core/interface/MonitorElement.h"
#include "DataFormats/SiStripCluster/interface/SiStripCluster.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "TrackingTools/PatternTools/interface/TrajTrackAssociation.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripMatchedRecHit2D.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripRecHit2D.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripRecHit1D.h"
#include "Geometry/TrackerGeometryBuilder/interface/StripGeomDetUnit.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "RecoLocalTracker/SiStripClusterizer/interface/SiStripClusterInfo.h"
#include "CalibTracker/SiStripLorentzAngle/interface/SiStripLorentzAngleCalibrationStruct.h"
//
// class declaration
//

class SiStripLorentzAnglePCLMonitor : public DQMEDAnalyzer {
public:
  explicit SiStripLorentzAnglePCLMonitor(const edm::ParameterSet&);
  ~SiStripLorentzAnglePCLMonitor() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void bookHistograms(DQMStore::IBooker&, edm::Run const&, edm::EventSetup const&) override;
  void analyze(const edm::Event&, const edm::EventSetup&) override;

  // ------------ member data ------------
  SiStripClusterInfo m_clusterInfo;
  SiStripLorentzAngleCalibrationHistograms iHists_;

  std::string folder_;
  const edm::EDGetTokenT<edm::View<reco::Track>> m_tracks_token;
  const edm::EDGetTokenT<TrajTrackAssociationCollection> m_association_token;
  const edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> m_tkGeomToken;

  struct OnTrackCluster {
    uint32_t det;
    const SiStripCluster* cluster;
    const Trajectory* traj;
    const reco::Track* track;
    const TrajectoryMeasurement& measurement;
    OnTrackCluster(uint32_t detId,
                   const SiStripCluster* stripCluster,
                   const Trajectory* trajectory,
                   const reco::Track* track_,
                   const TrajectoryMeasurement& measurement_)
        : det{detId}, cluster{stripCluster}, traj{trajectory}, track{track_}, measurement{measurement_} {}
  };
};

SiStripLorentzAnglePCLMonitor::SiStripLorentzAnglePCLMonitor(const edm::ParameterSet& iConfig)
    : m_clusterInfo(consumesCollector()),
      folder_(iConfig.getParameter<std::string>("folder")),
      m_tracks_token(consumes<edm::View<reco::Track>>(iConfig.getParameter<edm::InputTag>("Tracks"))),
      m_association_token(consumes<TrajTrackAssociationCollection>(iConfig.getParameter<edm::InputTag>("Tracks"))),
      m_tkGeomToken{esConsumes<>()} {}
//
// member functions
//

// ------------ method called for each event  ------------
void SiStripLorentzAnglePCLMonitor::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;

  const auto& tkGeom = iSetup.getData(m_tkGeomToken);

  edm::Handle<edm::View<reco::Track>> tracks;
  iEvent.getByToken(m_tracks_token, tracks);
  edm::Handle<TrajTrackAssociationCollection> trajTrackAssociations;
  iEvent.getByToken(m_association_token, trajTrackAssociations);

  edm::LogInfo("SiStripLorentzAnglePCLMonitor") << "I AM IN EVENT" << iEvent.id() << std::endl;

  std::vector<OnTrackCluster> clusters{};

  // first collect all the clusters
  for (const auto& assoc : *trajTrackAssociations) {
    const auto traj = assoc.key.get();
    const auto track = assoc.val.get();

    iHists_.h1_["track_pt"]->Fill(track->pt());
    iHists_.h1_["track_eta"]->Fill(track->eta());
    iHists_.h1_["track_phi"]->Fill(track->phi());
    iHists_.h1_["track_validhits"]->Fill(track->numberOfValidHits());
    iHists_.h1_["track_chi2ndof"]->Fill((track->chi2() / track->ndof()));
    iHists_.h2_["track_chi2xhits"]->Fill((track->chi2() / track->ndof()), track->numberOfValidHits());
    iHists_.h2_["track_ptxhits"]->Fill(track->pt(), track->numberOfValidHits());
    iHists_.h2_["track_etaxhits"]->Fill(track->eta(), track->numberOfValidHits());
    iHists_.h2_["track_ptxchi2"]->Fill(track->pt(), (track->chi2() / track->ndof()));
    iHists_.h2_["track_ptxeta"]->Fill(track->pt(), track->eta());
    iHists_.h2_["track_etaxchi2"]->Fill(track->eta(), (track->chi2() / track->ndof()));

    edm::LogInfo("SiStripLorentzAnglePCLMonitor")
        << " track pT()" << track->pt() << " track eta()" << track->eta() << std::endl;

    for (const auto& meas : traj->measurements()) {
      const auto& trajState = meas.updatedState();
      if (!trajState.isValid())
        continue;

      // there can be 2 (stereo module), 1 (no stereo module), or 0 (no strip hit) clusters per measurement
      const auto trechit = meas.recHit()->hit();
      const auto simple1d = dynamic_cast<const SiStripRecHit1D*>(trechit);
      const auto simple = dynamic_cast<const SiStripRecHit2D*>(trechit);
      const auto matched = dynamic_cast<const SiStripMatchedRecHit2D*>(trechit);
      if (matched) {
        clusters.emplace_back(matched->monoId(), &matched->monoCluster(), traj, track, meas);
        clusters.emplace_back(matched->stereoId(), &matched->stereoCluster(), traj, track, meas);
      } else if (simple) {
        clusters.emplace_back(simple->geographicalId().rawId(), simple->cluster().get(), traj, track, meas);
      } else if (simple1d) {
        clusters.emplace_back(simple1d->geographicalId().rawId(), simple1d->cluster().get(), traj, track, meas);
      }
    }
  }

  for (const auto clus : clusters) {
    uint32_t c_nstrips = clus.cluster->amplitudes().size();
    m_clusterInfo.setCluster(*clus.cluster, clus.det);
    float c_variance = m_clusterInfo.variance();
    const auto& trajState = clus.measurement.updatedState();
    const auto trackDir = trajState.localDirection();
    float c_localdirx = trackDir.x();
    float c_localdiry = trackDir.y();
    float c_localdirz = trackDir.z();
    const auto hit = clus.measurement.recHit()->hit();
    const auto stripDet = dynamic_cast<const StripGeomDetUnit*>(tkGeom.idToDet(hit->geographicalId()));
    float c_barycenter = stripDet->specificTopology().localPosition(clus.cluster->barycenter()).x();
    float c_localx = stripDet->toLocal(trajState.globalPosition()).x();
    float c_rhlocalx = hit->localPosition().x();
    float c_rhlocalxerr = hit->localPositionError().xx();
  }
}

void SiStripLorentzAnglePCLMonitor::bookHistograms(DQMStore::IBooker& ibook,
                                                   edm::Run const& run,
                                                   edm::EventSetup const& iSetup) {
  ibook.setCurrentFolder(folder_);
  edm::LogPrint("") << "booking in " << folder_ << std::endl;

  // prepare track histograms
  iHists_.h1_["track_pt"] = ibook.book1D("track_pt", "", 2000, 0, 1000);
  iHists_.h1_["track_eta"] = ibook.book1D("track_eta", "", 100, -4, 4);
  iHists_.h1_["track_phi"] = ibook.book1D("track_phi", "", 80, -3.2, 3.2);
  iHists_.h1_["track_validhits"] = ibook.book1D("track_validhits", "", 50, 0, 50);
  iHists_.h1_["track_chi2ndof"] = ibook.book1D("track_chi2ndof", "", 100, 0, 5);
  iHists_.h2_["track_chi2xhits"] = ibook.book2D("track_chi2xhits_2d", "", 100, 0, 5, 50, 0, 50);
  iHists_.h2_["track_ptxhits"] = ibook.book2D("track_ptxhits_2d", "", 200, 0, 100, 50, 0, 50);
  iHists_.h2_["track_etaxhits"] = ibook.book2D("track_etaxhits_2d", "", 60, -3, 3, 50, 0, 50);
  iHists_.h2_["track_ptxchi2"] = ibook.book2D("track_ptxchi2_2d", "", 200, 0, 100, 100, 0, 5);
  iHists_.h2_["track_ptxeta"] = ibook.book2D("track_ptxeta_2d", "", 200, 0, 100, 60, -3, 3);
  iHists_.h2_["track_etaxchi2"] = ibook.book2D("track_etaxchi2_2d", "", 60, -3, 3, 100, 0, 5);

  //
  iHists_.nlayers_["TIB"] = 4;
  iHists_.nlayers_["TOB"] = 6;
  iHists_.modtypes_.push_back("s");
  iHists_.modtypes_.push_back("a");

  // prepare modules histograms
  for (auto& layers : iHists_.nlayers_) {
    std::string subdet = layers.first;
    for (int l = 1; l <= layers.second; ++l) {
      for (auto& t : iHists_.modtypes_) {
        std::string locationtype = Form("%s_L%d%s", subdet.c_str(), l, t.c_str());
        //std::cout << "preparing histograms for " << locationtype << std::endl;
        iHists_.h1_[Form("%s_nstrips", locationtype.c_str())] =
            ibook.book1D(Form("%s_nstrips", locationtype.c_str()), "", 20, 0, 20);
        iHists_.h1_[Form("%s_tanthetatrk", locationtype.c_str())] =
            ibook.book1D(Form("%s_tanthetatrk", locationtype.c_str()), "", 300, -1.5, 1.5);
        iHists_.h1_[Form("%s_cosphitrk", locationtype.c_str())] =
            ibook.book1D(Form("%s_cosphitrk", locationtype.c_str()), "", 40, -1, 1);
        iHists_.h1_[Form("%s_variance_w2", locationtype.c_str())] =
            ibook.book1D(Form("%s_variance_w2", locationtype.c_str()), "", 100, 0, 1);
        iHists_.h1_[Form("%s_variance_w3", locationtype.c_str())] =
            ibook.book1D(Form("%s_variance_w3", locationtype.c_str()), "", 100, 0, 1);

        iHists_.h2_[Form("%s_tanthcosphtrk_nstrip", locationtype.c_str())] =
            ibook.book2D(Form("%s_tanthcosphtrk_nstrip", locationtype.c_str()), "", 360, -0.9, 0.9, 20, 0, 20);
        iHists_.h2_[Form("%s_thetatrk_nstrip", locationtype.c_str())] =
            ibook.book2D(Form("%s_thetatrk_nstrip", locationtype.c_str()), "", 360, -0.9, 0.9, 20, 0, 20);
        iHists_.h2_[Form("%s_tanthcosphtrk_var2", locationtype.c_str())] =
            ibook.book2D(Form("%s_tanthcosphtrk_var2", locationtype.c_str()), "", 360, -0.9, 0.9, 50, 0, 1);
        iHists_.h2_[Form("%s_tanthcosphtrk_var3", locationtype.c_str())] =
            ibook.book2D(Form("%s_tanthcosphtrk_var3", locationtype.c_str()), "", 360, -0.9, 0.9, 50, 0, 1);
        iHists_.h2_[Form("%s_thcosphtrk_var2", locationtype.c_str())] =
            ibook.book2D(Form("%s_thcosphtrk_var2", locationtype.c_str()), "", 360, -0.9, 0.9, 50, 0, 1);
        iHists_.h2_[Form("%s_thcosphtrk_var3", locationtype.c_str())] =
            ibook.book2D(Form("%s_thcosphtrk_var3", locationtype.c_str()), "", 360, -0.9, 0.9, 50, 0, 1);
      }
    }
  }
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void SiStripLorentzAnglePCLMonitor::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<std::string>("folder", "AlCaReco/SiStripLorentzAngle");
  desc.add<edm::InputTag>("Tracks", edm::InputTag("SiStripCalCosmics"));
  descriptions.addWithDefaultLabel(desc);
}

// define this as a plug-in
DEFINE_FWK_MODULE(SiStripLorentzAnglePCLMonitor);
