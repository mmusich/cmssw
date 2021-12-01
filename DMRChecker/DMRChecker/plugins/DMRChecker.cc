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

// user include files
#include "Alignment/OfflineValidation/interface/TrackerValidationVariables.h"
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
    }
  };

  using estimatorMap = std::map<uint32_t, running::Estimators>;
}  // namespace running

//
// class declaration
//

using reco::TrackCollection;
class DMRChecker : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit DMRChecker(const edm::ParameterSet&);
  ~DMRChecker() override;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void updateOnlineMomenta(running::estimatorMap& myDetails,
                           const uint32_t& theID,
                           const float& the_data,
                           const float& the_pull,
                           const running::dir& theDir);

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
  TrackerValidationVariables avalidator_;
  bool applyVertexCut_;

  const edm::EDGetTokenT<reco::VertexCollection> offlinePrimaryVerticesToken_;

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
};

//
// constructors and destructor
//
DMRChecker::DMRChecker(const edm::ParameterSet& iConfig)
    : avalidator_(iConfig, consumesCollector()),
      offlinePrimaryVerticesToken_(
          consumes<reco::VertexCollection>(iConfig.getParameter<std::string>("VertexCollection"))) {
  applyVertexCut_ = iConfig.getUntrackedParameter<bool>("VertexCut", true);
}

DMRChecker::~DMRChecker() = default;

//
// member functions
//
// ------------ method called for each event  ------------
void DMRChecker::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;

  edm::Handle<reco::VertexCollection> vertices;
  if (applyVertexCut_) {
    iEvent.getByToken(offlinePrimaryVerticesToken_, vertices);
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
          this->updateOnlineMomenta(resDetailsBPixX_, id, resX, pullX, running::X);
          this->updateOnlineMomenta(resDetailsBPixY_, id, resY, pullY, running::Y);
        } else if (subid == PixelSubdetector::PixelEndcap) {
          this->updateOnlineMomenta(resDetailsFPixX_, id, resX, pullX, running::X);
          this->updateOnlineMomenta(resDetailsFPixY_, id, resY, pullY, running::Y);
        }     // if FPix
      }       // if Pixel
      else {  // these are Strips
        if (subid == StripSubdetector::TIB) {
          this->updateOnlineMomenta(resDetailsTIB_, id, resX, pullX, running::X);
        } else if (subid == StripSubdetector::TOB) {
          this->updateOnlineMomenta(resDetailsTOB_, id, resX, pullX, running::X);
        } else if (subid == StripSubdetector::TID) {
          this->updateOnlineMomenta(resDetailsTID_, id, resX, pullX, running::X);
        } else if (subid == StripSubdetector::TEC) {
          this->updateOnlineMomenta(resDetailsTEC_, id, resX, pullX, running::X);
        }
      }
    }  // loop on hits
  }    // loop on tracks
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

//*************************************************************
// Implementation of the online variance algorithm
// as in https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Online_algorithm
//*************************************************************
void DMRChecker::updateOnlineMomenta(running::estimatorMap& myDetails,
                                     const uint32_t& theID,
                                     const float& the_data,
                                     const float& the_pull,
                                     const running::dir& theDir) {
  // if the detid has never occcurred yet, set the local orientations
  if (myDetails.find(theID) == myDetails.end()) {
    if (theDir == running::X)
      myDetails[theID].isX = true;
    if (theDir == running::Y)
      myDetails[theID].isY = false;
  }

  myDetails[theID].hitCount += 1;

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

//define this as a plug-in
DEFINE_FWK_MODULE(DMRChecker);
