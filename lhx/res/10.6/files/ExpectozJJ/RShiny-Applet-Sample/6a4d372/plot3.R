rm(list=ls())
if(!require("pacman")) install.packages("pacman")
pacman::p_load(tidyverse,ggplot2,ggthemes,googlesheets,gsheet,primes,tidyverse,latex2exp)

file <- file.path('Training.txt')
features <- read.table(file)

p<- plot_ly() %>%
  add_lines(x=~c(1:200),y=~features[1:200,1], type='scatter', mode='lines', name='X-axis') %>%
  add_lines(x=~c(1:200),y=~features[1:200,2], type='scatter', mode='lines',name='Y-axis') %>%
  add_lines(x=~c(1:200),y=~features[1:200,3], type='scatter', mode='lines',name='Z-axis') %>%
  layout(title = 'Training Data',
         xaxis = list(title = 'minutes'),
         yaxis = list(title = 'm/s<sup>2</sup>'))