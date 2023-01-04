import plotly.express as px
import pandas as pd

singapore_exports_df = pd.read_csv("C:\ASI_UROP\IATA_Database\CargoIS_Data\Singapore_Exports_2015_Map\singapore_exports_2015.csv")

fig = px.scatter_geo(
    data_frame=singapore_exports_df, 
    lat=singapore_exports_df['origin latitude'], 
    lon=singapore_exports_df['origin longitude'],
    size=singapore_exports_df['Log Shipments'],
    )