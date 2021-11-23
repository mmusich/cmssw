#!/bin/tcsh
foreach dir (`eos ls /eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCAPROMPT/PromptCalibProdSiPixelAli-Express-v1/000/346/`)
    #echo $dir
    foreach file (`/usr/bin/eos ls /eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCAPROMPT/PromptCalibProdSiPixelAli-Express-v1/000/346/$dir/00000/`)
	echo "root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCAPROMPT/PromptCalibProdSiPixelAli-Express-v1/000/346/$dir/00000/$file"
    end
end

foreach dir (`eos ls /eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCAPROMPT/PromptCalibProdSiPixelAli-Express-v1/000/347/`)
    #echo $dir
    foreach file (`/usr/bin/eos ls /eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCAPROMPT/PromptCalibProdSiPixelAli-Express-v1/000/347/$dir/00000/`)
	echo "root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/ALCAPROMPT/PromptCalibProdSiPixelAli-Express-v1/000/347/$dir/00000/$file"
    end
end
