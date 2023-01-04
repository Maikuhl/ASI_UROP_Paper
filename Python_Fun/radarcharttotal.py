import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

ASEAN = ["Singapore", "Brunei Darussalam", "Viet Nam", "Lao People's Democratic Republic", "Thailand", "Philippines", "Malaysia", "Indonesia", "Cambodia", "Myanmar"]

file_path = "C:\ASI_UROP\IATA_Database\CargoIS_Data\ASEAN_total_aggregate.csv"
df = pd.read_csv(file_path)

fig = go.Figure()
year = df.loc[df["Year"]==2015]
fig.add_trace(go.Scatterpolar(r=year["Log Aggregate Shipments"], theta = ASEAN, fill = 'toself', name = "2015"))
year = df.loc[df["Year"]==2016]
fig.add_trace(go.Scatterpolar(r=year["Log Aggregate Shipments"], theta = ASEAN, fill = 'toself', name = "2016"))
year = df.loc[df["Year"]==2017]
fig.add_trace(go.Scatterpolar(r=year["Log Aggregate Shipments"], theta = ASEAN, fill = 'toself', name = "2017"))
year = df.loc[df["Year"]==2018]
fig.add_trace(go.Scatterpolar(r=year["Log Aggregate Shipments"], theta = ASEAN, fill = 'toself', name = "2018"))
fig.update_layout(title_text=f"Total shipments (export & imports)",polar = dict(radialaxis=dict(visible=True, range=[0,6])))

# fig.show()
fig.write_html(f"C:\ASI_UROP\IATA_Database\CargoIS_Data\graph\ggregate.html")