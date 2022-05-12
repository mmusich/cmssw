/*
 * \class PixelVTXMonitor
 *
 * DQM FED Client
 *
 * \author  S. Dutta
 *
*/

#ifndef PIXELVTXMONITOR_H
#define PIXELVTXMONITOR_H

#include <string>
#include <vector>
#include <map>

#include "DQMServices/Core/interface/DQMEDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DQMServices/Core/interface/DQMStore.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "DataFormats/SiPixelCluster/interface/SiPixelCluster.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/Common/interface/TriggerResults.h"

//
// class declaration
//

class PixelVTXMonitor : public DQMEDAnalyzer {
public:
  typedef dqm::legacy::MonitorElement MonitorElement;
  typedef dqm::legacy::DQMStore DQMStore;
  PixelVTXMonitor(const edm::ParameterSet &);
  ~PixelVTXMonitor() override = default;

protected:
  void bookHistograms(DQMStore::IBooker &iBooker, const edm::Run &iRun, const edm::EventSetup &iSetup) override;

private:
  void dqmBeginRun(const edm::Run &iRun, const edm::EventSetup &iSetup) override;
  void analyze(const edm::Event &iEvent, const edm::EventSetup &iSetup) override;

  edm::ParameterSet parameters_;

  std::string moduleName_;
  std::string folderName_;
  edm::EDGetTokenT<SiPixelClusterCollectionNew> pixelClusterInputTagToken_;
  edm::EDGetTokenT<reco::VertexCollection> pixelVertexInputTagToken_;
  edm::EDGetTokenT<edm::TriggerResults> hltInputTagToken_;
  edm::InputTag pixelClusterInputTag_;
  edm::InputTag pixelVertexInputTag_;
  edm::InputTag hltInputTag_;
  float minVtxDoF_;

  HLTConfigProvider hltConfig_;

  struct PixelMEs {
    MonitorElement *clusME;
    MonitorElement *vtxME;
  };

  std::map<std::string, PixelMEs> histoMap_;
};

#endif  // PIXELVTXMONITOR_H

// Local Variables:
// show-trailing-whitespace: t
// truncate-lines: t
// End:
