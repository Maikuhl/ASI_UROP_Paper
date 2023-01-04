import pandas as pd 
import numpy as np 

file_path = "C:\ASI_UROP\IATA_Database\CargoIS_Data\CargoIS_2015-2018_WeightShipments_CountryLevel.csv"
df = pd.read_csv(file_path)

columns = df.columns

# print(columns)

ASEAN = ["Singapore", "Brunei Darussalam", "Viet Nam", "Lao People's Democratic Republic", "Thailand", "Philippines", "Malaysia", "Indonesia", "Cambodia", "Myanmar"]

ASEAN_df = df.loc[df['Origin Country Name'].isin(ASEAN)]
# print(ASEAN_df['Origin Country Name'].unique())

ASEAN_df = ASEAN_df.loc[ASEAN_df['Destination Country Name'].isin(ASEAN)]
# print(ASEAN_df['Origin Country Name'].unique())


# print(ASEAN_df)

# print(df['Data Month'][0][4:])

# group_by_years = ASEAN_df.groupby(ASEAN_df['Data Month'].apply(lambda x: x[4:]))

# print(group_by_years.sum())

# for i in years:
#     year_file_path = f"C:\ASI_UROP\IATA_Database\CargoIS_Data\{i}"
#     year = df.loc[ASEAN_df['Data Month'][0][4:].isin(i)]
#     year_df=pd.DataFrame(year)
#     year_df.to_csv(year_file_path)

all_years = ASEAN_df['Data Month'].unique()

year_2015 = all_years[0:12]
year_2016 = all_years[12:24]
year_2017 = all_years[24:36]
year_2018 = all_years[36:48]

year_lists = [year_2015,year_2016,year_2017,year_2018]

years = [2015,2016,2017,2018]

ASEAN_2015 = ASEAN_df.loc[ASEAN_df['Data Month'].isin(year_2015)]
print(ASEAN_2015['Origin Country Name'].unique())
ASEAN_2016 = ASEAN_df.loc[ASEAN_df['Data Month'].isin(year_2016)]
print(ASEAN_2016['Origin Country Name'].unique())
ASEAN_2017 = ASEAN_df.loc[ASEAN_df['Data Month'].isin(year_2017)]
print(ASEAN_2017['Origin Country Name'].unique())
ASEAN_2018 = ASEAN_df.loc[ASEAN_df['Data Month'].isin(year_2018)]
print(ASEAN_2018['Origin Country Name'].unique())

# for i in range(len(year_lists)):
#     year_file_path = f"C:\ASI_UROP\IATA_Database\CargoIS_Data\ASEAN_{years[i]}.csv"
#     ASEAN_year = ASEAN_df.loc[ASEAN_df['Data Month'].isin(year_lists[i])]
#     ASEAN_year.to_csv(year_file_path)

