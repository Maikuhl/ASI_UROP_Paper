# Forecasting Air Cargo Demand for Southeast Asia

Project report was collaborated on [Overleaf](https://www.overleaf.com/), an online LaTeX editor for real-time collaboration. 
LaTeX source files are stored and updated in this repository to keep track of revisions. 

This project fulfills the requirements of a UROP under SUTD, in collaboration with the [Aviation Studies Institute](https://asi.sutd.edu.sg/) and the [International Air Transport Association](https://www.iata.org/) [IATA].

Open-source macroeconomic data was used in this project, and air cargo data was obtained via IATA's CargoIS platform. More details can be found in the final report.

> R and SQL scripts for data wrangling can be found under *IATA_Database* folder. Graphs were created in R via ggplot, while the data was queried via SQL and cleaned with Pandas in Python. Original datasets were provided in .CSV format.

> Scripts for data wrangling in Python can be found under *Python_Fun* folder.

> Final Report in pdf can be found under *Final Report* folder.

# Examples of Graphs Produced

## Map Plots 

Used Google's open-source dspl dataset for geospatial coordinates of each country. Plotted in R via Leaflet. Original source file was an interactive html file, saved as a png to include in the final report. 

![Singapore_Map](https://github.com/Maikuhl/ASI_UROP_Paper/blob/main/Images_Used/Map_Plots/All/Singapore_Exports.png)

## Interactive Radar Plots

Used Plotly's Scatterpolar function in Python to produce radar plots for the imports exports of each country. Raw image exported in interactive html files, converted to png for display in report. 

![Plotly_Singapore](https://github.com/Maikuhl/ASI_UROP_Paper/blob/main/Images_Used/Interactive_Radar_Plots/Images/Singapore_Radar.png)

## Line Plots

Line Plots were generated in R via the ggplot library, displaying each country's total shipment activity.

![Line_Plot](https://github.com/Maikuhl/ASI_UROP_Paper/blob/main/Images_Used/Quarterly_Data/Line%20Plots%20ASEAN%20Shipments/ASEAN_Large_Quarterly_Shipments2.png)

## Correlation Plots

Pair plots were generated in R via the ggpairs library, displaying the relationship between bivariate data (GDP in this case). Plots along the diagonal represent the KDE plots of each variable. 

![Corrplot](https://github.com/Maikuhl/ASI_UROP_Paper/blob/main/Images_Used/Quarterly_Data/CorrPlots/Singapore_Corrplot.png)


