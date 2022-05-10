"""
Esta aplicación crea un diseño de barra lateral 
simple utilizando argumentos de estilo en línea y 
el componente dbc.Nav.

dcc.Location se usa para rastrear la ubicación actual,
y una devolución de llamada usa la ubicación 
actual para mostrar el contenido de la página correspondiente. 

El accesorio activo de cada NavLink se establece automáticamente de acuerdo
con el nombre de ruta actual. Para usar esta función, 
debe instalar dash-bootstrap-components >= 0.11.0.

Para obtener más detalles sobre la creación de aplicaciones de Dash de varias páginas, 
consulte la documentación de Dash: https://dash.plot.ly/urls

"""
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html,Dash
from apps import empresasTech,viajes

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = dbc.Card([
    dbc.CardBody([
            html.H2("Sidebar", className="display-4"),
            html.Hr(),
            html.P(
                "A simple sidebar layout with navigation links", className="lead"
            ),
            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/", active="exact"),
                    dbc.NavLink("Page 1", href="/page-1", active="exact"),
                    dbc.NavLink("Page 2", href="/page-2", active="exact"),
                ],
                vertical=True,
                pills=True,
            )
    ])
],
    color='light',
    style={
        'height':'100vh',
        'width':'16rem',
        'position':'fixed'
    }
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"),sidebar, content])

@app.callback(
    Output("page-content", "children"), 
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return html.P("This is the content of the home page!")
    elif pathname == "/page-1":
        return viajes.layout
    elif pathname == "/page-2":
        return empresasTech.layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(port=8888)