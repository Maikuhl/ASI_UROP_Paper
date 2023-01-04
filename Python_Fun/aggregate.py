import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

ASEAN = ["Singapore", "Brunei Darussalam", "Viet Nam", "Lao People's Democratic Republic", "Thailand", "Philippines", "Malaysia", "Indonesia", "Cambodia", "Myanmar"]

aggregate_shipments_per_year = []

file_path = f"C:\ASI_UROP\IATA_Database\CargoIS_Data\ASEAN_2018.csv"
df_year = pd.read_csv(file_path)

target_countries = []
total_shipments_per_country = []
total_weight_per_country = []
origin_array = []

# for origin in ASEAN:
#     for destination in ASEAN: 
#         export = df_year.loc[df_year["Origin Country Name"] == origin]
#         destination_country =  export.loc[export["Destination Country Name"] == destination]
#         # if destination == origin:
#         #     continue
#         origin_array.append(origin)
#         target_countries.append(destination)
#         total_shipments = destination_country["Number Shipments"].sum()
#         total_shipments_per_country.append(total_shipments)
#         total_weight = destination_country["Weight"].sum()
#         total_weight_per_country.append(total_weight)
#         # print(origin,destination, total_shipments)

for origin in ASEAN:
    for destination in ASEAN: 
        imports = df_year.loc[df_year["Destination Country Name"] == origin]
        destination_country =  imports.loc[imports["Origin Country Name"] == destination]
        # if destination == origin:
        #     continue
        origin_array.append(origin)
        target_countries.append(destination)
        total_shipments = destination_country["Number Shipments"].sum()
        total_shipments_per_country.append(total_shipments)
        total_weight = destination_country["Weight"].sum()
        total_weight_per_country.append(total_weight)
        # print(origin,destination, total_shipments)


data = {"Origin Country Name":origin_array, "Destination Country Name": target_countries,"Total Shipments": total_shipments_per_country, "Total Weight": total_weight_per_country }

df = pd.DataFrame(data)

df.to_csv("C:\ASI_UROP\IATA_Database\CargoIS_Data\ASEAN_2018_aggregate_imports.csv")

missing = df[df["Total Shipments"] == 0]

# missing.to_csv("C:\ASI_UROP\IATA_Database\CargoIS_Data\ASEAN_2018_missing_data.csv")

