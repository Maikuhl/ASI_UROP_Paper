import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

file_path = "C:\ASI_UROP\IATA_Database\CargoIS_Data\ASEAN_2018.csv"
df = pd.read_csv(file_path)

# print(df)

months = df["Data Month"].unique()
country = df["Origin Country Name"].unique()

# def logscale(dfin):
#     dfout = dfin.copy()
#     dfout = np.log(dfin)
#     return dfout 

# export = df.loc[df["Destination Country Name"] == "Singapore"]
# normalized_shipments = logscale(export["Number Shipments"])
# sns.lineplot(data=export, x=export["Data Month"], y= normalized_shipments , hue = export["Origin Country Name"])
# plt.show()

# export = df.loc[df["Destination Country Name"] == "Singapore"]
# sns.barplot(data=export, x=export["Data Month"], y=export["Number Shipments"], hue = export["Origin Country Name"])
# plt.show()

export = df.loc[df["Destination Country Name"] == "Singapore"]
# print(export["Number Shipments"].sum())

years = [2015,2016,2017,2018]

aggregate_shipments_per_year = []

singapore_gdp = [3.03*(10**11), 3.19*(10**11), 3.43*(10**11), 3.77*(10**11)]

for year in years:
    file_path = f"C:\ASI_UROP\IATA_Database\CargoIS_Data\ASEAN_{year}.csv"
    df_year = pd.read_csv(file_path)
    export = df_year.loc[df["Destination Country Name"] == "Singapore"]
    aggregate_shipments_per_year.append(export["Number Shipments"].sum())

print(aggregate_shipments_per_year)

# df_random = {}

# for i in range(len(aggregate_shipments_per_year)):
#     df_random[f"total shipments in {years[i]}"] = aggregate_shipments_per_year[i]
#     df_random[f"gdp in {years[i]}"] = singapore_gdp[i]

# # print(df_random)

# data = pd.DataFrame(df_random)
# print(data.corr())



# for i in country:
#     df = pd.read_csv(file_path)
#     export = df.loc[df["Destination Country Name"] == i]
#     svm = sns.lineplot(data=export, x=export["Data Month"], y=export["Weight"], hue = export["Origin Country Name"])
#     figure = svm.get_figure()
#     figure.savefig(f"C:\ASI_UROP\IATA_Database\CargoIS_Data\ASEAN_2018_Weights_Images\ASEAN_2018_Weights_{i}.png")
#     figure.clf()

# plt.show()

# for i in country:
#     df = pd.read_csv(file_path)
#     export = df.loc[df["Destination Country Name"] == i]
#     svm = sns.lineplot(data=export, x=export["Data Month"], y=export["Normalized Weight"], hue = export["Origin Country Name"])
#     figure = svm.get_figure()
#     figure.savefig(f"C:\ASI_UROP\IATA_Database\CargoIS_Data\ASEAN_2016_Weights_Images\ASEAN_2015_Weights_{i}.png")
#     figure.clf()

# def normalize_z(df):
#     dfout = df.copy()
#     dfout = (df["Shipments"]-df.mean()) / df.std()
#     return dfout