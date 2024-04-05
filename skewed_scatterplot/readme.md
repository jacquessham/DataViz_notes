# Skewed Scatterplot
When the data is very skewed, it is very hard to read on the scatterplot. It is a similar situation to a skewed bar chart. In order to fix it, we may take a logarithm to the data to reduce the skewness effect. This folder contains the notes and script for this Medium <a href="">post (Coming soon)</a>.
<br><br>
One classic example is to plot the relationship between GDP and population. If we plot the dataset directly, it will look like this:
<img src=gdp.png>

<br>
In order to fix this we can simple to a logarithm to both GDP and population, then the scatterplot become more readable while it preserve the relationship among observations:
<img src=loggdp.png>

## Data
There are two files in this folder:
<ul>
	<li><i>gdp.csv</i>: GDP of each territory</li>
	<li><i>populations.csv</i>: Population of each territory</li>
</ul>

<br>
<i>gdp.csv</i> consists of the territories GDP in 2021 provided by IMF (Data obtained from <a href="https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)">Wikipedia</a>). <i>populations.csv</i> consists of the territories populations obtained from <a href="https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population">Wikipedia</a> as well.

## Scripts
The scripts are written in Python and utilize Plotly to visualize. There are two scripts: <i>display_gdp.py</i> and <i>display_loggdp.py</i>

### display_gdp.py
This script simply plot GDP and population of each nation on a scatterplot, and expected to produce a very skewed plot with Plotly.

### display_loggdp.py
This script take a logarithm to both GDP and population of each nation on a scatterplot, and plot it with Plotly. The script did not manually take a logarithm, but rather adjust in the layout setting:

```
layout = {'title':{'text':'Nations\' GDP vs Population', 'x':0.5},
			'xaxis': {'gridcolor': 'lightgray',
				'type':'log' # Add this parameter to take a log on x-axis
			},
			'yaxis': {'gridcolor': 'lightgray',
				'type':'log' # Add this parameter to take a log on y-axis
			},
			'plot_bgcolor': 'rgba(0,0,0,0)'}

```
