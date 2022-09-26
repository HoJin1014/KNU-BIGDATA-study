ui <- fluidPage(
    tags$h1("자, 이제 너의 선택을 보여줘!"),
    
    selectInput("dataset", label = "Dataset",
                choices = c("iris", "mtcars", "state.x77")),
    
    tableOutput("table"),
    
    verbatimTextOutput("summary")
    
)

server <- function (input, output) {
    
    dataset <- reactive({
        #cat(input$dataset)
        get(input$dataset, "package:datasets")
    })
    
    output$summary <- renderPrint({
        #cat(input$dataset) # 디버깅
        #dataset <- get(input$dataset, "package:datasets")
        summary(dataset())
    })
    
    output$table <- renderTable({
        #dataset <- get(input$dataset, "package:datasets")
        head(dataset(), 5)
    })
}

shinyApp(ui, server)

