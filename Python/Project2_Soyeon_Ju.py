import dash
import dash_html_components as html
import dash_core_components as dcc
import base64
import datetime
import io
import dash_table
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px

external_stylesheets = ['http://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
     html.Div(className="app-header", children=[
            html.H4('Project #2'),
            html.Div('Spring 2021 | CS632P | Soyeon Ju', className="app-header--title")]),
    html.Div(children='Step1: Select your File', className='Step_name'),
    dcc.Upload(className='upload-data', id='upload',
               children=html.Div([ 'Drag and Drop or  ',
                        html.A('Select File', className='select_button')]),
               multiple=True),
    html.Button('file', id='parse',className='button', n_clicks=0),
    html.Hr(),
    html.Div(id='describe'),
    html.Div(id='filter'),
    html.Div(id='preview'),
])


def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))

    except Exception as e:
        print(e)
        return html.Div(['There was an error processing this file.'])

    return df

@app.callback (
    Output('parse', 'children'),
    Input('upload','filename'),
    prevent_initial_call=True)

def file_name(filename):
    return filename[0]

@app.callback(
    Output('describe', 'children'),
    Input('parse', 'n_clicks'),
    Input('upload', 'contents'),
    Input('upload', 'filename')
)
def parse(clicks,contents,filename):
    if clicks:
        table = html.Div()
        if contents:
            contents = contents[0]
            filename = filename[0]
            global df
            df = parse_contents(contents,filename)
            table = html.Div([
                     html.Div(id='desc-data', children=[html.Div('Step2: Describe your data',className='Step_name')]),
                     html.Table([
                        html.Tr([html.Th("Column name"),
                                 html.Th("Data type"),
                                 html.Th("Ignore")], className="step2_table"),
                        html.Td([html.Tr(f"{col}",className='step2_row') for col in df.columns]),
                        html.Td([html.Tr(dcc.Dropdown( id='data_type',
                                options=[{'label': 'date-time', 'value': 'date-time'},
                                         {'label': 'Numerical', 'value': 'Numerical'},
                                         {'label': 'String/Categorical', 'value': 'String'}],
                                value='', className='dt_dd')) for col in df.columns]),
                        html.Td([html.Tr(dcc.Checklist(
                            id='check',
                            options=[({'label': '', 'value': col}) for col in df.columns],className='checklist'))])],
                            style={'marginLeft':100, 'marginRight': 'auto','textAlign':'center',},),

                             html.Button('Next', id='Next', className='button', n_clicks=0)
         ])
        return table

@app.callback(
    Output('filter','children'),
    Input('Next', 'n_clicks'),
    State('check','value'),
    State('data_type','value'),
)
def filter_data(click,value,chosen_data):
    #date-time is not change at once. If you click continue button, and then data type changing works.
    if chosen_data == 'date-time':
        df['Date'] = pd.to_datetime(df['Date'])
        ddf = df.loc[:, ~df.columns.isin(value)]
        result = html.Div([
            dash_table.DataTable(columns=[{"name": i, 'id': i} for i in ddf.columns],
                                 data=ddf.to_dict('records'),
                                 page_size=10,
                                 style_cell={'textAlign': 'center'},
                                 style_table={'height': 400, 'width': 800}),
            html.Button('Continue', id="Continue", className='button')])
        return result

    elif chosen_data == "Numerical":
        f = df.astype('int')
        ddf = f.loc[:, ~df.columns.isin(value)]
        result = html.Div([
            dash_table.DataTable(columns=[{"name": i, 'id': i} for i in ddf.columns],
                                 data=ddf.to_dict('records'),
                                 page_size=10,
                                 style_cell={'textAlign': 'center'},
                                 style_table={'height': 400, 'width': 800}),
            html.Button('Continue', id="Continue", className='button'),
            ])
        return result

    elif chosen_data =='String':
        f = df.astype('string')
        ddf = f.loc[:, ~df.columns.isin(value)]
        result = html.Div([
            dash_table.DataTable(columns=[{"name": i, 'id': i} for i in ddf.columns],
                                 data=ddf.to_dict('records'),
                                 page_size=10,
                                 style_cell={'textAlign': 'center'},
                                 style_table={'height': 400, 'width': 800}),
            html.Button('Continue', id="Continue", className='button'),
        ])
        return result

@app.callback(
    Output('preview','children'),
    Input('Continue', 'n_clicks')
)
def preview(clicks):
    if clicks:
        return html.Div([html.Div(id="preview-data"),html.Br(),
                         html.H1(children="Step3: Preview your data ",className='Step_name'),
                         html.Div("Curve Identifiers to Display"),
                         dcc.Dropdown(id='drop-down',
                                      options=[({'label':x, 'value':x}) for x in df['Stock'].unique()],
                                      multi=True, className="dpdn",
                                      value=df['Stock'].unique()[0]),
                         html.Br(),
                         html.Div(id='selected_table'), # table here
                         html.Br(),
                         html.Div('Feature name to plot'),
                         html.Div([dcc.Dropdown(
                                    id ="feature-dpdn",
                                    options=[({'label': x, 'value': x}) for x in df.columns[1:3]],
                                    value=df.columns[1],
                                    searchable=True, className="dpdn"
                         )]),html.Br(),
                         html.Div('Securities'),
                         html.Div([dcc.Dropdown(
                             id="securities-dpdn",
                             options=[({'label': x, 'value': x}) for x in df['Stock'].unique()],
                             value=df.columns[2], className="dpdn",
                             multi=True,
                         )]),
                         dcc.Graph(id='my-graph')
                         ])

@app.callback(
    Output('selected_table', 'children'),
    Input('drop-down', 'value'),
)
def stock_table(value):
        stock_filter = df[df['Stock'].isin(value)]
        result= dash_table.DataTable(columns=[{"name": i, 'id': i} for i in df.columns],
                                    data=stock_filter.to_dict('records'),
                                    page_size=10,
                                    style_cell={'textAlign': 'center'},
                                    style_cell_conditional=[{'if':{'column_id':'Stock'},'background-color':' #faebd7'}],
                                    style_table={'height': 400, 'width': 800})
        return result
@app.callback(
    Output('my-graph', 'figure'),
    Input('securities-dpdn', 'value'),
    Input('feature-dpdn','value')
)
def update_graph(securities_dropdown,feature_dropdown):
    df['Date'] = pd.to_datetime(df['Date'])
    df_filtered = df[df['Stock'].isin(securities_dropdown)]
    selected_securities = df_filtered['Stock'].tolist()
    df_line = df[df['Stock'].isin(selected_securities)]
    chart= px.line(df_line, x='Date', y=feature_dropdown, color='Stock', width=1000)
    chart.update_layout(title={'text':f'Line Chart of {feature_dropdown} and Date'})
    chart.update_layout(uirevision='foo')

    return chart




if __name__ == '__main__':
    app.run_server(debug=False, dev_tools_ui=False, dev_tools_props_check=False)