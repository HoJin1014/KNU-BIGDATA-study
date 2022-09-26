library(shiny)
library(palmerpenguins)

pg <- penguins
pg <- pg[complete.cases(pg), ]

ui <- pageWithSidebar(
    
    headerPanel(
        h1("팔머펭귄 데이터셋")
    ),
    
    sidebarPanel(
        checkboxInput("outliers", "이상치 보여줌?",
                      FALSE),
        selectInput("indvar", "독립변수는?",
                    list("종류별" = "species",
                         "섬별" = "island",
                         "성별" = "sex")),
        
        selectInput("depvar", "종속변수는?",
                    list("부리 길이" = "bill_length_mm",
                         "부리 깊이" = "bill_depth_mm",
                         "날개 길이" = "flipper_length_mm",
                         "체질량" = "body_mass_g")),
    ),
    
    mainPanel(
        h3("포뮬러: "),
        h3(textOutput("caption")),
        plotOutput("penguinPlot")
    ))
    
    #sidebarPanel(
    #    selectInput("variable", "선택해봐바"),
    #        list("실린더" = "cyl", 
    #         "트랜스미션" = "am",
    #         "기어" = "gear")),
    #),
    
    #mainPanel(
    #    h3("포뮬러:"),
    #    h3(textOutput("caption"))
    #    plotOutput("penguinPlot")
    #)
#)

server <- function (input, output) {
    
    formulaText <- reactive({
        paste(input$depvar," ~ ", input$indvar)
    })

    output$caption <- renderText(
        formulaText()
    )
    
    output$penguinPlot <- renderPlot({
        boxplot(as.formula(formulaText()),
        data = pg,
        col = "orange",
        outline = input$outliers)
    })
}

shinyApp(ui, server)
