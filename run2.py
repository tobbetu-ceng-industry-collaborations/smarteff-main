
import dash_core_components as dcc
import dash_html_components as html
import dash

import json


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
tut=[]
indexOfevent=0
with open('data.json') as json_file:
    data = json.load(json_file)
    for p in data['events']:
        tut.append(str(p['id'])+","+p['action']+","+p['time']+" "+p['date'])


enum=[]
for idx, val in enumerate(tut,start=1):
    enum.append(idx)

hash = dict(zip(tut, enum))


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': 'White',
    'text': 'Black'
}

app.layout = html.Div(style={'backgroundColor': colors['background'],'display': 'inline-block'}, children=[
    html.H1(
        children='Event Log Editing Page',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='''
            Select event
        ''', style={'color': 'black', 'fontSize': 20, 'display': 'inline-block'}),

        dcc.Dropdown(id='input-box1',
                     options=[{ 'label': event, 'value': event} for event in tut],
                     value='x',
                     style={'width': '50%'}
                     ),

    html.Div(id='output-of-selection',children=" ", style={'color': 'Black', 'fontSize': 18, 'marginLeft': 500}),
    html.Div(id='output-of-selection2',children=" ", style={'color': 'Black', 'fontSize': 18, 'marginLeft': 500}),
    html.Div(id='output-of-selection3',children=" ", style={'color': 'Black', 'fontSize': 18, 'marginLeft': 500}),
    html.Div(id='output-of-selection_dump',children=" ", style={'color': 'Black', 'fontSize': 18, 'marginLeft': 500}),
    html.Div(id='output-of-selection_dump2',children=" ", style={'color': 'Black', 'fontSize': 18, 'marginLeft': 500}),
    html.Button('Delete', id='button1', style={'marginLeft': 500}),
    html.Button('Insert After', id='button2', style={'marginLeft': 10}),
    html.Button('Insert Before', id='button3', style={'marginLeft': 10}),

    html.H1(dcc.Input(id='input-box-event', type='text', value="Enter the event here: (with format ID,Event,Time)",
                      style={'width': '100%'}),
            style={'opacity': '1', 'color': 'black', 'fontSize': 15, 'marginLeft': 500}),

    html.Div(id='output-of-buttons', children=" ", style={'color': 'Black', 'fontSize': 18, 'marginLeft': 500}),
    html.Div(id='output-of-buttons2', children=" ", style={'color': 'Black', 'fontSize': 18, 'marginLeft': 500}),
    html.Div(id='output-of-buttons3', children=" ", style={'color': 'Black', 'fontSize': 18, 'marginLeft': 500})



])


@app.callback(
    dash.dependencies.Output('output-of-selection', 'children'),
    [dash.dependencies.Input('input-box1', 'value')])
def show_selection(value):
    global hash
    global indexOfevent
    temp = '  "{}" '.format(
        value

    )

    if value == "x":
        a=2
    else:

        indexOfevent= hash[value]
        print(indexOfevent)
        tutucuList= value.split(",")
        idEvent=tutucuList[0]



        return "UserID: " + idEvent


@app.callback(
    dash.dependencies.Output('output-of-selection2', 'children'),
    [dash.dependencies.Input('input-box1', 'value')])
def show_selection2(value):

    temp = '  "{}" '.format(
        value

    )
    if value == "x":
        a=2
    else:
        tutucuList= value.split(",")

        actEvent=tutucuList[1]



        return "Event: " + actEvent


@app.callback(
    dash.dependencies.Output('output-of-selection3', 'children'),
    [dash.dependencies.Input('input-box1', 'value')])
def show_selection3(value):

    temp = '  "{}" '.format(
        value

    )
    if value == "x":
        a=2
    else:
        tutucuList= value.split(",")

        timeEvent=tutucuList[2]


        return "Time: " + timeEvent



@app.callback(
    dash.dependencies.Output('output-of-buttons2', 'children'),
    [dash.dependencies.Input('button2', 'n_clicks')],
    [dash.dependencies.State('input-box-event', 'value')])
def insert_after(n_clicks, value):
    global tut
    global indexOfevent
    temp = ''.format(
        value,
        n_clicks,
    )
    if value=='Enter the event here: (with format ID,Event,Time)':
        a=2
        return " "
    else:
        tut.insert(indexOfevent,value)
        data['events'] = []
        for i in tut:
            jsonHolder = i.split(",")
            timeHolder = jsonHolder[2].split(" ")
            data['events'].append({
                'id': jsonHolder[0],
                'action': jsonHolder[1],
                'time': timeHolder[0],
                'date': timeHolder[1],
            })

        namejson = "edited_data.json"
        with open(namejson, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, sort_keys=False, indent=4, ensure_ascii=False)
        return "Insertion Completed"

@app.callback(
    dash.dependencies.Output('output-of-buttons3', 'children'),
    [dash.dependencies.Input('button3', 'n_clicks')],
    [dash.dependencies.State('input-box-event', 'value')])
def insert_before(n_clicks, value):
    global tut
    global indexOfevent
    temp = ''.format(
        value,
        n_clicks,
    )
    if value=='Enter the event here: (with format ID,Event,Time)':
        a=2
        return " "
    else:
        tut.insert(indexOfevent-1,value)
        data['events'] = []
        for i in tut:
            jsonHolder = i.split(",")
            timeHolder = jsonHolder[2].split(" ")
            data['events'].append({
                'id': jsonHolder[0],
                'action': jsonHolder[1],
                'time': timeHolder[0],
                'date': timeHolder[1],
            })

        namejson = "edited_data.json"
        with open(namejson, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, sort_keys=False, indent=4, ensure_ascii=False)
        return "Insertion Completed"


@app.callback(
    dash.dependencies.Output('output-of-buttons', 'children'),
    [dash.dependencies.Input('button1', 'n_clicks')],
    [dash.dependencies.State('input-box1', 'value')]
    )
def delete_event(n_clicks, value):
    global tut
    global indexOfevent
    temp = ''.format(
        value,
        n_clicks,
    )
    if value=='x':
        a=2
        return " "
    else:
        if value in tut:
            tut.remove(value)
            data['events'] = []
            for i in tut:
                jsonHolder = i.split(",")
                timeHolder = jsonHolder[2].split(" ")
                data['events'].append({
                    'id': jsonHolder[0],
                    'action': jsonHolder[1],
                    'time': timeHolder[0],
                    'date': timeHolder[1],
                })

            namejson = "edited_data.json"
            with open(namejson, 'w', encoding='utf-8') as outfile:
                json.dump(data, outfile, sort_keys=False, indent=4, ensure_ascii=False)
            return "Deletion Completed"
        else:
            return "Event Log does not contain this Event"



@app.callback(
    dash.dependencies.Output('input-box1', 'options'),
    [dash.dependencies.Input('input-box1', 'value')]
    )
def update_date_dropdown(name):
        return [{'label': i, 'value': i} for i in tut]






if __name__ == '__main__':
    app.run_server(debug=True)