#import required library and packages
import os
import pandas as pd
from plotly.offline import plot, iplot
import plotly.graph_objects as go

#import data and specify data types for some columns
df = pd.read_csv('/Users/teacher/Downloads/Billboad_Top_100_Weekly_2019.csv', dtype={"Weeks on Chart": int})
print(df.dtypes)

#Create a vertical bar graph of the top 10 most featured artists descending (count on Y axis, artist name on X axis)
artist_instances = df['Performer'].value_counts().rename_axis('artist_name').reset_index(name='counts')
top_10 = artist_instances.head(10)
print(top_10)

fig = go.Figure([go.Bar(x=________['artist_name'], y=_______['counts'])])
fig.update_layout(title='Top 10 Featured Artists',xaxis=dict(title='Artist Name'), yaxis=dict(title='Songs on Chart'))
fig.show()

#Create a vertical bar graph of the top 10 songs spending the most weeks on the charts (count on Y axis, artist name on X axis)
sorted_df = df.sort_values(by=['Weeks on Chart'], ascending=False)
no_duplicates = sorted_df.drop_duplicates(['Song'])
top_10 = no_duplicates.head(10)
print(top_10)

fig = go.Figure([go.Bar(x=____________________, y=__________________________)])
fig.update_layout(title='Top 25 Songs by Weeks on Chart',xaxis=dict(title='Song Title'), yaxis=dict(title='Weeks on Billboard'))
fig.show()

#Pick one song that has been on the chart for at least 25 weeks and graph its weekly position with a line graph (rank on Y axis, date on X axis)
talk = df['Song']=="Talk"
talk_df = df[talk]
print(talk_df)

fig = _______________(data=go.Scatter(x=_________________, y=__________________))
fig['layout']['yaxis']['autorange'] = "reversed"
fig.update_layout(title='Song Ranking by Week',xaxis=dict(title='_________'), yaxis=dict(title='_________'))
fig.show()
