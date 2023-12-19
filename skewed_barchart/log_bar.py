import math
import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)

# Data
names = ['Candidate 1','Candidate 2','Candidate 3','Candidate 4','Candidate 5']
scores = [50000, 800, 600, 500, 400]
scores_log = [math.log(score) for score in scores]

data = []
data.append(go.Bar(x=scores_log[::-1], y=names[::-1],
	               textposition='auto', text=scores[::-1],
	               orientation='h',
	               textfont=dict(color='white')))
# Layout
layout = {
	'title':{'text':'Voting Count', 'x':0.5}, 
	'xaxis':{'showticklabels': False}
	}

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='bar.html')
