setwd('~/Documents/Personal/Misc/Advent/')
options(stringsAsFactors = F)
library(stringr)
times <- read.delim('4.txt', sep='\t', header = F)
timestamp <- str_extract_all(times$V1, pattern = "\\[.*\\]")
timestamp <- unlist(timestamp)
timestamp <- gsub('\\[|\\]', '', timestamp)
timestamp <- strptime(timestamp, format = '%Y-%m-%d %H:%M')
descriptions <- str_extract_all(times$V1, pattern = "\\][[ ]].*")
descriptions <- unlist(descriptions)
descriptions <- gsub('\\] ', '', descriptions)
time_descriptions_df <- data.frame(timestamp = timestamp[order(timestamp)], description = descriptions[order(timestamp)])

guard_df <- data.frame(guard = numeric(), minute_asleep = numeric())
for (i in 1:nrow(time_descriptions_df)){
  k <- str_extract(time_descriptions_df$description[i], "[0-9]+")
  if(!is.na(k)) {
    guard_num <- k
  } else {
    starttime <- as.numeric(format(time_descriptions_df$timestamp[i], "%M"))
  }
}