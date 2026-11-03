#!/bin/bash
set -euo pipefail

RUN=398802
LUMIS=(3 125 246 366 485 605 724 842)   # sorted by LS

OUT=plots_final
rm -rf "$OUT"; mkdir -p "$OUT"          # avoid stale PNGs from earlier runs

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
mv *.pdf $OUT/P2_PercentDiffHistory_2025.pdf

getPayloadData.py \
    --plugin pluginEcalLaserAPDPNRatios_PayloadInspector \
    --plot plot_EcalLaserAPDPNRatiosP2MeanHistoryTwoTags \
    --tag EcalLaserAPDPNRatios_weekly_hlt \
    --tagtwo EcalLaserAPDPNRatios_prompt_v3_inRunLSIoVs \
    --time_type Run \
    --iovs '{"start_iov": "398675", "end_iov": "398858"}' \
    --iovstwo '{"start_iov": "1712296086732812", "end_iov": "1713082065748092"}' \
    --db Prod \
    --test

mv *.png $OUT/P2_MeanHistoryComparison_2025.png
mv *.pdf $OUT/P2_MeanHistoryComparison_2025.pdf

getPayloadData.py \
    --plugin pluginEcalLaserAPDPNRatios_PayloadInspector \
    --plot plot_EcalLaserAPDPNRatiosP2PercentDiffHistory \
    --tag EcalLaserAPDPNRatios_weekly_hlt \
    --tagtwo EcalLaserAPDPNRatios_prompt_v3_inRunLSIoVs \
    --time_type Run \
    --input_params '{"cmsLabel":"Preliminary","xAxis":"time"}' \
    --iovs '{"start_iov": "398675", "end_iov": "398858"}' \
    --iovstwo '{"start_iov": "1712296086732812", "end_iov": "1713082065748092"}' \
    --db Prod \
    --test

mv *.png $OUT/P2_PercentDiffHistory_2025_time.png
mv *.pdf $OUT/P2_PercentDiffHistory_2025_time.pdf

getPayloadData.py \
    --plugin pluginEcalLaserAPDPNRatios_PayloadInspector \
    --plot plot_EcalLaserAPDPNRatiosP2MeanHistoryTwoTags \
    --tag EcalLaserAPDPNRatios_weekly_hlt \
    --tagtwo EcalLaserAPDPNRatios_prompt_v3_inRunLSIoVs \
    --input_params '{"cmsLabel":"Preliminary","xAxis":"time"}' \
    --time_type Run \
    --iovs '{"start_iov": "398675", "end_iov": "398858"}' \
    --iovstwo '{"start_iov": "1712296086732812", "end_iov": "1713082065748092"}' \
    --db Prod \
    --test

mv *.png $OUT/P2_MeanHistoryComparison_2025_time.png
mv *.pdf $OUT/P2_MeanHistoryComparison_2025_time.pdf

