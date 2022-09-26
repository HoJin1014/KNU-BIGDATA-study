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
# ----------------------------------------------
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
df$평균 <- round(apply(df[, 3:5], MARGIN = 1, mean), 2)
head(df)
write.csv(df, "score.csv", row.names = F,)

df$평균
round(apply(df[, 3:5], MARGIN = 1, mean),digits=1)
?round

rm(list=ls())
a=1


# 7장 결측치
x <- c(45, NA, 87, 63, 55, NA, 72, 61, 59, 68)
is.na(x)

x[is.na(x)]

x[!is.na(x)]

x[is.na(x)] <- mean(x, na.rm =  T)
x

aq <- airquality
str(aq)
mean(aq$Ozone, na.rm = T)
is.na(aq$Ozone)
aq$Ozone[is.na(aq$Ozone)]
sum(is.na(aq$Ozone))

ozone <- aq$Ozone
ozone[is.na(ozone)] <- mean(ozone, na.rm = T)
ozone

mean(aq$Ozone, na.rm = T)
mean(ozone)

sd(aq$Ozone, na.rm = T)
sd(ozone)

dim(aq)

ozone <- aq$Ozone
ozone[is.na(ozone)] <- sample(na.omit(aq$Ozone), 37)
ozone

mean(aq$Ozone, na.rm = T)
mean(ozone)

sd(aq$Ozone, na.rm = T)
sd(ozone)


aq <- airquality
complete.cases(aq)
aq[!complete.cases(aq), ]
aq <- aq[complete.cases(aq), ]
aq

# install.packages("VIM")
library(VIM)
?aggr
aggr(airquality)

# 이상치: outliers or anomalies

st <- data.frame(state.x77)
boxplot(st$Income,
        col = "tomato",
        pch = 19,
        border = 'red')

class(boxplot.stats(st$Income))

boxplot.stats(st$Income)$out

st[st$Income == boxplot.stats(st$Income)$out, ]

df <- iris
boxplot(df$Sepal.Length, col = 'skyblue')

boxplot(Petal.Length ~ Species, data = iris,
        col = "steelblue")

boxplot(Petal.Width ~ Species, data = iris,
        col = "steelblue")

iris[iris$Species == 'setosa', ]

outlier <- boxplot.stats(iris[iris$Species == 'setosa', 4])$out

iris[iris$Petal.Width == outlier, ]

iris[iris$Petal.Width %in% outlier, ]

####### 8장 #######
st <- data.frame(state.x77)
st[st$Population == max(st$Population), c(3, 6)]

subset(st,
       subset = st$Population == max(st$Population),
       select = c(3, 6))

iris[, -5]
subset(iris, select = 1:4)

set <- iris[iris$Species == 'setosa', ]
vis <- iris[iris$Species == 'versicolor', ]
vrg <- iris[iris$Species == 'virginica', ]

levels(iris$Species)

split(iris, f = iris$Species)
sp <- split(iris, f = iris$Species)
length(sp)
names(sp)
class(sp)

sp$setosa
sp$versicolor
sp$virginica

dim(sp$setosa)
dim(sp$versicolor)
dim(sp$virginica)

df.2 <- rbind(sp$setosa, sp$versicolor)
dim(df.2)

iris[, 1:2]
iris[, 3:4]

df.3 <- cbind(iris[, 1:2], iris[, 3:4])
dim(df.3)
str(df.3)

library(readxl)
df.1 <- read_excel("성적표.xlsx", sheet = 1)
df.2 <- read_excel("성적표.xlsx", sheet = 2)
df.1
df.2

cbind(df.1, df.2)
merge(df.1, df.2)
merge(df.1, df.2, all = T)

df <- merge(df.1, df.2, all = T, 
            by.x = c('번호', '이름'),
            by.y = c('No', 'Name'))
str(df)

colnames(df) <- c('no',
                  'name',
                  'python',
                  'r',
                  'ml',
                  'dl',
                  'cloud')

colnames(df)[6] <- '딥러닝'
colnames(df)

#df$Deep.Learning

df <- iris
aggregate(df[, -5],
          by = list(품종=df$Species),
          FUN = mean)

aggregate(df[, -5],
          by = list(품종=df$Species),
          FUN = sd)

library(MASS)
data("survey")
df <- survey
str(df)

df <- na.omit(df)
df <- df[complete.cases(df), ]
dim(df)

hist(df$Height, breaks = 20)

hist(df[df$Sex == 'Male', ]$Height, 
     breaks = 20)

hist(df[df$Sex == 'Female', ]$Height, 
     breaks = 20)

mean(df[df$Sex == 'Male', ]$Height)
mean(df[df$Sex == 'Female', ]$Height)

aggregate(df[, c(10, 12)],
          by = list(Gender = df$Sex),
          FUN = mean)

table(df$Sex)
t.test(Height ~ Sex, data = df)

boxplot(Height ~ Sex, data = df,
        col = c("orange", "tomato"))
#####---------------------
s <- 0
for (i in 1:1000000) {
  x <- sample(1:10, size = 5)
  s <- s + sum(x == 7)
}
s

set.seed(2022)
sample(1:10, size=5, replace = T)

idx <- sample(1:nrow(iris), size = 50)
iris[idx, ]


##### 9장 #####
library(palmerpenguins)
data(package = "palmerpenguins")
data("penguins")

pg <- data.frame(penguins)
str(pg)

library(VIM)
aggr(pg, numbers = T, prop = F)
pg <- na.omit(pg)
dim(pg)

str(pg)
table(pg$species)
barplot(table(pg$species))

table(pg$island)
barplot(table(pg$island))

table(pg$sex)
barplot(table(pg$sex))

str(pg[, 3:6])
summary(pg[, 3:6])

par(mfrow = c(2, 2)) # 2, 2 # 1, 4
hist(pg$bill_length_mm, col = c("orange", "violet", "pink")) # 1:5
hist(pg$bill_depth_mm)
hist(pg$flipper_length_mm)
hist(pg$body_mass_g)
par(mfrow = c(1, 1))

my.color <- ifelse(pg$species == "Gentoo", "tomato",
                   ifelse(pg$species == "Adelie", "steelblue", "orange"))
plot(pg$bill_length_mm, pg$bill_depth_mm,
     pch = 19, col = my.color) # "tomato"

cor(pg$bill_length_mm, pg$bill_depth_mm)

cor(pg[pg$species == "Adelie", ]$bill_length_mm,
    pg[pg$species == "Adelie", ]$bill_depth_mm)


