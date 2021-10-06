bar_plot <- function(date_wanted){

  data <- import_CSV()
  
  timestamp <- data[1]
  prox <- data[2]
  
  date <- strptime(data$TimeStamp, format='%d/%m/%Y %H:%M:%S')
  
  data$date <- strftime(date, format="%d/%m/%Y")
  
  p <- ggplotly(ggplot(data=filter(data, data$date==date_wanted), aes(x=TimeStamp, y=Proximity, fill=Proximity, text=paste("Timestamp: ", TimeStamp, "<br>Proximity: ", Proximity))) + geom_bar(stat="identity", width = 0.75 )+
    theme_bw() +theme(axis.text.x = element_blank(),axis.ticks.x=element_blank())+
    xlab("Time of Day") +
    ylab("Proximity Reading") + labs(fill='Proximity Scale',title="Proximity Sensor Readings"), tooltip="text") 
  return(p)
}

import_CSV <- function(file){
  rm(list=ls())
  if(!require("pacman")) install.packages("pacman")
  pacman::p_load(tidyverse,ggplot2,ggthemes, plotly,googlesheets,gsheet,primes,tidyverse,latex2exp)
  
  data <- read.csv(file="C:\\Users\\JJ\\Documents\\R\\HelloWorld\\Proximity.csv", header=TRUE, sep=",")
  return(data)
}
