#!/bin/tcsh

#set ARRAY=(pp2012-2011Legacy pp2012-2012Repro pp2012-mp1511)
#set ARRAY=(pp2015-GT pp2015-hp1216 pp2015-hp1223 pp2015-mp1744 pp2015-TrackerAlignment_v2_hltvalidation)
#set ARRAY=(pp2015-PCLupdateZeroBias  pp2015-PCLupdateAndTemplatesZeroBias pp2015-PromptZeroBias pp2015-PromptZeroBiasAndTemplates)
#set ARRAY=(pp2015-PCLupdate pp2015-PCLupdateAndTemplates pp2015-Prompt pp2015-PromptAndTemplates)
#set ARRAY=(pp2015-hp1388 pp2015-hp1375 pp2015-hp1387 pp2015-hp1368)

#set ARRAY=(pp2015B-hp1368 pp2015B-hp1375 pp2015B-hp1387 pp2015B-hp1388 pp2015B-PCLupdateAndTemplates pp2015B-PCLupdate pp2015B-PromptAndTemplates pp2015B-Prompt pp2015B-Run1Ali pp2015B-Run2Ali0TCollisions pp2015B-Run2AliCosmics pp2015B-Run2AliCRUZET)

#set ARRAY=(pp2015B-mp1807)
#set ARRAY=(pp2015B-hp1394)

set ARRAY=(pp2015B-PCLAlignment pp2015B-hp1394 pp2015B-mp1819 pp2015B-mp1820)

foreach i (`seq $#ARRAY`)
    echo "---- I am preparing sample $ARRAY[$i]"

    if(! -d $ARRAY[$i]) then
	echo "$ARRAY[$i] does not exist yet: creating it"
	mkdir $ARRAY[$i]
    endif

    rm -fr ./$ARRAY[$i]/*   
    cp -pr ../TPLS/InputSource_$ARRAY[$i]_tpl ./$ARRAY[$i]

    #./listOfRuns.csh $ARRAY[$i] $ARRAY[$i] ZeroBias2015B
    ./listOfRuns.csh $ARRAY[$i] $ARRAY[$i] HLTPhysics2015B

end







