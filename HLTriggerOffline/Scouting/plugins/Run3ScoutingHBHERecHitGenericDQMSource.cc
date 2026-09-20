#include "DQMServices/Components/interface/GenericObjectDQMSource.h"
#include "HLTriggerOffline/Scouting/interface/Run3ScoutingHBHERecHitDQMVariables.h"
#include "FWCore/Framework/interface/MakerMacros.h"

using Run3ScoutingHBHERecHitGenericDQMSource = GenericObjectDQMSource<Run3ScoutingHBHERecHit>;

DEFINE_FWK_MODULE(Run3ScoutingHBHERecHitGenericDQMSource);
