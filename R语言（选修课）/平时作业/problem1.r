sink("./23.R-Project/R软件与数据分析测试.doc", append = TRUE, split = TRUE)

# 第一问,定义函数求解t值

tst <- function(x, y) {
    x_mean <- mean(x)
    y_mean <- mean(y)
    x_std <- sd(x) * sd(x)
    y_std <- sd(y) * sd(y)
    m <- length(x)
    n <- length(y)
    s_p <- sqrt(((m - 1) * x_std + (n - 1) * y_std) / (m + n - 2))
    t_value <- ((x_mean - y_mean) / (s_p * (sqrt(1 / m + 1 / n))))
    return(t_value)
}
x <- c(1, 4, 3, 6, 5)
y <- c(5, 4, 7, 6, 10)
print(tst(x, y))


# 第二问,绘图

data <- read.table('./23.R-Project/mydata1.txt', header = TRUE,  sep = '	',  stringsAsFactors = FALSE)
data[,1] <- gsub('Q1', '-03-01', data[,1])
data[,1] <- gsub('Q2', '-06-01', data[,1])
data[,1] <- gsub('Q3', '-09-01', data[,1])
data[,1] <- gsub('Q4', '-12-01', data[,1])
data[,1] <- as.Date(data[,1], format = '%Y-%m-%d')
print(data)
print(data[, 1])

par(mfrow = c(2, 2))
Time <- data[, 1]

plot(Time, data[,2], type = "b", pch = 16, lty = 1, main = "line plot",ylab = "")
lines(Time, data[,3], type = "b", pch = 17, lty = 3)
legend("topleft", inset = .05, title = "country", c("UK", "US"), lty = c(1, 3), pch = c(16, 17))
library(reshape2)
data2 <- melt(data, id = 'time')

boxplot(data2[,3]~data2[,2], data, main = 'box plot', ylab = 'value', xlab = 'value')

hist(data[,2], freq = F, main = 'Histogram and Density Curve', xlab = 'puk')
lines(density(data[,2]))

h <- hist(data[,3], xlab = "pus", main = "Histogram with Normal Curve")
x <- seq(min(data[,3]), max(data[,3]), length = 40)
y <- dnorm(x, mean(data[,3]), sd(data[,3]))
y <- y * diff(h$mids[1:2]) * length(data[,3])
lines(x, y)

sink()