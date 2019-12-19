#!/bin/bash

for d in *method*/ ; do
	Rscript GenerateCsv.R $d
	python settlingTime.py $d
	echo $d "finish"
done

python STMerge.py
