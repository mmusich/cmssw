#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "CondCore/Utilities/interface/PayloadInspectorModule.h"
#include "CondCore/Utilities/interface/PayloadInspector.h"
#include "CondCore/CondDB/interface/Time.h"

// the data format of the condition to be inspected
#include "CondFormats/GBRForest/interface/GBRForest.h"

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
  class GBRForest_Test : public PlotImage<GBRForest, SINGLE_IOV> {
  public:
    GBRForest_Test() : PlotImage<GBRForest, SINGLE_IOV>("Test GBRForest") {}

    bool fill() override {
      auto tag = PlotBase::getTag<0>();
      auto iov = tag.iovs.front();
      auto tagname = tag.name;
      std::shared_ptr<GBRForest> payload = fetchPayload(std::get<1>(iov));
      if (payload.get()) {

	std::vector<float> vars = {0.,1.};
	const auto& response = payload->GetResponse(vars.data());
	std::cout << response << std::endl;
        TCanvas canvas("GBRForest", "GBRForest", 1400, 1000);
        std::string fileName(m_imageFileName);
        canvas.SaveAs(fileName.c_str());
      }  // payload
      return true;
    }  // fill
  };
}

// Register the classes as boost python plugin
PAYLOAD_INSPECTOR_MODULE(GBRForest) {
  PAYLOAD_INSPECTOR_CLASS(GBRForest_Test);
}
