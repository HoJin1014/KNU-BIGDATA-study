library(shiny)
library(gapminder)
library(ggplot2)

ui <- pageWithSidebar(
    headerPanel (
        h1("우리는 요리사곰 조 입니다: 나령, 영효, 남광, 혜리")
    ),
    
    sidebarPanel(
        #tags$h2("여기가 사이드바임")
        #sliderInput("count", "니가 원하는게 얼마니?",
                    #min = 1, max = 10000, value = 5000)
        selectInput("year",
                    "몇 년도를 보여드릴까요?",
                    seq(1952, 2007, 5))
    ),
    
    mainPanel(
        #tags$h1("여기가 헤더임"),
        #tags$image(src = "https://cdnimg.melon.co.kr/cm2/artistcrop/images/002/61/143/261143_20210325180240_500.jpg?61e575e8653e5920470a38d1482d7312/melon/resize/416/quality/80/optimize")
        h3("해당 연도의 GDP 대비 기대수명 그래프입니다."),
        plotOutput("distPlot")
    )
)

server <- function (input, output) {
    
    #year <- reactive(get(input$year))
 
    output$distPlot <- renderPlot({
        ## ggplot2로 그래프를 그려보세요
        #ggplot(subset(gapminder, year == as.integer(year()), 
        #              aes(x = gdpPercap, y = lifeExp)) +
        #    geom_point(aes(color = continent)) +
        #    scale_x_log10() +
        #    geom_smooth()
        ggplot(subset(gapminder, year == input$year), aes(x = gdpPercap, y = lifeExp)) +
            geom_point(aes(color = continent)) +
            scale_x_log10() +
            geom_smooth()
        
        #dist <- rnorm(input$count)
        #hist(dist, col = "tomato", breaks = 20)
    })
    
}

shinyApp(ui, server)