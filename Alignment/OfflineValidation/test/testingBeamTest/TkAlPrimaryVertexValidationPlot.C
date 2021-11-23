
/****************************************
This can be run directly in root, or you
 can run ./TkAlMerge.sh in this directory
****************************************/

#include "Alignment/OfflineValidation/macros/FitPVResiduals.C"

void TkAlPrimaryVertexValidationPlot()
{

  // initialize the plot y-axis ranges
  thePlotLimits->init(230,         // mean of dxy vs Phi
                      230,          // mean of dz  vs Phi
                      150,         // mean of dxy vs Eta
                      150,          // mean of dz  vs Eta
                      0.5,     // mean of dxy vs Phi (norm)
                      0.5,      // mean of dz  vs Phi (norm)
                      0.5,     // mean of dxy vs Eta (norm)
                      0.5,      // mean of dz  vs Eta (norm)
                      450,         // width of dxy vs Phi
                      600,          // width of dz  vs Phi
                      450,         // width of dxy vs Eta
                      1000,          // width of dz  vs Eta
                      3.0,     // width of dxy vs Phi (norm)
                      3.0,      // width of dz  vs Phi (norm)
                      3.0,     // width of dxy vs Eta (norm)
                      3.0       // width of dz  vs Eta (norm)
		      );

  //loadFileList("PrimaryVertexValidation_run2021data_express.root","PVValidation", "express", 1, 24);
  //loadFileList("PrimaryVertexValidation_run2021data_PCL.root","PVValidation", "PCL", 2, 25);
  //loadFileList("PrimaryVertexValidation_run2021data_Antonio.root","PVValidation", "mp3437", 4, 26);
  //loadFileList("PrimaryVertexValidation_run2021data_mp3444.root","PVValidation", "mp3444", 4, 26);
  //loadFileList("PrimaryVertexValidation_run2021data_mp3445.root","PVValidation", "mp3445", 6, 25);
  //loadFileList("PrimaryVertexValidation_run2021data_mp3446.root","PVValidation", "mp3446", 8, 20);
  //loadFileList("PrimaryVertexValidation_run2021data_mp3447.root","PVValidation", "mp3447", 9, 21);
  loadFileList("PrimaryVertexValidation_run2021data_mp3448.root","PVValidation", "mp3448", 1, 20);
  loadFileList("PrimaryVertexValidation_run2021data_mp3448_fixedPointAPE.root","PVValidation", "mp3448+fixed APE", 2, 24);
  loadFileList("PrimaryVertexValidation_run2021data_mp3448_measuredAPEs.root","PVValidation", "mp3448+meas APE", 4, 26);
  //loadFileList("PrimaryVertexValidation_run2021data_mp3452.root","PVValidation", "mp3452", 3, 20);
  //loadFileList("PrimaryVertexValidation_run2021data_mp3449.root","PVValidation", "mp3449", 4, 26);
  //loadFileList("PrimaryVertexValidation_run2021data_mp3447_betterBS.root","PVValidation", "mp3449+BS", 4, 26);
  FitPVResiduals("",true,true,"",false);
}
