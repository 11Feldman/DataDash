from dash import Dash
import pathlib
import dash_bootstrap_components.themes as th

PATH = pathlib.Path(__file__).parent
PATH_FOLDER = PATH.joinpath('.../assets').resolve()
PATH_CSS = PATH_FOLDER.joinpath('me.css')

main_css= PATH_CSS


app = Dash(__name__,external_stylesheets=[th.SUPERHERO])

server = app.server