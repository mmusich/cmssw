#ifndef SimG4Core_Field_H
#define SimG4Core_Field_H

#include "G4MagneticField.hh"

class MagneticField;

namespace sim {
  class Field : public G4MagneticField {
  public:
    Field(const MagneticField *f, double d);
    ~Field() override;
    void GetFieldValue(const G4double p[4], G4double b[3]) const override;
    void SetOffset(double x, double y, double z);
    void SetMaterialOffset(double offset) { dxi = offset; }
    double GetMaterialOffset() const { return dxi; }

  private:
    const MagneticField *theCMSMagneticField;
    double theDelta;

    mutable double oldx[3];
    mutable double oldb[3];
    
    double offset[3];
    double dxi;
  };
};  // namespace sim
#endif
