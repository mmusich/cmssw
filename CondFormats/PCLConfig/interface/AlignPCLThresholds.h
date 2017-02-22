#ifndef _AlignPCLThresholds_h_
#define _AlignPCLThresholds_h_

#include "CondFormats/PCLConfig/interface/AlignPCLThreshold.h"
#include "CondFormats/Serialization/interface/Serializable.h"

#include <map>
#include <vector>

using namespace std;

class AlignPCLThresholds{
 public:
  typedef map<unsigned int,AlignPCLThreshold> threshold_map;

  AlignPCLThresholds(){}
  virtual ~AlignPCLThresholds(){}

  void setAlignPCLThreshold(unsigned int AlignableId, const AlignPCLThreshold & Threshold);
  void setAlignPCLThresholds(const threshold_map &Thresholds);

  const threshold_map& getThreshold_Map () const  {return m_thresholds;}

  AlignPCLThreshold   getAlignPCLThreshold(unsigned int AlignableId) const;
  AlignPCLThreshold & getAlignPCLThreshold(unsigned int AlignableId);
  
  double getSigCut(unsigned int AlignableId) const;
  double getXcut (unsigned int AlignableId) const;
  double getThetaXcut (unsigned int AlignableId) const;
  double getYcut (unsigned int AlignableId) const;
  double getThetaYcut (unsigned int AlignableId) const;
  double getZcut (unsigned int AlignableId) const;
  double getThetaZcut (unsigned int AlignableId) const;  
  double getMaxMoveCut (unsigned int AlignableId) const; 
  double getMaxErrorCut (unsigned int AlignableId) const;

  double size()const {return m_thresholds.size();}

 private:

  threshold_map m_thresholds;

  COND_SERIALIZABLE;

};

#endif
