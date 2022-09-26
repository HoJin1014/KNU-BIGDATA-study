# 집단별로 비율 확인
library(palmerpenguins)
df <- na.omit(penguins)
table(df$species)
prop.table(table(df$species))

table(df$sex)
prop.table(table(df$sex))

table(df$island, df$species)



tapply(df$species,
       INDEX = list(df$species),
       FUN = length)


library(gmodels)
CrossTable(df$island, df$species,
           prop.t = F, prop.chisq = F)

?CrossTable

install.packages("psych")
library(psych)
describe(df)[, c(2:4, 8:9)]

??ggplot2
library(ggplot2)

# aggregate() 함수를 이용하여 범주별
# 기술 통계랑 산출.
aggregate(df[, 3:6],
          by = list(sepcies = df$species),
          FUN = mean)

tapply(df$bill_length_mm,
       INDEX = list(species = df$species),
       FUN = mean)

tapply(df$bill_depth_mm,
       INDEX = list(species = df$species),
       FUN = mean)


boxplot(flipper_length_mm ~ species,
        data = df, col = 2:4)


#outlier <- boxplot.stats(df$flipper_length_mm[df$species == 'Adele'])$out
df <- data.frame(df)
adelie <- split(df, df$species)$Adelie
adelie
outlier <- boxplot.stats(adelie$flipper_length_mm)$out
outlier
df[df$flipper_length_mm %in% outlier, ]
length(df[df$flipper_length_mm %in% outlier, ])
nrow(df[df$flipper_length_mm %in% outlier, ])
dim(df[df$flipper_length_mm %in% outlier, ])

# 
library(palmerpenguins)
df <- na.omit(penguins)
df <- data.frame(df)
df
# 날개 길이 오름차순, 체질량 내림차순으로 정렬
ord <- order(df$flipper_length_mm, -df$body_mass_g)
ord
(df[ord, ]
head(df[ord, 5:6], n =10)


