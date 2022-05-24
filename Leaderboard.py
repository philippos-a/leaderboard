import pandas as pd
import plotly.graph_objects as go

df = pd.read_excel(f"./Discover Marketplace API List.xlsx")["AREA2"].value_counts()

df_dict = df.to_dict()
print(df_dict)

fig = go.Figure(go.Bar(
            x=list(df_dict.values()),
            y=list(df_dict.keys()),
            orientation='h'))

fig.show()
fig.write_image("leaderboard.png")