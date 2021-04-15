# Running the analysis
```
cmsRun OccupancyPlotsTest_pixelphase1_cfg.py globalTag=auto:run2_data inputFiles=root://cms-xrd-global.cern.ch//store/data/Run2018D/ZeroBias/RAW/v1/000/321/164/00000/20876FBF-419E-E811-B6D3-FA163EBAB20D.root,/store/data/Run2018D/ZeroBias/RAW/v1/000/321/164/00000/90B324C3-419E-E811-9A23-02163E019EDB.root,/store/data/Run2018D/ZeroBias/RAW/v1/000/321/164/00000/A8998B31-419E-E811-89E8-FA163E2640F4.root 
```

# Producing the plots
```
cd ../bin
root -l
root [0] TFile* f = TFile::Open("../test/OccupancyPlotsTest_pixelphase1_.root")
root [1] .L OccupancyPlotMacros.cc++g
root [2] PlotOccupancyMap(f,"occupancyplots/run_321164",0.01,0.1,1,100,4)
``
