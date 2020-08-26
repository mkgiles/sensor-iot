# Server script, reads data from database and generates live graphs for consumption
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from datetime import datetime as dt
from dash.dependencies import Input, Output
from sqlalchemy import create_engine
import pymysql
import flask

db_connection_str =  'INSERT SQL CONNECTION STRING HERE'
db_connection = create_engine(db_connection_str)
names = []
query = db_connection.execute('SHOW TABLES;')
results = query.fetchall()
for result in results:
        names.append({'label': result[0], 'value': result[0]})
selected = [names[0]['value']]
def generate_graph(name, start, end):
        df = pd.read_sql('SELECT * FROM ' + name + ' WHERE time BETWEEN \'' + start + '\' AND \'' + end + '\'', con=db_connection)
        if(df.size > 0):
                return html.Div([
                        dcc.Markdown('## ' + name),
                        dcc.Graph(id=name+'_graph', figure=px.line(df, x="time", y="ppm", color="type"))
                        ])
        else:
                return html.P("No data found for this time period.")
def generate_graphs(names, start, end):
        return [generate_graph(x, start, end) for x in names]
server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)
app.layout = html.Div([
        dcc.Markdown("""# Graphs"""),
        dcc.Dropdown(id='names_drop', options=names, value=selected, multi=True),
        dcc.DatePickerRange(id='range'),
        html.Div(generate_graphs(selected, dt.min.date().isoformat(), dt.today().date().isoformat()), id='graph'),
        dcc.Interval(
                id='interval-component',
                interval=60000,
                n_intervals=0
                )
        ])
@app.callback(Output('graph', 'children'),
              [Input('interval-component', 'n_intervals'),
               Input('range', 'start_date'),
               Input('range', 'end_date'),
               Input('names_drop', 'value')])
def update_graphs(n, start, end, options):
        selected = []
        if start is None:
                start = dt.min.date().isoformat()
        if end is None:
                end = dt.max.date().isoformat()
        for selection in options:
                selected.append(selection)
        return generate_graphs(selected, start, end)
if __name__ == '__main__':
        app.run_server(debug=True)
