# Read and parse
setwd('~/Documents/Personal/Misc/Advent/')
input <- read.table('2.txt')
library(stringr)

twos <- 0
threes <- 0
for(i in 1:nrow(input)){
  tab_input <- table(unlist(strsplit(input$V1[i], split='')))
  twos <- ifelse(length(which(tab_input==2)) > 0, twos+1, twos)
  threes <- ifelse(length(which(tab_input==3)) > 0, threes+1, threes)
}
twos*threes
#part 2
library(stringdist)
string_m <- stringdistmatrix(input$V1, input$V1)
matches <- which(string_m==1)
matches_string <- input$V1[matches[1,]]
match_matrix <- do.call('rbind', strsplit(matches_string, ''))
paste(match_matrix[,match_matrix[1,] == match_matrix[2,]][1,], collapse='')
