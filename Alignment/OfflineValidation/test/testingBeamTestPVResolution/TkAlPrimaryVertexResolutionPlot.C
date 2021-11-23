
/****************************************
This can be run directly in root, or you
 can run ./TkAlMerge.sh in this directory
****************************************/

#include "Alignment/OfflineValidation/macros/FitPVResolution.C"

void TkAlPrimaryVertexResolutionPlot()
{

  // initialize the plot y-axis ranges
  PVResolution::loadFileList("PrimaryVertexResolution_run2021data_express.root","PrimaryVertexResolution","express", 1, 24);
  //PVResolution::loadFileList("PrimaryVertexResolution_run2021data_PCL.root","PrimaryVertexResolution","PCL", 600, 25);
  PVResolution::loadFileList("PrimaryVertexResolution_run2021data_mp3448.root","PrimaryVertexResolution","mp3448", 632, 21);
  FitPVResolution("","");
}
