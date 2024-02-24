# Skewed Bar Chart
When the data is very skewed, it is very hard to read on the bar chart. In order to fix it, we may take a logarithm to the data to reduce the skewness effect. This folder contains the notes and script for this Medium <a href="">post</a>. The example we use is a hypotheical poll with 5 candidates, where 1 candidate has 50,000 votes, while the other 4 candidates have less than 1000 votes that shown a very skewed distribution on those 5 candidates. 

## Data
The dataset contains the candidate name and the number of votes of each candidate in the hypotheical poll. The data is hard coded in both scripts: <i>original_bar.py</i> and <i>log_bar.py</i>

## Scripts
The scripts are written in Python and utilize Plotly to visualize. There are two scripts:  <i>original_bar.py</i> and <i>log_bar.py</i>

### original_bar.py
The scripts declare the data and visualize with Plotly right away. Here is the visualization:

<img src=original_bar.png>

### log_bar.py
The scripts declare the data, take a logarithm of the observations, and visualize with Plotly afterward. Here is the visualization:

<img src=log_bar.png>