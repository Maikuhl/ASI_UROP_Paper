import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


file_path = f"C:\ASI_UROP\IATA_Database\CargoIS_Data\export_to_singapore.csv"
df = pd.read_csv(file_path)

print(df)

tp = df.T

print(tp)

sns.pairplot(tp)

plt.show()



