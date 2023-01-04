
# reading data
ASEAN_2015_Monthly <- read.csv("C:/ASI_UROP/IATA_Database/CargoIS_Data/ASEAN_Shipment_Data/ASEAN_2015_Monthly_Aggregate.csv")
ASEAN_2015_Monthly$Month = factor(ASEAN_2015_Monthly$Month, levels = unique(ASEAN_2015_Monthly$Month))

ASEAN_2016_Monthly <- read.csv("C:/ASI_UROP/IATA_Database/CargoIS_Data/ASEAN_Shipment_Data/ASEAN_2016_Monthly_Aggregate.csv")
ASEAN_2016_Monthly$Month = factor(ASEAN_2016_Monthly$Month, levels = unique(ASEAN_2016_Monthly$Month))

ASEAN_2017_Monthly <- read.csv("C:/ASI_UROP/IATA_Database/CargoIS_Data/ASEAN_Shipment_Data/ASEAN_2017_Monthly_Aggregate.csv")
ASEAN_2017_Monthly$Month = factor(ASEAN_2017_Monthly$Month, levels = unique(ASEAN_2017_Monthly$Month))

ASEAN_2018_Monthly <- read.csv("C:/ASI_UROP/IATA_Database/CargoIS_Data/ASEAN_Shipment_Data/ASEAN_2018_Monthly_Aggregate.csv")
ASEAN_2018_Monthly$Month = factor(ASEAN_2018_Monthly$Month, levels = unique(ASEAN_2018_Monthly$Month))

# plotting
ggplot(ASEAN_2015_Monthly, aes(Month, log10(Shipments)))  + 
  geom_point(aes(group=Country, color=Country)) + 
  geom_line(aes(group=Country, color=Country)) +
  geom_vline(xintercept = "Mar-15", linetype='dotted', size=1) +
  geom_vline(xintercept = "Apr-15", linetype='dotted', size=1) +
  geom_vline(xintercept = "Oct-15", linetype='dotted', size=1) +
  geom_vline(xintercept = "Nov-15", linetype='dotted', size=1) +
  labs(y="Shipments") +
  theme_bw()
  

ggplot(ASEAN_2016_Monthly, aes(Month, (Shipments)))  + 
  geom_point(aes(group=Country, color=Country)) + 
  geom_line(aes(group=Country, color=Country)) +
  geom_vline(xintercept = "Mar-16", linetype='dotted', size=1) +
  geom_vline(xintercept = "Apr-16", linetype='dotted', size=1) +
  geom_vline(xintercept = "Oct-16", linetype='dotted', size=1) +
  geom_vline(xintercept = "Nov-16", linetype='dotted', size=1) +
  labs(y="Shipments") +
  theme_bw()
  


ggplot(ASEAN_2017_Monthly, aes(Month, log10(Shipments)))  + 
  geom_point(aes(group=Country, color=Country)) + 
  geom_line(aes(group=Country, color=Country)) +
  geom_vline(xintercept = "Mar-17", linetype='dotted', size=1) +
  geom_vline(xintercept = "Apr-17", linetype='dotted', size=1) +
  geom_vline(xintercept = "Oct-17", linetype='dotted', size=1) +
  geom_vline(xintercept = "Nov-17", linetype='dotted', size=1) +
  labs(y="Shipments") +
  theme_bw()

ggplot(ASEAN_2018_Monthly, aes(Month, (Shipments)))  + 
  geom_point(aes(group=Country, color=Country)) + 
  geom_line(aes(group=Country, color=Country)) +
  geom_vline(xintercept = "Mar-18", linetype='dotted', size=1) +
  geom_vline(xintercept = "Apr-18", linetype='dotted', size=1) +
  geom_vline(xintercept = "Oct-18", linetype='dotted', size=1) +
  geom_vline(xintercept = "Nov-18", linetype='dotted', size=1) +
  labs(y="Shipments") +
  theme_bw()
