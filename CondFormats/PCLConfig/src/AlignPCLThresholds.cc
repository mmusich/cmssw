#include "CondFormats/PCLConfig/interface/AlignPCLThresholds.h"
#include "CondFormats/PCLConfig/interface/AlignPCLThreshold.h"
#include "FWCore/Utilities/interface/Exception.h" 
#include <iostream>
#include <iomanip>      // std::setw

void AlignPCLThresholds::setAlignPCLThreshold(unsigned int AlignableId, const AlignPCLThreshold & Threshold) {
  m_thresholds[AlignableId]=Threshold;
}

void AlignPCLThresholds::setAlignPCLThresholds(const threshold_map & AlignPCLThresholds){
  m_thresholds=AlignPCLThresholds;
}


AlignPCLThreshold AlignPCLThresholds::getAlignPCLThreshold(unsigned int id) const {
  threshold_map::const_iterator it = m_thresholds.find(id);

  if (it != m_thresholds.end()){
    return it->second;
  } else {
    throw cms::Exception("AlignPCLThresholds")<< "No Thresholds defined for Alignable id " << id << "\n";
  }
}

AlignPCLThreshold& AlignPCLThresholds::getAlignPCLThreshold(unsigned int id) {
  return m_thresholds[id];
}

float AlignPCLThresholds::getSigCut(unsigned int id,coordType type) const {
  AlignPCLThreshold a = getAlignPCLThreshold(id);
  switch(type){
  case X:
    return a.getSigXcut();
  case Y:
    return a.getSigYcut();
  case Z:
    return a.getSigZcut();
  case theta_X:
    return a.getSigThetaXcut();
  case theta_Y:
    return a.getSigThetaYcut();
  case theta_Z:
    return a.getSigThetaZcut();
  default:
    throw cms::Exception("AlignPCLThresholds")<<"Requested significance threshold for undefined coordinate"<< type << "\n";
  }
}

float AlignPCLThresholds::getCut(unsigned int id,coordType type) const {
  AlignPCLThreshold a = getAlignPCLThreshold(id);
  switch(type){
  case X:
    return a.getXcut();
  case Y:
    return a.getYcut();
  case Z:
    return a.getZcut();
  case theta_X:
    return a.getThetaXcut();
  case theta_Y:
    return a.getThetaYcut();
  case theta_Z:
    return a.getThetaZcut();
  default:
    throw cms::Exception("AlignPCLThresholds")<<"Requested significance threshold for undefined coordinate"<< type << "\n";
  }
}

float AlignPCLThresholds::getMaxMoveCut(unsigned int id,coordType type) const {
  AlignPCLThreshold a = getAlignPCLThreshold(id);
  switch(type){
  case X:
    return a.getMaxMoveXcut();
  case Y:
    return a.getMaxMoveYcut();
  case Z:
    return a.getMaxMoveZcut();
  case theta_X:
    return a.getMaxMoveThetaXcut();
  case theta_Y:
    return a.getMaxMoveThetaYcut();
  case theta_Z:
    return a.getMaxMoveThetaZcut();
  default:
    throw cms::Exception("AlignPCLThresholds")<<"Requested significance threshold for undefined coordinate"<< type << "\n";
  }
}

float AlignPCLThresholds::getMaxErrorCut(unsigned int id,coordType type) const {
  AlignPCLThreshold a = getAlignPCLThreshold(id);
   switch(type){
   case X:
     return a.getErrorXcut();
   case Y:
     return a.getErrorYcut();
   case Z:
     return a.getErrorZcut();
   case theta_X:
     return a.getErrorThetaXcut();
   case theta_Y:
     return a.getErrorThetaYcut();
   case theta_Z:
     return a.getErrorThetaZcut();
   default:
     throw cms::Exception("AlignPCLThresholds")<<"Requested significance threshold for undefined coordinate"<< type << "\n";
   }
}

void AlignPCLThresholds::printAll() const {
  
  std::cout<<"AlignPCLThresholds::printAll()"<<std::endl;
  for(auto it = m_thresholds.begin(); it != m_thresholds.end() ; ++it){
    std::cout<<" =================================================================================================================== " << std::endl;
    std::cout<<"keys : " << it->first <<std::endl 
	     <<"- Xcut             : " <<std::setw(4)<< (it->second).getXcut()            <<std::setw(5)<<"   um" 
	     <<"| sigXcut          : " <<std::setw(4)<< (it->second).getSigXcut()         <<std::setw(1)<<" "
	     <<"| maxMoveXcut      : " <<std::setw(4)<< (it->second).getMaxMoveXcut()     <<std::setw(5)<<"   um"
	     <<"| ErrorXcut        : " <<std::setw(4)<< (it->second).getErrorXcut()       <<std::setw(5)<<"   um" << std::endl
      
	     <<"- thetaXcut        : " <<std::setw(4)<< (it->second).getThetaXcut()       <<std::setw(5)<<" urad" 
      	     <<"| sigThetaXcut     : " <<std::setw(4)<< (it->second).getSigThetaXcut()    <<std::setw(1)<<" "
	     <<"| maxMoveThetaXcut : " <<std::setw(4)<< (it->second).getMaxMoveThetaXcut()<<std::setw(5)<<" urad"
	     <<"| ErrorThetaXcut   : " <<std::setw(4)<< (it->second).getErrorThetaXcut()  <<std::setw(5)<<" urad" << std::endl

	     <<"- Ycut             : " <<std::setw(4)<< (it->second).getYcut()            <<std::setw(5)<<"   um"  
      	     <<"| sigYcut          : " <<std::setw(4)<< (it->second).getSigXcut()         <<std::setw(1)<<" "
	     <<"| maxMoveYcut      : " <<std::setw(4)<< (it->second).getMaxMoveYcut()     <<std::setw(5)<<"   um"
	     <<"| ErrorYcut        : " <<std::setw(4)<< (it->second).getErrorYcut()       <<std::setw(5)<<"   um" << std::endl

	     <<"- thetaYcut        : " <<std::setw(4)<< (it->second).getThetaYcut()       <<std::setw(5)<<" urad" 
      	     <<"| sigthetaYcut     : " <<std::setw(4)<< (it->second).getSigThetaYcut()    <<std::setw(1)<<" "
	     <<"| maxMovethetaYcut : " <<std::setw(4)<< (it->second).getMaxMoveThetaYcut()<<std::setw(5)<<" urad"
	     <<"| ErrorthetaYcut   : " <<std::setw(4)<< (it->second).getErrorThetaYcut()  <<std::setw(5)<<" urad" << std::endl

	     <<"- Zcut             : " <<std::setw(4)<< (it->second).getZcut()            <<std::setw(5)<<"   um"	     
      	     <<"| sigZcut          : " <<std::setw(4)<< (it->second).getSigZcut()         <<std::setw(1)<<" "	     
	     <<"| maxMoveZcut      : " <<std::setw(4)<< (it->second).getMaxMoveZcut()     <<std::setw(5)<<"   um"	     
	     <<"| ErrorZcut        : " <<std::setw(4)<< (it->second).getErrorZcut()       <<std::setw(5)<<"   um" << std::endl
      
	     <<"- thetaZcut        : " <<std::setw(4)<< (it->second).getThetaZcut()       <<std::setw(5)<<" urad" 
      	     <<"| sigThetaZcut     : " <<std::setw(4)<< (it->second).getSigThetaZcut()    <<std::setw(1)<<" "
	     <<"| maxMoveThetaZcut : " <<std::setw(4)<< (it->second).getMaxMoveThetaZcut()<<std::setw(5)<<" urad"
	     <<"| ErrorThetaZcut   : " <<std::setw(4)<< (it->second).getErrorThetaZcut()  <<std::setw(5)<<" urad" 

	     <<std::endl;
  }
}


