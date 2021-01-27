import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/juliaryoshida/trabalhoapc/main/GameSales.csv')
lista = df.values.tolist()

def plataformas():# função que cria lista das plataformas
    plats = ['Nintendo 3DS']
    cont=0
    for x in range(len(lista)):
        for y in range(len(plats)):
            if plats[y] == lista[x][1]:
                cont = cont+1
             
        if cont == 0:  #se for zero, significa que n
            plats.append(lista[x][1])
        cont=0

    return plats

def categorias():# função que cria lista das categorias
    categoria = ['Action']
    cont=0
    for x in range(len(lista)):
        for y in range(len(categoria)):
            if categoria[y] == lista[x][3]:
                cont = cont+1
             
        if cont == 0:  #se for zero, significa que não tinha sido adicionada
            categoria.append(lista[x][3])
        cont=0

    return categoria

def publicadora():# função que cria lista das publicadoras
    publicadoras = ['Nintendo']
    cont=0
    for x in range(len(lista)):
        for y in range(len(publicadoras)):
            if publicadoras[y] == lista[x][2]:
                cont = cont+1
             
        if cont == 0: 
            publicadoras.append(lista[x][2])
        cont=0

    return publicadoras
                

def anos_especificos(anos):#pega anos específicos
    ano = []
    for x in range(len(lista)):
        if(lista[x][5] == anos):
            ano.append(lista[x])
    return ano

def jogos_especificos(esp):#pega plataformas selecionadas 
    plataforma = []
    for x in range(len(lista)):
        if(lista[x][1] == esp):
            plataforma.append(lista[x])
    return plataforma

def categorias_especificas(esp):#pega categorias selecionadas
    categoria = []
        if(lista[x][3] == esp):
            categoria.append(lista[x])
    return categoria

def publicadoras_especificas(esp):#pega publicadoras selecionadas
    publicadoras = []
    for x in range(len(lista)):
        if(lista[x][2] == esp):
            publicadoras.append(lista[x])
    return publicadoras

def colunas(lista_valores, coluna):#pega coluna específica de uma lista 
    valor=[]
    for x in range (len(lista_valores)):
        valor.append(lista_valores[x][coluna])
    return valor

def colunas_ano(lista_valores,ano):# seleciona a lista com anos específicos
    valor=[]
    for x in range (len(lista_valores)):
        if lista_valores[x][5]== ano:
            valor.append(lista_valores[x])
    return valor

def cria_grafico(nomex,nomey):
    fig =  go.Figure()
     
    
    fig.add_trace(
            go.Bar(
                x=nomex,
                y=nomey,
            )
    )
        
    fig.update_traces(
            marker_color='#1b7895', 
            marker_line_color='rgb(0,0,0)',
            marker_line_width=0.0, 
            opacity=1
    )

    fig.update_layout(
            xaxis = {'title': 'Jogos'},
            yaxis = {'title': 'Vendas em milhões'},
            plot_bgcolor = 'white',
            font_family='open-sans',
            font_color='#353839'

    )
    return fig

