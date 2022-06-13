install.packages('readxl')
library(readxl)



xlsadata <- read_excel("D:\pycpha\langauge\R\220610") # \를 / 로 바꿔라
View(xlsadata)

data_raw <- xlsadata[, c(2, 3, 4, 7)]
data_raw

head(data_raw)

#컴럼명 영어로 변경
#컬럼명이 한글이면 오류 가능성있음

names(data_raw)  #열의 헤더값 출력
names(data_raw) <- c("state", "city", "name", "addr")  #헤더값 value 수정
names(data_raw)

table(data_raw$state)
barplot(table(data_raw$state))


daejeon_data <- data_raw[data_raw$state == '대전', ]
daejeon_data
head(daejeon_data)
nrow(daejeon_data)

install.packages('ggmap')
library(ggmap)
ggmap_key <- "AIzaSyBwsEGi4zUu6qNjaZfWFQqcTxp7BiHS0tE"
register_google(ggmap_key)
daejeon_data <-mutate_geocode(data = daejeon_data,location = name, source = "google")
head(daejeon_data)
head(daejeon_data$lon)


daejeon_map <- get_googlemap('대전', maptype = 'roadmap', zoom = 12)
ggmap(daejeon_map) + geom_point(data = daejeon_data,
                                aes(x = lon, y = lat, color = factor(name)),
                                size = 3)





#print(xlsadata)
