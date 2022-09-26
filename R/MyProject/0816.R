#####
library(palmerpenguins)
pg <- penguins
str(pg)
pg <- pg[complete.cases(pg), -8]
str(pg)
dim(pg)

pg$is.adelie <- factor(
    ifelse(pg$species == 'Chinstrap',
           'Yes', 'No'))  #Adelie

barplot(table(pg$is.adelie))  

str(pg)
pg <- pg[,-1]
str(pg)

model <- glm(is.adelie ~ ., data=pg, family = binomial(link = "logit"))

summary(model)

model$fitted
pg$pred <- factor(ifelse(model$fitted.values > 0.5, 
                         "Yes", "No"))
table(pg$is.adelie, pg$pred)
#predict(model)

df <- iris
df$Species <- factor(ifelse(df$Species == "virginica",
                            "Yes", "No"))
model <- glm(Species ~ ., data =df ,
             family = binomial(link = "logit"))
summary(model)

df$pred <- factor(ifelse(model$fitted.values > 0.5,
                         "Yes", "No")) #model 예측값 p값들..
tab <- table(df$Species, df$pred) # species 실제값, pred 예측값

TP <- tab[2, 2]
TN <- tab[1, 1]
FP <- tab[2, 1]
FN <- tab[1, 2]

accuracy <- (TP + TN) / (TP + TN + FP + FN)
#precision <- 
#Recall <- 
#F1.score <- 
#install.packages("pROC")
library(pROC)
roc(Species ~ model$fitted.values, data = df,
    plot = TRUE, main = "ROC CURVE", col = "tomato")

#install.packages("faraway")
library(faraway)
str(sexab)

