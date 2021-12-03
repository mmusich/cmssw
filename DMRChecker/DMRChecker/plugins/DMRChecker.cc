// -*- C++ -*-
//
// Package:    DMRChecker/DMRChecker
// Class:      DMRChecker
//
/**\class DMRChecker DMRChecker.cc DMRChecker/DMRChecker/plugins/DMRChecker.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Marco Musich
//         Created:  Tue, 30 Nov 2021 11:08:17 GMT
//
//

// system include files
#include <memory>
#include <vector>
#include <fmt/printf.h>

// user include files
#include "Alignment/OfflineValidation/interface/TrackerValidationVariables.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"
#include "Geometry/Records/interface/TrackerTopologyRcd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "FWCore/Utilities/interface/ESGetToken.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "CommonTools/Utils/interface/TFileDirectory.h"

// ROOT includes
#include "TH1F.h"

/**
 * Auxilliary POD to store the data for
 * the running mean algorithm.
 */

namespace running {

  enum dir { X = 0, Y = 1, undef = -1 };

  struct Estimators {
    bool isX;
    bool isY;
    float rDirection;
    float zDirection;
    float rOrZDirection;
    int hitCount;
    float runningMeanOfRes_;
    float runningVarOfRes_;
    float runningNormMeanOfRes_;
    float runningNormVarOfRes_;

  public:
    Estimators() {
      this->isX = this->isY = false;
      this->hitCount = 0;
      this->runningMeanOfRes_ = this->runningVarOfRes_ = 0;
      this->runningNormMeanOfRes_ = this->runningNormVarOfRes_ = 0;
      this->rDirection = this->zDirection = this->rOrZDirection = 0.;
    }
  };

  using estimatorMap = std::map<uint32_t, running::Estimators>;
}  // namespace running

//
// class declaration
//

using reco::TrackCollection;
class DMRChecker : public edm::one::EDAnalyzer<edm::one::SharedResources, edm::one::WatchRuns> {
public:
  explicit DMRChecker(const edm::ParameterSet&);
  ~DMRChecker() override;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  // framework methods
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void beginRun(edm::Run const&, edm::EventSetup const&) override;
  void endRun(edm::Run const&, edm::EventSetup const&) override;
  void endJob() override;

  // user defined methods
  void updateOnlineMomenta(running::estimatorMap& myDetails,
                           const uint32_t& theID,
                           const float& the_data,
                           const float& the_pull);

  void setOrientations(running::estimatorMap& myDetails,
                       const uint32_t& theID,
                       const running::dir& theDir,
                       const TrackerGeometry& tkgeo);

  std::array<TH1D*, 2> bookSplitDMRHistograms(TFileDirectory dir,
                                              std::string subdet,
                                              std::string vartype,
                                              bool isBarrel);

  void fillDMRs(const running::estimatorMap& myDetails, TH1D* DMR, TH1D* DRnR, std::array<TH1D*, 2> DMRSplit);

  std::pair<std::string, int32_t> findSubdetAndLayer(uint32_t ModuleID, const TrackerTopology* tTopo);

  struct HistoPair {
    HistoPair() {
      base = nullptr;
      normed = nullptr;
    };
    TH1F* base;
    TH1F* normed;
  };

  struct HistoXY {
    HistoPair x;
    HistoPair y;
  };
  typedef std::map<std::pair<std::string, int32_t>, HistoXY> HistoSet;

  // ----------member data ---------------------------
  edm::Service<TFileService> fs;
  TrackerValidationVariables avalidator_;
  bool applyVertexCut_;

  // event tokens
  const edm::EDGetTokenT<reco::VertexCollection> offlinePVToken_;

  // event setup tokens
  const edm::ESGetToken<TrackerTopology, TrackerTopologyRcd> trackerTopologyRunToken_;
  const edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> trackerGeometryToken_;
  const edm::ESGetToken<TrackerTopology, TrackerTopologyRcd> trackerTopologyEventToken_;

  // Pixel
  running::estimatorMap resDetailsBPixX_;
  running::estimatorMap resDetailsBPixY_;
  running::estimatorMap resDetailsFPixX_;
  running::estimatorMap resDetailsFPixY_;

  // Strips
  running::estimatorMap resDetailsTIB_;
  running::estimatorMap resDetailsTOB_;
  running::estimatorMap resDetailsTID_;
  running::estimatorMap resDetailsTEC_;

  // by layer residuals
  HistoSet m_SubdetLayerResiduals;

  // Pixel
  TH1D* DMRBPixX_;
  TH1D* DMRBPixY_;
  TH1D* DMRFPixX_;
  TH1D* DMRFPixY_;
  TH1D* DRnRBPixX_;
  TH1D* DRnRBPixY_;
  TH1D* DRnRFPixX_;
  TH1D* DRnRFPixY_;

  // Strips
  TH1D* DMRTIB_;
  TH1D* DMRTOB_;
  TH1D* DMRTID_;
  TH1D* DMRTEC_;
  TH1D* DRnRTIB_;
  TH1D* DRnRTOB_;
  TH1D* DRnRTID_;
  TH1D* DRnRTEC_;

  // Split DMRs
  std::array<TH1D*, 2> DMRBPixXSplit_;
  std::array<TH1D*, 2> DMRBPixYSplit_;
  std::array<TH1D*, 2> DMRFPixXSplit_;
  std::array<TH1D*, 2> DMRFPixYSplit_;
  std::array<TH1D*, 2> DMRTIBSplit_;
  std::array<TH1D*, 2> DMRTOBSplit_;
  std::array<TH1D*, 2> DMRTIDSplit_;
  std::array<TH1D*, 2> DMRTECSplit_;
};

//
// constructors and destructor
//
DMRChecker::DMRChecker(const edm::ParameterSet& iConfig)
    : avalidator_(iConfig, consumesCollector()),
      offlinePVToken_(consumes<reco::VertexCollection>(iConfig.getParameter<std::string>("VertexCollection"))),
      trackerTopologyRunToken_{esConsumes<TrackerTopology, TrackerTopologyRcd, edm::Transition::BeginRun>()},
      trackerGeometryToken_{esConsumes<TrackerGeometry, TrackerDigiGeometryRecord, edm::Transition::BeginRun>()},
      trackerTopologyEventToken_{esConsumes<TrackerTopology, TrackerTopologyRcd>()} {
  applyVertexCut_ = iConfig.getUntrackedParameter<bool>("VertexCut", true);
  usesResource(TFileService::kSharedResource);  // for thread-efficient usage of TFileService
}

DMRChecker::~DMRChecker() = default;

void DMRChecker::endRun(edm::Run const& iRun, edm::EventSetup const& iSetup) {}  //endRun

void DMRChecker::beginRun(edm::Run const& iRun, edm::EventSetup const& iSetup) {
  const TrackerGeometry& TG = iSetup.getData(trackerGeometryToken_);
  // Collect list of modules from Tracker Geometry
  auto ids = TG.detIds();
  for (DetId id : ids) {
    auto ModuleID = id.rawId();

    switch (id.subdetId()) {
      case PixelSubdetector::PixelBarrel:
        this->setOrientations(resDetailsBPixX_, ModuleID, running::X, TG);
        this->setOrientations(resDetailsBPixY_, ModuleID, running::Y, TG);
        break;
      case PixelSubdetector::PixelEndcap:
        this->setOrientations(resDetailsFPixX_, ModuleID, running::X, TG);
        this->setOrientations(resDetailsFPixY_, ModuleID, running::Y, TG);
        break;
      case StripSubdetector::TIB:
        this->setOrientations(resDetailsTIB_, ModuleID, running::X, TG);
        break;
      case StripSubdetector::TOB:
        this->setOrientations(resDetailsTOB_, ModuleID, running::X, TG);
        break;
      case StripSubdetector::TID:
        this->setOrientations(resDetailsTID_, ModuleID, running::X, TG);
        break;
      case StripSubdetector::TEC:
        this->setOrientations(resDetailsTEC_, ModuleID, running::X, TG);
        break;
      default:
        throw cms::Exception("Inconsistent Data") << "Unknown Tracker subdetector: " << id.subdetId();
    }
  }
}  //beginRun

//
// member functions
//
// ------------ method called for each event  ------------
void DMRChecker::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;

  edm::Handle<reco::VertexCollection> vertices;
  if (applyVertexCut_) {
    iEvent.getByToken(offlinePVToken_, vertices);
    if (!vertices.isValid() || vertices->empty())
      return;
  }

  auto vtracks = std::vector<TrackerValidationVariables::AVTrackStruct>();
  avalidator_.fillTrackQuantities(
      iEvent,
      iSetup,
      // tell the validator to only look at good tracks
      [&](const reco::Track& track) -> bool {
        return (!applyVertexCut_ ||
                (track.pt() > 0.75 && abs(track.dxy(vertices->at(0).position())) < 5 * track.dxyError()));
      },
      vtracks);

  // loop on the tracks
  for (auto& track : vtracks) {
    // loop on the rechits
    for (auto& it : track.hits) {
      uint RawId = it.rawDetId;
      auto id = DetId(RawId);
      uint subid = id.subdetId();
      const auto& resX = it.resXprime;
      const auto& pullX = it.resXprime / it.resXprimeErr;

      auto isPixel = subid == PixelSubdetector::PixelBarrel || subid == PixelSubdetector::PixelEndcap;
      if (isPixel) {
        // y-residuals only for pixels
        const auto& resY = it.resYprime;
        const auto& pullY = it.resYprime / it.resYprimeErr;

        if (subid == PixelSubdetector::PixelBarrel) {
          this->updateOnlineMomenta(resDetailsBPixX_, RawId, resX, pullX);
          this->updateOnlineMomenta(resDetailsBPixY_, RawId, resY, pullY);
        } else if (subid == PixelSubdetector::PixelEndcap) {
          this->updateOnlineMomenta(resDetailsFPixX_, RawId, resX, pullX);
          this->updateOnlineMomenta(resDetailsFPixY_, RawId, resY, pullY);
        }     // if FPix
      }       // if Pixel
      else {  // these are Strips
        if (subid == StripSubdetector::TIB) {
          this->updateOnlineMomenta(resDetailsTIB_, RawId, resX, pullX);
        } else if (subid == StripSubdetector::TOB) {
          this->updateOnlineMomenta(resDetailsTOB_, RawId, resX, pullX);
        } else if (subid == StripSubdetector::TID) {
          this->updateOnlineMomenta(resDetailsTID_, RawId, resX, pullX);
        } else if (subid == StripSubdetector::TEC) {
          this->updateOnlineMomenta(resDetailsTEC_, RawId, resX, pullX);
        }
      }
    }  // loop on hits
  }    // loop on tracks
}

void DMRChecker::endJob() {
  // DMRs
  TFileDirectory DMeanR = fs->mkdir("DMRs");
  DMRBPixX_ = DMeanR.make<TH1D>("DMRBPix-X", "DMR of BPix-X;mean of X-residuals;modules", 100., -200, 200);
  DMRBPixY_ = DMeanR.make<TH1D>("DMRBPix-Y", "DMR of BPix-Y;mean of Y-residuals;modules", 100., -200, 200);

  DMRFPixX_ = DMeanR.make<TH1D>("DMRFPix-X", "DMR of FPix-X;mean of X-residuals;modules", 100., -200, 200);
  DMRFPixY_ = DMeanR.make<TH1D>("DMRFPix-Y", "DMR of FPix-Y;mean of Y-residuals;modules", 100., -200, 200);

  DMRTIB_ = DMeanR.make<TH1D>("DMRTIB", "DMR of TIB;mean of X-residuals;modules", 100., -200, 200);
  DMRTOB_ = DMeanR.make<TH1D>("DMRTOB", "DMR of TOB;mean of X-residuals;modules", 100., -200, 200);

  DMRTID_ = DMeanR.make<TH1D>("DMRTID", "DMR of TID;mean of X-residuals;modules", 100., -200, 200);
  DMRTEC_ = DMeanR.make<TH1D>("DMRTEC", "DMR of TEC;mean of X-residuals;modules", 100., -200, 200);

  TFileDirectory DMeanRSplit = fs->mkdir("SplitDMRs");
  DMRBPixXSplit_ = bookSplitDMRHistograms(DMeanRSplit, "BPix", "X", true);
  DMRBPixYSplit_ = bookSplitDMRHistograms(DMeanRSplit, "BPix", "Y", true);

  DMRFPixXSplit_ = bookSplitDMRHistograms(DMeanRSplit, "FPix", "X", false);
  DMRFPixYSplit_ = bookSplitDMRHistograms(DMeanRSplit, "FPix", "Y", false);

  DMRTIBSplit_ = bookSplitDMRHistograms(DMeanRSplit, "TIB", "X", true);
  DMRTOBSplit_ = bookSplitDMRHistograms(DMeanRSplit, "TOB", "X", true);

  DMRTIDSplit_ = bookSplitDMRHistograms(DMeanRSplit, "TID", "X", false);
  DMRTECSplit_ = bookSplitDMRHistograms(DMeanRSplit, "TEC", "X", false);

  // DRnRs
  TFileDirectory DRnRs = fs->mkdir("DRnRs");

  DRnRBPixX_ = DRnRs.make<TH1D>("DRnRBPix-X", "DRnR of BPix-X;rms of normalized X-residuals;modules", 100., 0., 3.);
  DRnRBPixY_ = DRnRs.make<TH1D>("DRnRBPix-Y", "DRnR of BPix-Y;rms of normalized Y-residuals;modules", 100., 0., 3.);

  DRnRFPixX_ = DRnRs.make<TH1D>("DRnRFPix-X", "DRnR of FPix-X;rms of normalized X-residuals;modules", 100., 0., 3.);
  DRnRFPixY_ = DRnRs.make<TH1D>("DRnRFPix-Y", "DRnR of FPix-Y;rms of normalized Y-residuals;modules", 100., 0., 3.);

  DRnRTIB_ = DRnRs.make<TH1D>("DRnRTIB", "DRnR of TIB;rms of normalized X-residuals;modules", 100., 0., 3.);
  DRnRTOB_ = DRnRs.make<TH1D>("DRnRTOB", "DRnR of TOB;rms of normalized Y-residuals;modules", 100., 0., 3.);

  DRnRTID_ = DRnRs.make<TH1D>("DRnRTID", "DRnR of TID;rms of normalized X-residuals;modules", 100., 0., 3.);
  DRnRTEC_ = DRnRs.make<TH1D>("DRnRTEC", "DRnR of TEC;rms of normalized Y-residuals;modules", 100., 0., 3.);

  // fill the distributions
  this->fillDMRs(resDetailsBPixX_, DMRBPixX_, DRnRBPixX_, DMRBPixXSplit_);
  this->fillDMRs(resDetailsBPixY_, DMRBPixY_, DRnRBPixY_, DMRBPixYSplit_);

  this->fillDMRs(resDetailsFPixX_, DMRFPixX_, DRnRFPixX_, DMRFPixXSplit_);
  this->fillDMRs(resDetailsFPixY_, DMRFPixY_, DRnRFPixY_, DMRFPixYSplit_);

  this->fillDMRs(resDetailsTIB_, DMRTIB_, DRnRTIB_, DMRTIBSplit_);
  this->fillDMRs(resDetailsTOB_, DMRTOB_, DRnRTOB_, DMRTOBSplit_);

  this->fillDMRs(resDetailsTID_, DMRTID_, DRnRTID_, DMRTIDSplit_);
  this->fillDMRs(resDetailsTEC_, DMRTEC_, DRnRTEC_, DMRTECSplit_);
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void DMRChecker::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<std::string>("vertexCollection", "offlinePrimaryVertices");
  descriptions.addWithDefaultLabel(desc);
}

std::pair<std::string, int32_t> DMRChecker::findSubdetAndLayer(uint32_t ModuleID, const TrackerTopology* tTopo) {
  std::string subdet = "";
  int32_t layer = 0;
  auto id = DetId(ModuleID);
  switch (id.subdetId()) {
    // Pixel Barrel, Endcap
    case PixelSubdetector::PixelBarrel:
      subdet = "BPIX";
      layer = tTopo->pxbLayer(id);
      break;
    case PixelSubdetector::PixelEndcap:
      subdet = "FPIX";
      layer = tTopo->pxfDisk(id) * (tTopo->pxfSide(ModuleID) == 1 ? -1 : +1);
      break;
    // Strip TIB, TID, TOB, TEC
    case StripSubdetector::TIB:
      subdet = "TIB";
      layer = tTopo->tibLayer(id);
      break;
    case StripSubdetector::TID:
      subdet = "TID";
      layer = tTopo->tidWheel(id) * (tTopo->tidSide(ModuleID) == 1 ? -1 : +1);
      break;
    case StripSubdetector::TOB:
      subdet = "TOB";
      layer = tTopo->tobLayer(id);
      break;
    case StripSubdetector::TEC:
      subdet = "TEC";
      layer = tTopo->tecWheel(id) * (tTopo->tecSide(ModuleID) == 1 ? -1 : +1);
      break;
    default:
      throw cms::Exception("Inconsistent Data") << "Unknown Tracker subdetector: " << id.subdetId();
  }
  return std::make_pair(subdet, layer);
}

void DMRChecker::setOrientations(running::estimatorMap& myDetails,
                                 const uint32_t& theID,
                                 const running::dir& theDir,
                                 const TrackerGeometry& tkgeom) {
  // if the detid has never occcurred yet, set the local orientations
  if (myDetails.find(theID) == myDetails.end()) {
    switch (theDir) {
      case running::X:
        myDetails[theID].isX = true;
        break;
      case running::Y:
        myDetails[theID].isY = false;
        break;
      default:
        edm::LogError("DMRChecker") << __FUNCTION__ << " : unrecognized orientation " << theDir;
    }

    const auto& id = DetId(theID);
    uint subDetId = id.subdetId();

    //variables concerning the tracker geometry
    const Surface::PositionType& gPModule = tkgeom.idToDet(theID)->position();
    const Surface& surface = tkgeom.idToDet(theID)->surface();
    //global Orientation of local coordinate system of dets/detUnits
    LocalPoint lUDirection(1., 0., 0.), lVDirection(0., 1., 0.), lWDirection(0., 0., 1.);
    GlobalPoint gUDirection = surface.toGlobal(lUDirection), gVDirection = surface.toGlobal(lVDirection),
                gWDirection = surface.toGlobal(lWDirection);
    double dR(999.), dZ(999.);

    // assign the rOrZDirection
    if (subDetId == PixelSubdetector::PixelBarrel || subDetId == StripSubdetector::TIB ||
        subDetId == StripSubdetector::TOB) {
      dR = gWDirection.perp() - gPModule.perp();
      dZ = gVDirection.z() - gPModule.z();
      if (dZ >= 0.)
        myDetails[theID].rOrZDirection = 1;
      else
        myDetails[theID].rOrZDirection = -1;
    } else if (subDetId == PixelSubdetector::PixelEndcap) {
      dR = gUDirection.perp() - gPModule.perp();
      dZ = gWDirection.z() - gPModule.z();
      if (dR >= 0.)
        myDetails[theID].rOrZDirection = 1;
      else
        myDetails[theID].rOrZDirection = -1;
    } else if (subDetId == StripSubdetector::TID || subDetId == StripSubdetector::TEC) {
      dR = gVDirection.perp() - gPModule.perp();
      dZ = gWDirection.z() - gPModule.z();
      if (dR >= 0.)
        myDetails[theID].rOrZDirection = 1;
      else
        myDetails[theID].rOrZDirection = -1;
    }

    // assingn the r-direction (barrel)
    if (dR >= 0.)
      myDetails[theID].rDirection = 1;
    else
      myDetails[theID].rDirection = -1;

    // assign the z-direction (endcaps)
    if (dZ >= 0.)
      myDetails[theID].zDirection = 1;
    else
      myDetails[theID].zDirection = -1;
  }
}

//*************************************************************
// Implementation of the online variance algorithm
// as in https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Online_algorithm
//*************************************************************
void DMRChecker::updateOnlineMomenta(running::estimatorMap& myDetails,
                                     const uint32_t& theID,
                                     const float& the_data,
                                     const float& the_pull) {
  // increase the hit counter
  myDetails[theID].hitCount += 1;

  // update the running mean
  float delta = 0;
  float n_delta = 0;

  if (myDetails[theID].hitCount != 1) {
    delta = the_data - myDetails[theID].runningMeanOfRes_;
    n_delta = the_pull - myDetails[theID].runningNormMeanOfRes_;
    myDetails[theID].runningMeanOfRes_ += (delta / myDetails[theID].hitCount);
    myDetails[theID].runningNormMeanOfRes_ += (n_delta / myDetails[theID].hitCount);
  } else {
    myDetails[theID].runningMeanOfRes_ = the_data;
    myDetails[theID].runningNormMeanOfRes_ = the_pull;
  }

  float delta2 = the_data - myDetails[theID].runningMeanOfRes_;
  float n_delta2 = the_pull - myDetails[theID].runningNormMeanOfRes_;

  myDetails[theID].runningVarOfRes_ += delta * delta2;
  myDetails[theID].runningNormVarOfRes_ += n_delta * n_delta2;
}

//*************************************************************
// Generic booker of split DMRs
//*************************************************************
std::array<TH1D*, 2> DMRChecker::bookSplitDMRHistograms(TFileDirectory dir,
                                                        std::string subdet,
                                                        std::string vartype,
                                                        bool isBarrel) {
  TH1F::SetDefaultSumw2(kTRUE);

  std::array<TH1D*, 2> out;
  std::array<std::string, 2> sign_name = {{"plus", "minus"}};
  std::array<std::string, 2> sign = {{">0", "<0"}};
  for (unsigned int i = 0; i < 2; i++) {
    const char* name_;
    const char* title_;
    const char* axisTitle_;

    if (isBarrel) {
      name_ = Form("DMR%s_%s_rDir%s", subdet.c_str(), vartype.c_str(), sign_name[i].c_str());
      title_ = Form("Split DMR of %s-%s (rDir%s)", subdet.c_str(), vartype.c_str(), sign[i].c_str());
      axisTitle_ = Form("mean of %s-residuals (rDir%s);modules", vartype.c_str(), sign[i].c_str());
    } else {
      name_ = Form("DMR%s_%s_zDir%s", subdet.c_str(), vartype.c_str(), sign_name[i].c_str());
      title_ = Form("Split DMR of %s-%s (zDir%s)", subdet.c_str(), vartype.c_str(), sign[i].c_str());
      axisTitle_ = Form("mean of %s-residuals (zDir%s);modules", vartype.c_str(), sign[i].c_str());
    }

    out[i] = dir.make<TH1D>(name_, fmt::sprintf("%s;%s", title_, axisTitle_).c_str(), 100., -200, 200);
  }
  return out;
}

//*************************************************************
// Fill the histograms using the running::estimatorMap
//**************************************************************
void DMRChecker::fillDMRs(const running::estimatorMap& myDetails, TH1D* DMR, TH1D* DRnR, std::array<TH1D*, 2> DMRSplit) {
  // protections
  if (!DMR) {
    edm::LogWarning("DMRChecker") << "DMR histogram not available! Skipping";
    return;
  }
  if (!DRnR) {
    edm::LogWarning("DMRChecker") << "DRnR histogram not available! Skipping";
    return;
  }
  if (!DMRSplit[0] || !DMRSplit[1]) {
    edm::LogWarning("DMRChecker") << "Splot DMRs histograms not available! Skipping";
    return;
  }

  for (const auto& element : myDetails) {
    // DMR
    DMR->Fill(element.second.runningMeanOfRes_);

    // split DMR
    if (element.second.rOrZDirection > 0) {
      DMRSplit[0]->Fill(element.second.runningMeanOfRes_);
    } else {
      DMRSplit[1]->Fill(element.second.runningMeanOfRes_);
    }

    // DRnR
    if (element.second.hitCount < 2) {
      DRnR->Fill(-1);
    } else {
      DRnR->Fill(sqrt(element.second.runningNormVarOfRes_ / (element.second.hitCount - 1)));
    }
  }
}

//define this as a plug-in
DEFINE_FWK_MODULE(DMRChecker);
