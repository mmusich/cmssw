#include "CondFormats/DataRecord/interface/SiPixelGenErrorDBObjectRcd.h"
#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"
#include "HeterogeneousCore/AlpakaCore/interface/alpaka/ESProducer.h"
#include "FWCore/Framework/interface/ModuleFactory.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/Records/interface/TrackerTopologyRcd.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "HeterogeneousCore/AlpakaCore/interface/alpaka/ESProducer.h"
#include "HeterogeneousCore/AlpakaCore/interface/alpaka/EventSetup.h"
#include "HeterogeneousCore/AlpakaCore/interface/alpaka/ModuleFactory.h"
#include "HeterogeneousCore/AlpakaInterface/interface/config.h"
#include "HeterogeneousCore/AlpakaInterface/interface/memory.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "RecoLocalTracker/ClusterParameterEstimator/interface/PixelClusterParameterEstimator.h"
#include "RecoLocalTracker/Records/interface/PixelCPEFastParamsRecord.h"
#include "RecoLocalTracker/Records/interface/TkPixelCPERecord.h"
#include "RecoLocalTracker/SiPixelRecHits/interface/PixelCPEFastParamsHost.h"
#include "RecoLocalTracker/SiPixelRecHits/interface/alpaka/PixelCPEFastParamsCollection.h"

// Define the ESProducer class
namespace ALPAKA_ACCELERATOR_NAMESPACE {
  template <typename TrackerTraits>
  class PixelCPEFastParamsToTkPixelCPEESProducerT : public ESProducer {
  public:
    // Constructor
    PixelCPEFastParamsToTkPixelCPEESProducerT(const edm::ParameterSet&);
    ~PixelCPEFastParamsToTkPixelCPEESProducerT() override = default;

    // Produce method for PixelClusterParameterEstimator
    std::unique_ptr<PixelClusterParameterEstimator> produce(const TkPixelCPERecord& iRecord);
    
  private:
    // Token to consume PixelCPEFastParams from PixelCPEFastParamsRecord
    edm::ESGetToken<PixelCPEFastParams<TrackerTraits>, PixelCPEFastParamsRecord> paramsToken_;
  };

  // Implementation of the constructor
  template <typename TrackerTraits>
  PixelCPEFastParamsToTkPixelCPEESProducerT<TrackerTraits>::PixelCPEFastParamsToTkPixelCPEESProducerT(const edm::ParameterSet& iConfig) : ESProducer(iConfig) {
    // Register the product the ESProducer will provide (PixelClusterParameterEstimator)
    auto cc = setWhatProduced(this);
    
    // Initialize the token to retrieve PixelCPEFastParams from PixelCPEFastParamsRecord
    paramsToken_ = cc.consumes();
  }
  
  // Implementation of the produce method
  template <typename TrackerTraits>
  std::unique_ptr<PixelClusterParameterEstimator> PixelCPEFastParamsToTkPixelCPEESProducerT<TrackerTraits>::produce(const TkPixelCPERecord& iRecord) {
    // Retrieve the PixelCPEFastParams from the event setup
    const auto& params = iRecord.get(paramsToken_);
    
    // Create the PixelClusterParameterEstimator based on the retrieved params
    auto pixelCPE = std::make_unique<PixelClusterParameterEstimator>();
    
    // Here you could customize the pixelCPE based on the params from PixelCPEFastParams
    // For example: pixelCPE->setParams(params); (custom logic to pass params to PixelCPE)
    
    return pixelCPE;
  }


  using PixelCPEFastParamsToTkPixelCPEESProducerPhase1 = PixelCPEFastParamsToTkPixelCPEESProducerT<pixelTopology::Phase1>;
  using PixelCPEFastParamsToTkPixelCPEESProducerPhase2 = PixelCPEFastParamsToTkPixelCPEESProducerT<pixelTopology::Phase2>;
  using PixelCPEFastParamsToTkPixelCPEESProducerHIonPhase1 = PixelCPEFastParamsToTkPixelCPEESProducerT<pixelTopology::HIonPhase1>;
}
 
DEFINE_FWK_EVENTSETUP_ALPAKA_MODULE(PixelCPEFastParamsToTkPixelCPEESProducerPhase1);
DEFINE_FWK_EVENTSETUP_ALPAKA_MODULE(PixelCPEFastParamsToTkPixelCPEESProducerPhase2);
DEFINE_FWK_EVENTSETUP_ALPAKA_MODULE(PixelCPEFastParamsToTkPixelCPEESProducerHIonPhase1);


