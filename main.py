from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd


# Bar Charts

df_Indep = pd.read_excel(r"C:\Users\Peter\OneDrive\TopKI\Machine_Learning\Tools_Algorithmen\Dash_Plotly\Knowhow_Plotly_Dash\Chart_sammlung\06_Dashboard_month\Indep.xlsx", index_col = 0)
df_Region= pd.read_excel(r"C:\Users\Peter\OneDrive\TopKI\Machine_Learning\Tools_Algorithmen\Dash_Plotly\Knowhow_Plotly_Dash\Chart_sammlung\06_Dashboard_month\Region.xlsx", index_col = 0)
df_Total= pd.read_excel(r"C:\Users\Peter\OneDrive\TopKI\Machine_Learning\Tools_Algorithmen\Dash_Plotly\Knowhow_Plotly_Dash\Chart_sammlung\06_Dashboard_month\Total.xlsx", index_col = 0)

df_Indep_0 = df_Indep[df_Indep['indep']==0]
df_Indep_1 = df_Indep[df_Indep['indep']==1]

df_Region_D = df_Region[df_Region['k306']=='D-CH']
df_Region_W = df_Region[df_Region['k306']=='W-CH']
df_Region_I = df_Region[df_Region['k306']=='I-CH']

# Bar Charts

def drawFigure_DCH():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        df_Region_D, x="t100", y="t900", color="a201"
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                        showlegend=False
                    ),
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])

def drawFigure_WCH():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        df_Region_W, x="t100", y="t900", color="a201"
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                        showlegend=False
                    ),
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])

def drawFigure_ICH():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        df_Region_I, x="t100", y="t900", color="a201"
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                        showlegend=False
                    ),
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])

def drawFigure_Indep():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        df_Indep_0, x="t100", y="t900", color="a201"
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                        showlegend=False
                    ),
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])



def drawFigure_Ketten():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        df_Indep_1, x="t100", y="t900", color="a201"
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                        showlegend=False
                    ),
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])


def drawFigure_Tot_bar():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.line(
                        df_Total, x="t100", y="t900", color="a201",
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                    ),
                    config={
                        'displayModeBar': False
                    }
                )
            ])
        ),  
    ])


def drawFigure_Tot_line():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        df_Total, x="t100", y="t900", color="a201",
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                        showlegend=False
                    ),
                    config={
                        'displayModeBar': False
                    }
                )
            ])
        ),  
    ])

# Text Felder

def drawText_DCH():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Umsatz Deutschschweiz"),
                ], style={'textAlign': 'center'}) 
            ])
        ),
    ])

def drawText_WCH():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Umsatz Westschweiz"),
                ], style={'textAlign': 'center'}) 
            ])
        ),
    ])

def drawText_ICH():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Umsatz Tessin"),
                ], style={'textAlign': 'center'}) 
            ])
        ),
    ])

def drawText_Ketten():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Umsatz Ketten"),
                ], style={'textAlign': 'center'}) 
            ])
        ),
    ])

def drawText_Indep():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Umsatz Unabhängig"),
                ], style={'textAlign': 'center'}) 
            ])
        ),
    ])

def drawText_Totline():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Umsatz Total nach Kategorie"),
                ], style={'textAlign': 'center'}) 
            ])
        ),
    ])

def drawText_Totbar():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Umsatz Total kumuliert"),
                ], style={'textAlign': 'center'}) 
            ])
        ),
    ])


# Build App
app = Dash(external_stylesheets=[dbc.themes.SLATE])

app.layout = html.Div([
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    drawText_DCH()
                ], width=3),
                dbc.Col([
                    drawText_WCH()
                ], width=3),                    
#                dbc.Col([
#                    drawText_ICH()
#                ], width=2),                    
                dbc.Col([
                    drawText_Ketten()
                ], width=3),
                dbc.Col([
                    drawText_Indep()
                ], width=3),
            ], align='center'), 
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawFigure_DCH() 
                ], width=3),
                dbc.Col([
                    drawFigure_WCH()
                ], width=3),
#                dbc.Col([
#                    drawFigure_ICH() 
#                ], width=2),
                dbc.Col([
                    drawFigure_Ketten()
                ], width=3),
                dbc.Col([
                    drawFigure_Indep() 
                ], width=3),
            ], align='center'), 
            html.Br(),            
            dbc.Row([
                dbc.Col([
                    drawText_Totline()
                ], width=9),
                dbc.Col([
                    drawText_Totbar()
                ], width=3),                    
            ], align='center'), 
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawFigure_Tot_bar()
                ], width=9),
                dbc.Col([
                    drawFigure_Tot_line()
                ], width=3),
            ], align='center'),      
        ]), color = 'dark'
    )
])
app.run_server()
# Run app and display result inline in the notebook