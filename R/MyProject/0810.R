# 데이터 탐색과 통계분석

# n: 관측값, size: 시행횟수 , prob: 성공확률
rbinom(n = 10, size = 10, prob = 0.5)
rbinom(n = 100, size = 10, prob = 0.5)
rbinom(n = 100, size = 30, prob = 0.5)

# windows 창으로 hist 보기 가능
windows(width = 7, height = 5)

v <- rbinom(n = 1000000, size = 1000, prob = 0.4)
hist(v, col = "orange", breaks = 30)

# 균일 분포를 따른 랜덤 값
set.seed(2022)
v <- runif(n = 100000, min = 0, max = 100)
hist(v, col = "tomato", breaks = 20)

mean(v)
sd(v)
# 색깔 선택
colors()

v <- rnorm(n = 10000, mean = 50, sd = 20)
hist(v, col = "violet", breaks = 20)

# 몬테카를로 시뮬레이션으로 원주율(𝜋) 계산하기

##### 3장 #####
# 정규 분포 곡선
x <- seq(0, 100, length = 100)
# y <- dnorm(x, mean = 50, sd = 20)
y <- dunif(x, min = 0, max = 100)
plot(x, y, type = "l", #type = "b"
     col = "tomato", lwd = 3)


x <- seq(140, 200, length = 100)
y <- dnorm(x, mean = 170, sd = 10)
plot(x, y, type = "l", #type = "b"
     col = "tomato", lwd = 3)


# pnorm(35000, 30000, 10000) - pnorm(25000, 30000, 10000)
pnorm(35000, 30000, 10000) - pnorm(25000, 30000, 10000)

pnorm(1, 0, 1) - pnorm(-1, 0, 1)

pnorm(2) - pnorm(-2)
pnorm(2.56) - pnorm(-2.56)

(1 - pnorm(87, mean = 68, sd = 10)) * 200

pnorm(87, mean = 68, sd = 10, lower.tail = F)

#  연습문제 15.1:
pnorm(25000, 30000, 10000)

1-pnorm(35000, 30000, 10000)

pnorm(70, 60, 10, lower.tail = F)
pnorm(80, 70, 20, lower.tail = F)

x <- rbinom(10000, size = 100, prob = 0.5)
hist(x, col = "skyblue", breaks = 20)
curve(dnorm(x, 50, 5), 25, 75, col = "tomato",
      add = T, lwd = 3, lty = 2)

# 모집단, 표본집단
x <- 1:9

sample(x, size=7)

sample(x, size = 10, replace = T)


# 중심극한정리: central limit theorem
library(MASS)
height <- na.omit(survey$Height)
length(height)
hist(height, col = "skyblue", breaks = 20)

mean(height)
sd(height)

for (i in 1:100000) {
    samp <- height[sample(1:209, size = 30)]
    X.bar[i] <- mean(samp)
    X.sd[i] <- sd(samp)
}
hist(X.bar, col = "skyblue", 
     breaks = 20, prob = T)
x <- seq(160, 180, length = 200)
curve(dnorm(x, mean(height), sd(X.bar)), 
      160, 180, col = "tomato",
      add = T, lwd = 3, lty = 2)
# samp <- height[sample(1:209, size = 30)]
# X.bar <- mean(samp)
# X.sd <- sd(samp)
# X.bar
# X.sd

windows(width = 7, height = 5)
x.1 <- rnorm(n = 5000, mean = 70, sd = 5)
x.2 <- rnorm(n = 5000, mean = 50, sd = 5)
x <- c(x.1, x.2)
hist(x, col = "skyblue", breaks = 20)

X.bar <- c()
for (i in 1:100000) {
    samp <- x[sample(x, size = 30)]
    X.bar[i] <- mean(samp)
}
hist(X.bar, col = "skyblue", 
     breaks = 20, prob = T)
x.samp <- seq(30, 90, length = 200)
curve(dnorm(x.samp, mean(X), sd(X.bar)), 
      30, 90, col = "tomato",
      add = T, lwd = 3, lty = 2)

X.norm <- rnorm(n = 10000, mean = 50, sd = 25)
hist(X.norm, col = "orange", freq = F, ylim = c(0, 0.02))
mean(X.norm)
sd(X.norm)


cor(iris[, -5])

cor.test(iris$Petal.Width, iris$Petal.Length)

binom.test(x = 60, n = 100, p = 0.5)

qnorm(p = 0.5, mean = 50, sd = 10)

qnorm(p = 0.68, mean = 50, sd = 10)

qnorm(p = 0.975, mean = 50, sd = 10)

qnorm(p = 0.025, mean = 50, sd = 10)

qnorm(p = 0.005, mean = 50, sd = 10)
qnorm(p = 0.995, mean = 50, sd = 10)

pnorm(75.75829, mean = 50, sd = 10)
pnorm(24.24171, mean = 50, sd = 10)
pnorm(69.59964, mean = 50, sd = 10)
pnorm(30.40036, mean = 50, sd = 10)

binom.test(x = 65, n = 100, p = 0.5)

binom.test(x = 65, n = 100, p = 0.5, conf.level = 0.99)

shapiro.test(survey$Height)
hist(survey$Height)

shapiro.test(survey$Age)

shapiro.test(iris$Petal.Length)

shapiro.test(mtcars$mpg)


qqnorm(survey$Height, col = "skyblue")
qqline(survey$Height, col = "tomato", lwd = 3)

qqnorm(survey$Age, col = "skyblue")
qqline(survey$Age, col = "tomato", lwd = 3)


### 6장 ###
v <- rt(n = 10000, df = 29)
hist(v, col = "skyblue", prob = T)

x <- seq(-4, 4, length = 200)
curve(dt(x, df = 19), -4, 4, add = T,
         col = "tomato", lwd = 3, lty = 2)

curve(dnorm(x), -4, 4, add = T,
      col = "violet", lwd = 5, lty = 4)

pt(q = 2.04523, df = 29)
pt(q = 2.756386, df = 29)

qt(p = 0.975, df = 29)
qt(p = 0.995, df = 29)

library(MASS)
data(cats)
str(cats)

table(cats$Sex)

mean(cats$Bwt)
tapply(cats$Bwt, INDEX = list(Sex=cats$Sex), mean)

t.test(Bwt ~ Sex, data = cats, conf.level = 0.99)

str(sleep)

t.test(extra ~ group, data = sleep, paired = T)


#windows(width = 7, height = 5)




