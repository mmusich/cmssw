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
  enum coordType {X, Y, Z, theta_X, theta_Y, theta_Z, endOfTypes}; 

  AlignPCLThresholds(){}
  virtual ~AlignPCLThresholds(){}

  void setAlignPCLThreshold(unsigned int AlignableId, const AlignPCLThreshold & Threshold);
  void setAlignPCLThresholds(const threshold_map &Thresholds);

  const threshold_map& getThreshold_Map () const  {return m_thresholds;}

  AlignPCLThreshold   getAlignPCLThreshold(unsigned int AlignableId) const;
  AlignPCLThreshold & getAlignPCLThreshold(unsigned int AlignableId);
  
  float getSigCut     (unsigned int AlignableId,coordType type) const;
  float getCut        (unsigned int AlignableId,coordType type) const;
  float getMaxMoveCut (unsigned int AlignableId,coordType type) const; 
  float getMaxErrorCut(unsigned int AlignableId,coordType type) const;

  double size()const {return m_thresholds.size();}

  void printAll() const;

 private:

  threshold_map m_thresholds;

  COND_SERIALIZABLE;

};

#endif
