#include "DQMServices/Components/interface/GenericObjectDQMSource.h"
#include "HLTriggerOffline/Scouting/interface/Run3ScoutingEBRecHitDQMVariables.h"
#include "FWCore/Framework/interface/MakerMacros.h"

using Run3ScoutingEBRecHitGenericDQMSource = GenericObjectDQMSource<Run3ScoutingEBRecHit>;

DEFINE_FWK_MODULE(Run3ScoutingEBRecHitGenericDQMSource);
