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
top_10 = artist_instances.head(____)
print(top_10)

#Create a vertical bar graph of the top 25 songs spending the most weeks on the charts (count on Y axis, artist name on X axis)
sorted_df = df.sort_values(by=['_________________'], ascending=False)
no_duplicates = sorted_df.drop_duplicates(['Song'])
top_25 = no_duplicates.head(____)
print(top_25)

#Pick one song that has been on the chart for at least 25 weeks and graph its weekly position with a line graph (rank on Y axis, date on X axis)
song_condition = df['_______']=="_____"
song_df = df[_______]
print(song_df)
