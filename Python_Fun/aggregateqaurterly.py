import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

years = [15,16,17,18]

data = []

ASEAN = ["Singapore", "Brunei Darussalam", "Viet Nam", "Lao People's Democratic Republic", "Thailand", "Philippines", "Malaysia", "Indonesia", "Cambodia", "Myanmar"]

for year in years: 
    file_path = f"C:\ASI_UROP\IATA_Database\CargoIS_Data\ASEAN_Shipment_Data\ASEAN_20{year}.csv"

    months = [f"Jan-{year}",f"Feb-{year}",f"Mar-{year}",f"Apr-{year}",f"May-{year}",f"Jun-{year}",f"Jul-{year}",f"Aug-{year}",f"Sep-{year}",f"Oct-{year}",f"Nov-{year}",f"Dec-{year}"]
    df = pd.read_csv(file_path)

    for country in ASEAN:
        export_df = df.loc[df['Origin Country Name'] == country]
        import_df = df.loc[df['Destination Country Name'] == country]


        for i in range(0,len(months),3):
            quarter = months[i:i+3]
            export_aggregate_by_quarter = export_df.loc[df['Data Month'].isin(quarter)]
            import_aggregate_by_quarter = import_df.loc[df['Data Month'].isin(quarter)]
            aggregate_qauterly_shipments = export_aggregate_by_quarter["Number Shipments"].sum() + import_aggregate_by_quarter["Number Shipments"].sum()
            data.append([f"20{year} Q{(i+3)//3}",country, aggregate_qauterly_shipments])

df = pd.DataFrame(data,columns=["Quarterly","Country","Aggregate Quarterly Shipments"])
    
# print(df)

df.to_csv("C:\ASI_UROP\IATA_Database\CargoIS_Data\ASEAN_quarterly_aggregate.csv")