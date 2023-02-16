sink("./23.R-Project/output.doc", append = TRUE, split = TRUE)
mytxt <- "
date age gender
20201101 25 1
20210601 68 2
20200801 32 1
20221001 36 1
20200201 70 2
"
date <- c("20201101", "20210601", "20200801", "20221001", "20200201")
age <- c(25, 68, 32, 36, 70)
gender <- c(1, 2, 1, 1, 2)
data_1 <- data.frame(date, age, gender)
print(data_1)

id <- c("a", "b", "c", "d", "e")
data_2 <- data.frame(id, data_1)
print(data_2)

data_3 <- subset(data_2, age < 65, select <- c("id", "date", "age", "gender"))
print(data_3)

data_4 <- data_2
data_4$group[data_2$age < 65] <- "young"
data_4$group[data_2$age > 65] <- "old"
print(data_4)

data_5 <- data_2
data_5$gender[data_2$gender == 1] <- "female"
data_5$gender[data_2$gender == 2] <- "male"
print(data_5)

print(data_5$gender)

data_date <- as.Date(data_2$date, "%Y%m%d")
data_2$date <- data_date
data_7 <- data.frame(data_2)
print(data_7)

sort_date <- data_date[order(data_date)]
sort_age <- age[order(data_date)]
sort_gender <- gender[order(data_date)]
sort_id <- id[order(data_date)]
date <- sort_date
age <- sort_age
gender <- sort_gender
id <- sort_id
data_8 <- data.frame(id, date, age, gender)
print(data_8)

x <- c(77, 56, 98, 69, 35, 37, 79, 33, 28, 36, 92, 50)
print(sort(x))
print(rank(x))
print(x[rank(x) == 10])
a <- x[rank(x) == 10]
print(order(x)[sort(x) == a])
sink()