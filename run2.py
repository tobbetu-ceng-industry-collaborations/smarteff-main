import dash
import dash_core_components as dcc
import dash_html_components as html
import webbrowser

import datetime

import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output, State
import dash_table

import pandas as pd
import json
import random
import requests


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



tut=[]
with open('data.json') as json_file:
    data = json.load(json_file)
    for p in data['events']:
        tut.append(str(p['id'])+","+p['action']+","+p['time']+"\t"+p['date'])





app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': 'White',
    'text': 'Black'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
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
                     options=[{'label':event, 'value':event} for event in tut],
                     value='x',
                     style={'width': '50%'}
                     ),

    html.Div(id='output-of-selection', style={'color': 'Black', 'fontSize': 18, 'marginLeft:': 30}),
    html.Button('Delete', id='button1', style={'marginLeft': 500}),
    html.Button('Insert After', id='button2', style={'marginLeft': 10}),
    html.Button('Insert Before', id='button3', style={'marginLeft': 10})





])


@app.callback(
    dash.dependencies.Output('output-of-selection', 'children'),
    [dash.dependencies.Input('input-box1', 'value')])
def show_selection(value):

    temp = '  "{}" '.format(
        value

    )
    if value == "x":
        a=2
    else:
        tutucuList= value.split(",")
        idEvent=tutucuList[0]
        actEvent=tutucuList[1]
        timeEvent=tutucuList[2]


        return ("UserID: " + idEvent + "\n"+ "Event: " + actEvent + "\n" + "Time: " + timeEvent)






if __name__ == '__main__':
    app.run_server(debug=True)