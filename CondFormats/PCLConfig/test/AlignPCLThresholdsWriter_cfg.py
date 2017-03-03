import FWCore.ParameterSet.Config as cms

process = cms.Process("ProcessOne")

process.source = cms.Source("EmptyIOVSource",
    timetype = cms.string('runnumber'),
                            firstValue = cms.uint64(1),
                            lastValue = cms.uint64(1),
                            interval = cms.uint64(1)
                            )
#Database output service

process.load("CondCore.CondDB.CondDB_cfi")
# output database (in this case local sqlite file)
process.CondDB.connect = 'sqlite_file:mythresholds.db'


process.PoolDBOutputService = cms.Service("PoolDBOutputService",
                                          process.CondDB,
                                          timetype = cms.untracked.string('runnumber'),
                                          toPut = cms.VPSet(cms.PSet(record = cms.string('AlignPCLThresholdsRcd'),
                                                                     tag = cms.string('PCLThresholds_express_v0')
                                                                     )
                                                            )
                                          )

process.WriteInDB = cms.EDAnalyzer("AlignPCLThresholdsWriter",
                                   record= cms.string('AlignPCLThresholdsRcd'),
                                   thresholds = cms.VPSet(cms.PSet(#### Barrel Pixel HB X- 
                                                                   alignableId        = cms.string("TPBHalfBarrelXminus"),
                                                                   Xcut               = cms.double(5.0),
                                                                   sigXcut            = cms.double(2.5),
                                                                   maxMoveXcut        = cms.double(200.0),
                                                                   maxErrorXcut       = cms.double(10.0),                                                               

                                                                   thetaXcut          = cms.double(30.0),
                                                                   sigThetaXcut       = cms.double(2.5),
                                                                   maxMoveThetaXcut   = cms.double(200.0),
                                                                   maxErrorThetaXcut  = cms.double(10.0),

                                                                   Ycut               = cms.double(10.0),
                                                                   sigYcut            = cms.double(2.5),
                                                                   maxMoveYcut        = cms.double(200.0),
                                                                   maxErrorYcut       = cms.double(10.0),                       

                                                                   thetaYcut          = cms.double(30.0),
                                                                   sigThetaYcut       = cms.double(2.5),
                                                                   maxMoveThetaYcut   = cms.double(200.0),
                                                                   maxErrorThetaYcut  = cms.double(10.0),

                                                                   Zcut               = cms.double(15.0),
                                                                   sigZcut            = cms.double(2.5),
                                                                   maxMoveZcut        = cms.double(200.0),
                                                                   maxErrorZcut       = cms.double(10.0),

                                                                   thetaZcut          = cms.double(30.0),
                                                                   sigThetaZcut       = cms.double(2.5),
                                                                   maxMoveThetaZcut   = cms.double(200.0),
                                                                   maxErrorThetaZcut  = cms.double(10.0)                         
                                                                   ),

                                                          ### Barrel Pixel HB X+
                                                          cms.PSet(alignableId        = cms.string("TPBHalfBarrelXplus"),
                                                                   Xcut               = cms.double(5.0),
                                                                   sigXcut            = cms.double(2.5),
                                                                   maxMoveXcut        = cms.double(200.0),
                                                                   maxErrorXcut       = cms.double(10.0),     
                                                          
                                                                   thetaXcut          = cms.double(30.0),
                                                                   sigThetaXcut       = cms.double(2.5),
                                                                   maxMoveThetaXcut   = cms.double(200.0),
                                                                   maxErrorThetaXcut  = cms.double(10.0),

                                                                   Ycut               = cms.double(10.0),
                                                                   sigYcut            = cms.double(2.5),
                                                                   maxMoveYcut        = cms.double(200.0),
                                                                   maxErrorYcut       = cms.double(10.0),                       

                                                                   thetaYcut          = cms.double(30.0),
                                                                   sigThetaYcut       = cms.double(2.5),
                                                                   maxMoveThetaYcut   = cms.double(200.0),
                                                                   maxErrorThetaYcut  = cms.double(10.0),

                                                                   Zcut               = cms.double(15.0),
                                                                   sigZcut            = cms.double(2.5),
                                                                   maxMoveZcut        = cms.double(200.0),
                                                                   maxErrorZcut       = cms.double(10.0),

                                                                   thetaZcut          = cms.double(30.0),
                                                                   sigThetaZcut       = cms.double(2.5),
                                                                   maxMoveThetaZcut   = cms.double(200.0),
                                                                   maxErrorThetaZcut  = cms.double(10.0)                         
                                                                   ),
                                                          
                                                          ### Forward Pixel HC X-,Z-
                                                          cms.PSet(alignableId        = cms.string("TPEHalfCylinderXminusZminus"),
                                                                   Xcut               = cms.double(5.0),
                                                                   sigXcut            = cms.double(2.5),
                                                                   maxMoveXcut        = cms.double(200.0),
                                                                   maxErrorXcut       = cms.double(10.0),                                                               

                                                                   thetaXcut          = cms.double(30.0),
                                                                   sigThetaXcut       = cms.double(2.5),
                                                                   maxMoveThetaXcut   = cms.double(200.0),
                                                                   maxErrorThetaXcut  = cms.double(10.0),

                                                                   Ycut               = cms.double(10.0),
                                                                   sigYcut            = cms.double(2.5),
                                                                   maxMoveYcut        = cms.double(200.0),
                                                                   maxErrorYcut       = cms.double(10.0),                       

                                                                   thetaYcut          = cms.double(30.0),
                                                                   sigThetaYcut       = cms.double(2.5),
                                                                   maxMoveThetaYcut   = cms.double(200.0),
                                                                   maxErrorThetaYcut  = cms.double(10.0),

                                                                   Zcut               = cms.double(15.0),
                                                                   sigZcut            = cms.double(2.5),
                                                                   maxMoveZcut        = cms.double(200.0),
                                                                   maxErrorZcut       = cms.double(10.0),

                                                                   thetaZcut          = cms.double(30.0),
                                                                   sigThetaZcut       = cms.double(2.5),
                                                                   maxMoveThetaZcut   = cms.double(200.0),
                                                                   maxErrorThetaZcut  = cms.double(10.0)                         
                                                                   ),

                                                          ### Forward Pixel HC X+,Z-
                                                          cms.PSet(alignableId        = cms.string("TPEHalfCylinderXplusZminus"),
                                                                   Xcut               = cms.double(5.0),
                                                                   sigXcut            = cms.double(2.5),
                                                                   maxMoveXcut        = cms.double(200.0),
                                                                   maxErrorXcut       = cms.double(10.0),                                                               
                                                                   
                                                                   thetaXcut          = cms.double(30.0),
                                                                   sigThetaXcut       = cms.double(2.5),
                                                                   maxMoveThetaXcut   = cms.double(200.0),
                                                                   maxErrorThetaXcut  = cms.double(10.0),
                                                                   
                                                                   Ycut               = cms.double(10.0),
                                                                   sigYcut            = cms.double(2.5),
                                                                   maxMoveYcut        = cms.double(200.0),
                                                                   maxErrorYcut       = cms.double(10.0),                       
                                                                   
                                                                   thetaYcut          = cms.double(30.0),
                                                                   sigThetaYcut       = cms.double(2.5),
                                                                   maxMoveThetaYcut   = cms.double(200.0),
                                                                   maxErrorThetaYcut  = cms.double(10.0),
                                                                   
                                                                   Zcut               = cms.double(15.0),
                                                                   sigZcut            = cms.double(2.5),
                                                                   maxMoveZcut        = cms.double(200.0),
                                                                   maxErrorZcut       = cms.double(10.0),
                                                                   
                                                                   thetaZcut          = cms.double(30.0),
                                                                   sigThetaZcut       = cms.double(2.5),
                                                                   maxMoveThetaZcut   = cms.double(200.0),
                                                                   maxErrorThetaZcut  = cms.double(10.0)                         
                                                                   ),

                                                          ### Forward Pixel HC X-,Z+
                                                          cms.PSet(alignableId        = cms.string("TPEHalfCylinderXminusZplus"),
                                                                   Xcut               = cms.double(5.0),
                                                                   sigXcut            = cms.double(2.5),
                                                                   maxMoveXcut        = cms.double(200.0),
                                                                   maxErrorXcut       = cms.double(10.0),                                                               
                                                                   
                                                                   thetaXcut          = cms.double(30.0),
                                                                   sigThetaXcut       = cms.double(2.5),
                                                                   maxMoveThetaXcut   = cms.double(200.0),
                                                                   maxErrorThetaXcut  = cms.double(10.0),
                                                                   
                                                                   Ycut               = cms.double(10.0),
                                                                   sigYcut            = cms.double(2.5),
                                                                   maxMoveYcut        = cms.double(200.0),
                                                                   maxErrorYcut       = cms.double(10.0),                       
                                                                   
                                                                   thetaYcut          = cms.double(30.0),
                                                                   sigThetaYcut       = cms.double(2.5),
                                                                   maxMoveThetaYcut   = cms.double(200.0),
                                                                   maxErrorThetaYcut  = cms.double(10.0),
                                                                   
                                                                   Zcut               = cms.double(15.0),
                                                                   sigZcut            = cms.double(2.5),
                                                                   maxMoveZcut        = cms.double(200.0),
                                                                   maxErrorZcut       = cms.double(10.0),
                                                                   
                                                                   thetaZcut          = cms.double(30.0),
                                                                   sigThetaZcut       = cms.double(2.5),
                                                                   maxMoveThetaZcut   = cms.double(200.0),
                                                                   maxErrorThetaZcut  = cms.double(10.0)                         
                                                                   ),

                                                          ### Forward Pixel HC X+,Z+
                                                          cms.PSet(alignableId        = cms.string("TPEHalfCylinderXplusZplus"),
                                                                   Xcut               = cms.double(5.0),
                                                                   sigXcut            = cms.double(2.5),
                                                                   maxMoveXcut        = cms.double(200.0),
                                                                   maxErrorXcut       = cms.double(10.0),                                                               
                                                                   
                                                                   thetaXcut          = cms.double(30.0),
                                                                   sigThetaXcut       = cms.double(2.5),
                                                                   maxMoveThetaXcut   = cms.double(200.0),
                                                                   maxErrorThetaXcut  = cms.double(10.0),
                                                                   
                                                                   Ycut               = cms.double(10.0),
                                                                   sigYcut            = cms.double(2.5),
                                                                   maxMoveYcut        = cms.double(200.0),
                                                                   maxErrorYcut       = cms.double(10.0),                       
                                                                   
                                                                   thetaYcut          = cms.double(30.0),
                                                                   sigThetaYcut       = cms.double(2.5),
                                                                   maxMoveThetaYcut   = cms.double(200.0),
                                                                   maxErrorThetaYcut  = cms.double(10.0),
                                                                   
                                                                   Zcut               = cms.double(15.0),
                                                                   sigZcut            = cms.double(2.5),
                                                                   maxMoveZcut        = cms.double(200.0),
                                                                   maxErrorZcut       = cms.double(10.0),
                                                                   
                                                                   thetaZcut          = cms.double(30.0),
                                                                   sigThetaZcut       = cms.double(2.5),
                                                                   maxMoveThetaZcut   = cms.double(200.0),
                                                                   maxErrorThetaZcut  = cms.double(10.0)                         
                                                                   )
                                                          )
                                   )

process.p = cms.Path(process.WriteInDB)
