#include "CondCore/BeamSpotPlugins/interface/BeamSpotPayloadInspectorHelper.h"
#include "CondCore/CondDB/interface/Time.h"
#include "CondCore/Utilities/interface/PayloadInspector.h"
#include "CondCore/Utilities/interface/PayloadInspectorModule.h"
#include "CondFormats/BeamSpotObjects/interface/BeamSpotOnlineObjects.h"

#include <TGraph.h>
#include <TGraphErrors.h>
#include <TH1F.h>
#include <TLegend.h>
#include <TLine.h>
#include <TPad.h>
#include <TStyle.h>

#include <algorithm>
#include <cmath>
#include <limits>
#include <map>

namespace {

  using namespace beamSpotPI;

  /************************************************
    history plots
  *************************************************/
  typedef BeamSpot_history<X, BeamSpotOnlineObjects> BeamSpotOnline_HistoryX;
  typedef BeamSpot_history<Y, BeamSpotOnlineObjects> BeamSpotOnline_HistoryY;
  typedef BeamSpot_history<Z, BeamSpotOnlineObjects> BeamSpotOnline_HistoryZ;
  typedef BeamSpot_history<sigmaX, BeamSpotOnlineObjects> BeamSpotOnline_HistorySigmaX;
  typedef BeamSpot_history<sigmaY, BeamSpotOnlineObjects> BeamSpotOnline_HistorySigmaY;
  typedef BeamSpot_history<sigmaZ, BeamSpotOnlineObjects> BeamSpotOnline_HistorySigmaZ;
  typedef BeamSpot_history<dxdz, BeamSpotOnlineObjects> BeamSpotOnline_HistorydXdZ;
  typedef BeamSpot_history<dydz, BeamSpotOnlineObjects> BeamSpotOnline_HistorydYdZ;

  /************************************************
    run history plots
  *************************************************/

  typedef BeamSpot_runhistory<X, BeamSpotOnlineObjects> BeamSpotOnline_RunHistoryX;
  typedef BeamSpot_runhistory<Y, BeamSpotOnlineObjects> BeamSpotOnline_RunHistoryY;
  typedef BeamSpot_runhistory<Z, BeamSpotOnlineObjects> BeamSpotOnline_RunHistoryZ;
  typedef BeamSpot_runhistory<sigmaX, BeamSpotOnlineObjects> BeamSpotOnline_RunHistorySigmaX;
  typedef BeamSpot_runhistory<sigmaY, BeamSpotOnlineObjects> BeamSpotOnline_RunHistorySigmaY;
  typedef BeamSpot_runhistory<sigmaZ, BeamSpotOnlineObjects> BeamSpotOnline_RunHistorySigmaZ;
  typedef BeamSpot_runhistory<dxdz, BeamSpotOnlineObjects> BeamSpotOnline_RunHistorydXdZ;
  typedef BeamSpot_runhistory<dydz, BeamSpotOnlineObjects> BeamSpotOnline_RunHistorydYdZ;

  /************************************************
    time history plots
  *************************************************/

  typedef BeamSpot_timehistory<X, BeamSpotOnlineObjects> BeamSpotOnline_TimeHistoryX;
  typedef BeamSpot_timehistory<Y, BeamSpotOnlineObjects> BeamSpotOnline_TimeHistoryY;
  typedef BeamSpot_timehistory<Z, BeamSpotOnlineObjects> BeamSpotOnline_TimeHistoryZ;
  typedef BeamSpot_timehistory<sigmaX, BeamSpotOnlineObjects> BeamSpotOnline_TimeHistorySigmaX;
  typedef BeamSpot_timehistory<sigmaY, BeamSpotOnlineObjects> BeamSpotOnline_TimeHistorySigmaY;
  typedef BeamSpot_timehistory<sigmaZ, BeamSpotOnlineObjects> BeamSpotOnline_TimeHistorySigmaZ;
  typedef BeamSpot_timehistory<dxdz, BeamSpotOnlineObjects> BeamSpotOnline_TimeHistorydXdZ;
  typedef BeamSpot_timehistory<dydz, BeamSpotOnlineObjects> BeamSpotOnline_TimeHistorydYdZ;

  /************************************************
    X-Y correlation plot
  *************************************************/

  typedef xyCorrelation<BeamSpotOnlineObjects> BeamSpotOnline_xy;

  /************************************************
    Display of Beam Spot parameters
  *************************************************/

  class BeamSpotOnlineParameters : public DisplayParameters<BeamSpotOnlineObjects> {
  public:
    std::shared_ptr<TH2F> fillTheExtraHistogram() const override {
      gStyle->SetHistMinimumZero();

      const auto span = parameters::startTime - parameters::lastLumi;
      edm::LogInfo("BeamSpotOnlineParameters") << "the span is" << span;

      auto h2_ExtraBSParameters =
          std::make_shared<TH2F>("ExtraParameters", "", 1, 0.0, 1.0, span, 0, static_cast<float>(span));
      h2_ExtraBSParameters->SetStats(false);

      //_____________________________________________________________________________
      std::function<int(parameters)> myIntFunctor = [this](parameters my_param) {
        int ret(-999);
        switch (my_param) {
          case lastLumi:
            return this->m_payload->lastAnalyzedLumi();
          case lastRun:
            return this->m_payload->lastAnalyzedRun();
          case lastFill:
            return this->m_payload->lastAnalyzedFill();
          case nTracks:
            return this->m_payload->numTracks();
          case nPVs:
            return this->m_payload->numPVs();
          case nUsedEvents:
            return this->m_payload->usedEvents();
          case maxPVs:
            return this->m_payload->maxPVs();
          default:
            return ret;
        }
      };

      //_____________________________________________________________________________
      std::function<float(parameters)> myFloatFunctor = [this](parameters my_param) {
        float ret(-999.);
        switch (my_param) {
          case meanPV:
            return this->m_payload->meanPV();
          case meanErrorPV:
            return this->m_payload->meanErrorPV();
          case rmsPV:
            return this->m_payload->rmsPV();
          case rmsErrorPV:
            return this->m_payload->rmsErrorPV();
          default:
            return ret;
        }
      };

      //_____________________________________________________________________________
      std::function<std::string(parameters)> myStringFunctor = [this](parameters my_param) {
        std::string ret("");
        switch (my_param) {
          case startTime:
            return this->m_payload->startTime();
          case endTime:
            return this->m_payload->endTime();
          case lumiRange:
            return this->m_payload->lumiRange();
          default:
            return ret;
        }
      };

      //_____________________________________________________________________________
      std::function<cond::Time_t(parameters)> myTimeFunctor = [this](parameters my_param) {
        cond::Time_t ret(1);
        switch (my_param) {
          case creationTime:
            return this->m_payload->creationTime();
          case startTimeStamp:
            return this->m_payload->startTimeStamp();
          case endTimeStamp:
            return this->m_payload->endTimeStamp();
          default:
            return ret;
        }
      };

      unsigned int yBin = span;
      for (int foo = parameters::lastLumi; foo != parameters::startTime; foo++) {
        parameters param = static_cast<parameters>(foo);
        std::string theLabel = this->getStringFromTypeEnum(param);
        h2_ExtraBSParameters->GetYaxis()->SetBinLabel(yBin, theLabel.c_str());

        if (foo <= parameters::maxPVs) {
          const auto output = try_<int, std::out_of_range>(std::bind(myIntFunctor, param), print_error);
          edm::LogInfo("BeamSpotOnline_PayloadInspector") << theLabel.c_str() << " : " << output << std::endl;
          h2_ExtraBSParameters->SetBinContent(1, yBin, output);
        } else if (foo <= parameters::rmsErrorPV) {
          const auto output = try_<float, std::out_of_range>(std::bind(myFloatFunctor, param), print_error);
          edm::LogInfo("BeamSpotOnline_PayloadInspector") << theLabel.c_str() << " : " << output << std::endl;
          h2_ExtraBSParameters->SetBinContent(1, yBin, output);
        } else if (foo <= parameters::endTimeStamp) {
          const auto output = try_<cond::Time_t, std::out_of_range>(std::bind(myTimeFunctor, param), print_error);
          edm::LogInfo("BeamSpotOnline_PayloadInspector") << theLabel.c_str() << " : " << output << std::endl;
          h2_ExtraBSParameters->SetBinContent(1, yBin, output);
          //} else if( foo <=parameters::lumiRange){
          // const auto output = try_<std::string,std::out_of_range>(std::bind(myStringFunctor, param), print_error);
          //edm::LogInfo("BeamSpotOnline_PayloadInspector") << theLabel.c_str() << " : " << output << std::endl;
          //h2_ExtraBSParameters->SetBinContent(1, yBin, output);
        }
        yBin--;
      }

      h2_ExtraBSParameters->GetYaxis()->SetLabelSize(0.05);
      h2_ExtraBSParameters->GetXaxis()->SetLabelSize(0.05);
      h2_ExtraBSParameters->GetXaxis()->SetBinLabel(1, "Value");
      h2_ExtraBSParameters->SetMarkerSize(2.);

      return h2_ExtraBSParameters;
    }

  protected:
    /************************************************/
    std::string getStringFromTypeEnum(const parameters& parameter) const override {
      switch (parameter) {
        case X:
          return "X [cm]";
        case Y:
          return "Y [cm]";
        case Z:
          return "Z [cm]";
        case sigmaX:
          return "#sigma_{X} [cm]";
        case sigmaY:
          return "#sigma_{Y} [cm]";
        case sigmaZ:
          return "#sigma_{Z} [cm]";
        case dxdz:
          return "#frac{dX}{dZ} [rad]";
        case dydz:
          return "#frac{dY}{dZ} [rad]";
        case lastLumi:
          return "last LS";
        case lastRun:
          return "last Run";
        case lastFill:
          return "last Fill";
        case nTracks:
          return "# tracks";
        case nPVs:
          return "# PVs";
        case nUsedEvents:
          return "# events";
        case maxPVs:
          return "max PVs";
        case meanPV:
          return "#LT # PV #GT";
        case meanErrorPV:
          return "#LT # PV #GT error";
        case rmsPV:
          return "RMS(# PV)";
        case rmsErrorPV:
          return "RMS(# PV) error";
        case creationTime:
          return "creation time";
        case startTimeStamp:
          return "start timestamp";
        case endTimeStamp:
          return "end timestamp";
        case startTime:
          return "startTime";
        case endTime:
          return "endTime";
        case lumiRange:
          return "lumiRange";
        default:
          return "should never be here";
      }
    }

    //slightly better error handler
    static void print_error(const std::exception& e) { edm::LogError("BeamSpotOnlineParameters") << e.what() << '\n'; }

    // method to catch exceptions
    template <typename T, class Except, class Func, class Response>
    T try_(Func f, Response r) const {
      try {
        LogDebug("BeamSpotOnlineParameters") << "I have tried" << std::endl;
        return f();
      } catch (Except& e) {
        LogDebug("BeamSpotOnlineParameters") << "I have caught!" << std::endl;
        r(e);
        return static_cast<T>(-999);
      }
    }
  };

  /************************************************
    Display of Beam Spot parameters Differences
  *************************************************/

  typedef DisplayParametersDiff<BeamSpotOnlineObjects, cond::payloadInspector::MULTI_IOV, 1>
      BeamSpotOnlineParametersDiffSingleTag;
  typedef DisplayParametersDiff<BeamSpotOnlineObjects, cond::payloadInspector::SINGLE_IOV, 2>
      BeamSpotOnlineParametersDiffTwoTags;

  /************************************************
    Comparison of two (lumi-based) tags over an IOV range,
    e.g. BeamSpotOnlineHLT_NGT vs BeamSpotOnlineHLT.
    The IOV boundaries of the two tags are merged: at each boundary
    the payload valid in each tag is used, so that the two tags are
    compared lumi-section by lumi-section even if they were updated
    at different times. Top pad: overlay; bottom pad: A - B.
  *************************************************/

  template <parameters my_param>
  class BeamSpotOnline_TwoTagsComparison
      : public cond::payloadInspector::PlotImage<BeamSpotOnlineObjects, cond::payloadInspector::MULTI_IOV, 2> {
  public:
    typedef cond::payloadInspector::PlotImage<BeamSpotOnlineObjects, cond::payloadInspector::MULTI_IOV, 2> Base;
    typedef std::vector<std::tuple<cond::Time_t, cond::Hash> > IOVs;

    BeamSpotOnline_TwoTagsComparison()
        : Base("BeamSpotOnline " + getStringFromParamEnum(my_param) + " comparison of two tags") {}

    bool fill() override {
      auto tagA = cond::payloadInspector::PlotBase::getTag<0>();
      auto tagB = cond::payloadInspector::PlotBase::getTag<1>();
      const IOVs& iovsA = tagA.iovs;
      const IOVs& iovsB = tagB.iovs;

      if (iovsA.empty() || iovsB.empty()) {
        edm::LogError("BeamSpotOnline_TwoTagsComparison")
            << "no IOVs found in the requested range for tag " << (iovsA.empty() ? tagA.name : tagB.name);
        return false;
      }

      // the range selection also returns the IOV valid at the start of the range,
      // whose since can lie before it: clamp to the requested start
      const cond::Time_t rangeStart = std::max(tagA.boundary.first, tagB.boundary.first);
      const cond::Time_t rangeEnd = std::min(tagA.boundary.second, tagB.boundary.second);

      const auto valuesA = getValues(iovsA);
      const auto valuesB = getValues(iovsB);

      // union of the IOV boundaries of the two tags
      std::vector<cond::Time_t> sinces;
      sinces.reserve(iovsA.size() + iovsB.size());
      for (const auto* iovs : {&iovsA, &iovsB}) {
        for (const auto& iov : *iovs) {
          const auto since = std::max(std::get<0>(iov), rangeStart);
          if (since <= rangeEnd)
            sinces.push_back(since);
        }
      }
      std::sort(sinces.begin(), sinces.end());
      sinces.erase(std::unique(sinces.begin(), sinces.end()), sinces.end());

      if (sinces.empty()) {
        edm::LogError("BeamSpotOnline_TwoTagsComparison") << "no common IOV boundaries in the requested range";
        return false;
      }

      const double scale = unitScale();
      const int nPoints = sinces.size();
      auto gA = std::make_unique<TGraphErrors>();
      auto gB = std::make_unique<TGraphErrors>();
      auto gDiff = std::make_unique<TGraph>();

      double yMin = std::numeric_limits<double>::max(), yMax = std::numeric_limits<double>::lowest();
      double dMin = std::numeric_limits<double>::max(), dMax = std::numeric_limits<double>::lowest();
      double sumDiff(0.), sumDiff2(0.);

      // run boundaries (index in the union, run number) for the axis labels
      std::vector<std::pair<int, unsigned int> > runStarts;

      for (int i = 0; i < nPoints; i++) {
        const auto since = sinces[i];
        const unsigned int run = unpack(since).first;
        if (runStarts.empty() || runStarts.back().second != run)
          runStarts.emplace_back(i, run);

        const double x = i + 0.5;
        const int iA = validIndex(iovsA, since);
        const int iB = validIndex(iovsB, since);

        if (iA >= 0) {
          const auto& [val, err] = valuesA[iA];
          gA->AddPoint(x, val * scale);
          gA->SetPointError(gA->GetN() - 1, 0., err * scale);
          yMin = std::min(yMin, val * scale), yMax = std::max(yMax, val * scale);
        }
        if (iB >= 0) {
          const auto& [val, err] = valuesB[iB];
          gB->AddPoint(x, val * scale);
          gB->SetPointError(gB->GetN() - 1, 0., err * scale);
          yMin = std::min(yMin, val * scale), yMax = std::max(yMax, val * scale);
        }
        if (iA >= 0 && iB >= 0) {
          const double diff = (valuesA[iA].first - valuesB[iB].first) * scale;
          gDiff->AddPoint(x, diff);
          dMin = std::min(dMin, diff), dMax = std::max(dMax, diff);
          sumDiff += diff, sumDiff2 += diff * diff;
        }
      }

      if (gA->GetN() == 0 || gB->GetN() == 0) {
        edm::LogError("BeamSpotOnline_TwoTagsComparison") << "no valid payloads in the requested range";
        return false;
      }

      gStyle->SetOptStat(0);
      TCanvas canvas("BeamSpotOnline comparison", "BeamSpotOnline comparison", 2000, 1000);

      TPad padTop("padTop", "", 0., 0.3, 1., 1.);
      padTop.SetTopMargin(0.08);
      padTop.SetBottomMargin(0.02);
      padTop.SetLeftMargin(0.08);
      padTop.SetRightMargin(0.02);
      padTop.SetGridy();
      padTop.Draw();

      TPad padBottom("padBottom", "", 0., 0., 1., 0.3);
      padBottom.SetTopMargin(0.02);
      padBottom.SetBottomMargin(0.30);
      padBottom.SetLeftMargin(0.08);
      padBottom.SetRightMargin(0.02);
      padBottom.SetGridy();
      padBottom.Draw();

      // frames, x-axis labelled with the run number at the run boundaries
      const std::string yTitle = getStringFromParamEnum(my_param) + " " + unitLabel();
      TH1F hFrameTop("hFrameTop", "", nPoints, 0., nPoints);
      TH1F hFrameBottom("hFrameBottom", "", nPoints, 0., nPoints);

      constexpr unsigned int kMaxLabels = 40;
      const unsigned int labelEvery = std::max<std::size_t>(1, (runStarts.size() + kMaxLabels - 1) / kMaxLabels);
      for (unsigned int r = 0; r < runStarts.size(); r += labelEvery) {
        hFrameBottom.GetXaxis()->SetBinLabel(runStarts[r].first + 1, std::to_string(runStarts[r].second).c_str());
      }

      const double yPad = (yMax > yMin) ? 0.1 * (yMax - yMin) : 0.1 * std::abs(yMax) + 1e-6;
      const double yLow = yMin - yPad, yHigh = yMax + 0.35 * (yMax - yMin + yPad);  // room for the legend
      hFrameTop.SetMinimum(yLow);
      hFrameTop.SetMaximum(yHigh);
      hFrameTop.GetYaxis()->SetTitle(yTitle.c_str());
      hFrameTop.GetYaxis()->SetTitleSize(0.05);
      hFrameTop.GetYaxis()->SetTitleOffset(0.75);
      hFrameTop.GetYaxis()->SetLabelSize(0.04);
      hFrameTop.GetYaxis()->SetTickLength(0.01);
      hFrameTop.GetXaxis()->SetLabelSize(0.);
      hFrameTop.GetXaxis()->SetTickLength(0.);

      const double dPad = (dMax > dMin) ? 0.1 * (dMax - dMin) : 0.1 * std::abs(dMax) + 1e-6;
      hFrameBottom.SetMinimum(dMin - dPad);
      hFrameBottom.SetMaximum(dMax + dPad);
      hFrameBottom.GetYaxis()->SetTitle(("#Delta " + unitLabel() + " (A - B)").c_str());
      hFrameBottom.GetYaxis()->SetTitleSize(0.10);
      hFrameBottom.GetYaxis()->SetTitleOffset(0.37);
      hFrameBottom.GetYaxis()->SetLabelSize(0.08);
      hFrameBottom.GetYaxis()->SetNdivisions(505);
      hFrameBottom.GetYaxis()->SetTickLength(0.01);
      hFrameBottom.GetXaxis()->SetTitle("run number");
      hFrameBottom.GetXaxis()->SetTitleSize(0.10);
      hFrameBottom.GetXaxis()->SetTitleOffset(1.35);
      hFrameBottom.GetXaxis()->SetLabelSize(0.07);
      hFrameBottom.GetXaxis()->LabelsOption("v");
      hFrameBottom.GetXaxis()->SetTickLength(0.);

      gA->SetMarkerStyle(20);
      gA->SetMarkerSize(0.5);
      gA->SetMarkerColor(kBlue);
      gA->SetLineColor(kBlue);
      gB->SetMarkerStyle(24);
      gB->SetMarkerSize(0.5);
      gB->SetMarkerColor(kRed);
      gB->SetLineColor(kRed);
      gDiff->SetMarkerStyle(20);
      gDiff->SetMarkerSize(0.5);
      gDiff->SetMarkerColor(kBlack);

      // light vertical lines at the labelled run boundaries
      std::vector<std::unique_ptr<TLine> > lines;
      auto drawRunLines = [&](double ymin, double ymax) {
        for (unsigned int r = 0; r < runStarts.size(); r += labelEvery) {
          auto& line = lines.emplace_back(std::make_unique<TLine>(runStarts[r].first, ymin, runStarts[r].first, ymax));
          line->SetLineColor(kGray);
          line->SetLineStyle(kDotted);
          line->Draw();
        }
      };

      padTop.cd();
      hFrameTop.Draw("AXIS");
      drawRunLines(yLow, yHigh);
      gB->Draw("P SAME");
      gA->Draw("P SAME");

      TLegend legend(0.10, 0.76, 0.55, 0.90);
      legend.SetBorderSize(0);
      legend.SetFillStyle(0);
      legend.SetTextSize(0.04);
      legend.AddEntry(gA.get(), ("A: " + tagA.name).c_str(), "PE");
      legend.AddEntry(gB.get(), ("B: " + tagB.name).c_str(), "PE");
      legend.Draw();

      const auto firstRunLS = unpack(sinces.front());
      const auto lastRunLS = unpack(sinces.back());
      TLatex ltx;
      ltx.SetNDC();
      ltx.SetTextFont(62);
      ltx.SetTextSize(0.045);
      ltx.SetTextAlign(11);
      ltx.DrawLatex(padTop.GetLeftMargin(),
                    1 - padTop.GetTopMargin() + 0.02,
                    fmt::sprintf("BeamSpot %s, runs %u (LS %u) - %u (LS %u), %d IOV boundaries",
                                 getStringFromParamEnum(my_param),
                                 firstRunLS.first,
                                 firstRunLS.second,
                                 lastRunLS.first,
                                 lastRunLS.second,
                                 nPoints)
                        .c_str());

      padBottom.cd();
      hFrameBottom.Draw("AXIS");
      drawRunLines(dMin - dPad, dMax + dPad);
      TLine zero(0., 0., nPoints, 0.);
      zero.SetLineColor(kRed);
      zero.SetLineStyle(kDashed);
      zero.Draw();
      gDiff->Draw("P SAME");

      const int nDiff = gDiff->GetN();
      const double meanDiff = sumDiff / nDiff;
      const double rmsDiff = std::sqrt(std::max(0., sumDiff2 / nDiff - meanDiff * meanDiff));
      TLatex ltxDiff;
      ltxDiff.SetNDC();
      ltxDiff.SetTextFont(42);
      ltxDiff.SetTextSize(0.09);
      ltxDiff.SetTextAlign(13);
      ltxDiff.DrawLatex(
          padBottom.GetLeftMargin() + 0.01,
          1 - padBottom.GetTopMargin() - 0.04,
          fmt::sprintf("#LT#Delta#GT = %.3g %s, RMS = %.3g %s", meanDiff, unitLabel(), rmsDiff, unitLabel()).c_str());

      std::string fileName(this->m_imageFileName);
      canvas.SaveAs(fileName.c_str());

      return true;
    }

  private:
    // (value, error) of the plotted parameter for each IOV, payloads cached by hash
    std::vector<std::pair<double, double> > getValues(const IOVs& iovs) {
      std::vector<std::pair<double, double> > ret;
      ret.reserve(iovs.size());
      for (const auto& iov : iovs) {
        const auto& hash = std::get<1>(iov);
        auto it = m_cache.find(hash);
        if (it == m_cache.end()) {
          auto payload = this->fetchPayload(hash);
          it = m_cache.emplace(hash, getFromPayload(*payload)).first;
        }
        ret.push_back(it->second);
      }
      return ret;
    }

    std::pair<double, double> getFromPayload(const BeamSpotOnlineObjects& payload) const {
      switch (my_param) {
        case X:
          return std::make_pair(payload.x(), payload.xError());
        case Y:
          return std::make_pair(payload.y(), payload.yError());
        case Z:
          return std::make_pair(payload.z(), payload.zError());
        case sigmaX:
          return std::make_pair(payload.beamWidthX(), payload.beamWidthXError());
        case sigmaY:
          return std::make_pair(payload.beamWidthY(), payload.beamWidthYError());
        case sigmaZ:
          return std::make_pair(payload.sigmaZ(), payload.sigmaZError());
        case dxdz:
          return std::make_pair(payload.dxdz(), payload.dxdzError());
        case dydz:
          return std::make_pair(payload.dydz(), payload.dydzError());
        default:
          return std::make_pair(-9999., -9999.);
      }
    }

    // index of the IOV valid at a given time, -1 if none (iovs are sorted by since)
    static int validIndex(const IOVs& iovs, cond::Time_t time) {
      auto it = std::upper_bound(
          iovs.begin(), iovs.end(), time, [](cond::Time_t t, const auto& iov) { return t < std::get<0>(iov); });
      return (it == iovs.begin()) ? -1 : static_cast<int>(std::distance(iovs.begin(), it)) - 1;
    }

    // transverse positions and widths in um, slopes in urad, longitudinal quantities in cm
    static double unitScale() {
      switch (my_param) {
        case X:
        case Y:
        case sigmaX:
        case sigmaY:
          return 1.e4;
        case dxdz:
        case dydz:
          return 1.e6;
        default:
          return 1.;
      }
    }

    static std::string unitLabel() {
      switch (my_param) {
        case X:
        case Y:
        case sigmaX:
        case sigmaY:
          return "[#mum]";
        case dxdz:
        case dydz:
          return "[#murad]";
        default:
          return "[cm]";
      }
    }

    std::map<cond::Hash, std::pair<double, double> > m_cache;
  };

  typedef BeamSpotOnline_TwoTagsComparison<X> BeamSpotOnline_TwoTagsComparisonX;
  typedef BeamSpotOnline_TwoTagsComparison<Y> BeamSpotOnline_TwoTagsComparisonY;
  typedef BeamSpotOnline_TwoTagsComparison<Z> BeamSpotOnline_TwoTagsComparisonZ;
  typedef BeamSpotOnline_TwoTagsComparison<sigmaX> BeamSpotOnline_TwoTagsComparisonSigmaX;
  typedef BeamSpotOnline_TwoTagsComparison<sigmaY> BeamSpotOnline_TwoTagsComparisonSigmaY;
  typedef BeamSpotOnline_TwoTagsComparison<sigmaZ> BeamSpotOnline_TwoTagsComparisonSigmaZ;
  typedef BeamSpotOnline_TwoTagsComparison<dxdz> BeamSpotOnline_TwoTagsComparisondXdZ;
  typedef BeamSpotOnline_TwoTagsComparison<dydz> BeamSpotOnline_TwoTagsComparisondYdZ;

}  // namespace

PAYLOAD_INSPECTOR_MODULE(BeamSpotOnline) {
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_xy);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnlineParameters);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnlineParametersDiffSingleTag);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnlineParametersDiffTwoTags);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_HistoryX);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_HistoryY);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_HistoryZ);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_HistorySigmaX);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_HistorySigmaY);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_HistorySigmaZ);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_HistorydXdZ);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_HistorydYdZ);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_RunHistoryX);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_RunHistoryY);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_RunHistoryZ);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_RunHistorySigmaX);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_RunHistorySigmaY);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_RunHistorySigmaZ);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_RunHistorydXdZ);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_RunHistorydYdZ);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_TimeHistoryX);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_TimeHistoryY);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_TimeHistoryZ);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_TimeHistorySigmaX);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_TimeHistorySigmaY);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_TimeHistorySigmaZ);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_TimeHistorydXdZ);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_TimeHistorydYdZ);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_TwoTagsComparisonX);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_TwoTagsComparisonY);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_TwoTagsComparisonZ);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_TwoTagsComparisonSigmaX);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_TwoTagsComparisonSigmaY);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_TwoTagsComparisonSigmaZ);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_TwoTagsComparisondXdZ);
  PAYLOAD_INSPECTOR_CLASS(BeamSpotOnline_TwoTagsComparisondYdZ);
}
