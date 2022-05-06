from dash import dcc,html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import pathlib

rows = 100000

PATH = pathlib.Path(__file__).parent
PATH_FOLDER = PATH.joinpath('../datasets').resolve()
data = PATH_FOLDER.joinpath('covid.csv')

df = pd.read_csv(data, nrows=rows)
genero = df.groupby(['genero'])['numero_de_caso'].sum().reset_index(name='cantidad')
provincia = df.groupby(['provincia'])['numero_de_caso'].sum().reset_index(name='cantidad')

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

bar = px.bar(data_frame=provincia,x='provincia', y = 'cantidad', color='provincia')
bar.update_layout(
    plot_bgcolor= colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
pie = px.pie(data_frame=genero,names='genero',values='cantidad', color ='genero')
pie.update_layout(
    plot_bgcolor= colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

layout = html.Div(
    children=[
    html.H1('COVID'),
    html.H3('Datos de covid...'),
    html.Div(
        children=[
            dcc.Graph(id='pie',figure=bar,className='graphical'),
            dcc.Graph(id='bar',figure=pie,className='graphical')
        ]
    ),
    ]
)