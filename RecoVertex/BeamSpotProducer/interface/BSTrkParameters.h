#ifndef BeamSpotProducer_BSTrkParameters_h
#define BeamSpotProducer_BSTrkParameters_h

/**_________________________________________________________________
   class:   BSTrkParameters.h
   package: RecoVertex/BeamSpotProducer
   
   author: Francisco Yumiceva, Fermilab (yumiceva@fnal.gov)
________________________________________________________________**/

class BSTrkParameters {
public:
  // constructor
  BSTrkParameters() {}
  // constructor from values
  BSTrkParameters(float z0,
                  float sigz0,
                  float d0,
                  float sigd0,
                  float phi0,
                  float pt,
                  float d0phi_d0 = 0.,
                  float d0phi_chi2 = 0.) {
    fz0 = z0;
    fsigz0 = sigz0;
    fd0 = d0;
    fsigd0 = sigd0;
    fphi0 = phi0;
    fpt = pt;
    fd0phi_d0 = d0phi_d0;
    fd0phi_chi2 = d0phi_chi2;
    fvx = 0.;
    fvy = 0.;
  };

  //
  float z0() const { return fz0; }
  float sigz0() const { return fsigz0; }
  float d0() const { return fd0; }
  float sigd0() const { return fsigd0; }
  float phi0() const { return fphi0; }
  float pt() const { return fpt; }
  float d0phi_chi2() const { return fd0phi_chi2; }
  float d0phi_d0() const { return fd0phi_d0; }
  float vx() const { return fvx; }
  float vy() const { return fvy; }
  void setVx(float vx) { fvx = vx; }
  void setVy(float vy) { fvy = vy; }

private:
  float fz0;
  float fsigz0;
  float fd0;
  float fsigd0;
  float fphi0;
  float fpt;
  float fd0phi_chi2;
  float fd0phi_d0;
  float fvx;
  float fvy;
};

#endif
