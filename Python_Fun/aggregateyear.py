import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

ASEAN = ["Singapore", "Brunei Darussalam", "Viet Nam", "Lao People's Democratic Republic", "Thailand", "Philippines", "Malaysia", "Indonesia", "Cambodia", "Myanmar"]
years = [2015,2016,2017,2018]

data = []

for year in years:
    file_path = f"C:\ASI_UROP\IATA_Database\CargoIS_Data\ASEAN_{year}.csv"
    df = pd.read_csv(file_path)
    for country in ASEAN:
        export_df = df.loc[df['Origin Country Name'] == country]
        import_df = df.loc[df['Destination Country Name'] == country]
        aggregate_shipments = export_df["Number Shipments"].sum() + import_df["Number Shipments"].sum()
        data.append([year,country, aggregate_shipments])

df = pd.DataFrame(data,columns=["Year","COuntry","Aggregate Shipments"])

df.to_csv("C:\ASI_UROP\IATA_Database\CargoIS_Data\ASEAN_total_aggregate.csv")