import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

structure = {}

# exports to ASEAN countries 


file_path = f"C:\ASI_UROP\IATA_Database\CargoIS_Data\ASEAN_2015.csv"
df_year = pd.read_csv(file_path)
export = df_year.loc[df_year["Destination Country Name"] == "Singapore"]

country_export = export['Origin Country Name'].unique()

main = []

for country in country_export:
    export_country = export.loc[df_year['Origin Country Name'] == country]
    export_country = export_country[["Data Month", "Number Shipments"]]
    export_array = export_country.to_numpy()
    array = []
    for i in range(12):
       array.append(export_array[i][1])
    main.append(array)


data = pd.DataFrame(main, index = list(country_export))

# data = pd.DataFrame(main, columns = [x for x in range(1,13)])

transpose = data.T

transpose.insert(0, "Months", [x for x in range(1,13)])

print(transpose.T)

# file_path = "C:\ASI_UROP\IATA_Database\CargoIS_Data\export_to_singapore2.csv"

# transpose.to_csv(file_path)