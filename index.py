from dash import html,dcc
from dash.dependencies import Input,Output
from app import app
from apps import covid,empresasTech,viajes

app.layout = html.Div(
    children=[
        html.Div([
            dcc.Link('covid',href='/covid',className='links'),
            dcc.Link('empresas',href='/empresasTech',className='links'),
            dcc.Link('viajes', href='/viajes',className='links')
            ],
            style={ 'display': 'inline-block'}
        ),
        dcc.Location(id='url', refresh=False),
        html.Div(id='body')
    ]
)

@app.callback(
    Output(component_id='body',component_property='children'),
    Input(component_id='url',component_property='pathname')
)
def update_page(pathname):
    if pathname == '/covid':
        return covid.layout
    elif pathname == '/empresasTech':
        return empresasTech.layout
    elif pathname == '/viajes':
       return viajes.layout
    else:
        return covid.layout

if __name__ == '__main__':
    app.run_server(debug=False)