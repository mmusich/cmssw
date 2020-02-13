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
mkdir $W_DIR/comparisons/

# Since: Run   Insertion Time       Payload                                   Object Type      
# -----------  -------------------  ----------------------------------------  --------------   
# 1            2019-10-25 16:37:43  79c5445574b7ea70301875cd5e389bba9f5bbe58  SiStripApvGain   
# 132440       2019-10-25 16:37:43  fee217fa41d8675ac954e0e2f11adcd21d2f89bd  SiStripApvGain   
# 134308       2019-10-25 16:37:43  e6e8e1f4c812878370728f816967ef78befe152b  SiStripApvGain   
# 135149       2019-10-25 16:37:43  f2be0f8875e7013ed4fffaa73fd56cac548a60ea  SiStripApvGain   
# 135175       2019-10-25 16:37:43  464fb3f19f1c47d4db49704388b01c47748fdab8  SiStripApvGain   
# 140058       2019-10-25 16:37:43  05f91d3767b3b3d41d14b0767f52d016c51e4043  SiStripApvGain   
# 160325       2019-10-25 16:37:43  d6293966dfc39cf19a377f765eb0a15b9e911e69  SiStripApvGain   
# 190000       2019-10-25 16:37:43  b2a61c92f40982e1aa5961ef11f36d5ac928a49e  SiStripApvGain   
# 193093       2019-10-25 16:37:43  bf83785692d54e7483265259522e720346ce6143  SiStripApvGain   
# 194115       2019-10-25 16:37:43  d46986e4ef4ac2064ce42a44c0744d9045903897  SiStripApvGain   
# 194825       2019-10-25 16:37:43  19296d98ddf30371f3bc117d97f457d5ac8a1e52  SiStripApvGain   
# 195540       2019-10-25 16:37:43  ebe7cc8ab0c3663e5d7bc57b4df6b0c15ad1dc48  SiStripApvGain   
# 195915       2019-10-25 16:37:43  532664793c42004600956a3529217bcc1d9795f2  SiStripApvGain   
# 200042       2019-10-25 16:37:43  e2458d868d688231f8b0540688dfff7ad9f6aec9  SiStripApvGain   
# 200961       2019-10-25 16:37:43  feb2995bc8e6da4a164cf075c662c7c861fb0fdc  SiStripApvGain   
# 201278       2019-10-25 16:37:43  c26f12cec6e935667594e6d9c26aa8e2594e1f2e  SiStripApvGain   
# 202093       2019-10-25 16:37:43  cf557c73534ef1c4bfc9f72e257dfd5b96ef17b5  SiStripApvGain   
# 203777       2019-10-25 16:37:43  52b16285d04bf50c35a751ec66ef4c541762a31e  SiStripApvGain   
# 204577       2019-10-25 16:37:43  08b6974edfe801bbd57394ff546dd8e0e729db46  SiStripApvGain   
# 205303       2019-10-25 16:37:43  30b0f9fc12eb85ce497a167622872b2f5bde28cd  SiStripApvGain   
# 205667       2019-10-25 16:37:43  5885255cbe46cfd0d02c31a9576c3a9f6bfe1f19  SiStripApvGain   
# 206257       2019-10-25 16:37:43  8a86056be2e356bf1de28e919e760a8630fe55d9  SiStripApvGain   
# 207214       2019-10-25 16:37:43  170c271c86dc06d6de7f7c87d3445b7b7a41f438  SiStripApvGain   
# 246951       2019-10-25 16:37:43  627dea56df454c888127e9e6f0046362a18df3bd  SiStripApvGain   
# 250974       2019-10-25 16:37:43  aca65617ef233eadb981274d238daea7ca9db23a  SiStripApvGain   
# 252116       2019-10-25 16:37:43  108f45243d72417478792e9bc10fc688751a8fc5  SiStripApvGain   
# 254227       2019-10-25 16:37:43  bb46a8556d4d1a968224f6afac9c67cd06672638  SiStripApvGain   
# 254289       2019-10-25 16:37:43  c13720e197088368b3d8322aa85f801866b67c23  SiStripApvGain   
# 254636       2019-10-25 16:37:43  63e23aa159d313239b99dd329f47bde0b81c6186  SiStripApvGain   
# 255981       2019-10-25 16:37:43  c13720e197088368b3d8322aa85f801866b67c23  SiStripApvGain   
# 256630       2019-10-25 16:37:43  4db1817332d232c21913a478c65c13377dc7823c  SiStripApvGain   
# 256868       2019-10-25 16:37:43  f2c05fa0ec3504f10555ed55df0e15ffd6dfbf84  SiStripApvGain   
# 256941       2019-10-25 16:37:43  2dabb12583db62a227042368618da9b7a2acd7b7  SiStripApvGain   
# 257969       2019-10-25 16:37:43  10eac8247477c769a0863372eb7d6f0cbe3fcc13  SiStripApvGain   
# 259152       2019-10-25 16:37:43  e1ab50d6e38e219745e4114dab22ebd7a004a64e  SiStripApvGain   
# 259626       2019-10-25 16:37:43  10eac8247477c769a0863372eb7d6f0cbe3fcc13  SiStripApvGain   
# 259924       2019-10-25 16:37:43  cc87ab147c15aa0cad045a3652f3b56ac6b871d3  SiStripApvGain   
# 260332       2019-10-25 16:37:43  e1ab50d6e38e219745e4114dab22ebd7a004a64e  SiStripApvGain   
# 271952       2019-10-25 16:37:43  4f107ab7e726bd08569b57fe8a6febf37b9ccf15  SiStripApvGain   
# 274602       2019-10-25 16:37:43  6c7efc020fe15ba484c331c98784cf3563e306a7  SiStripApvGain   
# 275567       2019-10-25 16:37:43  7e85b63a1bc328bdfaab5a3686eda69c67154b4b  SiStripApvGain   
# 277194       2019-10-25 16:37:43  451ae401501158ea61fddca96ffea5e577f8b174  SiStripApvGain   
# 278820       2019-10-25 16:37:43  252c5e2a36c2e5f8a51f083bf88daabf41ac3f16  SiStripApvGain   
# 279360       2019-10-25 16:37:43  bd3a3ddce874c98100348d036f6bd11fea965544  SiStripApvGain   
# 279596       2019-10-25 16:37:43  34362d87425ca8d65bdd8d32135ba5bee94a3f44  SiStripApvGain   
# 282024       2019-10-25 16:37:43  01c0d6c68ca16f649c569dfd85b9badbd86a34bb  SiStripApvGain   
# 283043       2019-10-25 16:37:43  1d5e741bd10832c16474a3957af5205baeba760a  SiStripApvGain   
# 283647       2019-10-25 16:37:43  1d5e741bd10832c16474a3957af5205baeba760a  SiStripApvGain   
# 285368       2019-10-25 16:37:43  f613daa5560331996c606232020fbe3b74a912ed  SiStripApvGain   
# 298430       2019-10-25 16:37:43  53d76e85ff754775b5dfc2165f98e096f7c2e84b  SiStripApvGain   
# 302322       2019-10-25 16:37:43  1063b428e1b700cbf3dc9343a91a0afd7f519fff  SiStripApvGain   
# 305040       2019-10-25 16:37:43  b3518f88e834932f922a0247a05fe2d7be8a8e60  SiStripApvGain   
# 306054       2019-10-25 16:37:43  28478ccb3485f229133bbd48c67dfb8d4c69d4aa  SiStripApvGain   
# 313120       2019-10-25 16:37:43  2b5bad86902a3f38122391dc6410d95716d328b6  SiStripApvGain   
# 317244       2019-10-25 16:37:43  d8a7f6c9ea5ca9272af550e7da31e55bc38e723f  SiStripApvGain   
# 320824       2019-10-25 16:37:43  a53409051a35f9b666247acb1b73cc697475df78  SiStripApvGain   
# 321475       2019-10-25 16:37:43  fa42302594204ccf2779d17def795b9546428700  SiStripApvGain   
# 323790       2019-10-25 16:37:43  475738753d337409cc87e5f1cbf93b2f21be59f3  SiStripApvGain  

declare -a arr=("1" "132440" "134308" "135149" "135175" "140058" "160325" "190000" "193093" "194115" "194825" "195540" "195915" "200042" "200961" "201278" "202093" "203777" "204577" "205303" "205667" "206257" "207214" "246951" "250974" "252116" "254227" "254289" "254636" "255981" "256630" "256868" "256941" "257969" "259152" "259626" "259924" "260332" "271952" "274602" "275567" "277194" "278820" "279360" "279596" "282024" "283043" "283647" "285368" "298430" "302322" "305040" "306054" "313120" "317244" "320824" "321475" "323790")

for i in "${arr[@]}"
do
    echo $i
    getPayloadData.py \
        --plugin pluginSiStripApvGain_PayloadInspector \
        --plot plot_SiStripApvGainsComparatorTwoTags \
        --tag SiStripApvGain_FromParticles_GR10_v12_offline  \
	--tagtwo cleanGains \
        --time_type Run \
        --iovs '{"start_iov": "'$i'", "end_iov": "'$i'"}' \
        --iovstwo '{"start_iov": "'$i'", "end_iov": "'$i'"}' \
        --db sqlite_file:forComparison.db \
        --test;

    mv *.png  $W_DIR/comparisons/SiStripG2GainComparison_IOV_$i.png
done

