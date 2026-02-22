# -*- coding: utf-8 -*-
'''
Callbacks: functions that are automatically called by Dash whenever an input 
component's property changes, in order to update some property in another 
component (the output).
'''

import dash
from dash import dcc
from dash import html
from dash import Input, Output

#app initialization
app = dash.Dash()

#layout section
app.layout = html.Div(id = 'parent', children = [
    
    #heading 
    html.H3(id = 'mytitle', children = 'Basic Callback example', style={'font-family':'Verdana', 'font-size':100, 'color':'red'}),
    
    html.Br(),
    
    dcc.Dropdown(id = 'dropdown',
                 options = [
                     {'label':'amazing', 'value':5},
                     {'label':'average','value':3},
                     {'label':'below average', 'value':1}
                     
                     ],
                 value = 5,
                 
                 
                 ),
    html.Br(),
    
    html.Div(id = 'output-text')
    
    
    ])


# the callback takes as Input the dropdown list, and in particular, it's triggered by the value property
# and return as Output a list of children components that will added to the output-text component.

@app.callback(Output(component_id='output-text',component_property='children'),
              [Input(component_id='dropdown',component_property='value')])
def basic_callback(input_value):
    return html.Div(input_value)


if __name__ == '__main__':
    app.run(debug=True)