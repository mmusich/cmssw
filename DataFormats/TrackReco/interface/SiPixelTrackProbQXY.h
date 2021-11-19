#ifndef SiPixelTrackProbQXY_H
#define SiPixelTrackProbQXY_H

#include <cstdint>
#include <vector>

namespace reco {
  /**
 * Class defining the combined charge and shape probabilities for tracks that go through the SiPixel detector 
 */
  class SiPixelTrackProbQXY {
  public:
    SiPixelTrackProbQXY() {}

    SiPixelTrackProbQXY(float probQonTrack, float probXYonTrack, float probQonTrackNoL1, float probXYonTrackNoL1)
        : probQonTrack_(probQonTrack),
          probXYonTrack_(probXYonTrack),
          probQonTrackNoL1_(probQonTrackNoL1),
          probXYonTrackNoL1_(probXYonTrackNoL1)
    //  m_rawDetId(rawDetId)
    {}

    // Return the combined charge probabilities for tracks that go through the SiPixel detector
    float probQonTrack() const { return probQonTrack_; }

    // Return the combined shape probabilities for tracks that go through the SiPixel detector
    float probXYonTrack() const { return probXYonTrack_; }

    // Return the combined charge probabilities for tracks that go through the SiPixel detector
    // This version now excludes layer 1 which was known to be noisy for 2017/2018
    float probQonTrackNoL1() const { return probQonTrack_; }

    // Return the combined shape probabilities for tracks that go through the SiPixel detector
    // This version now excludes layer 1 which was known to be noisy for 2017/2018
    float probXYonTrackNoL1() const { return probXYonTrackNoL1_; }

    //  uint32_t rawDetId() const {
    //      return m_rawDetId;
    //  }

  private:
    float probQonTrack_;
    float probXYonTrack_;
    float probQonTrackNoL1_;
    float probXYonTrackNoL1_;
    //    uint32_t m_rawDetId;
  };

  typedef std::vector<SiPixelTrackProbQXY> SiPixelTrackProbQXYCollection;

}  // namespace reco
#endif
