import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import json
from matplotlib import pyplot as plt
import seaborn as sns

app = Dash(__name__)


def create_map():
    df = pd.read_csv('deaths.csv') 
    
    df.rename(columns={'percent_deaths_f': 'Percentage (%)', 'country': 'Country'}, inplace=True)
    df = df.sort_values(['Percentage (%)']).reset_index(drop=True)

    f, ax = plt.subplots(figsize=(40, 5)) 

    plt.title('Percentage of sex-disaggregated COVID-19 deaths who were female, per country (as of Jan. 2023)')
    fig = sns.barplot(data=df, x='Country', y='Percentage (%)')
    plt.xticks(rotation=90, fontsize=8)
    vals = ax.get_yticks()
    ax.set_yticklabels(['{:.0f}%'.format(x) for x in vals])

    plt.show()
    
    app.layout = html.Div([
        dcc.Graph(figure=fig)
    ])
    
    app.run_server(debug=True)



create_map()