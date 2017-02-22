#ifndef _AlignPCLThreshold_h_
#define _AlignPCLThreshold_h_

#include "CondFormats/Serialization/interface/Serializable.h"

class AlignPCLThreshold
{
 public:
  virtual ~AlignPCLThreshold(){}

  AlignPCLThreshold(double Xcut=5.0,double tXcut=30.0, double Ycut=10.0, double tYcut=30.0, double Zcut=15.0, double tZcut=30.0, double maxMoveCut=200.0, double maxErrorCut=10.0 );

  double getXcut()        const {return m_Xcut;}
  double getThetaXcut()   const {return m_tXcut;}
  double getYcut()        const {return m_Ycut;}
  double getThetaYcut()   const {return m_tYcut;}
  double getZcut()        const {return m_Zcut;}
  double getThetaZcut()   const {return m_tZcut;}
  double getMaxMoveCut()  const {return m_maxMoveCut;}
  double getMaxErrorCut() const {return m_maxErrorCut;}
    
 private:
  double m_Xcut;
  double m_tXcut;
  double m_Ycut;
  double m_tYcut;
  double m_Zcut;
  double m_tZcut;
  double m_maxMoveCut;
  double m_maxErrorCut;

  COND_SERIALIZABLE;

};

#endif
