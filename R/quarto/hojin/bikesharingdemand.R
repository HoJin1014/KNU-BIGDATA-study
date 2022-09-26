### 3조 ###
df <- read.csv("../train.csv", header = T)
df1 <- read.csv("../test.csv", header = T)
str(df)
str(df1)

# train, test 데이터 합치기
library(dplyr)
alldf <- bind_rows(df, df1)
str(alldf)
summary(alldf)

# na 값 확인
for (i in 1:length(alldf)){
    cat(colnames(alldf)[i],sum(is.na(alldf[,i])),'\n')
}

# na 값 0으로 변경
alldf[is.na(alldf)] <- 0
# 변경 확인
for (i in 1:length(alldf)){
    cat(colnames(alldf)[i],sum(is.na(alldf[,i])),'\n')
}

str(alldf)
# 범주형 변경
# alldf$season <- factor(alldf$season, labels = c("Spring", "Summer", "Fall", "Winter"))
# sp_su<-alldf[alldf$season %in% c('Spring', 'Summer'),]



co_se <- oneway.test(count ~ season, data = alldf) # 계절 일원배치분산분석 (aov)
co_we <- oneway.test(count ~ weather, data = alldf) # 날씨 일원배치분산분석 (aov)
co_ho <- oneway.test(count ~ holiday, data = alldf) # 휴일 일원배치분산분석 (aov)
se <- aov(count ~ season, data = alldf,)
summary(se)
we <- aov(count ~ weather, data = alldf,)
summary(we)
ho <- aov(count ~ holiday, data = alldf,)
summary(ho)


library(gplots)
par(mfrow=c(3,1))
plotmeans(count~season ,data = alldf,
          barcol='tomato', barwidth=3, col='cornflowerblue', lwd=2,
          main='count & season')
plotmeans(count~weather ,data = alldf,
          barcol='tomato', barwidth=3, col='cornflowerblue', lwd=2,
          main='count & weather')
plotmeans(count~holiday ,data = alldf,
          barcol='tomato', barwidth=3, col='cornflowerblue', lwd=2,
          main='count & holiday')
par(mar = rep(1,1))


par(mfrow=c(3,1))
boxplot(count~season ,data = alldf, col = 'tomato',
        main ='count & season')
boxplot(count~weather ,data = alldf, col = 'tomato',
        main ='count & weather')
boxplot(count~holiday ,data = alldf, col = 'tomato',
        main ='count & holiday')
par(mar = rep(1,1))
# oneway.test(count ~ temp, data = alldf)
# oneway.test(count ~ humidity, data = alldf)
# oneway.test(count ~ windspeed, data = alldf)
# oneway.test(count ~ registered, data = alldf)





# 다중회귀분석
alldf <- alldf[, -1]
summary(alldf)

model1 <- lm(count ~ . , data = alldf)
summary(model1)

model2 <- lm(count ~ temp + atemp, data = alldf)
summary(model2)

model3 <- lm(count ~ humidity + windspeed, data = alldf)
summary(model3)

model4 <- lm(count ~ humidity + temp, data = alldf)
summary(model4)

model5 <- lm(count ~ atemp + windspeed, data = alldf)
summary(model5)

# 상관분석
#library(corrplot)
#corrplot(cor(alldf), method="circle")

library(psych)
pairs.panels(cor(alldf))

model6 <- lm(count ~ humidity + weather, data = alldf)
summary(model6)

model7 <- lm(count ~ weather, data = alldf)
summary(model7)

# 후진선택법
mod.selected <- step(model1, direction = "backward")
summary(mod.selected)






cor.test(alldf$count, alldf$season)


# mmmmmmmmmmmmmmmmmmmmmmmmmmmmm
par(mfrow=c(4,2))
par(mar = rep(2, 4))
hist(alldf$season)
hist(alldf$weather)
hist(alldf$humidity)
hist(alldf$holiday)
hist(alldf$workingday)
hist(alldf$temp)
hist(alldf$atemp)
hist(alldf$windspeed)

