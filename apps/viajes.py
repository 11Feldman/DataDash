from dash import dcc,html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import pathlib
from app import app
from dash.dependencies import Input,Output

rows = 100000

PATH = pathlib.Path(__file__).parent
PATH_FOLDER = PATH.joinpath('../datasets').resolve()
data = PATH_FOLDER.joinpath('viajes.csv')

df = pd.read_csv(data)
df = df.rename(columns={'TIPO_TRANSPORTE':'transporte'})
tipoTransporte = df.groupby(['transporte'])['CANTIDAD'].sum().reset_index(name='cantidad')

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

# @app.callback(
#     Output(component_id='scatter',component_property='figure'),
#     [
#         Input(component_id='xdrop',component_property='value'),
#         Input(component_id='ydrop',component_property='value')
#     ]
# )
# def upload_page(xdrop_value,ydrop_value):
#     x=df2[df2['Indicator Name']==xdrop_value]['Value']
#     y=df2[df2['Indicator Name']==ydrop_value]['Value']
#     fig =px.scatter(
#         x=x,
#         y=y,
#         hover_name=df2[df2['Indicator Name']== ydrop_value]['Country Name'],
        
#     )
#     fig.update_xaxes(title=xdrop_value)
#     fig.update_yaxes(title=ydrop_value)
#     fig.update_layout(
#         plot_bgcolor=colors['background'],
#         paper_bgcolor=colors['background'],
#         font_color=colors['text']
#     )
#     return fig