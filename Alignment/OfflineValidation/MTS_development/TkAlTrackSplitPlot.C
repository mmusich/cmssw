#include "Alignment/OfflineValidation/macros/trackSplitPlot.C"

void TkAlTrackSplitPlot() {
  TkAlStyle::legendheader = "";
  TkAlStyle::legendoptions = "all";
  TkAlStyle::set(INTERNAL, NONE, "", "3.8T cosmic rays (2022)");
  outliercut = -1.0;
  //fillmatrix();                                                         //(C)
  subdetector = "PIXEL";

  makePlots("/tmp/musich/CMSSW_14_0_X_2024-01-01-2300/src/Alignment/OfflineValidation/MTS_development/MTSValidation_PromptNewTemplate_1.0.root=Alignment in prompt with 400V pixel templates|1|2301,"
	    "/tmp/musich/CMSSW_14_0_X_2024-01-01-2300/src/Alignment/OfflineValidation/MTS_development/MTSValidation_mp3619_1.0.root=mp3619|600|2001,",
	    "/tmp/musich/CMSSW_14_0_X_2024-01-01-2300/src/Alignment/OfflineValidation/MTS_development/TrackSplittingPlots");
}
