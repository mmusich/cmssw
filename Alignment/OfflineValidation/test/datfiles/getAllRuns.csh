#!/bin/tcsh

set COUNT=0
#touch listOfRunsHLTPhysics.txt
touch listOfRunsZeroBias.txt

foreach inputfile (`ls ../../python | grep -v pyc`)
    #echo $inputfile
    set namebase=`echo $inputfile |awk '{split($0,b,"_"); print b[4]}'`
    #if ("$inputfile" =~ *"PVValidation_HLTPhysics2015B_TkAlMinBias"*) then
    if ("$inputfile" =~ *"PVValidation_ZeroBias2015B_TkAlMinBias"*) then
	echo $inputfile 
	#echo -n $namebase" " >> listOfRunsHLTPhysics.txt
	echo -n $namebase" " >> listOfRunsZeroBias.txt
    @ COUNT+=1
    endif  
end

echo "Will run on $COUNT runs"

