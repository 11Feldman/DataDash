from dash import dcc,Dash,html,Input,Output
import dash_bootstrap_components as dbc

app = Dash(__name__,external_stylesheets=[dbc.themes.DARKLY, ],)

SIDEBAR_STYLE = {
    'position': 'fixed',
    'top':0,
    'left':0,
    'bottom':0,
    'width':'16rem',
    'padding':'2rem 1rem',
    'background-color':'#f8f9fa',
}

CONTENT_STYLE = {
    '':'',
    '':'',
    '':''
}