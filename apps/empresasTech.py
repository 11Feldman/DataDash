from dash import html,dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import bd

df,sector,origen = bd.empresasTech()

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