import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

ASEAN = ["Singapore", "Brunei Darussalam", "Viet Nam", "Lao People's Democratic Republic", "Thailand", "Philippines", "Malaysia", "Indonesia", "Cambodia", "Myanmar"]
major_ASEAN = ["Singapore", "Viet Nam", "Cambodia", "Malaysia", "Indonesia"]

file_path = f"C:\ASI_UROP\IATA_Database\CargoIS_Data\ASEAN_2015_aggregate_imports.csv"
df_year2015 = pd.read_csv(file_path)
file_path2 = f"C:\ASI_UROP\IATA_Database\CargoIS_Data\ASEAN_2016_aggregate_imports.csv"
df_year2016 = pd.read_csv(file_path2)
file_path3 = f"C:\ASI_UROP\IATA_Database\CargoIS_Data\ASEAN_2017_aggregate_imports.csv"
df_year2017 = pd.read_csv(file_path3)
file_path4 = f"C:\ASI_UROP\IATA_Database\CargoIS_Data\ASEAN_2018_aggregate_imports.csv"
df_year2018 = pd.read_csv(file_path4)

# print(df_year)

# Showing one year of data
# fig = px.line_polar(df_year[df_year["Origin Country Name"]=="Singapore"], r="Total Shipments", theta = "Destination Country Name",title="Singapore's exports")
# fig.update_traces(fill="toself")
# fig.show()

# for country in ASEAN:
#     max_values = []
#     fig = go.Figure()
#     fig.add_trace(go.Scatterpolar(r=df_year2015[df_year2015["Origin Country Name"]==country]["Total Shipments"], theta = ASEAN, fill = 'toself', name = "2015"))
#     max_values.append(df_year2015[df_year2015["Origin Country Name"]==country]["Total Shipments"].max())
#     fig.add_trace(go.Scatterpolar(r=df_year2016[df_year2016["Origin Country Name"]==country]["Total Shipments"], theta = ASEAN, fill = 'toself', name = "2016"))
#     max_values.append(df_year2016[df_year2016["Origin Country Name"]==country]["Total Shipments"].max())
#     fig.add_trace(go.Scatterpolar(r=df_year2017[df_year2017["Origin Country Name"]==country]["Total Shipments"], theta = ASEAN, fill = 'toself', name = "2017"))
#     max_values.append(df_year2017[df_year2017["Origin Country Name"]==country]["Total Shipments"].max())
#     fig.add_trace(go.Scatterpolar(r=df_year2018[df_year2018["Origin Country Name"]==country]["Total Shipments"], theta = ASEAN, fill = 'toself', name = "2018"))
#     max_values.append(df_year2018[df_year2018["Origin Country Name"]==country]["Total Shipments"].max())
#     upper_limit = max(max_values)
#     fig.update_layout(title_text=f"{country} exports",polar = dict(radialaxis=dict(visible=True, range=[0,upper_limit])))
#     fig.write_html(f"C:\ASI_UROP\IATA_Database\CargoIS_Data\Interactive_Radar_Plots\{country}.html") 

for country in major_ASEAN:
    max_values = []
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=df_year2015[df_year2015["Origin Country Name"]==country]["Log Shipments"], theta = major_ASEAN, fill = 'toself', name = "2015"))
    max_values.append(df_year2015[df_year2015["Origin Country Name"]==country]["Log Shipments"].max())
    fig.add_trace(go.Scatterpolar(r=df_year2016[df_year2016["Origin Country Name"]==country]["Log Shipments"], theta = major_ASEAN, fill = 'toself', name = "2016"))
    max_values.append(df_year2016[df_year2016["Origin Country Name"]==country]["Log Shipments"].max())
    fig.add_trace(go.Scatterpolar(r=df_year2017[df_year2017["Origin Country Name"]==country]["Log Shipments"], theta = major_ASEAN, fill = 'toself', name = "2017"))
    max_values.append(df_year2017[df_year2017["Origin Country Name"]==country]["Log Shipments"].max())
    fig.add_trace(go.Scatterpolar(r=df_year2018[df_year2018["Origin Country Name"]==country]["Log Shipments"], theta = major_ASEAN, fill = 'toself', name = "2018"))
    max_values.append(df_year2018[df_year2018["Origin Country Name"]==country]["Log Shipments"].max())
    upper_limit = max(max_values)
    fig.update_layout(title_text=f"{country}'s Imports",polar = dict(radialaxis=dict(visible=True, range=[0,4.5])))
    fig.write_html(f"C:\ASI_UROP\IATA_Database\CargoIS_Data\Interactive_Radar_Plots\Imports_Log\major\{country}_imports_log_major.html") 

# fig.show()
# fig.write_html(f"C:\ASI_UROP\IATA_Database\CargoIS_Data\Interactive_Radar_Plots\{country}.html")    
# print(df_year2015[df_year2015["Origin Country Name"]=="Singapore"]["Total Shipments"].max())
