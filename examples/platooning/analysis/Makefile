# tool for indexing vec files
SCAVETOOL = scavetool
# scripts location
SCRIPTDIR = .
# results location
RESDIR = ../results
# script for merging
MERGESCRIPT = $(SCRIPTDIR)/merge.R

# match all .vec files for the SumoTraffic config
SUMOTRAFFIC      = $(wildcard $(RESDIR)/SumoTraffic*.vec)
# change suffix from .vec to .Rdata and add the sumo prefix
SUMOTRAFFIC_DATA = $(SUMOTRAFFIC:$(RESDIR)/%.vec=$(RESDIR)/sumo.%.Rdata)

# vector index files and Rdata files
VCI = $(VECTOR:%.vec=%.vci)
RDATA = $(VECTOR:%.vec=%.Rdata)
CSV = $(VECTOR:%.vec=%.csv)

# all make targets
all: SumoTraffic.Rdata 

# to make SumoTraffic.Rdata we need to merge all files starting with sumo.SumoTraffic
# before this, check that all SUMOTRAFFIC_DATA files have been processed
$(RESDIR)/SumoTraffic.Rdata: $(SUMOTRAFFIC_DATA)
	Rscript $(MERGESCRIPT) $(RESDIR)/ sumo.SumoTraffic $(notdir $@) map-config default Rdata
SumoTraffic.Rdata: $(RESDIR)/SumoTraffic.Rdata

# to make all sumo.*.Rdata files we need to run the generic parser
sumo.%.Rdata: %.vec %.vci
	Rscript generic-parser.R $< map-config default sumo Rdata

# if vec files are not indexed, index them
%.vci : %.vec
	$(SCAVETOOL) index $<

# helper to print variable values. e.g.: make print-DELAY_DATA
print-%:
	@echo '$*=$($*)'

# every intermediate file is kept instead of being automatically deleted.
# .vci files are detected as intermediate and thus cancelled when the make
# command terminates. however, such files can still be needed by other
# targets, so keep them instead of re-doing indexing
.SECONDARY :
