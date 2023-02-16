sink("./23.R-Project/output2.doc", append = TRUE, split = TRUE)
# R语言第二次作业，环境：R，编译器：VSCode('PPT第一题,未要求写，可以不做！')
# 恰有一次出现正面
p_1 <- dbinom(1, size = 3, prob = 0.5)
print(p_1)

# 至少有一次出现正面
p_2 <- 1 - dbinom(0, size = 3, prob = 0.5)
print((p_2))


print('-------------------放回的情况-------------------')
x <- c('白1', '白2', '白3', '白4', '红1', '红2')

# 取到两只都是白球的概率
p_3 <- dbinom(2, size = 2, prob = 2 / 3) 
print(p_3)

# 取到两只球颜色相同的概率
p_4 <- dbinom(2, size = 2, prob = 1 / 3) + dbinom(2, size = 2, prob = 2 / 3)
print(p_4)

# 取到两只球中至少有一只是白球的概率
p_5 <- 1 - dbinom(0, size = 2, prob = 2 / 3)
print(p_5)

print('-------------------不放回的情况-------------------')
# 考虑不放回的情况
# 取到两只都是白球的概率
sam <- choose(4, 1) * choose(3, 1)
all <- choose(6, 1) * choose(5, 1)
p_6 <- sam / all
print(p_6)

# 取到两只球颜色相同的概率
p_7 <- p_6 + (choose(2 , 1) / all)
print(p_7)

# 取到两只球中至少有一只是白球的概率
p_8 <- 1 - (choose(2, 1) / all)
print(p_8)

print('-------------------利用outer函数的放回情况-------------------')
output <- outer(x, x, FUN = 'paste')
print(output)
counts_3 <- 0
counts_4 <- 0
for (x_1 in x){
    for (x_2 in x){
        if (substr(x_1, 1, 1) == '白' & substr(x_2, 1, 1) == '白'){
            counts_3 <- counts_3 + 1
        }
        if (substr(x_1, 1, 1) == '红' & substr(x_2, 1, 1) == '红'){
            counts_4 <- counts_4 + 1
        }
    }
}
all_2 <- length(x) **2
a_4 <- counts_3 / all_2
print(a_4)

a_5 <- (counts_3 + counts_4) / all_2
print(a_5)

a_6 <- 1 - counts_4 / all_2
print(a_6)


print('-------------------利用outer函数的不放回情况-------------------')
counts_1 <- 0
counts_2 <- 0
x <- c('白1', '白2', '白3', '白4', '红1', '红2')
for (x_1 in x){
    y <- x[-which(x == x_1)]
    out <- outer(x_1, y, FUN = "paste")
    print(out)
    for (y_1 in y){
        if (substr(x_1, 1, 1) == '白' & substr(y_1, 1, 1) == '白'){
            counts_1 <- counts_1 + 1
        }
        if (substr(x_1, 1, 1) == '红' & substr(y_1, 1, 1) == '红'){
            counts_2 <- counts_2 + 1
        }
    }
}
all <- length(x) * length(y)
a_1 <- counts_1 / all
print(a_1)

a_2 <- a_1 + (counts_2 / all)
print(a_2)

a_3 <- 1 - (counts_2 / all)
print(a_3)

sink()