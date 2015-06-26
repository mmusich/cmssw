AlCaRecoMatrix ={'ExpressCosmics' : 'SiStripCalZeroBias+TkAlCosmics0T',
                 'StreamExpress'  : 'SiStripPCLHistos+SiStripCalZeroBias+SiStripCalMinBias+TkAlMinBias',
                 'Commissioning'  : 'HcalCalIsoTrk',
                 'Cosmics'        : 'TkAlCosmics0T+MuAlGlobalCosmics+HcalCalHOCosmics+DtCalibCosmics',
                 'SingleMu'       : 'TkAlMuonIsolated+DtCalib+MuAlCalIsolatedMu+MuAlOverlaps+MuAlZMuMu',
                 'DoubleMu'       : 'MuAlCalIsolatedMu+MuAlOverlaps+MuAlZMuMu+TkAlZMuMu',
                 'MuOnia'         : 'TkAlUpsilonMuMu',
                 'Charmonium'     : 'TkAlJpsiMuMu',
                 'MET'            : 'HcalCalNoise',
                 'JetHT'          : 'HcalCalDijets',
                 'SinglePhoton'   : 'HcalCalGammaJet',
                 'SingleElectron' : 'EcalCalWElectron+EcalUncalWElectron, EcalCalZElectron, EcalUncalZElectron',
                 'DoubleEG'       : 'EcalCalZElectron+EcalUncalZElectron',
                 'ZeroBias'       : 'SiStripCalZeroBias+TkAlMinBias+LumiPixelsMinBias',
                 'HcalNZS'        : 'HcalCalMinBias+HcalCalIterativePhiSym',
                 'HLTPhysics'     : 'SiStripCalMinBias+TkAlMinBias',
                 'AlCaLumiPixels' : 'LumiPixels',
                 'TestEnabledEcalHcal' : 'HcalCalMinBias',
                  # --------------------------------------------------------------------------------------------------------------------------
                  'HcalNZS'        : 'HcalCalMinBias',
                  # This is in the AlCaRecoMatrix, but no RelVals are produced
                  # 'TestEnablesTracker' : 'TkAlLAS'
                 } 

def buildList(pdList, matrix):
    """Takes a list of primary datasets (PDs) and the AlCaRecoMatrix (a dictinary) and returns a string with all the AlCaRecos for the selected PDs separated by the '+' character without duplicates."""
    alCaRecoList = []
    for pd in pdList:
        alCaRecoList.extend(matrix[pd].split("+"))
    # remove duplicates converting to a set
    alCaRecoList = set(alCaRecoList)
    stringList = ''
    for alCaReco in alCaRecoList:
        if stringList == '':
            stringList += alCaReco
        else:
            stringList += '+'+alCaReco
    return stringList

# Update the lists anytime a new PD is added to the matrix
autoAlca = { 'allForPrompt'         : buildList(['Commissioning', 'SingleMu', 'DoubleMu', 'MuOnia', 'Charmonium', 'MET', 'JetHT', 'SingleElectron', 'SinglePhoton', 'DoubleEG', 'ZeroBias' , 'HLTPhysics', 'AlCaLumiPixels', 'HcalNZS'], AlCaRecoMatrix),
             'allForExpress'        : buildList(['StreamExpress'], AlCaRecoMatrix),
             'allForPromptCosmics'  : buildList(['Cosmics'], AlCaRecoMatrix),
             'allForExpressCosmics' : buildList(['ExpressCosmics'], AlCaRecoMatrix) }
autoAlca.update(AlCaRecoMatrix)
