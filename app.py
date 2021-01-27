import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
from dash.dependencies import Input, Output
import estilos_graficos as graf

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

lista_de_plataformas = graf.plataformas()
lista_de_categorias = graf.categorias()
lista_de_publicadoras = graf.publicadora()

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def build_banner():
    return html.Div(
            id='logo-img',
            children=[
                html.Img(id='logo', src=('https://raw.githubusercontent.com/juliaryoshida/trabalhoapc/main/logo-img.png')),
            ],
        )


app.layout = html.Div([
    build_banner(),
    html.Div(
        children=[
            html.Div(
                className='row',
                children=[
                    html.Div(
                        className='four columns div-user-controls',
                        id='graph-1',
                        children=[
                            html.H1(
                                children ='Jogos mais vendidos por ano'
                            ),
                            html.Br(),
                            dcc.Slider(
                                id='ano',
                                min=2014,
                                max=2018,
                                value=2014,
                                marks={str(year): str(year) for year in range(2014,2019,1)},
                                included=False,
                                step=None
                            ),
                        ],
                    ),  
                    html.Div(
                        className='eight columns div-for-charts bg-grey',
                        children=[
                            dcc.Graph(
                                id='grafico1',
                                config={'modeBarButtonsToRemove': ['toImage','pan2d','zoom2d','lasso2d',
                                'zoomIn2d', 'zoomOut2d','hoverClosestCartesian','hoverCompareCartesian','select2d',
                                'toggleSpikelines','resetScale2d'],"displaylogo": False, 'displayModeBar':True}
                            ),
                        ],
                    ),  
                ],
            ),
        ],
    ),

    html.Div(
        children=[
            html.Div(
                className='row',
                children=[
                    html.Div(
                        className='four columns div-user-controls',
                        id='graph-2',
                        children=[
                            html.H1(
                                children ='Jogos mais vendidos por plataforma'
                            ),
                            html.Label(
                                id='label-2',
                                children=[
                                    "Filtrar por plataforma:",
                                    dcc.Dropdown(
                                        id='my_dinamic_dropdown',
                                        options = [
                                            {"label": x , "value":x}
                                            for x in lista_de_plataformas],
                                        value = 'Xbox One',
                                        clearable = False
                                    ),
                                ],
                            ),
                            html.Br(),
                            dcc.Slider(
                                id='ano2',
                                min=2014,
                                max=2018,
                                value=2014,
                                marks={str(year): str(year) for year in range(2014,2019,1)},
                                included=False,
                                step=None
                            ),
                        ],
                    ),  
                    html.Div(
                        className='eight columns div-for-charts bg-grey',
                        children=[
                            dcc.Graph(
                                id='grafico2',
                                config={'modeBarButtonsToRemove': ['toImage','pan2d','zoom2d','lasso2d',
                                'zoomIn2d', 'zoomOut2d','hoverClosestCartesian','hoverCompareCartesian','select2d',
                                'toggleSpikelines','resetScale2d'],"displaylogo": False, 'displayModeBar':True}
                            ),
                        ],
                    ),  
                ],
            ),
        ],
    ),

    html.Div(
        children=[
            html.Div(
                className='row',
                children=[
                    html.Div(
                        className='four columns div-user-controls',
                        id='graph-3',
                        children=[
                           html.H1(
                                children ='Jogos mais vendidos por gênero'
                            ),
                            html.Label(
                                id='label-3',
                                children=[
                                    "Filtrar por gênero:",
                                    dcc.Dropdown(
                                        id='categ',
                                        options = [
                                            {"label": x , "value":x}
                                            for x in lista_de_categorias],
                                        value = 'Action',
                                        clearable = False
                                    )
                                ],
                            ),
                            html.Br(),
                            dcc.Slider(
                                id='ano3',
                                min=2014,
                                max=2018,
                                value=2014,
                                marks={str(year): str(year) for year in range(2014,2019,1)},
                                included=False,
                                step=None
                            ),
                        ],
                    ),  
                    html.Div(
                        className='eight columns div-for-charts bg-grey',
                        children=[
                            dcc.Graph(
                                id='grafico3',
                                config={'modeBarButtonsToRemove': ['toImage','pan2d','zoom2d','lasso2d',
                                'zoomIn2d', 'zoomOut2d','hoverClosestCartesian','hoverCompareCartesian','select2d',
                                'toggleSpikelines','resetScale2d'],"displaylogo": False, 'displayModeBar':True}
                            ),
                        ],
                    ),  
                ],
            ),
        ],
    ),

    html.Div(
        children=[
            html.Div(
                className='row',
                children=[
                    html.Div(
                        className='four columns div-user-controls',
                        id='graph-4',
                        children=[
                           html.H1(
                                children='Jogos mais vendidos por distribuidora'
                            ),
                            html.Label(
                                id='label-4',
                                children=[
                                    "Filtrar por publicadora:",
                                    dcc.Dropdown(
                                        id='publicadora',
                                        options = [
                                            {"label": x , "value":x}
                                            for x in lista_de_publicadoras],
                                        value = 'Nintendo',
                                        clearable = False
                                    ),
                                ],
                            ),
                            html.Br(),
                            dcc.Slider(
                                id='ano4',
                                min=2014,
                                max=2018,
                                value=2014,
                                marks={str(year): str(year) for year in range(2014,2019,1)},
                                included=False,
                                step=None
                            ),
                        ],
                    ),  
                    html.Div(
                        className='eight columns div-for-charts bg-grey',
                        children=[
                            dcc.Graph(
                                id='grafico4',
                                config={'modeBarButtonsToRemove': ['toImage','pan2d','zoom2d','lasso2d',
                                'zoomIn2d', 'zoomOut2d','hoverClosestCartesian','hoverCompareCartesian','select2d',
                                'toggleSpikelines','resetScale2d'],"displaylogo": False, 'displayModeBar':True}
                                ),
                            ],
                        ),  
                    ],
                ),
            ],
        ),
    html.Br(),
    html.Br(),
    ],
)

@app.callback(
    Output('grafico1', 'figure'),
    [Input('ano', 'value'),]
)

def update_figure(year_value):
    ano = year_value
    lista_ano = graf.anos_especificos(year_value)
    lista_ano = lista_ano[0:10]
    
    nome_jogos = graf.colunas(lista_ano,0)# pega os nomes dos jogos que vão ser plotados
    vendas_ano = graf.colunas(lista_ano,4)#pega as vendas dos jogos que vão ser plotados
    grafico1 = graf.cria_grafico(nome_jogos,vendas_ano) #função que plota os gráficos

    return grafico1

@app.callback(
    Output('grafico2', 'figure'),
    [Input('my_dinamic_dropdown', 'value'),
    Input('ano2', 'value')]
)

def update_figure(my_dinamic_dropdown_value,year_value):
    lista=my_dinamic_dropdown_value
    val_plat = graf.jogos_especificos(lista)#gera uma lista com todos os jogos da plataforma selecionada
    plat_ano = graf.colunas_ano(val_plat,year_value)#pega aa lista anterior e filtra com o ano selecionado
    plat_ano = plat_ano[0:10]

    nome_jogos = graf.colunas(plat_ano,0)# pega os nomes dos jogos que vão ser plotados
    vendas_plat = graf.colunas(plat_ano,4)#pega as vendas dos jogos que vão ser plotados
    grafico2 = graf.cria_grafico(nome_jogos, vendas_plat) #função que plota os gráficos
    return grafico2


@app.callback(
    Output('grafico3', 'figure'),
    [Input('categ', 'value'),
    Input('ano3', 'value')]  
)


def update_figure(categ,year_value):
    lista=categ
    val_categ = graf.categorias_especificas(lista)
    categ_ano = graf.colunas_ano(val_categ,year_value)#pega as plataformas no ano específico
    categ_ano = categ_ano[0:10]
   
    nome_jogos = graf.colunas(categ_ano,0)# pega os nomes dos jogos
    vendas_categ = graf.colunas(categ_ano,4)#pega as vendas dos jogos
    grafico3 = graf.cria_grafico(nome_jogos, vendas_categ)
    return grafico3

@app.callback(
    Output('grafico4', 'figure'),
    [Input('publicadora', 'value'),
    Input('ano4', 'value')]
)

def update_figure(my_dinamic_dropdown_value,year_value):
    lista= my_dinamic_dropdown_value
    val_public = graf.publicadoras_especificas(lista)#gera uma lista com a publicadora elecionada
    public_ano = graf.colunas_ano(val_public,year_value)#pega as publicadoras no ano específico
    public_ano = public_ano[0:10]

    nome_jogos = graf.colunas(public_ano,0)# pega os nomes dos jogos
    vendas_public = graf.colunas(public_ano,4)#pega as vendas dos jogos
    grafico4 = graf.cria_grafico(nome_jogos, vendas_public)

    return grafico4

if __name__ == "__main__":
    app.run_server(debug=True)