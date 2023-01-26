# package installation
install.packages("ggplot2")
install.packages("GGally")
install.packages("readr")
install.packages("plotly")
install.packages("gapminder")
install.packages("tidyverse")

# loading required packages
library("ggplot2")
library("GGally")
library("readr")
library("xts")
library("zoo")
library("tidyverse")
library("plotly")
library("gapminder")

#reading data for individual country
sg_gdp_quarter <- read.csv("C:/ASI_UROP/IATA_Database/CargoIS_Data/Quarterly_Data/Macroeconomic/SG_GDP_Quarter.csv")
sg_gdp_quarter <- sg_gdp_quarter %>% remove_rownames %>% column_to_rownames(var="Quarter")

in_gdp_quarter <- read.csv("C:/ASI_UROP/IATA_Database/CargoIS_Data/Quarterly_Data/Total_Imports_Exports_Quarterly/Indonesia_quarterly_aggregate_shipments.csv")

my_gdp_quarter <- read.csv("C:/ASI_UROP/IATA_Database/CargoIS_Data/Quarterly_Data/Total_Imports_Exports_Quarterly/Malaysia_quarterly_aggregate_shipments.csv")

ph_gdp_quarter <- read.csv("C:/ASI_UROP/IATA_Database/CargoIS_Data/Quarterly_Data/Macroeconomic/PH_GDP_Quarter.csv")

th_gdp_quarter <- read.csv("C:/ASI_UROP/IATA_Database/CargoIS_Data/Quarterly_Data/Macroeconomic/Thai_GDP_Quarter.csv")

vn_gdp_quarter <- read.csv("C:/ASI_UROP/IATA_Database/CargoIS_Data/Total_Imports_Exports_Quarterly/Viet_Nam_quarterly_aggregate_shipments.csv")

bn_gdp_quarter <- read.csv("C:/ASI_UROP/IATA_Database/CargoIS_Data/Quarterly_Data/Total_Imports_Exports_Quarterly/Brunei_quarterly_aggregate_shipments.csv")

cam_gdp_quarter <- read.csv("C:/ASI_UROP/IATA_Database/CargoIS_Data/Total_Imports_Exports_Quarterly/Cambodia_quarterly_aggregate_shipments.csv")

lao_gdp_quarter <- read.csv("C:/ASI_UROP/IATA_Database/CargoIS_Data/Total_Imports_Exports_Quarterly/Lao_quarterly_aggregate_shipments.csv")

mm_gdp_quarter <- read.csv("C:/ASI_UROP/IATA_Database/CargoIS_Data/Total_Imports_Exports_Quarterly/Myanmar_quarterly_aggregate_shipments.csv")


# reading data for country aggregates
ASEAN_shipment_quarter_small <- read.csv("C:/ASI_UROP/IATA_Database/CargoIS_Data/Total_Imports_Exports_Quarterly/ASEAN_quarterly_aggregate_shipments_small.csv")

ASEAN_shipment_quarter_large <- read.csv("C:/ASI_UROP/IATA_Database/CargoIS_Data/Total_Imports_Exports_Quarterly/ASEAN_quarterly_aggregate_shipments_large.csv")


#, header = TRUE, row.names = "Quarter"

# formatting data for quarter
sg_gdp_quarter$Quarterly <- as.yearqtr(sg_gdp_quarter$Quarter, format = "%Y Q%q")

# correlation analysis
cor.test(x=th_gdp_quarter$GDP, y=th_gdp_quarter$Shipments, method = "pearson")
pairs(coredata(sg_gdp_quarter))

#pair plot of gdp and shipments of sg
ggpairs(sg_gdp_quarter, cardinality_threshold = NULL) + theme_bw()

# quarter-gdp plot of sg
ggplot(sg_gdp_quarter, aes(Quarterly, Aggregate.Quarterly.Shipments)) +geom_point() + geom_line() + theme_bw() + labs(x="Quarter", y="Total Imports & Exports (Shipments)") # +geom_smooth(color='red') 

# quarter-shipments plot of sg
ggplot(sg_gdp_quarter, aes(Quarterly)) + geom_point(aes(y=sg_my_gdp_quarter$Singapore, color="Singapore"))+ geom_point(aes(y=sg_my_gdp_quarter$Malaysia, color="Malaysia")) + geom_line(aes(y=sg_my_gdp_quarter$Malaysia, color="Malaysia")) + geom_line(aes(y=sg_my_gdp_quarter$Singapore, color="Singapore")) # + geom_smooth(method="lm", color='red') + theme_bw()

# quarter-shipments plot of ph
ph_gdp_quarter$X.Quarter <- as.yearqtr(ph_gdp_quarter$X.Quarter, format = "%Y Q%q")
ggplot(ph_gdp_quarter, aes(X.Quarter)) + 
  geom_point(aes(y=ph_gdp_quarter$ImportsExports)) + 
  geom_line(aes(y=ph_gdp_quarter$ImportsExports)) + 
  theme_bw() + 
  labs(x="Quarter", y="Total Imports & Exports (Shipments)")

# quarter-gdp plot of ph
ph_gdp_quarter$X.Quarter <- as.yearqtr(ph_gdp_quarter$X.Quarter, format = "%Y Q%q")
ggplot(ph_gdp_quarter, aes(X.Quarter)) + 
  geom_point(aes(y=ph_gdp_quarter$GDP)) + 
  geom_line(aes(y=ph_gdp_quarter$GDP)) + 
  theme_bw() + 
  labs(x="Quarter", y="GDP (in Billions of Pesos)")

# quarter-shipments plot of th
th_gdp_quarter$Quarter <- as.yearqtr(th_gdp_quarter$Quarter, format = "%Y Q%q")
ggplot(th_gdp_quarter, aes(Quarter)) + 
  geom_point(aes(y=th_gdp_quarter$Shipments)) + 
  geom_line(aes(y=th_gdp_quarter$Shipments)) + 
  theme_bw() + 
  labs(x="Quarter", y="Total Imports & Exports (Shipments)")

# quarter-gdp plot of th
th_gdp_quarter$Quarter <- as.yearqtr(th_gdp_quarter$Quarter, format = "%Y Q%q")
ggplot(th_gdp_quarter, aes(x=Quarter)) + 
  geom_point(aes(y=th_gdp_quarter$GDP)) + 
  geom_line(aes(y=th_gdp_quarter$GDP)) + 
  theme_bw() + 
  labs(x="Quarter", y="GDP (in Billions of Baht)")

# quarter-shipments plot of my
my_gdp_quarter$Quarter <- as.yearqtr(my_gdp_quarter$Quarter, format = "%Y Q%q")
ggplot(my_gdp_quarter, aes(Quarter)) + 
  geom_point(aes(y=my_gdp_quarter$Shipments)) + 
  geom_line(aes(y=my_gdp_quarter$Shipments)) + 
  theme_bw() + 
  labs(x="Quarter", y="Total Imports & Exports (Shipments)")

# quarter-gdp plot of my
my_gdp_quarter$Quarter <- as.yearqtr(my_gdp_quarter$Quarter, format = "%Y Q%q")
ggplot(my_gdp_quarter, aes(x=Quarter)) + 
  geom_point(aes(y=my_gdp_quarter$GDPB)) + 
  geom_line(aes(y=my_gdp_quarter$GDPB)) + 
  theme_bw() + 
  labs(x="Quarter", y="GDP (in Billions of RM)")

# quarter-shipments plot of in
in_gdp_quarter$Quarterly <- as.yearqtr(in_gdp_quarter$Quarterly, format = "%Y Q%q")
ggplot(in_gdp_quarter, aes(Quarterly)) + 
  geom_point(aes(y=in_gdp_quarter$Shipments)) + 
  geom_line(aes(y=in_gdp_quarter$Shipments)) + 
  theme_bw() + 
  labs(x="Quarter", y="Total Imports & Exports (Shipments)")

# quarter-gdp plot of in
my_gdp_quarter$Quarter <- as.yearqtr(my_gdp_quarter$Quarter, format = "%Y Q%q")
ggplot(my_gdp_quarter, aes(x=Quarter)) + 
  geom_point(aes(y=my_gdp_quarter$GDPB)) + 
  geom_line(aes(y=my_gdp_quarter$GDPB)) + 
  theme_bw() + 
  labs(x="Quarter", y="GDP (in Billions of RM)")

# quarter-shipments plot of bn
bn_gdp_quarter$Quarterly <- as.yearqtr(bn_gdp_quarter$Quarterly, format = "%Y Q%q")
ggplot(bn_gdp_quarter, aes(Quarterly)) + 
  geom_point(aes(y=bn_gdp_quarter$Shipments)) + 
  geom_line(aes(y=bn_gdp_quarter$Shipments)) + 
  theme_bw() + 
  labs(x="Quarter", y="Total Imports & Exports (Shipments)")

# quarter-gdp plot of bn
bn_gdp_quarter$Quarter <- as.yearqtr(bn_gdp_quarter$Quarterly, format = "%Y Q%q")
ggplot(bn_gdp_quarter, aes(x=Quarterly)) + 
  geom_point(aes(y=bn_gdp_quarter$GDP)) + 
  geom_line(aes(y=bn_gdp_quarter$GDP)) + 
  theme_bw() + 
  labs(x="Quarter", y="GDP (in Millions of BND)")

# plot of shipments for smaller countries
ASEAN_shipment_quarter_small$Quarter <- as.yearqtr(ASEAN_shipment_quarter_small$Quarter, format = "%Y Q%q")
ggplot(ASEAN_shipment_quarter_small, aes=(x=Quarter)) + 
  geom_point(aes(x=Quarter, y=`Brunei`, color="Brunei")) + 
  geom_point(aes(x=Quarter,y=`Cambodia`, color= "Cambodia")) + 
  geom_point(aes(x=Quarter,y=`Lao`, color= "Laos")) + 
  geom_point(aes(x=Quarter,y=`Myanmar`, color= "Myanmar")) + 
  geom_line(aes(x=Quarter,y=`Brunei`, color="Brunei")) + 
  geom_line(aes(x=Quarter,y=`Cambodia`, color= "Cambodia")) + 
  geom_line(aes(x=Quarter,y=`Lao`, color= "Laos")) + 
  geom_line(aes(x=Quarter,y=`Myanmar`, color= "Myanmar")) +
  labs(y="Total Imports & Exports (Shipments)", x = "Quarter", color= "Country") +
  theme_bw()

# plot of shipments for larger countries
ASEAN_shipment_quarter_large$Quarter <- as.yearqtr(ASEAN_shipment_quarter_large$Quarter, format = "%Y Q%q")
ggplot(ASEAN_shipment_quarter_large, aes=(x=Quarter)) + 
  geom_point(aes(x=Quarter, y=`Singapore`, color="Singapore")) + 
  geom_point(aes(x=Quarter,y=`Indonesia`, color= "Indonesia")) + 
  geom_point(aes(x=Quarter,y=`Malaysia`, color= "Malaysia")) + 
  geom_point(aes(x=Quarter,y=`Philippines`, color= "Philippines")) + 
  geom_point(aes(x=Quarter,y=`Thailand`, color= "Thailand")) +
  geom_point(aes(x=Quarter,y=`Vietnam`, color= "Vietnam")) +
  geom_line(aes(x=Quarter, y=`Singapore`, color="Singapore")) + 
  geom_line(aes(x=Quarter,y=`Indonesia`, color= "Indonesia")) + 
  geom_line(aes(x=Quarter,y=`Malaysia`, color= "Malaysia")) + 
  geom_line(aes(x=Quarter,y=`Philippines`, color= "Philippines")) + 
  geom_line(aes(x=Quarter,y=`Thailand`, color= "Thailand")) +
  geom_line(aes(x=Quarter,y=`Vietnam`, color= "Vietnam")) +
  labs(y="Total Imports & Exports (Shipments)", x = "Quarter", color= "Country") +
  theme_bw()


#pair plot of gdp and shipments

ggpairs(sg_gdp_quarter, cardinality_threshold = NULL) + theme_bw()

bn_gdp_quarter <- bn_gdp_quarter %>% remove_rownames %>% column_to_rownames(var="Quarter")
bn_gdp_quarter <- bn_gdp_quarter[,c(2,1)]
ggpairs(bn_gdp_quarter, cardinality_threshold = NULL) + theme_bw()

in_gdp_quarter <- in_gdp_quarter %>% remove_rownames %>% column_to_rownames(var="Quarter")
ggpairs(in_gdp_quarter, cardinality_threshold = NULL) + theme_bw()

ph_gdp_quarter <- ph_gdp_quarter %>% remove_rownames %>% column_to_rownames(var="X.Quarter")
ggpairs(ph_gdp_quarter, cardinality_threshold = NULL) + theme_bw()

my_gdp_quarter <- my_gdp_quarter %>% remove_rownames %>% column_to_rownames(var="Quarter")
my_gdp_quarter <- my_gdp_quarter[,c(2,1)]
ggpairs(my_gdp_quarter, cardinality_threshold = NULL) + theme_bw()

th_gdp_quarter <- th_gdp_quarter %>% remove_rownames %>% column_to_rownames(var="Quarter")
ggpairs(th_gdp_quarter, cardinality_threshold = NULL) + theme_bw()

  
