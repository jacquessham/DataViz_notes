import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Import data
df_gdp = pd.read_csv('gdp.csv')
df_pop = pd.read_csv('populations.csv')
df = df_gdp.merge(df_pop,how='left',on='Territory')

# Data
data = []
for region in df['Region'].unique():
	data.append(go.Scatter(x=df['Population'], y=df['Nominal_GDP'],
					marker_color='red',
					text=df['Territory'],
					hoverinfo='text',
					mode='markers'))
# Layout
layout = {'title':{'text':'Nations\' GDP vs Population', 'x':0.5},
			'xaxis': {'gridcolor': 'lightgray'},
			'yaxis': {'gridcolor': 'lightgray'},
			'plot_bgcolor': 'rgba(0,0,0,0)'}

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='nations_gdp_pop.html')