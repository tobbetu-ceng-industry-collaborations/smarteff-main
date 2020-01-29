import dash
import datetime
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
value = 'Inside'


app.layout = html.Div(children=[
    html.H1(children='\tEnter/Exit Simulation',style={'marginLeft': 400}),

    html.Div(children='''
        Current Time:
    ''', style={'color': 'black', 'fontSize': 20 ,'marginTop': 50}),
    html.H1(datetime.datetime.now().strftime('%Y-%m-%d'),style={'opacity': '1', 'color': 'black', 'fontSize': 15,'display': 'inline-block'}),
    html.H1(datetime.datetime.now().strftime('%H:%M:%S'),style={'opacity': '1', 'color': 'black', 'fontSize': 15}),
    html.Div(children='''
                Options
            ''', style={'color': 'black', 'fontSize': 20, 'marginLeft': 600}),
        dcc.Dropdown(
            options=[
                {'label': 'Show Users Inside', 'value': 1},
                {'label': 'Show Users Outside', 'value': 2},
            {'label': 'Show Devices in Use', 'value': 3},
            {'label': 'Show Devices Used By a User', 'value': 4},
            {'label': 'Turn All Devices On', 'value': 5}
        ],
        value='1',
        style={'width': '50%','marginLeft': 300}
    ),
    html.Button('View The Event Log', id='button1',style={'marginLeft': 550}),
    html.Button('Export the Event Log', id='button2',style={'marginLeft': 10}),

    html.Div(children='''
        SELECT USER
    ''', style={'color': 'black', 'fontSize': 20}),

    dcc.Dropdown(id='input-box1',
        options=[
            {'label': 'Ahmet', 'value': 'Ahmet'},
            {'label': 'Ali', 'value': 'Ali'},
            {'label': 'Ayşe', 'value': 'Ayşe'},
            {'label': 'Burak', 'value': 'Burak'},
            {'label': 'Beril', 'value': 'Beril'},
            {'label': 'Caner', 'value': 'Caner'},
            {'label': 'Eda', 'value': 'Eda'},
            {'label': 'Fatih', 'value': 'Fatih'}
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
    ),
    html.Button('Submit', id='button'),
    html.Div(id='output-container-button',style={'color': 'Black', 'fontSize': 18})


]
    , style={'marginBottom': 50, 'marginTop': 25,'marginLeft': 100})


@app.callback(
        dash.dependencies.Output('output-container-button', 'children'),
        [dash.dependencies.Input('button', 'n_clicks')],
        [dash.dependencies.State('input-box1', 'value')])
def update_output(n_clicks, value):
    return 'Kullanıcı : "{}" çıkış yaptı'.format(
            value,
            n_clicks,
    )


if __name__ == '__main__':
    app.run_server(debug=True)