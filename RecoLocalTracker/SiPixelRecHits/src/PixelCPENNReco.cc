// Include our own header first
#include "RecoLocalTracker/SiPixelRecHits/interface/PixelCPETemplateReco.h"
#include "RecoLocalTracker/SiPixelRecHits/interface/PixelCPENNReco.h"


// Geometry services
#include "Geometry/CommonDetUnit/interface/PixelGeomDetUnit.h"
#include "Geometry/TrackerGeometryBuilder/interface/RectangularPixelTopology.h"

//#define DEBUG

// MessageLogger

#include "FWCore/MessageLogger/interface/MessageLogger.h"

// Magnetic field
#include "MagneticField/Engine/interface/MagneticField.h"

// The template header files
#include "RecoLocalTracker/SiPixelRecHits/interface/SiPixelTemplateReco.h"

// Commented for now (3/10/17) until we figure out how to resuscitate 2D template splitter
/// #include "RecoLocalTracker/SiPixelRecHits/interface/SiPixelTemplateSplit.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include <vector>
#include "boost/multi_array.hpp"

#include <iostream>

using namespace SiPixelTemplateReco;
//using namespace SiPixelTemplateSplit;
using namespace std;

namespace {
  constexpr float micronsToCm = 1.0e-4;
  constexpr int cluster_matrix_size_x = 13;
  constexpr int cluster_matrix_size_y = 21;
  constexpr float pixelsize_x = 100., pixelsize_y = 150., pixelsize_z = 285.0;
}  // namespace

//-----------------------------------------------------------------------------
//  Constructor.
//
//-----------------------------------------------------------------------------
PixelCPENNReco::PixelCPENNReco(edm::ParameterSet const& conf,
                                           //const MagneticField* mag,
                                           const TrackerGeometry& geom,
                                           const TrackerTopology& ttopo,
                                           //const SiPixelLorentzAngle* lorentzAngle,
                                           //const SiPixelTemplateDBObject* templateDBobject,
                                           //const CacheData* cacheData
                                           )
    : PixelCPEBase(conf, nullptr, geom, ttopo, nullptr, nullptr, nullptr, nullptr, 1),
    inputTensorName_x(conf.getParameter<std::string>("inputTensorName_x")),
    anglesTensorName_x(conf.getParameter<std::string>("anglesTensorName_x")),
    outputTensorName_(conf.getParameter<std::string>("outputTensorName")),
    //session_x(tensorflow::createSession(cacheData->graphDef)),
    //use_det_angles(config.getParameter<bool>("use_det_angles")),
    cpe(conf.getParameter<std::string>("cpe")) {
  //cout << endl;
  //cout << "Constructing PixelCPENNReco::PixelCPENNReco(...)................................................." << endl;
  //cout << endl;

  // Configurable parameters
  //DoCosmics_ = conf.getParameter<bool>("DoCosmics"); // Not used in templates
  //LoadTemplatesFromDB_ = conf.getParameter<bool>("LoadTemplatesFromDB"); // Moved to Base

  //cout << " PixelCPENNReco : (int)LoadTemplatesFromDB_ = " << (int)LoadTemplatesFromDB_ << endl;
  //cout << "field_magnitude = " << field_magnitude << endl;

  // configuration parameter to decide between DB or text file template access
/*
  if (LoadTemplatesFromDB_) {
    //cout << "PixelCPENNReco: Loading templates from database (DB) --------- " << endl;

    // Initialize template store to the selected ID [Morris, 6/25/08]
    if (!SiPixelTemplate::pushfile(*templateDBobject_, thePixelTemp_))
      throw cms::Exception("PixelCPENNReco")
          << "\nERROR: Templates not filled correctly. Check the sqlite file. Using SiPixelTemplateDBObject version "
          << (*templateDBobject_).version() << "\n\n";
  } else {
    //cout << "PixelCPENNReco : Loading templates for barrel and forward from ASCII files ----------" << endl;
    barrelTemplateID_ = conf.getParameter<int>("barrelTemplateID");
    forwardTemplateID_ = conf.getParameter<int>("forwardTemplateID");
    templateDir_ = conf.getParameter<int>("directoryWithTemplates");

    if (!SiPixelTemplate::pushfile(barrelTemplateID_, thePixelTemp_, templateDir_))
      throw cms::Exception("PixelCPENNReco")
          << "\nERROR: Template ID " << barrelTemplateID_
          << " not loaded correctly from text file. Reconstruction will fail.\n\n";

    if (!SiPixelTemplate::pushfile(forwardTemplateID_, thePixelTemp_, templateDir_))
      throw cms::Exception("PixelCPENNReco")
          << "\nERROR: Template ID " << forwardTemplateID_
          << " not loaded correctly from text file. Reconstruction will fail.\n\n";
  }

  speed_ = conf.getParameter<int>("speed");
  LogDebug("PixelCPENNReco::PixelCPENNReco:") << "Template speed = " << speed_ << "\n";

  UseClusterSplitter_ = conf.getParameter<bool>("UseClusterSplitter");
  */
}

//-----------------------------------------------------------------------------
//  Clean up.
//-----------------------------------------------------------------------------
PixelCPENNReco::~PixelCPENNReco() {}

std::unique_ptr<PixelCPEBase::ClusterParam> PixelCPENNReco::createClusterParam(const SiPixelCluster& cl) const {
  return std::make_unique<ClusterParamTemplate>(cl);
}

//------------------------------------------------------------------
//  Public methods mandated by the base class.
//------------------------------------------------------------------

//------------------------------------------------------------------
//  The main call to the template code.
//------------------------------------------------------------------
LocalPoint PixelCPENNReco::localPosition(DetParam const& theDetParam, ClusterParam& theClusterParamBase) const {
  ClusterParamTemplate& theClusterParam = static_cast<ClusterParamTemplate&>(theClusterParamBase);

  if (!GeomDetEnumerators::isTrackerPixel(theDetParam.thePart))
    throw cms::Exception("PixelCPENNReco::localPosition :") << "A non-pixel detector type in here?";
  //  barrel(false) or forward(true)
  const bool fpix = GeomDetEnumerators::isEndcap(theDetParam.thePart);
/*
  int ID = -9999;
  if (LoadTemplatesFromDB_) {
    int ID0 = templateDBobject_->getTemplateID(theDetParam.theDet->geographicalId());  // just to comapre
    ID = theDetParam.detTemplateId;
    if (ID0 != ID)
      edm::LogError("PixelCPENNReco") << " different id" << ID << " " << ID0 << endl;
  } else {  // from asci file
    if (!fpix)
      ID = barrelTemplateID_;  // barrel
    else
      ID = forwardTemplateID_;  // forward
  }
  //cout << "PixelCPENNReco : ID = " << ID << endl;
*/
  if(fpix){
    throw cms::Exception("PixelCPENNReco::localPosition :") << "graph is trained on BPIX only";
  }
  // how to access layer info from det_id? can i use the tracker topology token here? so i have to add it to the det_id or 
  if(ttopo_.pxbLayer(theDetParam.theDet->geographicalId()) != 1){
    throw cms::Exception("PixelCPENNReco::localPosition :") << "graph is trained on BPIX L1 only";
  }

 // SiPixelTemplate templ(thePixelTemp_);

  // Preparing to retrieve ADC counts from the SiPixeltheClusterParam.theCluster->  In the cluster,
  // we have the following:
  //   int minPixelRow(); // Minimum pixel index in the x direction (low edge).
  //   int maxPixelRow(); // Maximum pixel index in the x direction (top edge).
  //   int minPixelCol(); // Minimum pixel index in the y direction (left edge).
  //   int maxPixelCol(); // Maximum pixel index in the y direction (right edge).
  // So the pixels from minPixelRow() will go into clust_array_2d[0][*],
  // and the pixels from minPixelCol() will go into clust_array_2d[*][0].

  int row_offset = theClusterParam.theCluster->minPixelRow();
  int col_offset = theClusterParam.theCluster->minPixelCol();

  // Store the coordinates of the center of the (0,0) pixel of the array that
  // gets passed to PixelTempReco1D
  // Will add these values to the output of  PixelTempReco1D
  float tmp_x = float(row_offset) + 0.5f;
  float tmp_y = float(col_offset) + 0.5f;

  // Store these offsets (to be added later) in a LocalPoint after tranforming
  // them from measurement units (pixel units) to local coordinates (cm)
  //
  //

  // In case of template reco failure, these are the lorentz drift corrections
  // to be applied
  float lorentzshiftX = 0.5f * theDetParam.lorentzShiftInCmX;
  float lorentzshiftY = 0.5f * theDetParam.lorentzShiftInCmY;

  // ggiurgiu@jhu.edu 12/09/2010 : update call with trk angles needed for bow/kink corrections
  LocalPoint lp;

  if (theClusterParam.with_track_angle)
    lp = theDetParam.theTopol->localPosition(MeasurementPoint(tmp_x, tmp_y), theClusterParam.loc_trk_pred);
  else {
    edm::LogError("PixelCPENNReco") << "@SUB = PixelCPENNReco::localPosition"
                                          << "Should never be here. PixelCPENNReco should always be called with "
                                             "track angles. This is a bad error !!! ";

    lp = theDetParam.theTopol->localPosition(MeasurementPoint(tmp_x, tmp_y));
  }

  // first compute matrix size
  int mrow = 0, mcol = 0;
  for (int i = 0; i != theClusterParam.theCluster->size(); ++i) {
    auto pix = theClusterParam.theCluster->pixel(i);
    int irow = int(pix.x);
    int icol = int(pix.y);
    mrow = std::max(mrow, irow);
    mcol = std::max(mcol, icol);
  }
  mrow -= row_offset;
  mrow += 1;
  mrow = std::min(mrow, cluster_matrix_size_x);
  mcol -= col_offset;
  mcol += 1;
  mcol = std::min(mcol, cluster_matrix_size_y);
  assert(mrow > 0);
  assert(mcol > 0);

  float clustMatrix[mrow][mcol], clustMatrix_temp[mrow][mcol], clustMatrix_x[mrow];
  memset(clustMatrix, 0, sizeof(float) * mrow * mcol);
  memset(clustMatrix_temp, 0, sizeof(float) * mrow * mcol);
  memset(clustMatrix_x, 0, sizeof(float) * mrow);

  int n_double_x = 0, n_double_y = 0;
  int mid_x = 0, mid_y = 0;    
    int clustersize = 0;
        int double_row[5], double_col[5]; 
        for(int i=0;i<5;i++){
          double_row[i]=-1;
          double_col[i]=-1;
        }
        
        int irow_sum = 0, icol_sum = 0;
        for (int i = 0;  i < theClusterParam.theCluster->size(); i++) {
          auto pix = theClusterParam.theCluster->pixel(i);
          int irow = int(pix.x) - row_offset;
          int icol = int(pix.y) - col_offset;
          if ((irow >= mrow) || (icol >= mcol)) continue; 
          if ((int)pix.x == 79 || (int)pix.x == 80){
            int flag=0;
            for(int j=0;j<5;j++){
              if(irow==double_row[j]) {flag = 1; break;}
            }
            if(flag!=1) {double_row[n_double_x]=irow; n_double_x++;}
          }
          if ((int)pix.y % 52 == 0 || (int)pix.y % 52 == 51){
            int flag=0;
            for(int j=0;j<5;j++){
              if(icol==double_col[j]) {flag = 1; break;}
            }
            if(flag!=1) {double_col[n_double_y]=icol; n_double_y++;}
          }
          irow_sum+=irow;
          icol_sum+=icol;
          clustersize++;
        //if(float(pix.adc) > cluster_max) cluster_max = float(pix.adc); 
        //if(float(pix.adc) < cluster_min) cluster_min = float(pix.adc); 

        }
        if(clustersize==0){edm::LogError("PixelCPENNReco") <<"EMPTY CLUSTER\n";} 
        if(n_double_x>2 or n_double_y>2){
        edm::LogError("PixelCPENNReco") << "MORE THAN 2 DOUBLE COL in X or Y";
      }
    n_double_x=0; n_double_y=0;
      //printf("max = %f, min = %f\n",cluster_max,cluster_min);
    int clustersize_x = theClusterParam.theCluster->sizeX(), clustersize_y = theClusterParam.theCluster->sizeY();
    mid_x = round(float(irow_sum)/float(clustersize));
    mid_y = round(float(icol_sum)/float(clustersize));
    int offset_x = 6 - mid_x;
    int offset_y = 10 - mid_y;
      


  // Copy clust's pixels (calibrated in electrons) into clusMatrix;
  for (int i = 0; i != theClusterParam.theCluster->size(); ++i) {
    auto pix = theClusterParam.theCluster->pixel(i);
    int irow = int(pix.x) - row_offset + offset_x;
    int icol = int(pix.y) - col_offset + offset_y;

    if ((irow >= mrow+offset_x) || (icol >= mcol+offset_y)){
        printf("irow or icol exceeded, SKIPPING. irow = %i, mrow = %i, offset_x = %i,icol = %i, mcol = %i, offset_y = %i\n",irow,mrow,offset_x,icol,mcol,offset_y);
        continue;
      }
      if ((int)pix.x == 79 || (int)pix.x == 80){
        int flag=0;
        for(int j=0;j<5;j++){
          if(irow==double_row[j]) {flag = 1; break;}
        }
        if(flag!=1) {double_row[n_double_x]=irow; n_double_x++;}
      }
      if ((int)pix.y % 52 == 0 || (int)pix.y % 52 == 51 ){
        int flag=0;
        for(int j=0;j<5;j++){
          if(icol==double_col[j]) {flag = 1; break;}
        }
        if(flag!=1) {double_col[n_double_y]=icol; n_double_y++;}
      }
    // Gavril : what do we do here if the row/column is larger than cluster_matrix_size_x/cluster_matrix_size_y  ?
    // Ignore them for the moment...
    if ((irow < mrow) & (icol < mcol))
      clustMatrix_temp[irow][icol] = float(pix.adc)/25000.;
  }
/*
  // Make and fill the bool arrays flagging double pixels
  bool xdouble[mrow], ydouble[mcol];
  // x directions (shorter), rows
  for (int irow = 0; irow < mrow; ++irow)
    xdouble[irow] = theDetParam.theRecTopol->isItBigPixelInX(irow + row_offset);

  // y directions (longer), columns
  for (int icol = 0; icol < mcol; ++icol)
    ydouble[icol] = theDetParam.theRecTopol->isItBigPixelInY(icol + col_offset);
*/
 // SiPixelTemplateReco::ClusMatrix clusterPayload{&clustMatrix[0][0], xdouble, ydouble, mrow, mcol};

  //deal with double width pixels
  if(n_double_x==1 && clustersize_x>12) {printf("clustersize_x > 12, SKIPPING\n"); } // NEED TO FIX CLUSTERSIZE COMPUTATION
    if(n_double_x==2 && clustersize_x>11) {printf("clustersize_x > 11, SKIPPING\n"); }
    if(n_double_y==1 && clustersize_y>20) {printf("clustersize_y = %i > 20, SKIPPING\n", clustersize_y);}
    if(n_double_y==2 && clustersize_x>19) {printf("clustersize_y = %i > 19, SKIPPING\n", clustersize_y);}

//first deal with double width pixels in x
    int k=0,m=0;
    for(int i=0;i<mrow;i++){
      if(i==double_row[m] and clustersize_x>1){
        printf("TREATING DPIX%i IN X\n",m+1);
        for(int j=0;j<mcol;j++){
          clustMatrix[i][j]=clustMatrix_temp[k][j]/2.;
          clustMatrix[i+1][j]=clustMatrix_temp[k][j]/2.;
        }
        i++;
        if(m==0 and n_double_x==2) {
          double_row[1]++;
          m++;
        }
      }
      else{
        for(int j=0;j<mcol;j++){
          clustMatrix[i][j]=clustMatrix_temp[k][j];
        }
      }
      k++;
    }
    k=0;m=0;
    for(int i=0;i<mrow;i++){
      for(int j=0;j<mcol;j++){
        clustMatrix_temp[i][j]=clustMatrix[i][j];
        clustMatrix[i][j]=0.;
      }
    }
    for(int j=0;j<mcol;j++){
      if(j==double_col[m] and clustersize_y>1){
        printf("TREATING DPIX%i IN Y\n",m+1);
        for(int i=0;i<mrow;i++){
          clustMatrix[i][j]=clustMatrix_temp[i][k]/2.;
          clustMatrix[i][j+1]=clustMatrix_temp[i][k]/2.;
        }
        j++;
        if(m==0 and n_double_y==2) {
          double_col[1]++;
          m++;
        }
      }
      else{
        for(int i=0;i<mrow;i++){
          clustMatrix[i][j]=clustMatrix_temp[i][k];
        }
      }
      k++;
    }
//compute the 1d projection 
   for(int i = 0;i < mrow; i++){
      for(int j = 0; j < mcol; j++){
        clustMatrix_x[i] += clustMatrix[i][j];
	}
    }
  // Output:
  float nonsense = -99999.9f;  // nonsense init value
  theClusterParam.NNXrec_ = theClusterParam.NNYrec_ = theClusterParam.NNSigmaX_ =
      theClusterParam.NNSigmaY_ = nonsense;
  // If the template recontruction fails, we want to return 1.0 for now
  //theClusterParam.templProbY_ = theClusterParam.templProbX_ = theClusterParam.templProbQ_ = 1.0f;
  //theClusterParam.templQbin_ = 0;
  // We have a boolean denoting whether the reco failed or not
  //theClusterParam.hasFilledProb_ = false;

  float NNYrec1_ = nonsense;
  float NNXrec1_ = nonsense;
  //float templYrec1_ = nonsense;
 // float templXrec1_ = nonsense;
 // float templYrec2_ = nonsense;
//  float templXrec2_ = nonsense;

  /******************************************************************
  // Do it! Use cotalpha_ and cotbeta_ calculated in PixelCPEBase

  float locBz = theDetParam.bz;
  float locBx = theDetParam.bx;

  theClusterParam.ierr = PixelTempReco1D(ID,
                                         theClusterParam.cotalpha,
                                         theClusterParam.cotbeta,
                                         locBz,
                                         locBx,
                                         clusterPayload,
                                         templ,
                                         theClusterParam.templYrec_,
                                         theClusterParam.templSigmaY_,
                                         theClusterParam.templProbY_,
                                         theClusterParam.templXrec_,
                                         theClusterParam.templSigmaX_,
                                         theClusterParam.templProbX_,
                                         theClusterParam.templQbin_,
                                         speed_,
                                         theClusterParam.templProbQ_);

  // ******************************************************************/

  //========================================================================================
        // define a tensor and fill it with cluster projection
        tensorflow::Tensor cluster_flat_x(tensorflow::DT_FLOAT, {1,TXSIZE,1});
      tensorflow::Tensor cluster_(tensorflow::DT_FLOAT, {1,TXSIZE,TYSIZE,1});
        // angles
      tensorflow::Tensor angles(tensorflow::DT_FLOAT, {1,2});
      angles.tensor<float,2>()(0, 0) = theClusterParam.cotalpha;
      angles.tensor<float,2>()(0, 1) = theClusterParam.cotbeta;

      for (int i = 0; i < TXSIZE; i++) {
        cluster_flat_x.tensor<float,3>()(0, i, 0) = 0;
        for (int j = 0; j < TYSIZE; j++){
            //1D projection in x
          cluster_flat_x.tensor<float,3>()(0, i, 0) = clustMatrix_x[i];
          cluster_.tensor<float,4>()(0, i, j, 0) = clustMatrix[i][j];
          
          //printf("%i ",int(clusbuf[i][j]));

        }
          //printf("\n");
      }
      //  Determine current time

          //gettimeofday(&now0, &timz);
        // define the output and run
      std::vector<tensorflow::Tensor> output_x;
      if(cpe=="cnn2d"){ //gettimeofday(&now0, &timz);
        tensorflow::run(session_x, {{inputTensorName_x,cluster_}, {anglesTensorName_x,angles}}, {outputTensorName_}, &output_x);
       // gettimeofday(&now1, &timz);
      }
      else { // gettimeofday(&now0, &timz);
        tensorflow::run(session_x, {{inputTensorName_x,cluster_flat_x}, {anglesTensorName_x,angles}}, {outputTensorName_}, &output_x);
       // gettimeofday(&now1, &timz);
      }
      // convert microns to cms
      theClusterParam.NNXrec_ = output_x[0].matrix<float>()(0,0);
      
      //printf("x_nn[%i] = %f\n",count,x_nn[count]);
      //if(isnan(x_nn[count])){
      //for(int i=0;i<TXSIZE;i++){
      //  for(int j=0;j<TYSIZE;j++)
      //    printf("%i ",int(clusbuf[i][j]));
      //  printf("\n");
      //}
      //printf("\n");}
      theClusterParam.NNXrec_ = theClusterParam.NNXrec_ + pixelsize_x*(mid_x); 
      //for testing purposes
      theClusterParam.NNYrec_ = 500;
      theClusterParam.NNSigmaX_ = 1;
      theClusterParam.NNSigmaY_ = 1;
      if(isnan(NNXrec1_) or NNXrec1_>=999e4) theClusterParam.ierr = 12345;
      else theClusterParam.ierr = 0.;

  // Check exit status
  if UNLIKELY (theClusterParam.ierr != 0) {
    LogDebug("PixelCPENNReco::localPosition")
        << "reconstruction failed with error " << theClusterParam.ierr << "\n";

    // Template reco has failed, compute position estimates based on cluster center of gravity + Lorentz drift
    // Future improvement would be to call generic reco instead

    // ggiurgiu@jhu.edu, 21/09/2010 : trk angles needed to correct for bows/kinks
    if (theClusterParam.with_track_angle) {
      theClusterParam.NNXrec_ =
          theDetParam.theTopol->localX(theClusterParam.theCluster->x(), theClusterParam.loc_trk_pred) + lorentzshiftX;
      theClusterParam.NNYrec_ =
          theDetParam.theTopol->localY(theClusterParam.theCluster->y(), theClusterParam.loc_trk_pred) + lorentzshiftY;
    } else {
      edm::LogError("PixelCPENNReco") << "@SUB = PixelCPENNReco::localPosition"
                                            << "Should never be here. PixelCPENNReco should always be called "
                                               "with track angles. This is a bad error !!! ";

      theClusterParam.NNXrec_ = theDetParam.theTopol->localX(theClusterParam.theCluster->x()) + lorentzshiftX;
      theClusterParam.NNYrec_ = theDetParam.theTopol->localY(theClusterParam.theCluster->y()) + lorentzshiftY;
    }
  } 
  /*
  else if UNLIKELY (UseClusterSplitter_ && theClusterParam.templQbin_ == 0) {
    edm::LogError("PixelCPENNReco") << " PixelCPENNReco: Qbin = 0 but using cluster splitter, we should "
                                             "never be here !!!!!!!!!!!!!!!!!!!!!! \n"
                                          << "(int)UseClusterSplitter_ = " << (int)UseClusterSplitter_ << endl;

    //ierr =
    //PixelTempSplit( ID, fpix, cotalpha_, cotbeta_,
    //		clust_array_2d, ydouble, xdouble,
    //		templ,
    //		templYrec1_, templYrec2_, templSigmaY_, templProbY_,
    //		templXrec1_, templXrec2_, templSigmaX_, templProbX_,
    //		templQbin_ );

    // Commented for now (3/10/17) until we figure out how to resuscitate 2D template splitter
    ///      std::vector< SiPixelTemplateStore2D > thePixelTemp2D_;
    ///SiPixelTemplate2D::pushfile(ID, thePixelTemp2D_);
    ///SiPixelTemplate2D templ2D_(thePixelTemp2D_);

    theClusterParam.ierr = -123;
    */
    /*
       float dchisq;
       float templProbQ_;
       SiPixelTemplateSplit::PixelTempSplit( ID, theClusterParam.cotalpha, theClusterParam.cotbeta,
       clust_array_2d,
       ydouble, xdouble,
       templ,
       templYrec1_, templYrec2_, theClusterParam.templSigmaY_, theClusterParam.templProbY_,
       templXrec1_, templXrec2_, theClusterParam.templSigmaX_, theClusterParam.templProbX_,
       theClusterParam.templQbin_,
       templProbQ_,
       true,
       dchisq,
       templ2D_ );
       
       */
  /*
    if (theClusterParam.ierr != 0) {
      // Template reco has failed, compute position estimates based on cluster center of gravity + Lorentz drift
      // Future improvement would be to call generic reco instead

      // ggiurgiu@jhu.edu, 12/09/2010 : trk angles needed to correct for bows/kinks
      if (theClusterParam.with_track_angle) {
        theClusterParam.templXrec_ =
            theDetParam.theTopol->localX(theClusterParam.theCluster->x(), theClusterParam.loc_trk_pred) + lorentzshiftX;
        theClusterParam.templYrec_ =
            theDetParam.theTopol->localY(theClusterParam.theCluster->y(), theClusterParam.loc_trk_pred) + lorentzshiftY;
      } else {
        edm::LogError("PixelCPENNReco") << "@SUB = PixelCPENNReco::localPosition"
                                              << "Should never be here. PixelCPENNReco should always be called "
                                                 "with track angles. This is a bad error !!! ";
        theClusterParam.templXrec_ = theDetParam.theTopol->localX(theClusterParam.theCluster->x()) + lorentzshiftX;
        theClusterParam.templYrec_ = theDetParam.theTopol->localY(theClusterParam.theCluster->y()) + lorentzshiftY;
      }
    } else {
      // go from micrometer to centimeter
      //NNXrec1_ *= micronsToCm;
      //NNYrec1_ *= micronsToCm;
      templXrec1_ *= micronsToCm;
      templYrec1_ *= micronsToCm;
      templXrec2_ *= micronsToCm;
      templYrec2_ *= micronsToCm;

      // go back to the module coordinate system
      NNXrec1_ += lp.x();
      NNYrec1_ += lp.y();
      templXrec1_ += lp.x();
      templYrec1_ += lp.y();
      templXrec2_ += lp.x();
      templYrec2_ += lp.y();

      // calculate distance from each hit to the track and choose the hit closest to the track
      float distX1 = std::abs(templXrec1_ - theClusterParam.trk_lp_x);
      float distX2 = std::abs(templXrec2_ - theClusterParam.trk_lp_x);
      float distY1 = std::abs(templYrec1_ - theClusterParam.trk_lp_y);
      float distY2 = std::abs(templYrec2_ - theClusterParam.trk_lp_y);
      theClusterParam.templXrec_ = (distX1 < distX2 ? templXrec1_ : templXrec2_);
      theClusterParam.templYrec_ = (distY1 < distY2 ? templYrec1_ : templYrec2_);
    }
  }  // else if ( UseClusterSplitter_ && templQbin_ == 0 )
*/
  else  // apparenly this is the good one!
  {
    // go from micrometer to centimeter
    theClusterParam.NNXrec_ *= micronsToCm;
    theClusterParam.NNYrec_ *= micronsToCm;

    // go back to the module coordinate system
    theClusterParam.NNXrec_ += lp.x();
    theClusterParam.NNYrec_ += lp.y();

    // Compute the Alignment Group Corrections [template ID should already be selected from call to reco procedure]
    /*
    if (doLorentzFromAlignment_) {
      // Do only if the lotentzshift has meaningfull numbers
      if (theDetParam.lorentzShiftInCmX != 0.0 || theDetParam.lorentzShiftInCmY != 0.0) {
        // the LA width/shift returned by templates use (+)
        // the LA width/shift produced by PixelCPEBase for positive LA is (-)
        // correct this by iserting (-)
        //float temp1 = -micronsToCm*templ.lorxwidth();  // old
        //float temp2 = -micronsToCm*templ.lorywidth();  // does not incl 1/2
        float templateLorbiasCmX = -micronsToCm * templ.lorxbias();  // new
        float templateLorbiasCmY = -micronsToCm * templ.lorybias();  //incl. 1/2
        // now, correctly, we can use the difference of shifts
        //theClusterParam.templXrec_ += 0.5*(theDetParam.lorentzShiftInCmX - templateLorbiasCmX);
        //theClusterParam.templYrec_ += 0.5*(theDetParam.lorentzShiftInCmY - templateLorbiasCmY);
        theClusterParam.templXrec_ += (0.5 * (theDetParam.lorentzShiftInCmX) - templateLorbiasCmX);
        theClusterParam.templYrec_ += (0.5 * (theDetParam.lorentzShiftInCmY) - templateLorbiasCmY);
        //cout << "Templates: la lorentz offset = "
        //   <<(0.5*(theDetParam.lorentzShiftInCmX)-templateLorbiasCmX)
        //   <<" "<<templateLorbiasCmX<<" "<<templateLorbiasCmY
        //   <<" "<<temp1<<" "<<temp2
        //   <<" "<<theDetParam.lorentzShiftInCmX
        //   <<" "<<theDetParam.lorentzShiftInCmY
        //   << endl; //dk
      }  //else {cout<<" LA is 0, disable offset corrections "<<endl;} //dk
    } */   //else {cout<<" Do not do LA offset correction "<<endl;} //dk
  }

  // Save probabilities and qBin in the quantities given to us by the base class
  // (for which there are also inline getters).  &&& templProbX_ etc. should be retired...
  /*
  theClusterParam.probabilityX_ = theClusterParam.templProbX_;
  theClusterParam.probabilityY_ = theClusterParam.templProbY_;
  theClusterParam.probabilityQ_ = theClusterParam.templProbQ_;
  theClusterParam.qBin_ = theClusterParam.templQbin_;
  */
   theClusterParam.probabilityX_ = 0.05;
  theClusterParam.probabilityY_ = 0.05;
  theClusterParam.probabilityQ_ = 0.05;
  theClusterParam.qBin_ = 0.05;

  if (theClusterParam.ierr == 0)  // always true here
    theClusterParam.hasFilledProb_ = true;

  return LocalPoint(theClusterParam.NNXrec_, theClusterParam.NNYrec_);
}

//------------------------------------------------------------------
//  localError() relies on localPosition() being called FIRST!!!
//------------------------------------------------------------------
LocalError PixelCPENNReco::localError(DetParam const& theDetParam, ClusterParam& theClusterParamBase) const {
  ClusterParamTemplate& theClusterParam = static_cast<ClusterParamTemplate&>(theClusterParamBase);

  //cout << endl;
  //cout << "Set PixelCPETemplate errors .............................................." << endl;

  //cout << "CPETemplate : " << endl;

  //--- Default is the maximum error used for edge clusters.
  //--- (never used, in fact: let comment it out, shut up the complains of the static analyzer, and save a few CPU cycles)
  //   const float sig12 = 1./sqrt(12.0);
  //   float xerr = theDetParam.thePitchX *sig12;
  //   float yerr = theDetParam.thePitchY *sig12;
  float xerr, yerr;

  // Check if the errors were already set at the clusters splitting level
  if (theClusterParam.theCluster->getSplitClusterErrorX() > 0.0f &&
      theClusterParam.theCluster->getSplitClusterErrorX() < clusterSplitMaxError_ &&
      theClusterParam.theCluster->getSplitClusterErrorY() > 0.0f &&
      theClusterParam.theCluster->getSplitClusterErrorY() < clusterSplitMaxError_) {
    xerr = theClusterParam.theCluster->getSplitClusterErrorX() * micronsToCm;
    yerr = theClusterParam.theCluster->getSplitClusterErrorY() * micronsToCm;

    //cout << "Errors set at cluster splitting level : " << endl;
    //cout << "xerr = " << xerr << endl;
    //cout << "yerr = " << yerr << endl;
  } else {
    // If errors are not split at the cluster splitting level, set the errors here

    //cout  << "Errors are not split at the cluster splitting level, set the errors here : " << endl;

    int maxPixelCol = theClusterParam.theCluster->maxPixelCol();
    int maxPixelRow = theClusterParam.theCluster->maxPixelRow();
    int minPixelCol = theClusterParam.theCluster->minPixelCol();
    int minPixelRow = theClusterParam.theCluster->minPixelRow();

    //--- Are we near either of the edges?
    bool edgex = (theDetParam.theRecTopol->isItEdgePixelInX(minPixelRow) ||
                  theDetParam.theRecTopol->isItEdgePixelInX(maxPixelRow));
    bool edgey = (theDetParam.theRecTopol->isItEdgePixelInY(minPixelCol) ||
                  theDetParam.theRecTopol->isItEdgePixelInY(maxPixelCol));

    if (theClusterParam.ierr != 0) {
      // If reconstruction fails the hit position is calculated from cluster center of gravity
      // corrected in x by average Lorentz drift. Assign huge errors.
      //xerr = 10.0 * (float)theClusterParam.theCluster->sizeX() * xerr;
      //yerr = 10.0 * (float)theClusterParam.theCluster->sizeX() * yerr;

      if (!GeomDetEnumerators::isTrackerPixel(theDetParam.thePart))
        throw cms::Exception("PixelCPENNReco::localPosition :") << "A non-pixel detector type in here?";

      // Assign better errors based on the residuals for failed template cases
      if (GeomDetEnumerators::isBarrel(theDetParam.thePart)) {
        xerr = 55.0f * micronsToCm;
        yerr = 36.0f * micronsToCm;
      } else {
        xerr = 42.0f * micronsToCm;
        yerr = 39.0f * micronsToCm;
      }

      //cout << "xerr = " << xerr << endl;
      //cout << "yerr = " << yerr << endl;

      //return LocalError(xerr*xerr, 0, yerr*yerr);
    } else if (edgex || edgey) {
      // for edge pixels assign errors according to observed residual RMS
      if (edgex && !edgey) {
        xerr = xEdgeXError_ * micronsToCm;
        yerr = xEdgeYError_ * micronsToCm;
      } else if (!edgex && edgey) {
        xerr = yEdgeXError_ * micronsToCm;
        yerr = yEdgeYError_ * micronsToCm;
      } else if (edgex && edgey) {
        xerr = bothEdgeXError_ * micronsToCm;
        yerr = bothEdgeYError_ * micronsToCm;
      } else {
        throw cms::Exception(" PixelCPENNReco::localError: Something wrong with pixel edge flag !!!");
      }

      //cout << "xerr = " << xerr << endl;
      //cout << "yerr = " << yerr << endl;
    } else {
      // &&& need a class const
      //const float micronsToCm = 1.0e-4;

      xerr = theClusterParam.NNSigmaX_ * micronsToCm;
      yerr = theClusterParam.NNSigmaY_ * micronsToCm;

      //cout << "xerr = " << xerr << endl;
      //cout << "yerr = " << yerr << endl;

      // &&& should also check ierr (saved as class variable) and return
      // &&& nonsense (another class static) if the template fit failed.
    }

    if (theVerboseLevel > 9) {
      LogDebug("PixelCPENNReco") << " Sizex = " << theClusterParam.theCluster->sizeX()
                                       << " Sizey = " << theClusterParam.theCluster->sizeY() << " Edgex = " << edgex
                                       << " Edgey = " << edgey << " ErrX  = " << xerr << " ErrY  = " << yerr;
    }

  }  // else

  if (!(xerr > 0.0f))
    throw cms::Exception("PixelCPENNReco::localError")
        << "\nERROR: Negative pixel error xerr = " << xerr << "\n\n";

  if (!(yerr > 0.0f))
    throw cms::Exception("PixelCPENNReco::localError")
        << "\nERROR: Negative pixel error yerr = " << yerr << "\n\n";

  //cout << "Final errors set to: " << endl;
  //cout << "xerr = " << xerr << endl;
  //cout << "yerr = " << yerr << endl;
  //cout << "Out of PixelCPENNREco..........................................................................." << endl;
  //cout << endl;

  return LocalError(xerr * xerr, 0, yerr * yerr);
}

void PixelCPENNReco::fillPSetDescription(edm::ParameterSetDescription& desc) {
  desc.add<int>("barrelTemplateID", 0);
  desc.add<int>("forwardTemplateID", 0);
  desc.add<int>("directoryWithTemplates", 0);
  desc.add<int>("speed", -2);
  desc.add<bool>("UseClusterSplitter", false);
  //some defaults for testing
  desc.add<std::string>("graphPath_x","/uscms_data/d3/ssekhar/CMSSW_11_1_2/src/TrackerStuff/PixelHitsCNN/data/graph_x_1dcnn_p1_2024_by25k_irrad_BPIXL1_022122.pb");
  desc.add<std::string>("inputTensorName_x","input_1");
  desc.add<std::string>("anglesTensorName_x","input_2");
  desc.add<std::string>("outputTensorName","Identity");
  desc.add<bool>("use_det_angles", false);
  desc.add<std::string>("cpe", "cnn1d");
}
