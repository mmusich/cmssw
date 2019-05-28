#!/usr/bin/env python
#test execute: export CMSSW_BASE=/tmp/CMSSW && ./validateAlignments.py -c defaultCRAFTValidation.ini,test.ini -n -N test
from __future__ import print_function
import subprocess
import os
import sys
import optparse
import datetime
import shutil
import fnmatch
import fileinput
import fileinput
from abc import ABCMeta, abstractmethod
import copy
import itertools
import pprint

import six
import Alignment.OfflineValidation.TkAlAllInOneTool.configTemplates \
    as configTemplates
import Alignment.OfflineValidation.TkAlAllInOneTool.crabWrapper as crabWrapper
from Alignment.OfflineValidation.TkAlAllInOneTool.TkAlExceptions \
    import AllInOneError
from Alignment.OfflineValidation.TkAlAllInOneTool.helperFunctions \
    import replaceByMap, getCommandOutput2, addIndex
from Alignment.OfflineValidation.TkAlAllInOneTool.betterConfigParser \
    import BetterConfigParser
from Alignment.OfflineValidation.TkAlAllInOneTool.alignment import Alignment

from Alignment.OfflineValidation.TkAlAllInOneTool.genericValidation \
    import GenericValidation, ParallelValidation, ValidationWithComparison, ValidationWithPlots
from Alignment.OfflineValidation.TkAlAllInOneTool.geometryComparison \
    import GeometryComparison
from Alignment.OfflineValidation.TkAlAllInOneTool.offlineValidation \
    import OfflineValidation, OfflineValidationDQM
from Alignment.OfflineValidation.TkAlAllInOneTool.monteCarloValidation \
    import MonteCarloValidation
from Alignment.OfflineValidation.TkAlAllInOneTool.trackSplittingValidation \
    import TrackSplittingValidation
from Alignment.OfflineValidation.TkAlAllInOneTool.zMuMuValidation \
    import ZMuMuValidation
from Alignment.OfflineValidation.TkAlAllInOneTool.primaryVertexValidation \
    import PrimaryVertexValidation
from Alignment.OfflineValidation.TkAlAllInOneTool.preexistingValidation \
    import *
from Alignment.OfflineValidation.TkAlAllInOneTool.plottingOptions \
    import PlottingOptions
import Alignment.OfflineValidation.TkAlAllInOneTool.globalDictionaries \
    as globalDictionaries
from Alignment.OfflineValidation.TkAlAllInOneTool.overlapValidation \
    import OverlapValidation 

####################--- Classes ---############################
class ParallelMergeJob(object):
    
    def __init__(self, _name, _path, _dependency):
        self.name=_name
        self.path=_path
        self.dependencies=_dependency
    def addDependency(self,dependency):
        if isinstance(dependency,list):
            self.dependencies.extend(dependency)
        else:
            self.dependencies.append(dependency)
    def runJob(self, config):
        repMap = {
        "commands": config.getGeneral()["jobmode"].split(",")[1],
        "jobName": self.name,
        "logDir": config.getGeneral()["logdir"],
        "script": self.path,
        "bsub": "/afs/cern.ch/cms/caf/scripts/cmsbsub",
        "conditions": '"' + " && ".join(["ended(" + jobId + ")" for jobId in self.dependencies]) + '"'
        }
        return getCommandOutput2("%(bsub)s %(commands)s "
            "-J %(jobName)s "
            "-o %(logDir)s/%(jobName)s.stdout "
            "-e %(logDir)s/%(jobName)s.stderr "
            "-w %(conditions)s "
            "%(script)s"%repMap)

class ValidationBase(object):

    __metaclass__ = ABCMeta

    def __init__( self, validation, config, options ):

        if validation[1] == "":
            # intermediate syntax
            valString = validation[0].split( "->" )[0]
            self.alignments = validation[0].split( "->" )[1]
            # force user to use the normal syntax
            if "->" in validation[0]:
                msg = ("Instead of using the intermediate syntax\n'"
                       +valString.strip()+"-> "+alignments.strip()
                       +":'\nyou have to use the now fully supported syntax \n'"
                       +valString.strip()+": "
                       +alignments.strip()+"'.")
                raise AllInOneError(msg)
        else:
            valString = validation[0]
            self.alignments = validation[1]
        valString = valString.split()
        self.valType = valString[0]
        self.valName = valString[1]
        self.commandLineOptions = options
        self.config = config
        self.preexisting = ("preexisting" in self.valType)
        if self.valType[0] == "*":
            self.valType = self.valType[1:]
            self.preexisting = True

        # workaround for intermediate parallel version
        if self.valType == "offlineParallel":
            print ("offlineParallel and offline are now the same.  To run an offline parallel validation,\n"
                   "just set parallelJobs to something > 1.  There is no reason to call it offlineParallel anymore.")
            self.valType = "offline"            
        self.valSection = self.valType + ":" + self.valName
        if not self.config.has_section( self.valSection ):
            raise AllInOneError("Validation '%s' of type '%s' is requested in"
                                " '[validation]' section, but is not defined."
                                  "\nYou have to add a '[%s]' section."
                                  %( self.valName, self.valType, self.valSection ))


    @abstractmethod
    def createJob( self ):
        pass

    @abstractmethod
    def runJob( self ):
        pass

    @abstractmethod
    def getValidation( self ):
        pass

    @abstractmethod
    def needsproxy(self):
        pass


class ValidationJob(ValidationBase):

    # these count the jobs of different varieties that are being run
    crabCount = 0
    interactCount = 0
    batchCount = 0
    batchJobIds = []
    batchJobs = {}
    jobCount = 0
    condorConf = {}

    def __init__( self, validation, config, options, *args, **kwargs ):

        self.start = 0
        self.end = args
        self.JobId=[]
        super(ValidationJob, self).__init__( validation, config, options )
        self.validation = self.__getValidation( self.valType, self.valName,
                                                  self.alignments, config,
                                                  options )

    def __getValidation( self, valType, name, alignments, config, options ):
        if valType == "compare":
            alignmentsList = alignments.split( "," )
            firstAlignList = alignmentsList[0].split()
            firstAlignName = firstAlignList[0].strip()
            if firstAlignName == "IDEAL":
                raise AllInOneError("'IDEAL' has to be the second (reference)"
                                      " alignment in 'compare <val_name>: "
                                      "<alignment> <reference>'.")
            if len( firstAlignList ) > 1:
                firstRun = firstAlignList[1]
            else:
                raise AllInOneError("Have to provide a run number for geometry comparison")
            firstAlign = Alignment( firstAlignName, config, firstRun )
            firstAlignName = firstAlign.name
            secondAlignList = alignmentsList[1].split()
            secondAlignName = secondAlignList[0].strip()
            if secondAlignName == "IDEAL":
                secondAlign = secondAlignName
            else:
                if len( secondAlignList ) > 1:
                    secondRun = secondAlignList[1]
                else:
                    raise AllInOneError("Have to provide a run number for geometry comparison")
                secondAlign = Alignment( secondAlignName, config,
                                         secondRun )
                secondAlignName = secondAlign.name
                
            validation = GeometryComparison( name, firstAlign, secondAlign,
                                             config,
                                             self.commandLineOptions.getImages)
        elif valType == "offline":
            validation = OfflineValidation( name, 
                Alignment( alignments.strip(), config ), config )
        elif valType == "preexistingoffline":
            validation = PreexistingOfflineValidation(name, config)
        elif valType == "offlineDQM":
            validation = OfflineValidationDQM( name, 
                Alignment( alignments.strip(), config ), config )
        elif valType == "mcValidate":
            validation = MonteCarloValidation( name, 
                Alignment( alignments.strip(), config ), config )
        elif valType == "preexistingmcValidate":
            validation = PreexistingMonteCarloValidation(name, config)
        elif valType == "split":
            validation = TrackSplittingValidation( name, 
                Alignment( alignments.strip(), config ), config )
        elif valType == "preexistingsplit":
            validation = PreexistingTrackSplittingValidation(name, config)
        elif valType == "zmumu":
            validation = ZMuMuValidation( name, 
                Alignment( alignments.strip(), config ), config )
        elif valType == "primaryvertex":
            validation = PrimaryVertexValidation( name, 
                Alignment( alignments.strip(), config ), config )
        elif valType == "preexistingprimaryvertex":
            validation = PreexistingPrimaryVertexValidation(name, self.__config)
        elif valType == "overlap":
            validation = OverlapValidation( name,
                Alignment( alignments.strip(), self.__config ), self.__config )
        else:
            raise AllInOneError("Unknown validation mode '%s'"%valType)

        return validation

    def __createJob( self, jobMode, outpath ):
        """This private method creates the needed files for the validation job.
           """
        self.validation.createConfiguration( outpath )
        if self.preexisting:
            return
        self.scripts = sum([addIndex(script, self.validation.NJobs) for script in self.validation.createScript( outpath )], [])
        if jobMode.split( ',' )[0] == "crab":
            self.validation.createCrabCfg( outpath )
        return None

    def createJob(self):
        """This is the method called to create the job files."""
        self.__createJob( self.validation.jobmode,
                          os.path.abspath( self.commandLineOptions.Name) )

    def runJob( self ):
        if self.preexisting:
            if self.validation.jobid:
                self.batchJobIds.append(self.validation.jobid)
            log = ">             " + self.validation.name + " is already validated."
            return log
        else:
            if self.validation.jobid:
                print("jobid {} will be ignored, since the validation {} is not preexisting".format(self.validation.jobid, self.validation.name))

        general = self.config.getGeneral()
        log = ""
        for script in self.scripts:
            name = os.path.splitext( os.path.basename( script) )[0]
            ValidationJob.jobCount += 1
            if self.commandLineOptions.dryRun:
                print("%s would run: %s"%( name, os.path.basename( script) ))
                continue
            log = ">             Validating "+name
            print(">             Validating "+name)
            if self.validation.jobmode == "interactive":
                log += getCommandOutput2( script )
                ValidationJob.interactCount += 1
            elif self.validation.jobmode.split(",")[0] == "lxBatch":
                repMap = { 
                    "commands": self.validation.jobmode.split(",")[1],
                    "logDir": general["logdir"],
                    "jobName": name,
                    "script": script,
                    "bsub": "/afs/cern.ch/cms/caf/scripts/cmsbsub"
                    }
                for ext in ("stdout", "stderr", "stdout.gz", "stderr.gz"):
                    oldlog = "%(logDir)s/%(jobName)s."%repMap + ext
                    if os.path.exists(oldlog):
                        os.remove(oldlog)
                bsubOut=getCommandOutput2("%(bsub)s %(commands)s "
                                          "-J %(jobName)s "
                                          "-o %(logDir)s/%(jobName)s.stdout "
                                          "-e %(logDir)s/%(jobName)s.stderr "
                                          "%(script)s"%repMap)
                #Attention: here it is assumed that bsub returns a string
                #containing a job id like <123456789>
                jobid=bsubOut.split("<")[1].split(">")[0]
                self.JobId.append(jobid)
                ValidationJob.batchJobIds.append(jobid)
                log+=bsubOut
                ValidationJob.batchCount += 1
                if self.validation.config.has_section("IOV"):
                    iov = self.validation.config.items("IOV")[0][1]
                    key = (self.valName, iov, general["logdir"])
                    if key in ValidationJob.batchJobs:
                        ValidationJob.batchJobs[key].append((jobid, self.validation.name))
                    else:
                        ValidationJob.batchJobs[key] = [(jobid, self.validation.name)]
                else:
                    key = (self.valName, 1, general["logdir"])
                    if key in ValidationJob.batchJobs:
                        ValidationJob.batchJobs[key].append((jobid, self.validation.name))
                    else:
                        ValidationJob.batchJobs[key] = [(jobid, self.validation.name)]
            
            elif self.validation.jobmode.split( "," )[0] == "condor":
                iov = self.validation.config.items("IOV")[0][1]
                key = (self.valName, iov)
                if key in ValidationJob.condorConf:
                    ValidationJob.condorConf[key].append((name[22:].replace(".", "_"), iov, general["logdir"], script))
                else:
                    ValidationJob.condorConf[key] = [(name[22:].replace(".", "_"), iov, general["logdir"], script)]

            elif self.validation.jobmode.split( "," )[0] == "crab":
                os.chdir( general["logdir"] )
                crabName = "crab." + os.path.basename( script )[:-3]
                theCrab = crabWrapper.CrabWrapper()
                options = { "-create": "",
                            "-cfg": crabName + ".cfg",
                            "-submit": "" }
                try:
                    theCrab.run( options )
                except AllInOneError as e:
                    print("crab:", str(e).split("\n")[0])
                    exit(1)
                ValidationJob.crabCount += 1

            else:
                raise AllInOneError("Unknown 'jobmode'!\n"
                                      "Please change this parameter either in "
                                      "the [general] or in the ["
                                      + self.valType + ":" + self.valName
                                      + "] section to one of the following "
                                      "values:\n"
                                      "\tinteractive\n\tlxBatch, -q <queue>\n"
                                      "\tcrab, -q <queue>")

        return log

    def getValidation( self ):
        return self.validation

    def needsproxy(self):
        return self.validation.needsproxy and not self.preexisting and not self.commandLineOptions.dryRun

    def __iter__(self):
        yield self

    def __next__(self):
        if self.start >= len(self.end):
            raise StopIteration
        else:
            self.start += 1
            return self.end[self.start-1]
        

class ValidationJobMultiIOV(ValidationBase):

    def __init__( self, validation, config, options, outPath, *args, **kwargs):
        self.start = 0
        self.end = args
        super(ValidationJobMultiIOV, self).__init__( validation, config, options )
        self.optionMultiIOV = self.config.getboolean( self.valSection, "multiIOV" )
        if self.optionMultiIOV == True:
            self.validation = validation
            self.config = config 
            self.options = options
            self.outPath = outPath
            self.validations = self.__performMultiIOV(self.validation, self.config,
                                                  self.options, self.outPath)


    def __performMultiIOV(self, validation, config, options, outPath):
        validations = []
        datasetList = self.config.get( self.valSection, "dataset" ).split( ", " )
        for dataset in datasetList:
            sectionMultiIOV = "multiIOV:%s"%dataset
            if not self.config.has_section(sectionMultiIOV):
                raise AllInOneError("section'[%s]' not found. Please define the dataset"%sectionMultiIOV)
            else:
                datasetBaseName = self.config.get( sectionMultiIOV, "dataset" )
                iovList = self.config.get( sectionMultiIOV, "iovs" ).split( ", " )
                for iov in iovList:
                    datasetName = datasetBaseName+"_since%s"%iov
                    tmpConfig = BetterConfigParser()
                    tmpConfig.read( options.config )
                    general = tmpConfig.getGeneral()
                    tmpConfig.add_section("IOV")
                    tmpConfig.set("IOV", "iov", iov)
                    tmpConfig.add_section("OptionMultiIOV")
                    tmpConfig.set("OptionMultiIOV", "optionMultiIOV", True)
                    tmpConfig.set( self.valSection, "dataset", datasetName )
                    tmpConfig.set("internals","workdir",os.path.join(general["workdir"], options.Name, self.valType + "_" + self.valName + "_%s"%iov) )
                    tmpConfig.set("internals","scriptsdir",os.path.join(outPath, self.valType + "_" + self.valName + "_" + iov) )
                    tmpConfig.set("general","datadir",os.path.join(general["datadir"], options.Name, self.valType + "_" + self.valName + "_%s"%iov) )
                    tmpConfig.set("general","logdir",os.path.join(general["logdir"], options.Name, self.valType + "_" + self.valName + "_%s"%iov) )
                    tmpConfig.set("general","eosdir",os.path.join("AlignmentValidation", general["eosdir"], options.Name, self.valType + "_" + self.valName + "_%s"%iov) )
                    tmpOptions = copy.deepcopy(options) 
                    tmpOptions.Name = os.path.join(options.Name, self.valType + "_" + self.valName + "_%s"%iov)
                    tmpOptions.config = tmpConfig
                    newOutPath = os.path.abspath( tmpOptions.Name )
                    if not os.path.exists( newOutPath ):
                        os.makedirs( newOutPath )
                    elif not os.path.isdir( newOutPath ):
                        raise AllInOneError("the file %s is in the way rename the Job or move it away"%newOutPath)
                    job = ValidationJob( validation, tmpConfig, tmpOptions, len(iovList) )
                    validations.append(job)

        return validations

    def createJob( self ):
        map( lambda validation: validation.createJob(), self.validations )

    def runJob( self ):
        return [validation.runJob() for validation in self.validations]

    @staticmethod
    def runCondorJobs(outdir, mergeKeys):
        dagmanLog = "{}/daglogs".format(outdir)
        os.system("mkdir -p {}".format(dagmanLog))


        with open("{}/validation.condor".format(outdir), "w") as condor:
            condor.write("universe = vanilla" + "\n")
            condor.write("executable = $(scriptName).sh" + "\n")
            condor.write("log = $(scriptName).log" + "\n")
            condor.write("error = $(scriptName).stderr" + "\n")
            condor.write("output = $(scriptName).stdout" + "\n")
            condor.write('requirements = (OpSysAndVer =?= "SLCern6")' + "\n")
            condor.write('+JobFlavour = "tomorrow"' + "\n")
            condor.write("queue")
             
        with open("{}/validation.dagman".format(outdir), "w") as dagman:
            parents = {}
            for (valName, iov), alignments in six.iteritems(ValidationJob.condorConf):
                parents[iov] = []
                
                for jobInfo in alignments: 
                    dagman.write("JOB {}_{} {}/validation.condor".format(jobInfo[0], iov, outdir) + "\n")
                    dagman.write('VARS {}_{} '.format(jobInfo[0], iov) + 'scriptName="{}"'.format('.'.join(jobInfo[3].split('.')[:-1])) + "\n")
                    parents[iov].append('{}_{}'.format(jobInfo[0], iov))
                    dagman.write("\n")

                path =  os.path.join(jobInfo[2], "TkAlMerge.sh")
                if os.path.exists( path ):
                    dagman.write("JOB Merge_{}_{} {}/validation.condor".format(valName, iov, outdir) + "\n")
                    #dagman.write('VARS {}_{} '.format(jobInfo[0], iov) + 'scriptName="{}"'.format(os.path.join(jobInfo[2], "TkAlMerge")) + "\n")
                    dagman.write("VARS Merge_{}_{} ".format(valName, iov) + 'scriptName="{}"'.format(os.path.join(jobInfo[2], "TkAlMerge")) + "\n")
                    dagman.write("\n")
                else:
                    raise AllInOneError("Merge script '[%s]' not found!"%path)

            for (valName, iov), alignments in six.iteritems(ValidationJob.condorConf):
                dagman.write('PARENT {} '.format(" ".join([parent for parent in parents[iov]])) + 'CHILD Merge_{}_{}'.format(valName, iov) + "\n")

        submitCommands = ["condor_submit_dag -no_submit -outfile_dir {} {}/validation.dagman".format(dagmanLog, outdir), "condor_submit {}/validation.dagman.condor.sub".format(outdir)]

        for command in submitCommands:
            subprocess.call(command.split(" "))

    def getValidation( self ):
        return [validation.getValidation() for validation in self.validations]

    def needsproxy( self ):
        return [validation.needsproxy() for validation in self.validations].join("and") and not self.preexisting and not self.commandLineOptions.dryRun

    def __iter__(self):
        yield self

    def __next__(self):
        if self.start >= len(self.end):
            raise StopIteration
        else:
            self.start += 1
            return self.end[self.start-1]


####################--- Functions ---############################
def createMergeScript( path, validations, options ):
    if(len(validations) == 0):
        raise AllInOneError("Cowardly refusing to merge nothing!")

    repMap = {}

    comparisonLists = {} # directory of lists containing the validations that are comparable
    for validation in validations:
        if validation.config.has_section("IOV"):
            iov = validation.config.get("IOV", "iov")
            validation.defaultReferenceName = iov
        for referenceName in validation.filesToCompare:
            #referenceName = givenIOV
            validationtype = type(validation)
            if issubclass(validationtype, PreexistingValidation):
                #find the actual validationtype
                for parentclass in validationtype.mro():
                    if not issubclass(parentclass, PreexistingValidation):
                        validationtype = parentclass
                        break
            key = (validationtype, referenceName)


            if key in comparisonLists:
                comparisonLists[key].append(validation)
            else:
                comparisonLists[key] = [validation]
                repMap[key] = validation.config.getGeneral()
                repMap[key].update({
                        "DownloadData":"",
                        "CompareAlignments":"",
                        "RunValidationPlots":"",
                        "CMSSW_BASE": os.environ["CMSSW_BASE"],
                        "SCRAM_ARCH": os.environ["SCRAM_ARCH"],
                        "CMSSW_RELEASE_BASE": os.environ["CMSSW_RELEASE_BASE"],
                        })

    # introduced to merge individual validation outputs separately
    #  -> avoids problems with merge script
                repMap[key]["doMerge"] = "mergeRetCode=0\n"
                repMap[key]["rmUnmerged"] = ("if [[ mergeRetCode -eq 0 ]]; then\n"
                            "    echo -e \\n\"Merging succeeded, removing original files.\"\n")
                repMap[key]["beforeMerge"] = ""
                repMap[key]["mergeParallelFilePrefixes"] = ""
                repMap[key]["createResultsDirectory"]=""
    

    anythingToMerge = []
    mergeKeys = {}
    filePaths = []
    parallelMergeObjects={}

    for (validationType, referencename), validations in six.iteritems(comparisonLists):
        for validation in validations:
            #parallel merging
            if not (isinstance(validation, PreexistingValidation)
                or validation.NJobs == 1
                or not isinstance(validation, ParallelValidation)):
		    if options.mergeOfflineParallel and validationType.valType=='offline' and validation.jobmode.split(",")[0]=="lxBatch":
		        repMapTemp=repMap[(validationType, referencename)].copy()
		        if validationType not in anythingToMerge:
		            anythingToMerge += [validationType]
		            #create init script
		            fileName="TkAlMergeInit"
		            filePath = os.path.join(path, fileName+".sh")
		            theFile = open( filePath, "w" )
		            repMapTemp["createResultsDirectory"]="#!/bin/bash"
		            repMapTemp["createResultsDirectory"]+=replaceByMap(configTemplates.createResultsDirectoryTemplate, repMapTemp)
		            theFile.write( replaceByMap( configTemplates.createResultsDirectoryTemplate, repMapTemp ) )
		            theFile.close()
		            os.chmod(filePath,0o755)
		            #create handle
		            parallelMergeObjects["init"]=ParallelMergeJob(fileName, filePath,[])
		            #clear 'create result directory' code
		            repMapTemp["createResultsDirectory"]=""
		        
		        #edit repMapTmp as necessary:
		        #fill contents of mergeParallelResults
		        repMapTemp["beforeMerge"] += validationType.doInitMerge()
		        repMapTemp["doMerge"] += '\n\n\n\necho -e "\n\nMerging results from %s jobs with alignment %s"\n\n' % (validationType.valType,validation.alignmentToValidate.name)
		        repMapTemp["doMerge"] += validation.doMerge()
		        for f in validation.getRepMap()["outputFiles"]:
		            longName = os.path.join("/eos/cms/store/group/alca_trackeralign/AlignmentValidation/",
		                                    validation.getRepMap()["eosdir"], f)
		            repMapTemp["rmUnmerged"] += "    rm "+longName+"\n"
		        
		        repMapTemp["rmUnmerged"] += ("else\n"
		                                     "    echo -e \\n\"WARNING: Merging failed, unmerged"
		                                     " files won't be deleted.\\n"
		                                     "(Ignore this warning if merging was done earlier)\"\n"
		                                     "fi\n")
		        
		        #fill mergeParallelResults area of mergeTemplate
		        repMapTemp["DownloadData"] = replaceByMap( configTemplates.mergeParallelResults, repMapTemp )
		        #fill runValidationPlots area of mergeTemplate
                        validation.getRepMap()
		        repMapTemp["RunValidationPlots"] = validationType.doRunPlots(validations)
		        
		        #create script file
		        fileName="TkAlMergeOfflineValidation"+validation.name+validation.alignmentToValidate.name
		        filePath = os.path.join(path, fileName+".sh")
		        theFile = open( filePath, "w" )
		        theFile.write( replaceByMap( configTemplates.mergeParallelOfflineTemplate, repMapTemp ) )
		        theFile.close()
		        os.chmod(filePath,0o755)
		        #create handle object
		        if "parallel" in parallelMergeObjects:
		            parallelMergeObjects["parallel"].append(ParallelMergeJob(fileName, filePath,[]))
		        else:
		            parallelMergeObjects["parallel"]=[ParallelMergeJob(fileName, filePath,[])]
		        continue
		    
		    
		    else:
		        if validationType not in anythingToMerge:
		            anythingToMerge += [validationType]
		            repMap[(validationType, referencename)]["doMerge"] += '\n\n\n\necho -e "\n\nMerging results from %s jobs"\n\n' % validationType.valType
		            repMap[(validationType, referencename)]["beforeMerge"] += validationType.doInitMerge()
		        repMap[(validationType, referencename)]["doMerge"] += validation.doMerge()
		        for f in validation.getRepMap()["outputFiles"]:
		            longName = os.path.join("/eos/cms/store/group/alca_trackeralign/AlignmentValidation/",
		                                    validation.getRepMap()["eosdir"], f)
		            repMap[(validationType, referencename)]["rmUnmerged"] += "    rm "+longName+"\n"
		        
		        
    
        repMap[(validationType, referencename)]["rmUnmerged"] += ("else\n"
                                                                  "    echo -e \\n\"WARNING: Merging failed, unmerged"
                                                                  " files won't be deleted.\\n"
                                                                  "(Ignore this warning if merging was done earlier)\"\n"
                                                                  "fi\n")
    
    
    
        if anythingToMerge:
            repMap[(validationType, referencename)]["DownloadData"] += replaceByMap( configTemplates.mergeParallelResults, repMap[(validationType, referencename)] )
        else:
            repMap[(validationType, referencename)]["DownloadData"] = ""


        repMap[(validationType, referencename)]["RunValidationPlots"] = ""
        repMap[(validationType, referencename)]["plottingscriptpath"] = ""
        if issubclass(validationType, ValidationWithPlots):
            validation.getRepMap()
            repMap[(validationType, referencename)]["RunValidationPlots"] = validationType.doRunPlots(validations)

        repMap[(validationType, referencename)]["CompareAlignments"] = "#run comparisons"
        if issubclass(validationType, ValidationWithComparison):
            repMap[(validationType, referencename)]["CompareAlignments"] += validationType.doComparison(validations)
    
    #if user wants to merge parallely and if there are valid parallel scripts, create handle for plotting job and set merge script name accordingly
        if options.mergeOfflineParallel and parallelMergeObjects!={}:
            parallelMergeObjects["continue"]=ParallelMergeJob("TkAlMergeFinal",os.path.join(path, "TkAlMergeFinal.sh"),[])
            filePath = os.path.join(path, "TkAlMergeFinal.sh")
    #if not merging parallel, add code to create results directory and set merge script name accordingly
        elif validation.config.has_section("IOV"):
            repMap[(validationType, referencename)]["createResultsDirectory"]=replaceByMap(configTemplates.createResultsDirectoryTemplate, repMap[(validationType, referencename)])
            filePath = os.path.join(repMap[(validationType, referencename)]["scriptsdir"], "TkAlMerge.sh")
        else:
            repMap[(validationType, referencename)]["createResultsDirectory"]=replaceByMap(configTemplates.createResultsDirectoryTemplate, repMap[(validationType, referencename)])
            filePath = os.path.join(path, "TkAlMerge.sh")
    
        theFile = open( filePath, "w" )
        theFile.write( replaceByMap( configTemplates.mergeTemplate, repMap[(validationType, referencename)]) )
        theFile.close()
        os.chmod(path,0o755)
        filePaths.append(filePath)

    for path in filePaths:    
        if "TkAlMerge" in mergeKeys:
            mergeKeys["TkAlMerge"].append(path)
        else:
            mergeKeys["TkAlMerge"] = [path]
        if "parallelMergeObjects" in mergeKeys:
            mergeKeys["parallelMergeObjects"].append(parallelMergeObjects)
        else:
            mergeKeys["parallelMergeObjects"] = [parallelMergeObjects]
    
        
    if options.mergeOfflineParallel:
        return mergeKeys
    else:
        return filePath
    
def loadTemplates( config ):
    if config.has_section("alternateTemplates"):
        for templateName in config.options("alternateTemplates"):
            if templateName == "AutoAlternates":
                continue
            newTemplateName = config.get("alternateTemplates", templateName )
            #print "replacing default %s template by %s"%( templateName, newTemplateName)
            configTemplates.alternateTemplate(templateName, newTemplateName)

    
####################--- Main ---############################
def main(argv = None):
    if argv == None:
       argv = sys.argv[1:]
    optParser = optparse.OptionParser()
    optParser.description = """All-in-one Alignment Validation.
This will run various validation procedures either on batch queues or interactively.
If no name is given (-N parameter) a name containing time and date is created automatically.
To merge the outcome of all validation procedures run TkAlMerge.sh in your validation's directory.
"""
    optParser.add_option("-n", "--dryRun", dest="dryRun", action="store_true", default=False,
                         help="create all scripts and cfg File but do not start jobs (default=False)")
    optParser.add_option( "--getImages", dest="getImages", action="store_true", default=True,
                         help="get all Images created during the process (default= True)")
    defaultConfig = "TkAlConfig.ini"
    optParser.add_option("-c", "--config", dest="config", default = defaultConfig,
                         help="configuration to use (default TkAlConfig.ini) this can be a comma-seperated list of all .ini file you want to merge", metavar="CONFIG")
    optParser.add_option("-N", "--Name", dest="Name",
                         help="Name of this validation (default: alignmentValidation_DATE_TIME)", metavar="NAME")
    optParser.add_option("-r", "--restrictTo", dest="restrictTo",
                         help="restrict validations to given modes (comma seperated) (default: no restriction)", metavar="RESTRICTTO")
    optParser.add_option("-s", "--status", dest="crabStatus", action="store_true", default = False,
                         help="get the status of the crab jobs", metavar="STATUS")
    optParser.add_option("-d", "--debug", dest="debugMode", action="store_true",
                         default = False,
                         help="run the tool to get full traceback of errors",
                         metavar="DEBUG")
    optParser.add_option("-m", "--autoMerge", dest="autoMerge", action="store_true", default = False,
                         help="submit TkAlMerge.sh to run automatically when all jobs have finished (default=False)."
                              " Works only for batch jobs")
    optParser.add_option("--mergeOfflineParallel", dest="mergeOfflineParallel", action="store_true", default = False,
                         help="Enable parallel merging of offline data. Best used with -m option. Only works with lxBatch-jobmode", metavar="MERGE_PARALLEL")


    (options, args) = optParser.parse_args(argv)


    if not options.restrictTo == None:
        options.restrictTo = options.restrictTo.split(",")

    options.config = [ os.path.abspath( iniFile ) for iniFile in \
                       options.config.split( "," )]

    config = BetterConfigParser()
    outputIniFileSet = set( config.read( options.config ) )
    failedIniFiles = [ iniFile for iniFile in options.config if iniFile not in outputIniFileSet ]

    # Check for missing ini file
    if options.config == [ os.path.abspath( defaultConfig ) ]:
        if ( not options.crabStatus ) and \
               ( not os.path.exists( defaultConfig ) ):
                raise AllInOneError( "Default 'ini' file '%s' not found!\n"
                                       "You can specify another name with the "
                                       "command line option '-c'/'--config'."
                                       %( defaultConfig ))
    else:
        for iniFile in failedIniFiles:
            if not os.path.exists( iniFile ):
                raise AllInOneError( "'%s' does not exist. Please check for "
                                       "typos in the filename passed to the "
                                       "'-c'/'--config' option!"
                                       %( iniFile ))
            else:
                raise AllInOneError(( "'%s' does exist, but parsing of the "
                                       "content failed!" ) % iniFile)

    # get the job name
    if options.Name == None:
        if not options.crabStatus:
            options.Name = "alignmentValidation_%s"%(datetime.datetime.now().strftime("%y%m%d_%H%M%S"))
        else:
            existingValDirs = fnmatch.filter( os.walk( '.' ).next()[1],
                                              "alignmentValidation_*" )
            if len( existingValDirs ) > 0:
                options.Name = existingValDirs[-1]
            else:
                print("Cannot guess last working directory!")
                print ( "Please use the parameter '-N' or '--Name' to specify "
                        "the task for which you want a status report." )
                return 1

    # set output path
    outPath = os.path.abspath( options.Name )

    # Check status of submitted jobs and return
    if options.crabStatus:
        os.chdir( outPath )
        crabLogDirs = fnmatch.filter( os.walk('.').next()[1], "crab.*" )
        if len( crabLogDirs ) == 0:
            print("Found no crab tasks for job name '%s'"%( options.Name ))
            return 1
        theCrab = crabWrapper.CrabWrapper()
        for crabLogDir in crabLogDirs:
            print()
            print("*" + "=" * 78 + "*")
            print ( "| Status report and output retrieval for:"
                    + " " * (77 - len( "Status report and output retrieval for:" ) )
                    + "|" )
            taskName = crabLogDir.replace( "crab.", "" )
            print("| " + taskName + " " * (77 - len( taskName ) ) + "|")
            print("*" + "=" * 78 + "*")
            print()
            crabOptions = { "-getoutput":"",
                            "-c": crabLogDir }
            try:
                theCrab.run( crabOptions )
            except AllInOneError as e:
                print("crab:  No output retrieved for this task.")
            crabOptions = { "-status": "",
                            "-c": crabLogDir }
            theCrab.run( crabOptions )
        return

    general = config.getGeneral()
    config.set("internals","workdir",os.path.join(general["workdir"],options.Name) )
    config.set("internals","scriptsdir",outPath)
    config.set("general","datadir",os.path.join(general["datadir"],options.Name) )
    config.set("general","logdir",os.path.join(general["logdir"],options.Name) )
    config.set("general","eosdir",os.path.join("AlignmentValidation", general["eosdir"], options.Name) )

    if not os.path.exists( outPath ):
        os.makedirs( outPath )
    elif not os.path.isdir( outPath ):
        raise AllInOneError("the file %s is in the way rename the Job or move it away"%outPath)

    # replace default templates by the ones specified in the "alternateTemplates" section
    loadTemplates( config )

    #save backup configuration file
    backupConfigFile = open( os.path.join( outPath, "usedConfiguration.ini" ) , "w"  )
    config.write( backupConfigFile )

    #copy proxy, if there is one
    try:
        proxyexists = int(getCommandOutput2("voms-proxy-info --timeleft")) > 10
    except RuntimeError:
        proxyexists = False

    if proxyexists:
        shutil.copyfile(getCommandOutput2("voms-proxy-info --path").strip(), os.path.join(outPath, ".user_proxy"))

    validations = []
    jobs = []
    mergeKeys = {}

    for validation in config.items("validation"):
        alignmentList = [validation[1]]
        validationsToAdd = [(validation[0],alignment) \
                                for alignment in alignmentList]
        validations.extend(validationsToAdd)

    for validation in validations:
        job = ValidationJobMultiIOV(validation, config, options, outPath, len(validations))
        if (job.optionMultiIOV == True):
            jobs.extend(job)
        else:
            jobs.extend( ValidationJob(validation, config, options, 1) )

    for job in jobs:
        if job.needsproxy and not proxyexists:
            raise AllInOneError("At least one job needs a grid proxy, please init one.")

    map( lambda job: job.createJob(), jobs )
    validations = [ job.getValidation() for job in jobs ]
    validations = [item for sublist in validations for item in sublist]

    if options.mergeOfflineParallel:
        parallelMergeObjectsList = createMergeScript(outPath, validations, options)['parallelMergeObjects']
        mergeKeys = createMergeScript(outPath, validations, options)
    else:
        createMergeScript(outPath, validations, options)


    map( lambda job: job.runJob(), jobs )

    if options.autoMerge and ValidationJob.jobCount == ValidationJob.batchCount and config.getGeneral()["jobmode"].split(",")[0] == "lxBatch":
        print(">             Automatically merging jobs when they have ended")
        # if everything is done as batch job, also submit TkAlMerge.sh to be run
        # after the jobs have finished
        
        #if parallel merge scripts: manage dependencies
        for parallelMergeObjects in parallelMergeObjectsList:
            if options.mergeOfflineParallel and parallelMergeObjects!={}:
                initID=parallelMergeObjects["init"].runJob(config).split("<")[1].split(">")[0]
                parallelIDs=[]
                for parallelMergeScript in parallelMergeObjects["parallel"]:
                    parallelMergeScript.addDependency(initID)
                    for job in jobs:
                        if isinstance(job.validation, OfflineValidation) and "TkAlMerge"+job.validation.alignmentToValidate.name==parallelMergeScript.name:
                            parallelMergeScript.addDependency(job.JobId)
                    parallelIDs.append(parallelMergeScript.runJob(config).split("<")[1].split(">")[0])
                parallelMergeObjects["continue"].addDependency(parallelIDs)
                parallelMergeObjects["continue"].addDependency(ValidationJob.batchJobIds)
                parallelMergeObjects["continue"].runJob(config)
            
            
        
    
        else:
            #repMap = {
            #    "commands": config.getGeneral()["jobmode"].split(",")[1],
            #    "jobName": "TkAlMerge_{}_{}".format(),
            #    "logDir": config.getGeneral()["logdir"],
            #    "script": "TkAlMerge.sh",
            #    "bsub": "/afs/cern.ch/cms/caf/scripts/cmsbsub",
            #    "conditions": '"' + " && ".join(["ended(" + jobId + ")" for jobId in ValidationJob.batchJobIds]) + '"'
            #    }
            #
            #for ext in ("stdout", "stderr", "stdout.gz", "stderr.gz"):
            #    oldlog = "%(logDir)s/%(jobName)s."%repMap + ext
            #    if os.path.exists(oldlog):
            #        os.remove(oldlog)

            for (valName, iov, logdir), alignments in six.iteritems(ValidationJob.batchJobs):
                alignmentDependencies = []
                for jobInfo in alignments:
                    alignmentDependencies.append(jobInfo[0]) #append jobID
                #mergeName = "Merge_{}_{}".format(valName, iov)
                repMap = {
                    "commands": config.getGeneral()["jobmode"].split(",")[1],
                    "jobName": "TkAlMerge",
                    "logDir": logdir,
                    "script": "TkAlMerge.sh",
                    "bsub": "/afs/cern.ch/cms/caf/scripts/cmsbsub",
                    "conditions": '"' + " && ".join(["ended(" + jobId + ")" for jobId in alignmentDependencies]) + '"'
                    }

                for ext in ("stdout", "stderr", "stdout.gz", "stderr.gz"):
                    oldlog = "%(logDir)s/%(jobName)s."%repMap + ext

                #issue job
                getCommandOutput2("%(bsub)s %(commands)s "
                                  "-o %(logDir)s/%(jobName)s.stdout "
                                  "-e %(logDir)s/%(jobName)s.stderr "
                                  "-w %(conditions)s "
                                  "%(logDir)s/%(script)s"%repMap)


    elif config.getGeneral()["jobmode"].split(",")[0] == "condor":
        ValidationJobMultiIOV.runCondorJobs(outPath, mergeKeys)
    

if __name__ == "__main__":        
    # main(["-n","-N","test","-c","defaultCRAFTValidation.ini,latestObjects.ini","--getImages"])
    if "-d" in sys.argv[1:] or "--debug" in sys.argv[1:]:
        main()
    else:
        try:
            main()
        except AllInOneError as e:
            print("\nAll-In-One Tool:", str(e))
            exit(1)
