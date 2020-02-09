import dash
import datetime
import dash_core_components as dcc
import dash_html_components as html
import json

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
valuee = 'Inside'
events = []
datetimes = []

inside =[]
outside=[]

temp = ""
dyear = datetime.datetime.now().strftime('%Y-%m-%d')
dtime = datetime.datetime.now().strftime('%H:%M:%S')
data = {}

app.layout = html.Div(children=[
    html.H1(children='\tEnter/Exit Simulation', style={'marginLeft': 400}),

    html.Div(children='''
        Current Time:
    ''', style={'color': 'black', 'fontSize': 30, 'marginTop': 50}),
    html.H1(datetime.datetime.now().strftime('%Y-%m-%d'),
            style={'opacity': '1', 'color': 'black', 'fontSize': 15, 'display': 'inline-block'}),
    html.H1(datetime.datetime.now().strftime('%H:%M:%S'), style={'opacity': '1', 'color': 'black', 'fontSize': 15}),
    html.Div(children='''
                Options
            ''', style={'color': 'black', 'fontSize': 20, 'marginLeft': 600}),
    dcc.Dropdown(id='ozellikler',
        options=[
            {'label': 'Show Users Inside', 'value': 1},
            {'label': 'Show Users Outside', 'value': 2},
            {'label': 'Show Devices in Use', 'value': 3},
            {'label': 'Show Devices Used By a User', 'value': 4},
            {'label': 'Turn All Devices On', 'value': 5}
        ],
        value='1',
        style={'width': '50%', 'marginLeft': 300}
    ),
    html.Button('View The Event Log', id='button1', style={'marginLeft': 550}),
    html.Button('Export the Event Log', id='button2', style={'marginLeft': 10}),
    html.Div(id='output-container-button2', style={'color': 'Black', 'fontSize': 18}),

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
                 value='x',
                 style={'width': '50%'}
                 ),

    html.Div(children='''
        Inside/Outside
    ''', style={'color': 'black', 'fontSize': 30, 'marginTop': 50}),
    html.Div(id='display-selected-values', style={'color': 'red', 'fontSize': 18, 'marginTop': 10}),

    html.Div(children='''
        Action
    ''', style={'color': 'black', 'fontSize': 30, 'marginTop': 50}),
    html.Button('Enter', id='button'),
    html.Button('Exit', id='buttonE',style={'marginLeft': 10}),
    html.Div(id='output-container-button', style={'color': 'Black', 'fontSize': 18}),
    html.Div(id='output-container-button3', style={'color': 'Black', 'fontSize': 18})

]
    , style={'marginBottom': 50, 'marginTop': 25, 'marginLeft': 100})


@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box1', 'value')])
def enter_event(n_clicks, value):

    temp = 'Kullanıcı : "{}" çıkış yaptı. Tarih :'.format(
        value,
        n_clicks,
    )
    acti="enter"
    if(value!='x') :
        if(value in inside):
            a=2
        else:
            if(value in outside):
                outside.remove(value)
            inside.append(value)
            events.append(value+","+dyear+","+dtime+","+acti)





@app.callback(
    dash.dependencies.Output('output-container-button3', 'children'),
    [dash.dependencies.Input('buttonE', 'n_clicks')],
    [dash.dependencies.State('input-box1', 'value')])
def exit_event(n_clicks, value):

    temp = 'Kullanıcı : "{}" çıkış yaptı. Tarih :'.format(
        value,
        n_clicks,
    )

    act="exit"
    if (value != 'x'):
        if (value in outside):
            a = 2
        else:
            if (value in inside):
                inside.remove(value)
            outside.append(value)
            events.append(value + "," + dyear + "," + dtime + "," + act)

@app.callback(
    dash.dependencies.Output('display-selected-values', 'children'),
    [dash.dependencies.Input('input-box1', 'value'),dash.dependencies.Input('buttonE', 'n_clicks')])
def update_inout(value,n_clicks):
    if value in outside:
        return "outside"
    else:
        return "inside"


@app.callback(
    dash.dependencies.Output('output-container-button2', 'children'),
    [dash.dependencies.Input('button2', 'n_clicks')],
    [dash.dependencies.State('input-box1', 'value')])
def update_backlog(n_clicks, value):
    temp = 'Kullanıcı : "{}" çıkış yaptı. Tarih :'.format(
        value,
        n_clicks,
    )
    data['events'] = events
    with open('data.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, sort_keys=False, indent=4, ensure_ascii=False)






if __name__ == '__main__':
    app.run_server(debug=True)
