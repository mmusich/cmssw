#!/bin/bash

# Query for datasets
datasets=$(dasgoclient -query='dataset dataset=/Muon/Run2022*-TkAlZMuMu*/ALCARECO status=*')

# Loop over datasets
for dataset in $datasets; do
    echo "Querying files for dataset: $dataset"
    dasgoclient -query="file dataset=$dataset" > listOfFiles_data_${dataset//\//_}.txt
done



