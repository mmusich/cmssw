#!/bin/bash                                                                                                                                                 
# Save current working dir so img can be outputted re later
W_DIR=$(pwd);
# Set SCRAM architecture var                                                                                                                                                                                
SCRAM_ARCH=slc6_amd64_gcc630;
export SCRAM_ARCH;
source /afs/cern.ch/cms/cmsset_default.sh;
eval `scram run -sh`;
# Go back to original working directory                                                                                                                                                                     
cd $W_DIR;
# Run get payload data script                                                                                                                                                                              
rm *.png
mkdir $W_DIR/inspection

#369141286, APV 1: G2 Gain = 3.29817 Total Gain = 2.81282 | TIB+ Layer 2 int String 34 Module for phase0 1 r-phi glued Module for phase2 1 upper stack (369141286)
#369141861, APV 2: G2 Gain = 3.23233 Total Gain = 3.9692 | TIB+ Layer 2 ext String 6 Module for phase0 1 stereo glued Module for phase2 1 lower stack (369141861)
#369141861, APV 3: G2 Gain = 4.14172 Total Gain = 4.77912 | TIB+ Layer 2 ext String 6 Module for phase0 1 stereo glued Module for phase2 1 lower stack (369141861)
#369141861, APV 4: G2 Gain = 3.84832 Total Gain = 4.44057 | TIB+ Layer 2 ext String 6 Module for phase0 1 stereo glued Module for phase2 1 lower stack (369141861)
#369174772, APV 1: G2 Gain = 5.01899 Total Gain = 7.69608 | TIB+ Layer 4 ext String 15 Module for phase0 1 module Module for phase2 1 module (369174772)
#369174780, APV 4: G2 Gain = 3.11048 Total Gain = 4.75484 | TIB+ Layer 4 ext String 15 Module for phase0 3 module Module for phase2 3 module (369174780)
#369174788, APV 4: G2 Gain = 6.55735 Total Gain = 10.0885 | TIB+ Layer 4 ext String 16 Module for phase0 1 module Module for phase2 1 module (369174788)
#369174796, APV 1: G2 Gain = 5.19043 Total Gain = 4.75087 | TIB+ Layer 4 ext String 16 Module for phase0 3 module Module for phase2 3 module (369174796)
#369174804, APV 3: G2 Gain = 13.6606 Total Gain = 20.0137 | TIB+ Layer 4 ext String 17 Module for phase0 1 module Module for phase2 1 module (369174804)
#369175256, APV 4: G2 Gain = 53.7844 Total Gain = 48.8631 | TIB+ Layer 4 ext String 45 Module for phase0 2 module Module for phase2 2 module (369175256)
#470329381, APV 4: G2 Gain = 5.24924 Total Gain = 4.64303 | TEC Side   2+ Wheel 2 Petal 8 front Ring 1 Module for phase0 1 stereo glued Module for phase2 1 lower stack (470329381)

declare -a arr=("369141286" "369141861" "369174772" "369174780" "369174788" "369174796" "369174804" "369175256" "470329381")

for i in "${arr[@]}"
do
    echo $i
    getPayloadData.py \
	--plugin pluginSiStripPedestals_PayloadInspector \
	--plot plot_SiStripPedestalPerDetId \
	--tag SiStripPedestals_v2_prompt \
	--time_type Run \
	--iovs '{"start_iov": "323790", "end_iov": "323790"}' \
	--db Prod \
	--input_params '{"DetId":"'${i}'"}' \
	--test ;
    
    mv *.png  $W_DIR/inspection/SiStripPedestalsProfile_DetId_$i.png

    getPayloadData.py \
	--plugin pluginSiStripNoises_PayloadInspector \
	--plot plot_SiStripNoisePerDetId \
	--tag SiStripNoise_v2_prompt \
	--time_type Run \
	--iovs '{"start_iov": "323790", "end_iov": "323790"}' \
	--db Prod \
	--input_params '{"DetId":"'${i}'"}' \
	--test ;
    
    mv *.png  $W_DIR/inspection/SiStripNoiseProfile_DetId_$i.png

done
