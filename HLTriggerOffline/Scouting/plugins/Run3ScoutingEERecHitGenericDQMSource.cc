#include "DQMServices/Components/interface/GenericObjectDQMSource.h"
#include "HLTriggerOffline/Scouting/interface/Run3ScoutingEERecHitDQMVariables.h"
#include "FWCore/Framework/interface/MakerMacros.h"

using Run3ScoutingEERecHitGenericDQMSource = GenericObjectDQMSource<Run3ScoutingEERecHit>;

DEFINE_FWK_MODULE(Run3ScoutingEERecHitGenericDQMSource);
