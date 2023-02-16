mytxt <- "
date age gender
20201101 25 1
20210601 68 2
20200801 32 1
20221001 36 1
20200201 70 2
"
group <- c("old", "young")
x <- c(77, 56, 98, 69, 35, 37, 79, 33, 28, 36, 92, 50)

# sink("./23.R-Project/output.doc", append = TRUE, split = TRUE)
print("===========================第一题=============================")
date <- c("20201101", "20210601", "20200801", "20221001", "20200201")
age <- c(15, 68, 32, 36, 70)
gender <- c(1, 2, 1, 1, 2)
my_data <- data.frame(date, age, gender)
print(my_data)
print("===========================第二题=============================")
id <- c("01", "02", "03", "04", "05")
my_data_2 <- data.frame(my_data, id)
print(my_data_2)
my_data_3 <- cbind(my_data, id)
print(my_data_3)
print("===========================第三题=============================")
print(subset(my_data_2, age < 65, select <- c("date", "age", "gender", "id")))
print("===========================第四题=============================")
my_data_2$group[my_data_2$age < 65] <- "young"
my_data_2$group[my_data_2$age > 65] <- "old"
print(my_data_2)
print("===========================第五题=============================")
my_data_2$gender[my_data_2$gender == 1] <- "female"
my_data_2$gender[my_data_2$gender == 2] <- "male"
print(my_data_2)
print("===========================第六题=============================")
print(my_data_2$gender)
print("===========================第七题=============================")
new_date <- as.Date(my_data$date, "%Y%m%d")
my_data$date <- new_date
my_data_4 <- data.frame(my_data, id)
print(my_data_4)
print("===========================第八题=============================")
sort_date <- new_date[order(new_date)]
sort_age <- age[order(new_date)]
sort_gender <- gender[order(new_date)]
sort_id <- id[order(new_date)]
my_data_5 <- data.frame(sort_date, sort_age, sort_gender, sort_id)
print(my_data_5)
print("===========================第九题=============================")
print(sort(x))
print(rank(x))
print(x[rank(x) == 10])
a = x[rank(x) == 3]
print(order(x)[sort(x) == a])
# sink()