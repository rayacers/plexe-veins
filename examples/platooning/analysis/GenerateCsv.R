args<-commandArgs(T)

load(paste0(args[1],"/SumoTraffic.Rdata"))

write.csv(allData,paste0(args[1],"/output.csv"))
