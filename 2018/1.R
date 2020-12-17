read.table('https://adventofcode.com/2018/day/1/input')
library(XML)
# Read and parse HTML file
setwd('~/Documents/Personal/Misc/Advent/')
input <- read.table('1.txt')
start <- 0
for (i in 1:nrow(input)){
  start <- start + input$V1[i]
}
start
#2

cum_input <- cumsum(rep(input$V1,1))
the_repeats <- which(duplicated(cum_input))

j <- 0
while(length(the_repeats) < 1){
  j <- j+1
  cum_input <- cumsum(rep(input$V1,j))
  the_repeats <- which(duplicated(cum_input))
}
cum_input[the_repeats[1]]
