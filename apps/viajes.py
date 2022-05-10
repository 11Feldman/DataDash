from dash import dcc,html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import bd

df,tipoTransporte = bd.viajes()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

bar = px.bar(data_frame=tipoTransporte,x='transporte', y ='cantidad', color='transporte')
bar.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
pie = px.pie(data_frame=tipoTransporte,names='transporte',values='cantidad',color='transporte')
pie.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

layout = html.Div(
    children=[
    html.H1('VIAJES'),
    html.H3('Datos de Viajes...'),
    html.Div(
        children=[
            dcc.Graph(id='pie',figure=bar, className='graphical'),
            dcc.Graph(id='bar',figure=pie, className='graphical')
        ]
    ),
    ]
)