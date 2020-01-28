import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
value = 'in'
app.layout = html.Div(children=[
    html.H1(children='Enter/Exit Simulation'),

    html.Div(children='''
        SELECT USER
    ''', style={'color': 'black', 'fontSize': 20,'marginLeft': 100, 'marginRight': 50, 'marginTop': 10, 'marginBottom': 10,
               'backgroundColor':'#F7FBFE'}),

    dcc.Dropdown(
        options=[
            {'label': 'Ahmet', 'value': 1},
            {'label': 'Ali', 'value': 2},
            {'label': 'Ayşe', 'value': 3},
            {'label': 'Burak', 'value': 4},
            {'label': 'Beril', 'value': 5},
            {'label': 'Caner', 'value': 6},
            {'label': 'Eda', 'value': 7},
            {'label': 'Fatih', 'value': 8}
        ],
        value='1',
        style={'width': '50%'}
    ),


    html.Div(children='''
        Inside/Outside
    ''', style={'color': 'black', 'fontSize': 20, 'marginTop': 50}),
    dcc.Markdown(value
     ,
     style={'color': 'red', 'fontSize': 18}
    ),


    html.Div(children='''
        Action
    ''', style={'color': 'black', 'fontSize': 20, 'marginTop': 50}),
    dcc.RadioItems(
        options=[
            {'label': 'Exit', 'value': 1},
            {'label': 'Enter', 'value': 2}
        ],
        value=1,
        labelStyle={'display': 'inline-block'},  style={'color': 'red', 'fontSize': 18}
    )
], style={'marginBottom': 50, 'marginTop': 25,'marginLeft': 500})

if __name__ == '__main__':
    app.run_server(debug=True)