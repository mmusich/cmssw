#!/bin/bash
set -euo pipefail

RUN=398802
LUMIS=(3 125 246 366 485 605 724 842)   # sorted by LS

OUT=plots
rm -rf "$OUT"; mkdir -p "$OUT"          # avoid stale PNGs from earlier runs

for ls in "${LUMIS[@]}"; do
  iov=$(( (RUN << 32) | ls ))           # packed run/LS IoV
  name=$(printf "LS_%04d" "$ls")
  getPayloadData.py \
    --plugin pluginEcalLaserAPDPNRatios_PayloadInspector \
    --plot plot_EcalLaserAPDPNRatiosHistCompareTwoTags \
    --tag EcalLaserAPDPNRatios_prompt_v3_inRunLSIoVs \
    --input_params "{}" \
    --tagtwo EcalLaserAPDPNRatios_weekly_hlt \
    --time_type Run \
    --iovs "{\"start_iov\": \"${iov}\", \"end_iov\": \"${iov}\"}" \
    --iovstwo '{"start_iov": "398785", "end_iov": "398785"}' \
    --db Prod --test 
  mv *.png $OUT/$name.png
done

# explicit numeric LS ordering for the GIF
#convert -delay 100 -loop 0 $(ls $OUT/LS_*.png | sort -V) apdpn_ratios_compare.gif

getPayloadData.py \
    --plugin pluginEcalLaserAPDPNRatios_PayloadInspector \
    --plot plot_EcalLaserAPDPNRatiosP2PercentDiffHistory \
    --tag EcalLaserAPDPNRatios_weekly_hlt \
    --tagtwo EcalLaserAPDPNRatios_prompt_v3_inRunLSIoVs \
    --time_type Run \
    --iovs '{"start_iov": "401623", "end_iov": "403937"}' \
    --iovstwo '{"start_iov": "1724957650321411", "end_iov": "1734896204644951"}' \
    --db Prod \
    --test

mv *.png $OUT/P2_PercentDiffHistory_2026.png

getPayloadData.py \
    --plugin pluginEcalLaserAPDPNRatios_PayloadInspector \
    --plot plot_EcalLaserAPDPNRatiosP2PercentDiffHistory \
    --tag EcalLaserAPDPNRatios_weekly_hlt \
    --tagtwo EcalLaserAPDPNRatios_prompt_v3_inRunLSIoVs \
    --time_type Run \
    --iovs '{"start_iov": "398675", "end_iov": "398858"}' \
    --iovstwo '{"start_iov": "1712296086732812", "end_iov": "1713082065748092"}' \
    --db Prod \
    --test

mv *.png $OUT/P2_PercentDiffHistory_2025.png

getPayloadData.py \
    --plugin pluginEcalLaserAPDPNRatios_PayloadInspector \
    --plot plot_EcalLaserAPDPNRatiosP2MeanHistoryTwoTags \
    --tag EcalLaserAPDPNRatios_weekly_hlt \
    --tagtwo EcalLaserAPDPNRatios_prompt_v3_inRunLSIoVs \
    --time_type Run \
    -input_params '{"cmsLabel":"Preliminary"}' \
    --iovs '{"start_iov": "401623", "end_iov": "403937"}' \
    --iovstwo '{"start_iov": "1724957650321411", "end_iov": "1734896204644951"}' \
    --db Prod \
    --test

mv *.png $OUT/P2_MeanHistoryComparison_2026.png

getPayloadData.py \
    --plugin pluginEcalLaserAPDPNRatios_PayloadInspector \
    --plot plot_EcalLaserAPDPNRatiosP2MeanHistoryTwoTags \
    --tag EcalLaserAPDPNRatios_weekly_hlt \
    --tagtwo EcalLaserAPDPNRatios_prompt_v3_inRunLSIoVs \
    --time_type Run \
    -input_params '{"cmsLabel":"Preliminary"}' \
    --iovs '{"start_iov": "398675", "end_iov": "398858"}' \
    --iovstwo '{"start_iov": "1712296086732812", "end_iov": "1713082065748092"}' \
    --db Prod \
    --test

mv *.png $OUT/P2_MeanHistoryComparison_2025.png
