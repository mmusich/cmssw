#!/bin/tcsh

setenv CMSSW_DIR ${CMSSW_BASE}/src/Alignment/OfflineValidation/test

set COUNT = 0

#foreach folder (`/bin/ls $CMSSW_DIR/datfiles | grep pp2012 | grep -v ppRun2013 | grep -v csh | grep -v txt`)
#foreach folder (`/bin/ls $CMSSW_DIR/datfiles | grep mp1819`) #| grep -v ppRun2013 | grep -v csh | grep -v txt`)
foreach folder (`/bin/ls $CMSSW_DIR/datfiles/for2015D`)
    set COUNTbyFolder=0
    foreach inputfile (`/bin/ls $CMSSW_DIR/datfiles/$folder | grep dat`)
	@ COUNT+=1
	@ COUNTbyFolder+=1
	echo $inputfile
	echo "--- submitting $COUNTbyFolder job: " $folder/$inputfile "in task:" $folder
	bsub -o tmp.tmp -q cmscaf1nd PVValidationSubmitter.csh ${CMSSW_DIR}/datfiles/$folder/$inputfile $folder 
	if ($COUNTbyFolder>1000) then 
	    break
	endif		    
    end
    echo "submitted $COUNTbyFolder jobs"
end
echo "---------------------------------------------"
echo " submitted $COUNT jobs"
