#install.packages("plotly")
library(plotly)
library(ggplot2)

df <- data.frame(
    x = c(1,2,3,4),
    y = c(1,2,3,4),
    f = c(1,2,3,4)
)

p <- ggplot(df, aes(x, y)) +
    geom_point(aes(frame = f))

ggplotly(p)

p <- ggplot(subset(gapminder, year == 2007), aes(x = gdpPercap, y = lifeExp)) +
        geom_point(aes(color = continent)) +
        scale_x_log10() +
        geom_smooth()

ggplotly(p)


data(sleep)
sleep %>%
    plot_ly() %>%
    add_trace(x = ~ID,
              y = ~extra,
              type = "bar") %>%
    layout(title = "Bar Plot",
           xaxis = list(title = "Species"),
           yaxis = list(title = "Frequency"))

penguins %>%
    plot_ly(x = ~bill_length_mm,
            y = ~bill_depth_mm,
            name = ~species,
            hovertext = ~island,
            hoverinfo = "x+y+name+text")

# x축은 gdpPercap, y축은 lifeExp
# hover는 국가, 인구가 나타나도록
gapminder %>%
    plot_ly(x = ~gdpPercap,
            y = ~lifeExp,
            name = ~country,
            hovertext = ~pop,
            hoverinfo = "x+y+name+text")





