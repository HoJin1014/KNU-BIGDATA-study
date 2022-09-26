### 데이터 시각화의 이해 ###
library(tidyverse)

str(diamonds)
str(mpg)

anscombe
ans <- anscombe

mean(ans$x1)
mean(ans$x2)
mean(ans$x3)
mean(ans$x4)

mean(ans$y1)
mean(ans$y2)
mean(ans$y3)
mean(ans$y4)

cor(ans$x1, ans$y1)
cor(ans$x2, ans$y2)
cor(ans$x3, ans$y3)
cor(ans$x4, ans$y4)

lm(y1 ~ x1, data = ans)
lm(y2 ~ x2, data = ans)
lm(y3 ~ x3, data = ans)
lm(y4 ~ x4, data = ans)

par("mar")
par(mar=c(1, 1, 1, 1))
par(mfrow = c(2, 2))

plot(ans$x1, ans$y1, col = "orange", pch = 19)
abline(lm(y1 ~ x1, data = ans), col = "tomato")

plot(ans$x2, ans$y2, col = "orange", pch = 19)
abline(lm(y2 ~ x2, data = ans), col = "tomato")

plot(ans$x3, ans$y3, col = "orange", pch = 19)
abline(lm(y3 ~ x3, data = ans), col = "tomato")

plot(ans$x4, ans$y4, col = "orange", pch = 19)
abline(lm(y4 ~ x4, data = ans), col = "tomato")
par(mfrow = c(1, 1))


?mpg


ggplot(data = mpg,
       mapping = aes(x = displ, y = hwy)) +
    geom_point()

p <- ggplot(data = mpg,
       mapping = aes(x = displ, y = hwy,
                     color = "tomato"))
p + geom_point()


p1 <- ggplot(data = mpg,
             mapping = aes(x = displ, y = hwy))

p1 + geom_point(mapping = aes(color = class))

table(mpg$class)

p1 + geom_point(mapping = aes(color = class,
                              size = class))

p1 + geom_point(mapping = aes(color = class,
                              size = class,
                              alpha = 0.3,
                              shape = class)) #투명도

p1 + geom_point(color = "tomato") +
    facet_wrap(~class, nrow = 3)

p1 + geom_point(color = "tomato") + 
    facet_grid(drv ~ cyl)

p1 + geom_point(mapping = aes(color = class)) + 
    geom_smooth(color = "tomato")


##### 다이아몬드 #####
p <- ggplot(data = diamonds,
            mapping = aes(x = cut))

table(diamonds$cut)


p + geom_bar()
diamonds
diamonds$clarity
table(diamonds$clarity)

p + geom_bar(mapping = aes(fill = clarity))


p + geom_bar(mapping = aes(fill = clarity), 
             position = "dodge")


#install.packages("datasauRus")
library(datasauRus)

data(package = "datasauRus")
dd <- datasaurus_dozen

str(dd)
unique(dd$dataset)

plot(y ~ x, 
     data = subset(dd, dataset == "dino"), 
     pch = 19, col = "tomato")

ggplot(data = subset(dd, dataset == "dino"),
       mapping = aes(x = x, y = y)) + 
  geom_point(color = "#FFFF00")


ggplot(data = dd,
       mapping = aes(x = x, y = y)) + 
  geom_point(mapping = aes(color = dataset)) + 
  facet_wrap(~ dataset, nrow = 3)


p <- ggplot(mpg, aes(x = class, y = hwy))
p + geom_boxplot(fill = "tomato") +
  coord_flip()         # x축 y축 변경

p <- ggplot(diamonds, aes(x = cut, fill = cut))
p + geom_bar(show.legend = F, width = 1) + 
  coord_polar()

# 지도 그리기
library(maps)
world <- map_data("world")
ggplot(world, aes(long, lat, group = group)) +
  geom_polygon(fill = "skyblue", color = "blue")

str(mpg)

sd(mpg[mpg$hwy > mean(mpg$hwy), c(1, 2, 9, 11)]$hwy)

v <- c(10, 30, 50, 20, 40)
sort(v)

best.in.class <- mpg %>%
  group_by(class) %>%
  filter(row_number(desc(hwy)) == 1)

p <- ggplot(data = mpg,
            mapping = aes(x = displ, y = hwy))
p + geom_point(mapping = aes(color = class)) + 
  geom_label(mapping = aes(label = model),
            data = best.in.class,
            nudge_y = 2, alpha = 0.5) +
  theme(legend.position = "bottom") +
  theme_minimal() # 위치

#getwd()
#ggsave("myfig.png",width = 1920, height = 1080, units = "px")
#ggsave("./figures/")




# p <- data %>%
  ggplot(aes(x = value, fill = type)) +
  geom_histogram(color = "e9ecef", alpha = 0.6, position = 'identity') +
  scale_fill_manual(values=c("#69b3a2", "#404080")) + 
    theme_ipsum() +
    labs(fill="")
  
# library
# install.packages("hrbrthemes")
library(ggplot2)
library(dplyr)
library(hrbrthemes)
  
# Build dataset with different distributions
data <- data.frame(
  type = c( rep("variable 1", 1000), rep("variable 2", 1000) ),
  value = c( rnorm(1000), rnorm(1000, mean=4) )
)
  
# Represent it
p <- data %>%
  ggplot( aes(x=value, fill=type)) +
  geom_histogram( color="#e9ecef", alpha=0.6, position = 'identity') +
  scale_fill_manual(values=c("#69b3a2", "#404080")) +
  theme_ipsum() +
  labs(fill="")
  
  
library(palmerpenguins)
str(penguins)
pg <- penguins  
pg <- pg[complete.cases(pg), ]

pg %>%
  ggplot(aes(x = body_mass_g, fill = sex)) +
  geom_histogram(color = "#e9ecef", alpha = 0.6, position = 'identity') +
  scale_fill_manual(values=c("#69b3a2", "#404080")) +
  theme_ipsum() +
  labs(fill="")

#install.packages("esquisse")
library(gapminder)
library(esquisse)


library(dplyr)
library(ggplot2)

gapminder::gapminder %>%
 filter(year >= 2007L & year <= 2007L) %>%
 ggplot() +
 aes(x = gdpPercap, y = lifeExp, fill = year, colour = continent, size = pop) +
 geom_point(shape = "bullet") +
 scale_fill_gradient() +
 scale_color_hue(direction = 1) +
 labs(x = "수입", 
 y = "기대수명", title = "Gapminder 따라하기", subtitle = "나 쫌 짱인듯", caption = "Fig. 1. 한스 로슬링 따라하기") +
 theme_minimal()


### 수정전 ###
ggplot(gapminder::gapminder) +
  aes(x = gdpPercap,
      y = lifeExp,
    fill = year,
    colour = continent,
    size = pop
  ) +
  geom_point(shape = "circle") +
  scale_fill_gradient() +
  scale_color_hue(direction = 1) +
  theme_minimal()



