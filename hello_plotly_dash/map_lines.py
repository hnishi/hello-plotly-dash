import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
# import plotly.graph_objects as go

import map_fig

# Keep this out of source code repository - save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = {
    'hello': 'world'
}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

# fig = go.Figure(
#     data=go.Bar(y=[2, 3, 1], marker_color='Gold'))
fig = map_fig.get_fig()

app.layout = html.Div([
    html.H1('Welcome to the app'),
    html.H3('You are successfully authorized'),
    dcc.Graph(id="map",
              figure=fig),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['A', 'B']],
        value='A'
    ),
    dcc.Graph(id='graph')
], className='container')

server = app.server


@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('dropdown', 'value')])
def update_graph(dropdown_value):
    return {
        'layout': {
            'title': 'Graph of {}'.format(dropdown_value),
            'margin': {
                'l': 20,
                'b': 20,
                'r': 10,
                't': 60
            }
        },
        'data': [{'x': [1, 2, 3], 'y': [4, 1, 2]}]
    }


if __name__ == '__main__':
    app.run_server(debug=True)
