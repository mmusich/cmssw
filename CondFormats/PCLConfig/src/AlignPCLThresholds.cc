#include "CondFormats/PCLConfig/interface/AlignPCLThresholds.h"
#include "CondFormats/PCLConfig/interface/AlignPCLThreshold.h"
#include "FWCore/Utilities/interface/Exception.h" 
#include <iostream>
#include <iomanip>      // std::setw

void AlignPCLThresholds::setAlignPCLThreshold(string AlignableId, const AlignPCLThreshold & Threshold) {
  m_thresholds[AlignableId]=Threshold;
}

void AlignPCLThresholds::setAlignPCLThresholds(const int & Nrecords,const threshold_map & AlignPCLThresholds){
  m_nrecords=Nrecords;
  m_thresholds=AlignPCLThresholds;
}

void AlignPCLThresholds::setNRecords(const int &Nrecords){
  m_nrecords=Nrecords;
}

AlignPCLThreshold AlignPCLThresholds::getAlignPCLThreshold(string AlignableId) const {
  threshold_map::const_iterator it = m_thresholds.find(AlignableId);

  if (it != m_thresholds.end()){
    return it->second;
  } else {
    throw cms::Exception("AlignPCLThresholds")<< "No Thresholds defined for Alignable id " << AlignableId << "\n";
  }
}

AlignPCLThreshold& AlignPCLThresholds::getAlignPCLThreshold(string AlignableId) {
  return m_thresholds[AlignableId];
}

float AlignPCLThresholds::getSigCut(string AlignableId,coordType type) const {
  AlignPCLThreshold a = getAlignPCLThreshold(AlignableId);
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

// overloaded method
array<float,6> AlignPCLThresholds::getSigCut(string AlignableId) const {
  AlignPCLThreshold a = getAlignPCLThreshold(AlignableId);
  return {{a.getSigXcut(),a.getSigYcut(), a.getSigZcut(), a.getSigThetaXcut(), a.getSigThetaYcut(),a.getSigThetaZcut()}};
}

float AlignPCLThresholds::getCut(string AlignableId,coordType type) const {
  AlignPCLThreshold a = getAlignPCLThreshold(AlignableId);
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

// overloaded method
array<float,6> AlignPCLThresholds::getCut(string AlignableId) const {
  AlignPCLThreshold a = getAlignPCLThreshold(AlignableId);
  return {{a.getXcut(),a.getYcut(), a.getZcut(), a.getThetaXcut(), a.getThetaYcut(),a.getThetaZcut()}};
}

float AlignPCLThresholds::getMaxMoveCut(string AlignableId,coordType type) const {
  AlignPCLThreshold a = getAlignPCLThreshold(AlignableId);
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

// overloaded method
array<float,6> AlignPCLThresholds::getMaxMoveCut(string AlignableId) const {
  AlignPCLThreshold a = getAlignPCLThreshold(AlignableId);
  return {{a.getMaxMoveXcut(),a.getMaxMoveYcut(), a.getMaxMoveZcut(), a.getMaxMoveThetaXcut(), a.getMaxMoveThetaYcut(),a.getMaxMoveThetaZcut()}};
}


float AlignPCLThresholds::getMaxErrorCut(string AlignableId,coordType type) const {
  AlignPCLThreshold a = getAlignPCLThreshold(AlignableId);
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

// overloaded method
array<float,6> AlignPCLThresholds::getMaxErrorCut(string AlignableId) const {
  AlignPCLThreshold a = getAlignPCLThreshold(AlignableId);
  return {{a.getErrorXcut(),a.getErrorYcut(), a.getErrorZcut(), a.getErrorThetaXcut(), a.getErrorThetaYcut(),a.getErrorThetaZcut()}};
}

void AlignPCLThresholds::printAll() const {
  
  std::cout<<"AlignPCLThresholds::printAll()"<<std::endl;
  std::cout<<" =================================================================================================================== " << std::endl;
  std::cout<<"N records cut: "<<this->getNrecords()<<std::endl;    
  for(auto it = m_thresholds.begin(); it != m_thresholds.end() ; ++it){
    std::cout<<" =================================================================================================================== " << std::endl;
    std::cout<<"key : " << it->first <<std::endl 
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
      	     <<"| sigThetaYcut     : " <<std::setw(4)<< (it->second).getSigThetaYcut()    <<std::setw(1)<<" "
	     <<"| maxMoveThetaYcut : " <<std::setw(4)<< (it->second).getMaxMoveThetaYcut()<<std::setw(5)<<" urad"
	     <<"| ErrorThetaYcut   : " <<std::setw(4)<< (it->second).getErrorThetaYcut()  <<std::setw(5)<<" urad" << std::endl

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

vector<string> AlignPCLThresholds::getAlignableList() const {
  vector<string> alignables_;
  alignables_.reserve(m_thresholds.size());

  for(auto it = m_thresholds.begin(); it != m_thresholds.end() ; ++it){
    alignables_.push_back(it->first);
  }
  return alignables_;
}
