#!/bin/bash
set -euo pipefail

RUN=398802
LUMIS=(3 125 246 366 485 605 724 842)   # sorted by LS

OUT=plots_final_all
rm -rf "$OUT"; mkdir -p "$OUT"          # avoid stale PNGs from earlier runs

# plot name in the plugin -> output name
declare -A PLOTS=(
    [PercentDiffHistory]=PercentDiffHistory
    [MeanHistoryTwoTags]=MeanHistoryComparison
)

# x axis -> input parameters and output suffix
declare -A PARAMS=(
    [run]='{}'
    [time]='{"cmsLabel":"Preliminary","xAxis":"time"}'
)
declare -A SUFFIX=(
    [run]=''
    [time]='_time'
)

for P in 1 2 3; do
    for PLOT in PercentDiffHistory MeanHistoryTwoTags; do
        for AXIS in run time; do
            NAME="P${P}_${PLOTS[$PLOT]}_2025${SUFFIX[$AXIS]}"
            echo ">>> $NAME"
            getPayloadData.py \
                --plugin pluginEcalLaserAPDPNRatios_PayloadInspector \
                --plot plot_EcalLaserAPDPNRatiosP${P}${PLOT} \
                --tag EcalLaserAPDPNRatios_weekly_hlt \
                --tagtwo EcalLaserAPDPNRatios_prompt_v3_inRunLSIoVs \
                --time_type Run \
                --input_params "${PARAMS[$AXIS]}" \
                --iovs '{"start_iov": "398675", "end_iov": "398858"}' \
                --iovstwo '{"start_iov": "1712296086732812", "end_iov": "1713082065748092"}' \
                --db Prod \
                --test

            mv ./*.png "$OUT/$NAME.png"
            mv ./*.pdf "$OUT/$NAME.pdf"
        done
    done
done
