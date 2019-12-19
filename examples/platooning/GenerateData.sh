#!/bin/bash

rm *.log

cd ~/src/plexe-veins
./configure
make -j 2 MODE=release

cd examples/platooning
./run -u Cmdenv -c SumoTrafficNoGui -r 4

cd analysis
make
Rscript plot-sumotraffic.R

mkdir -p new
cp sumo-acceleration.pdf new/acceleration.pdf
cp sumo-controller-acceleration.pdf new/controller-acceleration.pdf
cp sumo-distance.pdf new/distance.pdf
cp sumo-speed.pdf new/speed.pdf
cp ../results/SumoTraffic.Rdata new/SumoTraffic.Rdata
