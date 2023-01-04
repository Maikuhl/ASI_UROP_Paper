import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

ASEAN = ["Singapore", "Brunei Darussalam", "Viet Nam", "Lao People's Democratic Republic", "Thailand", "Philippines", "Malaysia", "Indonesia", "Cambodia", "Myanmar"]

# file_path = "C:\ASI_UROP\IATA_Database\CargoIS_Data\ASEAN_total_aggregate.csv"
# df = pd.read_csv(file_path)

# print(df.columns)

# df["Year"] = df["Year"].astype(str)

# print(df)

# sns_plot = sns.lineplot(data=df, x="Year",y="Aggregate Shipments", hue = "Country")
# plt.show()
# fig = sns_plot.get_figure()
# fig.savefig("C:\ASI_UROP\IATA_Database\CargoIS_Data\graph\ASEAN_total_aggregate.png")

year = 17

months = [f"Jan-{year}",f"Feb-{year}",f"Mar-{year}",f"Apr-{year}",f"May-{year}",f"Jun-{year}",f"Jul-{year}",f"Aug-{year}",f"Sep-{year}",f"Oct-{year}",f"Nov-{year}",f"Dec-{year}"]
data = []

file_path = f"C:\ASI_UROP\IATA_Database\CargoIS_Data\ASEAN_Shipment_Data\ASEAN_20{year}.csv"
df = pd.read_csv(file_path)
# print(df['Data Month'][0][0:3])

for month in months:
    monthly = df.loc[df['Data Month'] == month]
    for country in ASEAN:
        export_df = monthly.loc[df['Origin Country Name'] == country]
        import_df = monthly.loc[df['Destination Country Name'] == country]
        aggregate_shipments = export_df["Number Shipments"].sum() + import_df["Number Shipments"].sum()
        data.append([month,country, aggregate_shipments])

dataf = pd.DataFrame(data,columns=["Data Month","Country","Aggregate Shipments"])

dataf.to_csv(f"C:\ASI_UROP\IATA_Database\CargoIS_Data\ASEAN_Shipment_Data\ASEAN_20{year}_Monthly_Aggregate.csv")

# graph = sns.lineplot(data=dataf, x="Data Month",y="Aggregate Shipments", hue = "Country")
# graph.axvline(x = f"Mar-{year}",color="black",linestyle="dashed")
# graph.axvline(x = f"Apr-{year}",color="black",linestyle="dashed")
# graph.axvline(x = f"Oct-{year}",color="black",linestyle="dashed")
# graph.axvline(x = f"Nov-{year}",color="black",linestyle="dashed")
# plt.show()