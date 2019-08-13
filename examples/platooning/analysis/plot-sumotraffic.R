#load ggplot for quick and dirty plotting
library(ggplot2)

cntr = c(
   "ACC (0.3 s)",
   "ACC (1.2 s)",
   "CACC",
   "PLOEG",
   "CONSENSUS",
   "FLATBED"
)
#map controller id to name
controller <- function(id, headway) {
    ifelse(id == 0,
        ifelse(headway < 1, cntr[1], cntr[2]),
        cntr[id+2]
    )
}

load('../results/SumoTraffic.Rdata')
allData$controllerName <- controller(allData$controller, allData$headway)

p.speed <- ggplot(allData, aes(x=time, y=speed*3.6, col=factor(nodeId))) +
           geom_line() +
           facet_grid(controllerName~., scales='free_y')
ggsave('sumo-speed.pdf', p.speed, width=16, height=3)
#print(p.speed)

p.distance <- ggplot(subset(allData, distance != -1), aes(x=time, y=distance, col=factor(nodeId))) +
              geom_line() +
              facet_grid(controllerName~., scales='free_y')
ggsave('sumo-distance.pdf', p.distance, width=16, height=3)
#print(p.distance)

p.accel <- ggplot(allData, aes(x=time, y=acceleration, col=factor(nodeId))) +
           geom_line() +
           facet_grid(controllerName~., scales='free_y')
ggsave('sumo-acceleration.pdf', p.accel, width=16, height=3)
#print(p.accel)

p.caccel <- ggplot(allData, aes(x=time, y=controllerAcceleration, col=factor(nodeId))) +
            geom_line() +
            facet_grid(controllerName~., scales='free_y')
ggsave('sumo-controller-acceleration.pdf', p.caccel, width=16, height=3)
#print(p.caccel)

