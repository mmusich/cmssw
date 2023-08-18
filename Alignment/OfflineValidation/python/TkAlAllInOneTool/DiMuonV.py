import copy
import os

def DiMuonV(config, validationDir):
    ##List with all jobs
    jobs = []
    dimuonvType = "single"

    ##List with all wished IOVs
    IOVs = []

    ##Start with single DiMuonV jobs
    if not dimuonvType in config["validations"]["DiMuonV"]:
        raise Exception("No 'single' key word in config for DiMuonV")

    for datasetName in config["validations"]["DiMuonV"][dimuonvType]:
        for IOV in config["validations"]["DiMuonV"][dimuonvType][datasetName]["IOV"]:
            ##Save IOV to loop later for merge jobs
            if not IOV in IOVs:
                IOVs.append(IOV)

            for alignment in config["validations"]["DiMuonV"][dimuonvType][datasetName]["alignments"]:
                ##Work directory for each IOV
                workDir = "{}/DiMuonV/{}/{}/{}/{}".format(validationDir, dimuonvType, datasetName, alignment, IOV)

                ##Write local config
                local = {}
                local["output"] = "{}/{}/{}/{}/{}/{}".format(config["LFS"], config["name"], dimuonvType, alignment, datasetName, IOV)
                local["alignment"] = copy.deepcopy(config["alignments"][alignment])
                local["validation"] = copy.deepcopy(config["validations"]["DiMuonV"][dimuonvType][datasetName])
                local["validation"].pop("alignments")
                local["validation"]["IOV"] = IOV
                if "goodlumi" in local["validation"]:
                    local["validation"]["goodlumi"] = local["validation"]["goodlumi"].format(IOV)

                ##Write job info
                job = {
                    "name": "DiMuonV_{}_{}_{}_{}".format(dimuonvType, alignment, datasetName, IOV),
                    "dir": workDir,
                    "exe": "cmsRun",
                    "cms-config": "{}/src/Alignment/OfflineValidation/python/TkAlAllInOneTool/DiMuonV_cfg.py".format(os.environ["CMSSW_BASE"]),
                    "run-mode": "Condor",
                    "dependencies": [],
                    "config": local,
                }

                jobs.append(job)

    ##Do merge DiMuonV if wished
    if "merge" in config["validations"]["DiMuonV"]:
        ##List with merge jobs, will be expanded to jobs after looping
        mergeJobs = []
        dimuonvType = "merge"

        ##Loop over all merge jobs/IOVs which are wished
        for mergeName in config["validations"]["DiMuonV"][dimuonvType]:
            for IOV in IOVs:
                ##Work directory for each IOV
                workDir = "{}/DiMuonV/{}/{}/{}".format(validationDir, dimuonvType, mergeName, IOV)

                ##Write job info
                local = {}

                job = {
                    "name": "DiMuonV_{}_{}_{}".format(dimuonvType, mergeName, IOV),
                    "dir": workDir,
                    "exe": "DiMuonVmerge",
                    "run-mode": "Condor",
                    "dependencies": [],
                    "config": local,
                }

                for alignment in config["alignments"]:
                    ##Deep copy necessary things from global config
                    local.setdefault("alignments", {})
                    local["alignments"][alignment] = copy.deepcopy(config["alignments"][alignment])
                    local["validation"] = copy.deepcopy(config["validations"]["DiMuonV"][dimuonvType][mergeName])
                    local["output"] = "{}/{}/{}/{}/{}".format(config["LFS"], config["name"], dimuonvType, mergeName, IOV)

                ##Loop over all single jobs
                for singleJob in jobs:
                    ##Get single job info and append to merge job if requirements fullfilled
                    alignment, datasetName, singleIOV = singleJob["name"].split("_")[2:]

                    if int(singleIOV) == IOV and datasetName in config["validations"]["DiMuonV"][dimuonvType][mergeName]["singles"]:
                        local["alignments"][alignment]["file"] = singleJob["config"]["output"]
                        job["dependencies"].append(singleJob["name"])

                mergeJobs.append(job)

        jobs.extend(mergeJobs)

    return jobs
