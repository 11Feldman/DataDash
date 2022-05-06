from dash import html,dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import pathlib

rows = 100000

PATH = pathlib.Path(__file__).parent
PATH_FOLDER = PATH.joinpath('../datasets').resolve()
data = PATH_FOLDER.joinpath('empresasTech.csv')

df = pd.read_csv(data)
df['cantidad'] = 1
sector = df.groupby(['sector'])['cantidad'].sum().reset_index(name='cantidad')
origen = df.groupby(['origen'])['cantidad'].sum().reset_index(name='cantidad')

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

bar = px.bar(data_frame=sector, x='sector', y='cantidad', color='sector')
bar.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
pie = px.pie(data_frame=origen, names='origen', values='cantidad',color='origen')
pie.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)


layout = html.Div(
    children=[
    html.H1('Empresas'),
    html.H3('Datos de Empresas...'),
    html.Div([
        dcc.Graph(id='pie',figure=bar,className='graphical'),
        dcc.Graph(id='bar',figure=pie,className='graphical')
        ]
    )
])