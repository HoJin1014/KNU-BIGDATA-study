### 5장 함수의 이해
# 사용자 정의 함수: user-defined functions
#function.name <- function (parameters) {
#  function.bodies
#  return (returnValue)
#}

add <- function (x, y) {
  z <- x + y
  return (z)
}
add(3, 4)

func1 <- function(x, y, z) {
  return (x+2 * y+3 * z)
}

func1(1, 2, 3)

func1(x  = 1, y = 2, z = 3)

func1(3, 2, 1)


func2 <- function (x, y = 1, z = 0) {
  return (x + 2 * y + 3 * z)
}
func2(1, 2, 3)

pi <- 3.141592
round(x = pi, digits = 4)

getwd()

# ---------------------------------
library(palmerpenguins)
df <- na.omit(penguins)
df <- data.frame(df)

str(df)
View(df)


### data(package = "palmerpenguins")
data("penguins")





