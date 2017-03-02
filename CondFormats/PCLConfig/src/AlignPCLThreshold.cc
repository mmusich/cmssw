#include "CondFormats/PCLConfig/interface/AlignPCLThreshold.h"

AlignPCLThreshold:: AlignPCLThreshold(coordThresholds X,
				      coordThresholds tX,
				      coordThresholds Y,
				      coordThresholds tY,
				      coordThresholds Z, 
				      coordThresholds tZ 
				      ){
  m_xCoord      = X;	 
  m_yCoord      = Y;
  m_zCoord      = Z;	 
  m_thetaXCoord = tX;
  m_thetaYCoord = tY;
  m_thetaZCoord = tZ;

};
