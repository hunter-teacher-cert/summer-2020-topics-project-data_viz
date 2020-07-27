#import required library and packages
import os
import pandas as pd
from plotly.offline import plot, iplot
import plotly.graph_objects as go

#import data and specify data types for some columns
#df = pd.read_csv('/Users/teacher/Downloads/Billboad_Top_100_Weekly_2019.csv', dtype={"Week Position": object, "Instance": object, "Previous Week Position": object, "Peak Position": object, "Weeks on Chart": int})
df = pd.read_csv('/Users/teacher/Downloads/Billboad_Top_100_Weekly_2019.csv', dtype={"Weeks on Chart": int})
print(df.dtypes)
#df_types = df.astype({'Week Position': 'int32', 'WeekID': 'datetime64'}).dtypes

#Create a horizontal bar graph displaying the #1 song each week of the year (date on Y axis, artist and song name on X axis)
top_condition = df['Week Position']=="1"
filter_df = df[top_condition]
filter_df = filter_df.reindex(index=filter_df.index[::-1]) #reverses data frame

#df["2nd"] = pd.to_numeric(df["2nd"])
#print(filter_df.dtypes)
#print(filter_df.head(20))

fig = go.Figure([go.Bar(x=filter_df['Week Number'], y=filter_df['Song'])])
#fig = go.Figure(data=go.Bar(y=[6, 7, 1]))
fig.show()



#Create a vertical bar graph of the top 25 songs spending the most weeks on the charts (count on Y axis, artist name on X axis)
sorted_df = df.sort_values(by=['Weeks on Chart'], ascending=False)
no_duplicates = sorted_df.drop_duplicates(['Song'])
top_25 = no_duplicates.head(25)

fig = go.Figure([go.Bar(x=top_25['Song'], y=top_25['Weeks on Chart'])])
fig.show()

#Create a vertical bar graph of the top 10 most featured artists descending (count on Y axis, artist name on X axis)
#artist_instances = df['Performer'].value_counts()
artist_instances = df['Performer'].value_counts().rename_axis('artist_name').reset_index(name='counts')
top_25 = artist_instances.head(25)
print(top_25)

fig = go.Figure([go.Bar(x=top_25['artist_name'], y=top_25['counts'])])
fig.show()


#Pick one song that has been on the chart for at least 25 weeks and graph its weekly position with a line graph (rank on Y axis, date on X axis)
talk = df['Song']=="Talk"
talk_df = df[talk]
print(talk_df)

fig = go.Figure(data=go.Scatter(x=talk_df['Week Number'], y=talk_df['Week Position']))
fig['layout']['yaxis']['autorange'] = "reversed"
fig.show()
