import dash
import dash_bootstrap_components as dbc

font_awesome1 = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css'
font_awesome2 = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" integrity="sha384-rPBDXfZXFOhqD8dGGJ7u8ObbF+jIbI3UizCkl1AovNYV6ZlRL9iJME2PD8f3vUqz'
font_awesome3 = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/solid.min.css'

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.DARKLY, font_awesome1, font_awesome2,font_awesome3, 'https://fonts.googleapis.com/css?family=Roboto:400,700&display=swap']
)

server = app.server
