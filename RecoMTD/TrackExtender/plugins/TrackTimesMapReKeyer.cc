#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/TrackExtraFwd.h"

#include "DataFormats/Math/interface/deltaR.h"

namespace {
  constexpr float defaultInvalidTrackReso = 0.350f;
}

class TrackTimesMapReKeyer : public edm::global::EDProducer<> {
public:
  explicit TrackTimesMapReKeyer(const edm::ParameterSet &);
  ~TrackTimesMapReKeyer() override = default;

  static void fillDescriptions(edm::ConfigurationDescriptions &descriptions);

private:
  void produce(edm::StreamID, edm::Event &, const edm::EventSetup &) const override;

  template <class H, class T>
  void fillValueMap(edm::Event& iEvent, const H& handle, const std::vector<T>& vec, const edm::EDPutToken& token) const;

  // memeber data
  const edm::EDGetTokenT<reco::TrackCollection> inputTrack_;
  const edm::EDGetTokenT<reco::TrackCollection> originalTrack_;
  const edm::EDGetTokenT<edm::ValueMap<float>> inputTimes_;
  const edm::EDGetTokenT<edm::ValueMap<float>> inputResol_;
  const edm::EDPutToken tmTrkToken_;
  const edm::EDPutToken sigmatmTrkToken_;  
};

TrackTimesMapReKeyer::TrackTimesMapReKeyer(const edm::ParameterSet &iConfig)
    : inputTrack_(consumes(iConfig.getParameter<edm::InputTag>("src"))),
      originalTrack_(consumes(iConfig.getParameter<edm::InputTag>("originalTracks"))),
      inputTimes_(consumes(iConfig.getParameter<edm::InputTag>("times"))),
      inputResol_(consumes(iConfig.getParameter<edm::InputTag>("resolutions"))),
      tmTrkToken_(produces<edm::ValueMap<float>>("times")),
      sigmatmTrkToken_(produces<edm::ValueMap<float>>("resolutions")){}

// ------------ method called for each event  ------------
void TrackTimesMapReKeyer::produce(edm::StreamID, edm::Event &iEvent, const edm::EventSetup &iSetup) const {
  using namespace edm;

  auto const &tracks = iEvent.getHandle(inputTrack_);
  auto const &oriTracks = iEvent.getHandle(originalTrack_);
  
  auto const &times = iEvent.get(inputTimes_);
  auto const &resolutions = iEvent.get(inputResol_);

  std::vector<float> tm;
  std::vector<float> sigmatm;

  for (unsigned int i = 0; i < (*tracks).size(); i++) {

    float time{0.0};
    float timeReso{defaultInvalidTrackReso};
    
    unsigned int matchedIdx{9999};
    float dR2min{10.};
    
    for (unsigned int j = 0; j < (*oriTracks).size(); j++) {
      double dr2 = reco::deltaR2((*tracks)[i], (*oriTracks)[j]);
      if (dr2 < dR2min){
	dR2min = dr2;
	matchedIdx = j;
      }
    }

    if(matchedIdx < (*tracks).size()) {
      reco::TrackRef ref(oriTracks, matchedIdx);    
      time = times[ref];
      timeReso = resolutions[ref];
    }

    tm.push_back(time); 
    sigmatm.push_back(timeReso);        
  }

  fillValueMap(iEvent, tracks, tm, tmTrkToken_);
  fillValueMap(iEvent, tracks, sigmatm, sigmatmTrkToken_);
}

template <class H, class T>
void TrackTimesMapReKeyer::fillValueMap(edm::Event& iEvent,
					const H& handle,
					const std::vector<T>& vec,
					const edm::EDPutToken& token) const {
  auto out = std::make_unique<edm::ValueMap<T>>();
  typename edm::ValueMap<T>::Filler filler(*out);
  filler.insert(handle, vec.begin(), vec.end());
  filler.fill();
  iEvent.put(token, std::move(out));
}

void TrackTimesMapReKeyer::fillDescriptions(edm::ConfigurationDescriptions &descriptions) {
  edm::ParameterSetDescription desc;
  desc.setComment("Simple prooducer to re-key value maps of refitted tracks");
  desc.add<edm::InputTag>("src", edm::InputTag("generalTracks"))->setComment("input track collections");
  desc.add<edm::InputTag>("originalTracks", edm::InputTag("generalTracks"))->setComment("input original track collection");
  desc.add<edm::InputTag>("times", edm::InputTag(""));
  desc.add<edm::InputTag>("resolutions", edm::InputTag(""));
  descriptions.addWithDefaultLabel(desc);
}

DEFINE_FWK_MODULE(TrackTimesMapReKeyer);
