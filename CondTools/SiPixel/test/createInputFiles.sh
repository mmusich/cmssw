#!/bin/bash
mkdir -p results
for i in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
do
   echo "Welcome $i times"
   #cp -pr SiPixelQuality_allROC0.txt SiPixelQuality_allROC${i}.txt
   #sed -i 's/ROC 0/ROC '${i}'/g' SiPixelQuality_allROC${i}.txt
   #cmsRun SiPixelBadModuleByHandBuilderFromROCList_cfg.py inputFile=SiPixelQuality_allROC${i}
   getPayloadData.py --plugin pluginSiPixelQuality_PayloadInspector --plot plot_SiPixelBPixQualityMap --tag SiPixelQuality_allROC${i} --input_params '{}' --time_type Lumi --iovs '{"start_iov": "1", "end_iov": "1"}' --db sqlite_file:SiPixelQuality_allSameROC.db --test ;
   mv *.png $PWD/results/SiPixelQuality_allROC${i}.png
done
