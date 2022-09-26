### 14장 회귀분석의 유형###

library(car)
data(Prestige)
df <- Prestige
str(df)

table(df$type)
barplot(table(df$type), col = "orange")

hist(df$income, col = "tomato", breaks = 20)
shapiro.test(df$income)

hist(df$education, col = "tomato", breaks = 20)
hist(df$women, col = "tomato", breaks = 20)
hist(df$prestige, col = "tomato", breaks = 20)

shapiro.test(df$prestige)

plot(df[, -(5:6)], pch = 19, col = "steelblue")

lm(income ~ education, data = df)

cor(df[, -(5:6)])

model <- lm(income ~ education, data = df)
summary(model)

plot(income ~ education, data =df,
     col = "skyblue", pch = 19)

abline(model, col = "tomato", lwd = 2)

a <- lm(income ~ women, data = df)
summary(a)

plot(income ~ women, data = df,
     col = "tomato", pch = 19)

abline(a, col = "steelblue", lwd = 2)

model <- lm(income ~ education + women + prestige,
            data =df)
summary(model)

model <- lm(income ~ education + women,
            data =df)
summary(model)

model <- lm(income ~ education,
            data =df)
summary(model)

model <- lm(income ~ women + prestige,
            data =df)
summary(model)


library(stargazer)
stargazer(model, type = "text")

par(mfrow = c(2,2))
plot(model)
par(mfrow = c(1,1))

model <- lm(income ~ education, data = df)
plot(income ~ education, data = df,
     col = "skyblue", pch = 19)

model <- lm(income ~ education + I(education^2),
            data = df)
summary(model)
abline(model)


library(dplyr)
model <- lm(income ~ education + I(education^2),
            data = df)
plot(income ~ education, data = df,
     col = "skyblue", pch = 19)

with(df,
     lines(arrange(data.frame(education,
                              fitted(model))),
           education),
     lty = 1, lwd = 3, col = "tomato")

summary(model)


### 15장 회귀모델의 설명력 ###
df <- mtcars
str(df)
df <- mtcars[, 1:6]
str(df)

plot(df, col = "green")

cor(df)

library(corrgram)
corrgram(df)

lm(mpg ~ . , data = df)
model <- lm(mpg ~ . , data = df)
summary(model)

model <- lm(mpg ~ hp + wt, data = df)
summary(model)



model <- lm(mpg ~ disp + drat+ wt, 
            data = df)
mod.selected <- steep(model, direction = "backward")

summary(model)
# modle <- lm$
    
# 연습문제:
# Kaggle House Price 데이터셋에서
# 다중 선형 회귀의 변수 선택을 통해
# 최적의 독립 변수 조합을 찾아보시오.
# 1. 전진선택법으로 찾은 조합은? R2, Adjusted R2 값은?
# 2. 후진선택법으로 찾은 조합은? R2, Adjusted R2 값은?

df <- read.csv("./houseprice.csv")
str(df)
dim(df)
is.num <- c()
for (i in 1:80) {
    is.num[i] <- is.numeric(df[, i])
}
is.num
df <- df[, is.num] # 수치형이 아닌 컬럼 제외
df <- df[,-1] # ID 컬럼을 제외
dim(df)
str(df)

#df <- na.omit(df)
df <- df[complete.cases(df), ] #결측치 행 제거
dim(df)

str(df)
summary(df)

# 후진선택법
model <- lm(SalePrice ~ . , data = df)
summary(model)
mod.selected <- step(model, direction = "backward")
summary(mod.selected)


# 전진선택법
model <- lm(SalePrice ~ 1, data = df)
mod.selected <- step(model, 
                     direction = "forward",
                     scope = list(lower = ~1,
                                  upper = ~ OverallQual + OverallCond + YearBuilt + MasVnrArea + BsmtFinSF1 + 
                                      X1stFlrSF + X2ndFlrSF + BsmtFullBath + FullBath + BedroomAbvGr + 
                                      KitchenAbvGr + TotRmsAbvGrd + Fireplaces + GarageCars + WoodDeckSF + 
                                      ScreenPorch + PoolArea))

summary(mod.selected)

df <- InsectSprays
str(df)
lm(count ~ spray, data = df)
model <- lm(count ~ spray, data = df)
summary(model)

contrasts(df$spray)


df <- mtcars[, 1:6]
str(df)

df$cyl <- factor(df$cyl)
head(df)
table(df$cyl)

lm(mpg ~ ., data = df)
model <- lm(mpg ~ ., data = df)
summary(model)


### 16장 선형모델의 일반화 ###

df <- split(iris, f = iris$Species)
df <- rbind(df$setosa, df$versicolor)
plot(df[, c(3,5)])

library(robust)
data(breslow.dat)

df <- breslow.dat
str(df)

df <- df[, c("Base", "Age", "Trt", "sumY")]
str(df)
dim(df)

model <- glm(sumY ~ ., data = df, family = poisson)
summary(model)

exp(coef(model))

df <- split(iris, f = iris$Species)
df <- rbind(df$setosa, df$versicolor)
plot(df[, c(3, 5)])

df$Species <- as.integer(df$Species)
model <- glm(Species ~ Petal.Length, data = df)
summary(model)

# --------------------------------------------------
mtcars1 <- mtcars
str(mtcars1)
summary(mtcars1)

lm(mtcars1$mpg ~ mtcars1$wt, data = mtcars1)
ex <- lm(mtcars1$mpg ~ mtcars1$wt, data = mtcars1)
summary(ex)
plot(mtcars1$mpg, mtcars1$wt)


