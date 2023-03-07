// system includes
#include <map>
#include <memory>
#include <string>
#include <iostream>
#include <fstream>

// user includes
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/SiPixelDetId/interface/PXBDetId.h"
#include "DataFormats/SiPixelDetId/interface/PXFDetId.h"
#include "DataFormats/SiPixelDetId/interface/PixelSubdetector.h"
#include "DataFormats/TrackerCommon/interface/PixelBarrelName.h"
#include "DataFormats/TrackerCommon/interface/PixelEndcapName.h"
#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "Geometry/CommonDetUnit/interface/PixelGeomDetUnit.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/Records/interface/TrackerTopologyRcd.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"

//#define CHECK_ORIENT

class SiPixelDetsAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  SiPixelDetsAnalyzer(const edm::ParameterSet& conf);
  ~SiPixelDetsAnalyzer() override = default;
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void printDet(DetId detid, const TrackerTopology* tt);

private:
  bool phase1_;
  const edm::ESGetToken<TrackerTopology, TrackerTopologyRcd> trackerTopoToken_;
  const edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> trackerGeomToken_;
  const edm::ESGetToken<MagneticField, IdealMagneticFieldRecord> magfieldToken_;
};

using namespace std;
using namespace edm;

//Constructor

SiPixelDetsAnalyzer::SiPixelDetsAnalyzer(edm::ParameterSet const& conf)
    : phase1_(conf.getUntrackedParameter<bool>("phase1", false)),
      trackerTopoToken_(esConsumes()),
      trackerGeomToken_(esConsumes()),
      magfieldToken_(esConsumes()) {
  usesResource("TFileService");
}

// Analyzer: Functions that gets called by framework every event
void SiPixelDetsAnalyzer::analyze(const edm::Event& e, const edm::EventSetup& es) {
  const bool PRINT = false;
  const bool PRINT_TABLE = true;
  const bool doReversedTest = false;

  edm::ESHandle<TrackerGeometry> tkgeom = es.getHandle(trackerGeomToken_);
  const TrackerGeometry& theTracker(*tkgeom);
  edm::ESHandle<TrackerTopology> tTopoH = es.getHandle(trackerTopoToken_);
  const TrackerTopology* tTopo = tTopoH.product();

  edm::ESHandle<MagneticField> magfield = es.getHandle(magfieldToken_);

  if (PRINT)
    cout << " There are " << tkgeom->detUnits().size() << " detectors" << std::endl;

  // Test new TrackerGeometry features
  cout << "Test of TrackerGeometry::isThere";
  cout << " is there PixelBarrel: " << tkgeom->isThere(GeomDetEnumerators::PixelBarrel);
  cout << " is there PixelEndcap: " << tkgeom->isThere(GeomDetEnumerators::PixelEndcap);
  cout << " is there P1PXB: " << tkgeom->isThere(GeomDetEnumerators::P1PXB);
  cout << " is there P1PXEC: " << tkgeom->isThere(GeomDetEnumerators::P1PXEC);
  cout << endl;

  // switch on the phase1
  if ((tkgeom->isThere(GeomDetEnumerators::P1PXB)) && (tkgeom->isThere(GeomDetEnumerators::P1PXEC)))
    phase1_ = true;
  else
    phase1_ = false;

  if (phase1_)
    cout << "This is for phase1 geometry " << endl;

  //for(TrackerGeometry::DetUnitContainer::const_iterator it = tkgeom->detUnits().begin();
  for (TrackerGeometry::DetContainer::const_iterator it = tkgeom->detUnits().begin(); it != tkgeom->detUnits().end();
       it++) {
    // Is it a pixel detetector
    if (dynamic_cast<PixelGeomDetUnit const*>((*it)) == 0)
      continue;  // no, than skip

    DetId detId = (*it)->geographicalId();

    const GeomDetUnit* geoUnit = tkgeom->idToDetUnit(detId);
    const PixelGeomDetUnit* pixDet = dynamic_cast<const PixelGeomDetUnit*>(geoUnit);
    const PixelTopology& topol = pixDet->specificTopology();

    // Get the module sizes.
    int nrows = topol.nrows();     // rows in x
    int ncols = topol.ncolumns();  // cols in y
    double detThick = pixDet->specificSurface().bounds().thickness();
    double detZ = pixDet->surface().position().z();
    double detR = pixDet->surface().position().perp();
    double detPhi = pixDet->surface().position().phi();
    GlobalVector normVect = pixDet->surface().normalVector();
    // add the module direction, so we know the E field

    if (PRINT)
      cout << "Position " << detR << " " << detZ << " " << detPhi << " " << detThick << " " << nrows << " " << ncols
           << endl;

#ifdef CHECK_ORIENT
    //const PixelGeomDetUnit * pixDet  = dynamic_cast<const PixelGeomDetUnit*>(geoUnit);
    const PixelTopology* ptopol = &(pixDet->specificTopology());

    MeasurementPoint mp1(0., 0.);
    LocalPoint lp1 = ptopol->localPosition(mp1);
    //cout<<lp1.x()<<" "<<lp1.y()<<endl;
    GlobalPoint gp1 = pixDet->surface().toGlobal(lp1);  // or need? Local3DPoint?
    //cout<<gp1.x()<<" "<<gp1.y()<<endl;

    MeasurementPoint mp2((float(nrows) - 1.), (float(ncols) - 1.));
    LocalPoint lp2 = ptopol->localPosition(mp2);
    //cout<<lp2.x()<<" "<<lp2.y()<<endl;
    GlobalPoint gp2 = pixDet->surface().toGlobal(lp2);  // or need? Local3DPoint?

    LocalPoint lp3(0., 0.);
    //cout<<lp3.x()<<" "<<lp3.y()<<endl;
    GlobalPoint gp3 = pixDet->surface().toGlobal(lp3);  // or need? Local3DPoint?

    LocalVector Bfield = pixDet->surface().toLocal(magfield->inTesla(pixDet->surface().position()));

#endif  // CHECK_ORIENT

    // bpix
    if (detId.subdetId() == static_cast<int>(PixelSubdetector::PixelBarrel)) {
      //continue;

      unsigned int rawId = detId.rawId();
      if (PRINT)
        cout << "Det raw: " << rawId << " " << detId.null() << " " << detId.det() << " " << detId.subdetId() << endl;
      //cout<<" print det "<< tTopo->print(detId) <<endl; // does not seem to work in 752

      // Use new indecies
      // Barell layer = 1,2,3
      unsigned int layerC = tTopo->pxbLayer(detId);
      // Barrel ladder id 1-20,32,44.
      unsigned int ladderC = tTopo->pxbLadder(detId);
      // Barrel Z-index=1,8
      unsigned int zindex = tTopo->pxbModule(detId);

      if (PRINT)
        cout << " Barrel layer, ladder, module " << layerC << " " << ladderC << " " << zindex << endl;

      //printDet(detId, tTopo);

      // Convert to online
      PixelBarrelName pbn(detId, tTopo, phase1_);  // use det-id
      //PixelBarrelName pbn(detId, tTopo, false); // use det-id, select phase0
      //PixelBarrelName pbn(detId, tTopo, true); // use det-id, select phase1
      //PixelBarrelName pbn(pxdetid); // or pixel det id
      PixelBarrelName::Shell sh = pbn.shell();  //enum
      int sector = pbn.sectorName();
      int ladder = pbn.ladderName();
      int layer = pbn.layerName();
      int module = pbn.moduleName();
      bool half = pbn.isHalfModule();
      string name = pbn.name();
      PixelModuleName::ModuleType moduleType = pbn.moduleType();
      DetId det = pbn.getDetId(tTopo);

      // Sometimes we also use the additional sign convention
      int ladderSigned = ladder;
      int moduleSigned = module;
      // Shell { mO = 1, mI = 2 , pO =3 , pI =4 };
      int shell = int(sh);
      // change the module sign for z<0
      if (shell == 1 || shell == 2)
        moduleSigned = -module;
      // change ladeer sign for Outer )x<0)
      if (shell == 1 || shell == 3)
        ladderSigned = -ladder;

      if (PRINT)
        cout << " shell " << sh << "(" << shell << ") " << sector << " " << layer << " " << ladderSigned << " "
             << moduleSigned << " " << half << " " << name << " " << moduleType << " " << det.rawId() << " " << endl;

      if (PRINT_TABLE)
        cout << detId.rawId() << " " << name << " r/phi/z = " << detR << "/" << detPhi << "/" << detZ
             << " cmssw layer/ladder/module " << layerC << "/" << ladderC << "/" << zindex << " E-phi "
             << normVect.phi()  // <<" "<<normVect.perp()   <<" "<<normVect.barePhi() same
             << endl;

      // Now check if teh id is the same
      if (rawId != det.rawId())
        cout << " Wrong bpix ID, old = " << rawId << " new = " << det.rawId() << endl;

      if (!phase1_) {
        PXBDetId pxbdet = pbn.getDetId();
        if (rawId != pxbdet.rawId())
          cout << " Wrong bpix (old) ID, old = " << rawId << " new = " << pxbdet.rawId() << endl;
      }

      // Check the revers transformation (special test)
      if (doReversedTest) {
        PixelBarrelName pbn2(name, phase1_);  // use name to get detId
        //PixelBarrelName pbn2(name); // use name to get detId
        //cout<<name<<" "<<pbn2.name()<<endl;
        PixelBarrelName::Shell sh2 = pbn2.shell();  //enum
        int sector2 = pbn2.sectorName();
        int ladder2 = pbn2.ladderName();
        int layer2 = pbn2.layerName();
        int module2 = pbn2.moduleName();
        string name2 = pbn2.name();
        PixelModuleName::ModuleType moduleType2 = pbn2.moduleType();
        DetId det2 = pbn2.getDetId(tTopo);
        if (name != name2)
          cout << " wrong  name " << endl;
        if (shell != sh2)
          cout << " wrong shell " << endl;
        if (sector != sector2)
          cout << " wrong sector " << endl;
        if (layer != layer2)
          cout << " wrong layer " << endl;
        if (ladder != ladder2)
          cout << " wrong ladder " << endl;
        if (module != module2)
          cout << " wrong module " << endl;
        if (moduleType != moduleType2)
          cout << " wrong module type " << endl;
        if (det2.rawId() != det.rawId())
          cout << " wrong rawid " << endl;
      }

#ifdef CHECK_ORIENT
      cout << "     0-0:  " << lp1.x() << " " << lp1.y() << " " << gp1.x() << " " << gp1.y() << " " << gp1.z() << " "
           << gp1.perp() << " " << gp1.phi() << " " << gp1.z() << endl;
      cout << "   " << (nrows - 1) << "-" << (ncols - 1) << ": " << lp2.x() << " " << lp2.y() << " " << gp2.x() << " "
           << gp2.y() << " " << gp2.z() << " " << gp2.perp() << " " << gp2.phi() << " " << gp2.z() << endl;
      cout << " center: " << lp3.x() << " " << lp3.y() << " " << gp3.x() << " " << gp3.y() << " " << gp3.z() << " "
           << gp3.perp() << " " << gp3.phi() << " " << gp3.z() << endl;
      cout << " B: " << Bfield.x() << " " << Bfield.y() << " " << Bfield.z() << endl;
#endif  // CHECK_ORIENT

      // FPIX
    } else if (detId.subdetId() == static_cast<int>(PixelSubdetector::PixelEndcap)) {
      // Now the fpix values
      //continue;

      unsigned int rawId = detId.rawId();

      if (PRINT)
        cout << "Det: " << rawId << " " << detId.null() << " " << detId.det() << " " << detId.subdetId() << endl;

      // new ids
      int disk = tTopo->pxfDisk(detId);    //1,2,3
      int blade = tTopo->pxfBlade(detId);  // 1-56, goes over all blades for ring 1 and ring2 in sequence
      int plaq = tTopo->pxfModule(detId);  // always 1 for phase1
      int side = tTopo->pxfSide(detId);    //sizd=1 for -z, 2 for +z
      int panel = tTopo->pxfPanel(detId);  //panel=1,2, the side of the blade

      if (PRINT)
        cout << "endcap, side=" << side << " disk=" << disk << ", blade=" << blade << ", panel=" << panel << endl;

      // Convert to online
      PixelEndcapName pen(detId, tTopo, phase1_);  // use det-id phase0
      //PixelEndcapName pen(detId,tTopo,false); // use det-id phase0
      //PixelEndcapName pen(detId,tTopo,true); // use det-id phase1
      PixelEndcapName::HalfCylinder sh = pen.halfCylinder();  //enum
      string nameF = pen.name();
      int diskName = pen.diskName();
      int bladeName = pen.bladeName();
      int pannelName = pen.pannelName();
      int plaquetteName = pen.plaquetteName();
      int ringName = pen.ringName();
      DetId det = pen.getDetId(tTopo);
      //PixelEndcapName::HalfCylinder part = pen.halfCylinder();
      PixelModuleName::ModuleType moduleType = pen.moduleType();
      if (PRINT)
        cout << sh << " " << nameF << " " << diskName << " " << bladeName << " " << pannelName << " " << plaquetteName
             << " " << ringName << " " << moduleType << " " << det.rawId() << endl;

      if (PRINT_TABLE)
        cout << rawId << " " << nameF << " r/phi/z = " << detR << "/" << detPhi << "/" << detZ
             << " cmssw side/disk/blade/pannel/plaq=" << side << "/" << disk << "/" << blade << "/" << panel << "/"
             << plaq << " E-z " << normVect.z() << endl;

      // Now check if teh id is the same
      if (rawId != det.rawId())
        cout << " Wrong fpix ID, old = " << rawId << " new = " << det.rawId() << endl;

      if (!phase1_) {
        PXFDetId pxfdet = pen.getDetId();
        if (rawId != pxfdet.rawId())
          cout << " Wrong fpix (old) ID, old = " << rawId << " new = " << pxfdet.rawId() << endl;
      }

      // Reverse the transformation to check the name translation
      if (doReversedTest) {
        PixelEndcapName pen2(nameF, phase1_);  // get id from name

        PixelEndcapName::HalfCylinder sh2 = pen2.halfCylinder();  //enum
        string nameF2 = pen2.name();
        int diskName2 = pen2.diskName();
        int bladeName2 = pen2.bladeName();
        int pannelName2 = pen2.pannelName();
        int plaquetteName2 = pen2.plaquetteName();
        DetId det2 = pen2.getDetId(tTopo);
        PixelModuleName::ModuleType moduleType2 = pen2.moduleType();
        if (nameF != nameF2)
          cout << " wrong name " << endl;
        if (sh != sh2)
          cout << " wrong shell " << endl;
        if (diskName != diskName2)
          cout << " wrong disk " << endl;
        if (bladeName != bladeName2)
          cout << " wrong blade " << endl;
        if (pannelName != pannelName2)
          cout << " wrong panel " << endl;
        if (plaquetteName != plaquetteName2)
          cout << " wrong plaquette " << endl;
        if (moduleType != moduleType2)
          cout << " wrong module type " << endl;
        if (det.rawId() != det2.rawId())
          cout << " wrong rawid " << endl;
      }

#ifdef CHECK_ORIENT
      cout << "     0-0:  " << lp1.x() << " " << lp1.y() << " " << gp1.perp() << " " << gp1.phi() << " " << gp1.z()
           << endl;
      cout << "   " << (nrows - 1) << "-" << (ncols - 1) << ": " << lp2.x() << " " << lp2.y() << " " << gp2.perp()
           << " " << gp2.phi() << " " << gp2.z() << endl;
      cout << " center: " << lp3.x() << " " << lp3.y() << " " << gp3.perp() << " " << gp3.phi() << " " << gp3.z()
           << endl;
      cout << " B: " << Bfield.x() << " " << Bfield.y() << " " << Bfield.z() << endl;
#endif  // CHECK_ORIENT

    } else {  // b/fpix

      cout << "detid is Pixel but neither bpix nor fpix" << endl;

    }  // b/fpix

  }  // end for det loop
}

void SiPixelDetsAnalyzer::printDet(DetId detid, const TrackerTopology* tt) {
  // new indecies
  // Barell layer = 1,2,3
  unsigned int layer = tt->pxbLayer(detid);
  // Barrel ladder id 1-20,32,44.
  unsigned int ladder = tt->pxbLadder(detid);
  // Barrel Z-index=1,8
  unsigned int zindex = tt->pxbModule(detid);
  cout << " Barrel layer, ladder, module " << layer << " " << ladder << " " << zindex << endl;
}

//define this as a plug-in
DEFINE_FWK_MODULE(SiPixelDetsAnalyzer);
