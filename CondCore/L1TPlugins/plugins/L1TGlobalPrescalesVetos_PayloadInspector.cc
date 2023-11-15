/*!
  \file L1TGlobalPrescalesVetos_PayloadInspector
  \Payload Inspector Plugin for L1TGlobalPrescalesVetos payloads
  \author M. Musich
  \version $Revision: 1.0 $
  \date $Date: 2023/11/15 14:49:00 $
*/

#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "CondCore/Utilities/interface/PayloadInspectorModule.h"
#include "CondCore/Utilities/interface/PayloadInspector.h"
#include "CondCore/CondDB/interface/Time.h"

// the data format of the condition to be inspected
#include "CondFormats/L1TObjects/interface/L1TGlobalPrescalesVetos.h"

#include <memory>
#include <sstream>
#include <iostream>

// include ROOT
#include "TH2F.h"
#include "TLegend.h"
#include "TCanvas.h"
#include "TLine.h"
#include "TGraph.h"
#include "TStyle.h"
#include "TLatex.h"
#include "TPave.h"
#include "TPaveStats.h"

namespace {

  using namespace cond::payloadInspector;

  /************************************************
    test class
  *************************************************/

  class L1TGlobalPrescalesVetosTest : public Histogram1D<L1TGlobalPrescalesVetos, SINGLE_IOV> {
  public:
    L1TGlobalPrescalesVetosTest()
        : Histogram1D<L1TGlobalPrescalesVetos, SINGLE_IOV>(
              "L1TGlobalPrescalesVetos test", "L1TGlobalPrescalesVetos test", 10, 0.0, 10.0) {}

    bool fill() override {
      auto tag = PlotBase::getTag<0>();
      for (auto const& iov : tag.iovs) {
        std::shared_ptr<L1TGlobalPrescalesVetos> payload = Base::fetchPayload(std::get<1>(iov));
        if (payload.get()) {
          fillWithValue(1.);
        }  // payload
      }    // iovs
      return true;
    }  // fill
  };

  PAYLOAD_INSPECTOR_MODULE(L1TGlobalPrescalesVetos) { PAYLOAD_INSPECTOR_CLASS(L1TGlobalPrescalesVetosTest); }
}  // namespace
