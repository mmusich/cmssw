#include "CondFormats/PCLConfig/interface/AlignPCLThresholds.h"
#include "FWCore/Utilities/interface/Exception.h" 
#include <iostream>

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

  AlignPCLThreshold a;
  return a;
}

AlignPCLThreshold& AlignPCLThresholds::getAlignPCLThreshold(unsigned int id) {
  return m_thresholds[id];
}

double AlignPCLThresholds::getSigCut(unsigned int id) const {
  AlignPCLThreshold a = getAlignPCLThreshold(id);
  double sig= a.getSigCut();
  return sig;
}

double AlignPCLThresholds::getXcut(unsigned int id) const {
  AlignPCLThreshold a = getAlignPCLThreshold(id);
  double x= a.getXcut();
  return x;
}

double AlignPCLThresholds::getThetaXcut(unsigned int id) const {
  AlignPCLThreshold a = getAlignPCLThreshold(id);
  double tx= a.getThetaXcut();
  return tx;
}

double AlignPCLThresholds::getYcut(unsigned int id) const {
  AlignPCLThreshold a = getAlignPCLThreshold(id);
  double y= a.getYcut();
  return y;
}

double AlignPCLThresholds::getThetaYcut(unsigned int id) const {
  AlignPCLThreshold a = getAlignPCLThreshold(id);
  double ty= a.getThetaYcut();
  return ty;
}

double AlignPCLThresholds::getZcut(unsigned int id) const {
  AlignPCLThreshold a = getAlignPCLThreshold(id);
  double z= a.getZcut();
  return z;
}

double AlignPCLThresholds::getThetaZcut(unsigned int id) const {
  AlignPCLThreshold a = getAlignPCLThreshold(id);
  double tz= a.getThetaZcut();
  return tz;
}

double AlignPCLThresholds::getMaxMoveCut(unsigned int id) const {
  AlignPCLThreshold a = getAlignPCLThreshold(id);
  double maxcut= a.getMaxMoveCut();
  return maxcut;
}

double AlignPCLThresholds::getMaxErrorCut(unsigned int id) const {
  AlignPCLThreshold a = getAlignPCLThreshold(id);
  double maxerrorcut= a.getMaxErrorCut();
  return maxerrorcut;
}



