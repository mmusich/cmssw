#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "CondCore/Utilities/interface/PayloadInspectorModule.h"
#include "CondCore/Utilities/interface/PayloadInspector.h"
#include "CondCore/CondDB/interface/Time.h"

// the data format of the condition to be inspected
#include "CondFormats/PhysicsToolsObjects/interface/DeDxCalibration.h"

#include <memory>
#include <sstream>
#include <fstream>
#include <iostream>
#include <array>
#include <map>

// include ROOT
#include "TH2F.h"
#include "TF1.h"
#include "TLegend.h"
#include "TCanvas.h"
#include "TLine.h"
#include "TStyle.h"
#include "TLatex.h"
#include "TPave.h"
#include "TPaveStats.h"

namespace {

  using namespace cond::payloadInspector;

  /************************************************
     DeDxCalibration Payload Inspector of 1 IOV 
  *************************************************/
  class DeDxCalibrationTest : public Histogram1D<DeDxCalibration, SINGLE_IOV> {
  public:
    DeDxCalibrationTest()
        : Histogram1D<DeDxCalibration, SINGLE_IOV>("Test DeDxCalibration", "Test DeDxCalibration", 1, 0.0, 1.0) {}

    bool fill() override {
      auto tag = PlotBase::getTag<0>();
      for (auto const& iov : tag.iovs) {
        std::shared_ptr<DeDxCalibration> payload = Base::fetchPayload(std::get<1>(iov));
        if (payload.get()) {
          const auto& thresholds = payload->thr();
          const auto& alphas = payload->alpha();
          const auto& sigmas = payload->sigma();

          assert(thresholds.size() == alphas.size());
          assert(alphas.size() == sigmas.size());

          for (unsigned int i = 0; i < thresholds.size(); i++) {
            std::cout << "threshold:" << thresholds[i] << " alpha: " << alphas[i] << " sigma: " << sigmas[i]
                      << std::endl;
          }
        }
      }
      return true;
    }
  };

  // Inspector to show the values of thresholds, alphas, sigmas, and gains in DeDxCalibration
  class DeDxCalibrationInspector : public PlotImage<DeDxCalibration> {
  public:
    DeDxCalibrationInspector() : PlotImage<DeDxCalibration>("DeDxCalibration Inspector") {}

    bool fill(const std::vector<std::tuple<cond::Time_t, cond::Hash>>& iovs) override {
      auto tag = std::get<1>(iovs.front());
      std::shared_ptr<DeDxCalibration> payload = fetchPayload(tag);

      if (payload.get()) {
        const std::vector<double>& thr = payload->thr();
        const std::vector<double>& alpha = payload->alpha();
        const std::vector<double>& sigma = payload->sigma();

        // Ensure that thr, alpha, sigma have the same size
        assert(thr.size() == alpha.size());
        assert(alpha.size() == sigma.size());

        // Create a 2D histogram
        int nBinsX = 3;           // For thr, alpha, sigma, gain
        int nBinsY = thr.size();  // Number of elements in the vectors

        TH2D h2("h2", "DeDxCalibration Values;Variable Type;Value", nBinsX, 0, nBinsX, nBinsY, 0, nBinsY);

        // Label the x-axis with the variable names
        h2.GetXaxis()->SetBinLabel(1, "Threshold");
        h2.GetXaxis()->SetBinLabel(2, "Alpha");
        h2.GetXaxis()->SetBinLabel(3, "Sigma");

        // Fill the histogram
        for (size_t i = 0; i < thr.size(); ++i) {
          h2.Fill(0.5, i, thr[i]);
          h2.Fill(1.5, i, alpha[i]);
          h2.Fill(2.5, i, sigma[i]);
        }

        // Draw the histogram on a canvas
        TCanvas canvas("Canvas", "DeDxCalibration Values", 1200, 800);
        canvas.cd();
        h2.Draw("COLZ TEXT");

        std::string fileName(m_imageFileName);
        canvas.SaveAs(fileName.c_str());

        return true;
      } else {
        return false;
      }
    }
  };
}  // namespace

// Register the classes as boost python plugin
PAYLOAD_INSPECTOR_MODULE(DeDxCalibration) {
  PAYLOAD_INSPECTOR_CLASS(DeDxCalibrationTest);
  PAYLOAD_INSPECTOR_CLASS(DeDxCalibrationInspector);
}
