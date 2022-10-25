#include "TrackingTools/GsfTracking/interface/GsfMultiStateUpdator.h"
#include "TrackingTools/GsfTools/interface/GetComponents.h"
#include "TrackingTools/KalmanUpdators/interface/KFUpdator.h"
#include "TrackingTools/PatternTools/interface/MeasurementExtractor.h"
#include "TrackingTools/TransientTrackingRecHit/interface/TransientTrackingRecHit.h"
#include "DataFormats/GeometrySurface/interface/BoundPlane.h"
#include "TrackingTools/TrajectoryState/interface/TrajectoryStateOnSurface.h"
#include "TrackingTools/GsfTools/interface/BasicMultiTrajectoryState.h"
#include "TrackingTools/GsfTracking/interface/PosteriorWeightsCalculator.h"
#include "TrackingTools/GsfTools/interface/MultiTrajectoryStateAssembler.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

TrajectoryStateOnSurface GsfMultiStateUpdator::update(const TrajectoryStateOnSurface& tsos,
                                                      const TrackingRecHit& aRecHit) const {
  GetComponents comps(tsos);
  auto const& predictedComponents = comps();
  if (predictedComponents.empty()) {
    edm::LogError("GsfMultiStateUpdator") << "Trying to update trajectory state with zero components! ";
    return TrajectoryStateOnSurface();
  }

  auto&& weights = PosteriorWeightsCalculator(predictedComponents).weights(aRecHit);
  if (weights.empty()) {
    edm::LogError("GsfMultiStateUpdator") << " no weights could be retreived. invalid updated state !.";
    return TrajectoryStateOnSurface();
  }

  MultiTrajectoryStateAssembler result;

  int i = 0;
  //float pzSign = 1.;
  for (auto const& tsosI : predictedComponents) {
    TrajectoryStateOnSurface updatedTSOS = KFUpdator().update(tsosI, aRecHit);
    /*
    if (i == 0) {
      // select the pz sign of the first component
      pzSign = updatedTSOS.localParameters().pzSign();
    } else {
      // skip components with the "wrong" pz sign
      if (pzSign * updatedTSOS.localParameters().pzSign() < 0) {
    	edm::LogError("GsfMultiStateUpdator") << "KF updated state " << i << " leads to mixed pZ signs. Skipping...";
        continue;
      }
    }
   
    // in order to check for pos-def of error matrix
    std::function<bool(AlgebraicSymMatrix55, int)> sylvesterCriterion = [this](AlgebraicSymMatrix55 curvError,
                                                                               int index) {
      //Sylvester's criterion, start from the smaller submatrix size
      double det = 0;      
      if ((!curvError.Sub<AlgebraicSymMatrix22>(0, 0).Det(det)) || det < 0) {
        edm::LogInfo("GsfMultiStateUpdator") << "Fail pos-def check sub2.det for state " << index;
        return false;
      } else if ((!curvError.Sub<AlgebraicSymMatrix33>(0, 0).Det(det)) || det < 0) {
        edm::LogInfo("GsfMultiStateUpdator") << "Fail pos-def check sub3.det for state " << index;
        return false;
      } else if ((!curvError.Sub<AlgebraicSymMatrix44>(0, 0).Det(det)) || det < 0) {
        edm::LogInfo("GsfMultiStateUpdator") << "Fail pos-def check sub4.det for state " << index;
        return false;
      } else if ((!curvError.Det2(det)) || det < 0) {
        edm::LogInfo("GsfMultiStateUpdator") << "Fail pos-def check det for state " << index;
        return false;
      }
      // in case all the above was not realized
      return true;
    };
    */

    std::function<bool(AlgebraicSymMatrix55)> posDef = [this](AlgebraicSymMatrix55 curvError) {
      if ((curvError(0, 0) >= 0) && (curvError(1, 1) >= 0) && (curvError(2, 2) >= 0) && (curvError(3, 3) >= 0) && (curvError(4, 4) >= 0)){
	return true; 
      } else {
	edm::LogWarning("GsfMultiStateUpdator") << "local error not pos-def\n" << curvError;
	return false;
      }
    };

    if (updatedTSOS.isValid() && updatedTSOS.localError().valid() && updatedTSOS.localError().posDef() 
	//&& sylvesterCriterion(updatedTSOS.curvilinearError().matrix(), i)
	&& posDef(updatedTSOS.curvilinearError().matrix())) {
      result.addState(TrajectoryStateOnSurface(weights[i],
                                               updatedTSOS.localParameters(),
                                               updatedTSOS.localError(),
                                               updatedTSOS.surface(),
                                               &(tsos.globalParameters().magneticField()),
                                               tsosI.surfaceSide()));
    } else {
      edm::LogError("GsfMultiStateUpdator") << "KF updated state " << i << " is invalid. skipping.";
    }
    ++i;
  }

  edm::LogPrint("GsfMultiStateUpdator") << "################## returning a multi-state with " << i << "states"<< std::endl;
// 
  return result.combinedState();
}
