#include "CondFormats/PCLConfig/interface/AlignPCLThreshold.h"

 AlignPCLThreshold:: AlignPCLThreshold(double Xcut,double tXcut, 
				       double Ycut,double tYcut, 
				       double Zcut,double tZcut, 
				       double maxMoveCut,double maxErrorCut 
				       ){
   
   m_Xcut        = Xcut;              
   m_tXcut       = tXcut;      
   m_Ycut        = Ycut;       
   m_tYcut       = tYcut;      
   m_Zcut        = Zcut;       
   m_tZcut       = tZcut;      
   m_maxMoveCut  = maxMoveCut; 
   m_maxErrorCut = maxErrorCut;

};
