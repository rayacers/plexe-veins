#!/bin/bash

for d in */ ; do
	Rscript GenerateCsv.R $d
	python settlingTime.py $d
done
