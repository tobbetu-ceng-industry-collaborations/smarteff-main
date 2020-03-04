import dash
import datetime
import dash_core_components as dcc
import dash_html_components as html
import json
import random

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
valuee = 'Inside'
events = []
datetimes = []
user = []
time = []
date = []
action = []
randomAct=["enter","exit"]
randomAction=""
allUsers = ["Ahmet", "Ali", "Ayşe",
            "Burak",
            "Beril",
            "Caner",
            "Eda",
            "Fatih",
            "Furkan",
            "Fulya",
            "Damla",
            "Deniz",
            "Derin",
            "Dursun",
            "Emel",
            "Erkan",
            "Erdem",
            "Mehmet",
            "Toygar",
            "Özlem",
            "Serdar",
            "Doğukan",
            "Oğuzhan",
            "Eren",
            "Zafer",
            "Osman",
            "Gülseren", "Vildan", "Berkcan", "Cahit", "Cengiz", "Timur", "Alperen", "Melike", "Aylin", "Atakan",
            "Mustafa", "Kemal", "Cemal", "Atilla", "Şahin", "Celal", "Necati", "Adem", "Onur", "Aydın", "Beyza",
            "Ayhan", "Burhan", "Koray"]

inside = []
outside = []
inUsers = ""
outUsers = ""

temp = ""
dyear = datetime.datetime.now().strftime('%Y-%m-%d')
dtime = datetime.datetime.now().strftime('%H:%M:%S')
data = {}

app.layout = html.Div(children=[
    html.H1(children='\tEnter/Exit Simulation', style={'marginLeft': 400}),

    html.Div(children='''
        Current Time:
    ''', style={'color': 'black', 'fontSize': 30, 'marginTop': 50}),
    html.H1(dcc.Input(id='input-box-date', type='text', value=datetime.datetime.now().strftime('%d-%m-%Y')),
            style={'opacity': '1', 'color': 'black', 'fontSize': 15, 'display': 'inline-block'}),
    html.H1(dcc.Input(id='input-box-time', type='text', value=datetime.datetime.now().strftime('%H:%M:%S')),
            style={'opacity': '1', 'color': 'black', 'fontSize': 15}),
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
                     {'label': 'Fatih', 'value': 'Fatih'},
                     {'label': 'Furkan', 'value': 'Furkan'},
                     {'label': 'Fulya', 'value': 'Fulya'},
                     {'label': 'Damla', 'value': 'Damla'},
                     {'label': 'Deniz', 'value': 'Deniz'},
                     {'label': 'Derin', 'value': 'Derin'},
                     {'label': 'Dursun', 'value': 'Dursun'},
                     {'label': 'Emel', 'value': 'Emel'},
                     {'label': 'Erkan', 'value': 'Erkan'},
                     {'label': 'Erdem', 'value': 'Erdem'},
                     {'label': 'Mehmet', 'value': 'Mehmet'},
                     {'label': 'Toygar', 'value': 'Toygar'},
                     {'label': 'Özlem', 'value': 'Özlem'},
                     {'label': 'Serdar', 'value': 'Serdar'},
                     {'label': 'Doğukan', 'value': 'Doğukan'},
                     {'label': 'Oğuzhan', 'value': 'Oğuzhan'},
                     {'label': 'Eren', 'value': 'Eren'},
                     {'label': 'Zafer', 'value': 'Zafer'},
                     {'label': 'Osman', 'value': 'Osman'},
                     {'label': 'Gülseren', 'value': 'Gülseren'},
                     {'label': 'Vildan', 'value': 'Vildan'},
                     {'label': 'Berkcan', 'value': 'Berkcan'},
                     {'label': 'Cahit', 'value': 'Cahit'},
                     {'label': 'Cengiz', 'value': 'Cengiz'},
                     {'label': 'Timur', 'value': 'Timur'},
                     {'label': 'Alperen', 'value': 'Alperen'},
                     {'label': 'Melike', 'value': 'Melike'},
                     {'label': 'Aylin', 'value': 'Aylin'},
                     {'label': 'Atakan', 'value': 'Atakan'},
                     {'label': 'Mustafa', 'value': 'Mustafa'},
                     {'label': 'Kemal', 'value': 'Kemal'},
                     {'label': 'Cemal', 'value': 'Cemal'},
                     {'label': 'Atilla', 'value': 'Atilla'},
                     {'label': 'Şahin', 'value': 'Şahin'},
                     {'label': 'Celal', 'value': 'Celal'},
                     {'label': 'Necati', 'value': 'Necati'},
                     {'label': 'Adem', 'value': 'Adem'},
                     {'label': 'Onur', 'value': 'Onur'},
                     {'label': 'Aydın', 'value': 'Aydın'},
                     {'label': 'Beyza', 'value': 'Beyza'},
                     {'label': 'Ayhan', 'value': 'Ayhan'},
                     {'label': 'Burhan', 'value': 'Burhan'},
                     {'label': 'Koray', 'value': 'Koray'}
                 ],
                 value='x',
                 style={'width': '50%'}
                 ),
    html.Div(children='''
      
    ''', style={'color': 'black', 'fontSize': 30, 'marginLeft': 600}),
    html.Div(id='display-options', style={'color': 'red', 'fontSize': 18, 'marginLeft': 550}),

    html.Div(children='''
        Inside/Outside
    ''', style={'color': 'black', 'fontSize': 30, 'marginTop': 50}),
    html.Div(id='display-selected-values', style={'color': 'red', 'fontSize': 18, 'marginTop': 10}),

    html.Div(children='''
        Action
    ''', style={'color': 'black', 'fontSize': 30, 'marginTop': 50}),
    html.Button('Enter', id='button'),
    html.Button('Exit', id='buttonE', style={'color':'Red','marginLeft': 10}),
    html.Div(id='output-container-button4', style={'color': 'Black', 'fontSize': 18}),
    html.Button('SIMULATE', id='buttonSim', style={'backgroundColor':'Black','color':'Red','marginLeft': 20,'marginTop': 15,'fontSize': 20}),
    html.Div(id='output-container-button', style={'color': 'Black', 'fontSize': 18}),
    html.Div(id='output-container-button3', style={'color': 'Black', 'fontSize': 18})

]
    , style={'marginBottom': 50, 'marginTop': 25, 'marginLeft': 100})


@app.callback(
    dash.dependencies.Output('output-container-button4', 'children'),
    [dash.dependencies.Input('buttonSim', 'n_clicks')],[dash.dependencies.State('input-box1', 'value')])

def simulate_event(n_clicks, value):
    temp = 'Kullanıcı : "{}" çıkış yaptı. Tarih :'.format(
        value,
        n_clicks,
    )

    for z in range(30):
        isim=random.choice(allUsers)
        randomAction=random.choice(randomAct)

        if randomAction == 'enter':
            print(isim)
            print("ENTERDAYIZ"+randomAction)
            if isim in inside:
                a = 2
            else:
                if isim in outside:
                    outside.remove(isim)
                inside.append(isim)
                user.append(isim)
                date.append(dyear)
                time.append(dtime)
                action.append(randomAction)

        if randomAction == 'exit':
            print(isim)
            print("EXİTTAYIZ:"+randomAction)
            if isim in outside:
                a = 2 
            else:
                if isim in inside:
                    inside.remove(isim)
                outside.append(isim)
                user.append(isim)
                date.append(dyear)
                time.append(dtime)
                action.append(randomAction)




@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box1', 'value'),
     dash.dependencies.State('input-box-time', 'value'),
     dash.dependencies.State('input-box-date', 'value')])
def enter_event(n_clicks, value, value3, value2):
    temp = 'Kullanıcı : "{}" çıkış yaptı. Tarih :'.format(
        value,
        n_clicks,
    )
    acti = "enter"
    if (value != 'x'):
        if (value in inside):
            a = 2
        else:
            if (value in outside):
                outside.remove(value)
            inside.append(value)
            # events.append(value+","+dyear+","+dtime+","+acti)
            dyear = value2
            dtime = value3
            user.append(value)
            date.append(dyear)
            time.append(dtime)
            action.append(acti)


@app.callback(
    dash.dependencies.Output('output-container-button3', 'children'),
    [dash.dependencies.Input('buttonE', 'n_clicks')],
    [dash.dependencies.State('input-box1', 'value'),
     dash.dependencies.State('input-box-time', 'value'),
     dash.dependencies.State('input-box-date', 'value')])
def exit_event(n_clicks, value, value3, value2):
    temp = 'Kullanıcı : "{}" çıkış yaptı. Tarih :'.format(
        value,
        n_clicks,
    )

    act = "exit"
    if (value != 'x'):
        if (value in outside):
            a = 2
        else:
            if (value in inside):
                inside.remove(value)
            outside.append(value)
            # events.append(value + "," + dyear + "," + dtime + "," + act)
            dyear = value2
            dtime = value3
            user.append(value)
            date.append(dyear)
            time.append(dtime)
            action.append(act)


@app.callback(
    dash.dependencies.Output('display-selected-values', 'children'),
    [dash.dependencies.Input('input-box1', 'value'), dash.dependencies.Input('buttonE', 'n_clicks')])
def update_input(value, n_clicks):
    if value in outside:
        return "outside"
    if value in inside:
        return "inside"
    else:
        return "-"


@app.callback(
    dash.dependencies.Output('display-options', 'children'),
    [dash.dependencies.Input('button1', 'n_clicks')],
    [dash.dependencies.State('ozellikler', 'value')])
def update_input2(value, n_clicks):
    global inUsers
    global outUsers
    for x in inside:
        inUsers = inUsers + "," + x

    for y in outside:
        outUsers = outUsers + "," + y

    if value == 1:
        return "Users Inside:\n" + inUsers
    if value == 2:
        return "Users Outside:\n" + outUsers
    if value == 3:
        return ""
    if value == 4:
        return ""
    if value == 5:
        return ""
    else:
        return ""


@app.callback(
    dash.dependencies.Output('output-container-button2', 'children'),
    [dash.dependencies.Input('button2', 'n_clicks')],
    [dash.dependencies.State('input-box1', 'value')])
def update_backlog(n_clicks, value):
    temp = 'Kullanıcı : "{}" çıkış yaptı. Tarih :'.format(
        value,
        n_clicks,
    )

    events.append(user)
    events.append(date)
    events.append(time)
    events.append(action)
    # data['events'] = { "name":user,"date":date,"time":time,"action",action }
    person_dict = {"name": user, "date": date, "time": time, "action": action}
    data['events'] = person_dict

    # for i in range(6):
    # print("random item from list is: ", random.choice(allUsers))

    with open('data.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, sort_keys=False, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    app.run_server(debug=True)
