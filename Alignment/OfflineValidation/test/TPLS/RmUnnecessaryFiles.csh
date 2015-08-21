#!/bin/tcsh
set ARRAY=(pp2015-PCLupdate pp2015-PCLupdateAndTemplates pp2015-PCLupdateAndTemplatesZeroBias pp2015-PCLupdateZeroBias pp2015-Prompt pp2015-PromptAndTemplates pp2015-PromptZeroBias pp2015-PromptZeroBiasAndTemplates pp2015-Run1Ali pp2015-Run2AliCRUZET pp2015-Run2AliCollisions pp2015-Run2AliCosmics pp2015-TrackerAlignment_v2_hltvalidation pp2015-hp1216 pp2015-hp1223 pp2015-hp1368 pp2015-hp1375 pp2015-hp1387 pp2015-hp1388)

foreach i (`seq $#ARRAY`)
    echo "---- I am preparing sample $ARRAY[$i]"

    cmsRmdir /store/caf/user/musich/Alignment/PVValidation/$ARRAY[$i]
    #foreach file (`eos ls /store/caf/user/musich/Alignment/PVValidation/$ARRAY[$i]`)
    #    echo "removing /store/caf/user/musich/Alignment/PVValidation/$ARRAY[$i]/$file"
    #	cmsRm /store/caf/user/musich/Alignment/PVValidation/$ARRAY[$i]/$file 
    #end	

end
