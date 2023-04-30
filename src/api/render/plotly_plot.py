import plotly.express as px
import pandas as pd

# Plotly plot to extract lanmarks manually

df = pd.read_csv('./data/subject10.txt', sep="  ", header=None)
df.columns = ["x", "y", "z"]

fig = px.scatter_3d(df, x='x', y='y', z='z')
fig.update_traces(marker=dict(size=4,
                              line=dict(width=1, color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
fig.show()