3 + 4
print("Hello, R!")

x = 3
3 = x
x <- 3
3 -> y

x <- 3

x <- 3
y <- 5
z <- x + y
print(z)
z

getwd()
plot(iris)
?iris
View(iris)

library(cowsay)
library(ggplot2)

say("안녕, 난 주니온이야!")
say("안녕", by = "chicken")

str(cars)
?cars


plot(cars$speed, cars$dist, 
     col = "tomato",
     pch = 19)

str(iris)
mean(iris$Petal.Length)
var(iris$Petal.Length)
sd(iris$Petal.Length)
hist(iris$Petal.Length, col = "tomato",
     breaks = 10)

v.1 <- 10

7%%3
7%/% 3
7.３


n <- 15
order <- "Diet"
if (n %% 3 == 0 & n %% 5 == 0) {
  order <- "PizzaChicken"
} else if (n %% 3 == 0) {
  order <- "Pizza"
} else if (n %% 5 == 0) {
  order <- "Chicken"
}
order


v <- c(10, 20, 30, 40, 50, 60, 70)
v

v[1]
v[7]

v[1:3]
v[3:6]

v[c(1, 3, 4 ,7)]
v[8]
v[6:8]


v
v[-(1:3)]
v

v <- c(10, 20, 30 , 40, 50, 60, 70)
v

v[c(T, T, F, F, F, T, F)]

v + 1

c(10, 20) + c(30, 40)

v > 30
v[v > 30]

1:9 + 1:2

rep(1:3, times = 3)

v
v[c(T, F)]

# 1에서 100까지의 수 중에서 7의 배수의 합은?
seq(7, 100, 7)
sum(seq(7, 100, 7))

v <- 1:100
sum(v[v %% 7 == 0])

v <- c()
for (i in 1:10) {
  v <- c(v, i)
}
v
# --------------------------------------
v <- c()
for (i in 1:10) {
  v[i] <- i
}
v

v <- c(10, 20, 30)
v

v[7] <- 70
v

iris$Sepal.Length
iris$Species

f <- factor(c(1, 2, 1, 2),
            levels = 1:3,
            labels = c("Male", "Female", "TG"))
levels(f)

f[f == "Male"]
f[f == "Female"]
f[6] <- "Male"
f

f[7] <- "TG"
f

v.1 <- c(1, 2, 3)
v.2 <- c("F", "F", "M")
c(v.1, v.2)

lst <- list(id = v.1, gender = factor(v.2))
lst

lst[[1:2]]

lst$id
lst$gender

v <- 1:10
which(v > 5)

n <- 32
# n의 약수를 모두 출력하시오.
# 반복문은 사용하지 마시오.
v <- c(1:n)
v[n%%v == 0]

n <- 32
v <- 1:n
v[n %% v == 0]
length(v[n %% v ==0])

n %% v
n %% v ==0
v[n %% v == 0]
length(v[n %% v ==0])

iris
str(iris)
view(iris)

iris[ 1 ,  ]
iris[ 1:5 ,  ]

iris[ 1:5 , 1 ]
iris[ 1:5 , 1:2 ]

iris[ 1:5 , 1:4 ]
iris[ 1:5 , -5 ]

iris[, 1]
iris$Sepal.Length
iris[ iris$Sepal.Length < 5 , -5 ]

nrow(iris[ iris$Sepal.Length < 5 , -5 ])

# Petal.Length 가 평균보다 큰 데이터의
# Petal.Length 평균 값은 얼마인가?
mean(iris$Petal.Length)
mean(iris[iris$Petal.Length > mean(iris$Petal.Length), -5]$Petal.Width)

# --------------------------------------------
mean(iris[iris$Petal.Length > mean(iris$Petal.Length), "Petal.Width"])

fun <- function (x) {
  return (x + y + 5)
}
y <- 3
fun(5)

my.fun <- function (x, y, z) {
    cat(x, y, z, '\n')
    return (x + y * 2 + z * 3)
}
my.fun
my.fun(1, 2, 3)

seq(from =2, to = 100, by =2)
seq(2, 100, 2)

rep(x = 1:3, each = 2)

head(iris[, -5], n =5)

hist(iris$Sepal.Length, 
     main = "histograM",
     xlab = "x label",
     ylab = "y label")

head(x = iris[, -5], n = 10)

# n의 약수 구하기

divisor <- function (n) {
  # to do

  v <- 1:n
  x <- v[n %% v == 0]
  return (x)
}

divisor(n = 32)
# ------------------------------------
divisor <- function (n) {
  # to do
  
  v <- 1:n
  x <- v[n %% v == 0]
  x
}

divisor(n = 32)
# ------------------------------------

divisor <- function (n) length((1:n)[n %% (1:n) == 0])

divisor(n = 32)
# 05 함수의 이해 (연습문제 4.1)
div.cnt <- function (n) length((1:n)[n %% (1:n) == 0])
div.cnt(n = 32)

for (i in 1:15) {
  cat(i, div.cnt(i), '\n')
}
sapply(1:15, FUN = div.cnt)

# 05 함수의 이해 (연습문제 4.2)
prime.cnt <- 

# --------------------------------------
f1 <- function (n) n ^ 2
f1(n = 5)

sapply(1:9, FUN = f1)

# 1에서 100까지의 소수
(1:100)[sapply(1:100, FUN = div.cnt) == 2]

# 1에서 100까지의 소수 갯수
length((1:100)[sapply(1:100, FUN = div.cnt) == 2])

##### Homework #####
### 2장 2.1
class(iris$Species)

levels(iris$Species)
table(iris$Species)
barplot(table(iris$Species), col="tomato",
        main ="품종의 막대그래프",
        xlab ="품종",
        ylab ="개수")

### 2장 2.2
# 꽃잎의 너비(Petal.Width)에 대해서 다음 통계랑을 구하시오
# 평균- mean, 분산- var, 표준편차- sd
mean(iris$Petal.Width)
var(iris$Petal.Width)
sd(iris$Petal.Width)

hist(iris$Petal.Width, col = "tomato",
     main ="꽃잎의 너비에 대한 히스토그램",
     xlab ="꽃잎의 너비",
     ylab ="빈도수")

### 2장 2.3
# mtcars 데이터셋에서
# 마력(hp)의 히스토그램을 그려보시오.
# 히스토그램에서 축의 범위를 바꿔보시오. x축:c(0,400), y축:c(0,12)
hist(mtcars$hp,
     xlim = c(0, 400),
     ylim = c(0, 12))

# 마력(hp)과 연비(mpg)의 관계를 나타내는 산점도를 그려보시오.
plot(mtcars$hp, mtcars$mpg, col = "tomato", pch = 19)


### 2장 2.4
# R의 내장 데이터셋인 cars 데이터셋에 대하여
# 변수와 관측값의 개수는 각각 얼마?
str(cars)
# speed, dist 변수에 대해 통계량을 각각 구하시오.
# 평균, 중앙값, 최대값, 최소값, 1 사분위 값, 3 사분위 값
summary(cars$speed)
summary(cars$dist)
# speed와 dist 변수의 관계를 나타내는 산점도를 그려보시오
# 산점도에서 점의 색과 모양을 바꿔보시오
# 산점도의 세로축과 가로축의 범위를 바꿔보시오
plot(cars$speed, cars$dist)

### 3장 3.1
# 한 변의 길이가 x인 정사각형의 넓이 area를 구하는 수싯을 만드시오.
## x가 5, 10, 15일 때 area의 값을 확인해 보시오.
area <- function (v) v ^ 2
x <- c(5, 10, 15)
y <- area(x)
y

area <- function (v) v ^ 2
sapply(x, area)
# 반지름의 길이가 r인 원의 둘레 round와 넓이 area를 구하는 수식어를 만드시오.
## r이 5, 10, 15일 때 round와 area의 값을 확인해 보시오.
round <- function (v) 2 * pi * r
r <- c(5, 10, 15)
x <- round(r)
x

area <- function (v) pi * (r ^ 2)
r <- c(5, 10, 15)
x <- round(r)
x

### 3장 3.2
v <- 1:15
order <- ifelse(v %% 15 == 0, "PizzaChicken",
                ifelse (v%%3 ==0, "Pizza",
                        ifelse(v %% 5 == 0, "Chicken", "Diet")))

order

order <- function(v) ifelse(v %% 15 == 0, "PizzaChicken",
                            ifelse (v%%3 ==0, "Pizza",
                                    ifelse(v %% 5 == 0, "Chicken", "Diet")))
v <- 1:15
w <- order(v)
w

### 3장 3.3
sum((1:10) ^ 3)

cumsum <- function(x) sum((1:x) ^ 3)
n <- c(10, 15, 20)
s <- sapply(n, cumsum)
s

cumsum.1 <- function (x) ((x*(x+1)/2)^2)
sapply(n, cumsum.1)


# 0805-------------------------------------------------
div <- function (n) (1:n)[n %% (1:n) == 0]
div(48)


div.2 <- function (n) {
  for (i in 1:sqrt(n)) {
    if (n%%i == 0)
      cat(i, n / i, '\n')
  }
}
div.2(48)

### 데이터 프레임
df <- iris
str(df)
class(df)
dim(df)
nrow(df)
ncol(df)
head(df)

rownames(df)
colnames(df)

v <- c(85, 77, 96)
v

names(v)
names(v) <- c('Kor', 'Eng', 'Math')
names(v)
v

v["Kor"]
v[c("Eng", "Math")]

df$Sepal.Length
df$Sepal.Width

df$Sepal.Sum <-  df$Sepal.Length + df$Sepal.Width
str(df)

head(df[,5:6])

df$Sepal.Sep <- ifelse(df$Sepal.Sum > mean(df$Sepal.Sum),
                        "Big", "Small")
df$Sepal.Sep <- factor(df$Sepal.Sep)
str(df)
levels(df$Sepal.Sep)
table(df$Sepal.Sep)
barplot(table(df$Sepal.Sep), col="tomato")

?state.x77
class(state.x77)
is.data.frame(state.x77)
st <- as.data.frame(state.x77)
class(st)
str(st)
dim(st)

View(st)

nrow(st)
col(st)
max(st$Murder)
max(st$Population)
nrow(max(st$Population))

df <- iris
df$Sepal.Sum <- df$Sepal.Length + df$Sepal.Width
write.csv(df, 'my.iris.csv', row.names = F)
getwd()

df <- read.csv("my.iris.csv", header = T)
str(df)

##### 엑셀 파일
# install.packages("readxl")
library(readxl)
df <- read_excel("성적표.xlsx", sheet = 1)
str(df)
class(df)

df <- data.frame(df) # df를 xlsx
str(df)
# df$평균 <- (df$파이썬 + df$머신러닝 + df$R) / 3
df$평균 <- apply(df[, 3:5], MARGIN = 1, mean)
head(df)
write.csv(df, "score.csv", row.names = F)




