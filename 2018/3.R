setwd('~/Documents/Personal/Misc/Advent/')
options(stringsAsFactors = F)
library(stringr)
claims_raw <- read.delim('3.txt', sep=' ', header = F)
names(claims_raw) <- c('Claim', 'At', 'Start', 'Size')

start_coords <- str_extract_all(claims_raw$Start, pattern = '[[0-9]]+', simplify = T)
start_coords <- as.data.frame(start_coords)
names(start_coords) <- c('Start_x', 'Start_y')
size_coords <- str_extract_all(claims_raw$Size, pattern = '[[0-9]]+', simplify = T)
size_coords <- as.data.frame(size_coords)
names(size_coords) <- c('Size_x', 'Size_y')

claims_full <- cbind(claims_raw, start_coords, size_coords)
claims_full[,4:8] <- apply(claims_full[,5:8], 2, as.numeric)
#setup bare matrix
range(claims_full$Start_x + claims_full$Size_x)
range(claims_full$Start_y + claims_full$Size_y) 


tapestry <- matrix(0,nrow=1000, ncol=1000)
for(i in 1:nrow(claims_full)){
  x <- claims_full$Size_x[i]
  y <- claims_full$Size_y[i]
  start_x <- claims_full$Start_x[i]
  start_y <- claims_full$Start_y[i]
  tapestry[(start_x+1):(start_x+x), (start_y+1):(start_y+y)] <- tapestry[(start_x+1):(start_x+x), (start_y+1):(start_y+y)] + 1
}
length(which(tapestry > 1))

for(i in 1:nrow(claims_full)){
  x <- claims_full$Size_x[i]
  y <- claims_full$Size_y[i]
  start_x <- claims_full$Start_x[i]
  start_y <- claims_full$Start_y[i]
  if(max(tapestry[(start_x+1):(start_x+x), (start_y+1):(start_y+y)]) == 1) {
    print(i)
  }
}

claims_full[894,]
