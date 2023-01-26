# function for checking and loading required packages
loadPkg <- function(pkgname){
  # require() is the same as library() but returns a logical.
  # character.only= TRUE means pkgname is the name of the package.
  isInstalled <- require(pkgname,character.only = TRUE) 
  # If the package has not been installed yet, then install and try again.
  if (!isInstalled) {install.packages(pkgname); library(pkgname,character.only=TRUE)} 
}


# loading required packages
loadPkg("DBI")
loadPkg("RSQLite")
loadPkg("tidyverse")
loadPkg("leaflet")
loadPkg("htmlwidgets")
library("htmlwidgets")
library("leaflet")
# loadPkg("glue")
# loadPkg("geosphere")
library("htmltools")

# Open an SQLite connection using the filename shown
conn <- dbConnect(RSQLite::SQLite(),"CargoIS_Data/CargoIS_data.db")
# Close the connection.
dbDisconnect(conn)



#Loading Database 

ASEAN2015 <- read_csv("C:/ASI_UROP/IATA_Database/CargoIS_Data/ASEAN_Shipment_Data/ASEAN_Aggregate_Shipments.csv") 

ASEAN2016 <- read_csv("C:/ASI_UROP/IATA_Database/CargoIS_Data/ASEAN_2016_aggregate_imports.csv")

ASEAN2017 <- read_csv("C:/ASI_UROP/IATA_Database/CargoIS_Data/ASEAN_2017_aggregate_imports.csv")

ASEAN2018 <- read_csv("C:/ASI_UROP/IATA_Database/CargoIS_Data/ASEAN_2018_aggregate_imports.csv")


# asean_list <- list(ASEAN2015, ASEAN2016, ASEAN2017, ASEAN2018)
# 
# for (i in asean_list) {
#   
# }

## 2015 Stuff

# initiating variables for 2015 column names 

olat15 = ASEAN2015$origin_latitude 

dlat15 = ASEAN2015$destination_latitude 

olong15 = ASEAN2015$origin_longitude 

dlong15 = ASEAN2015$destination_longitude 

ship15 = ASEAN2015$`Total Shipments` 

dname15 = ASEAN2015$`Destination Country Name` 

wgt15 = ASEAN2015$`Total Weight` 


#Initiate Map object 

m15 = leaflet(data = ASEAN2015) %>% addTiles() 

#Loop to add polyline and circle marker layers 

for (i in 1:10) { 
  
  m15 = m15 %>% 
    
    addPolylines(data = ASEAN2015, lat =c(olat15[i],dlat15[i]), lng =c(olong15[i],dlong15[i]), color = "red", weight = log10(ship15[i])) %>% 
    
    addCircleMarkers(data = ASEAN2015, lat=olat15, lng=olong15, radius=1, color="red", group = "Singapore") %>% 
    
    addCircleMarkers(data = ASEAN2015, lat=dlat15[i], lng=dlong15[i], radius=1, label = ~paste(dname15[i], "<br>Shipments:", ship15[i]) %>% lapply(htmltools::HTML), labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
    
} 

m15 


# saves the map widget as a html file
saveWidget(m15, file="CargoIS_Data/Map_Plots/singapore_exports_all.html")
# 
# 
# ##################################################################################################################################################################
# 
# 
# #Initiate Map object
# 
m15 = leaflet(data = ASEAN2015) %>% addTiles()

#Loop to add polyline and circle marker layers 

for (i in 11:20) { 
  
  m15 = m15 %>% 
    
    addPolylines(data = ASEAN2015, lat =c(olat15[i],dlat15[i]), lng =c(olong15[i],dlong15[i]), color = "orange", weight = log10(ship15[i])) %>% 
    
    addCircleMarkers(data = ASEAN2015, lat=olat15, lng=olong15, radius=1, color="red", group = "Brunei") %>% 
    
    addCircleMarkers(data = ASEAN2015, lat=dlat15[i], lng=dlong15[i], radius=1, label = ~paste(dname15[i], "<br>Shipments:", ship15[i]) %>% lapply(htmltools::HTML), labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
    # addLayersControl(map = m15, overlayGroups = c("Singapore", "Brunei"), options = layersControlOptions(collapsed = FALSE))
} 

m15 


# saves the map widget as a html file
saveWidget(m15, file="CargoIS_Data/Map_Plots/brunei_exports_all.html") 


##################################################################################################################################################################


#Initiate Map object 

m15 = leaflet(data = ASEAN2015) %>% addTiles() 

#Loop to add polyline and circle marker layers 

for (i in 21:30) { 
  
  m15 = m15 %>% 
    
    addPolylines(data = ASEAN2015, lat =c(olat15[i],dlat15[i]), lng =c(olong15[i],dlong15[i]), color = "violet", weight = log10(ship15[i])) %>% 
    
    addCircleMarkers(data = ASEAN2015, lat=olat15, lng=olong15, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2015, lat=dlat15[i], lng=dlong15[i], radius=1, label = ~paste(dname15[i], "<br>Shipments:", ship15[i]) %>% lapply(htmltools::HTML), labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m15 


# saves the map widget as a html file
saveWidget(m15, file="CargoIS_Data/Map_Plots/vietnam_all.html") 


##################################################################################################################################################################

#Initiate Map object 

m15 = leaflet(data = ASEAN2015) %>% addTiles() 

#Loop to add polyline and circle marker layers 

for (i in 31:40) { 
  
  m15 = m15 %>% 
    
    addPolylines(data = ASEAN2015, lat =c(olat15[i],dlat15[i]), lng =c(olong15[i],dlong15[i]), color = "navy", weight = log10(ship15[i])) %>% 
    
    addCircleMarkers(data = ASEAN2015, lat=olat15, lng=olong15, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2015, lat=dlat15[i], lng=dlong15[i], radius=1, label = ~paste(dname15[i], "<br>Shipments:", ship15[i]) %>% lapply(htmltools::HTML), labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m15 


# saves the map widget as a html file
saveWidget(m15, file="CargoIS_Data/Map_Plots/laos_exports_all.html") 


##################################################################################################################################################################

#Initiate Map object 

m15 = leaflet(data = ASEAN2015) %>% addTiles() 

#Loop to add polyline and circle marker layers 

for (i in 41:50) { 
  
  m15 = m15 %>% 
    
    addPolylines(data = ASEAN2015, lat =c(olat15[i],dlat15[i]), lng =c(olong15[i],dlong15[i]), color = "blue", weight = log10(ship15[i])) %>% 
    
    addCircleMarkers(data = ASEAN2015, lat=olat15, lng=olong15, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2015, lat=dlat15[i], lng=dlong15[i], radius=1, label = ~paste(dname15[i], "<br>Shipments:", ship15[i]) %>% lapply(htmltools::HTML), labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m15 


# saves the map widget as a html file
saveWidget(m15, file="CargoIS_Data/Map_Plots/thailand_exports_all.html") 


##################################################################################################################################################################

#Initiate Map object 

m15 = leaflet(data = ASEAN2015) %>% addTiles() 

#Loop to add polyline and circle marker layers 

for (i in 51:60) { 
  
  m15 = m15 %>% 
    
    addPolylines(data = ASEAN2015, lat =c(olat15[i],dlat15[i]), lng =c(olong15[i],dlong15[i]), color = "green", weight = log10(ship15[i])) %>% 
    
    addCircleMarkers(data = ASEAN2015, lat=olat15, lng=olong15, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2015, lat=dlat15[i], lng=dlong15[i], radius=1, label = ~paste(dname15[i], "<br>Shipments:", ship15[i]) %>% lapply(htmltools::HTML), labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m15 


# saves the map widget as a html file
saveWidget(m15, file="CargoIS_Data/Map_Plots/philippines_exports_all.html") 


##################################################################################################################################################################

#Initiate Map object 

m15 = leaflet(data = ASEAN2015) %>% addTiles() 

#Loop to add polyline and circle marker layers 

for (i in 61:70) { 
  
  m15 = m15 %>% 
    
    addPolylines(data = ASEAN2015, lat =c(olat15[i],dlat15[i]), lng =c(olong15[i],dlong15[i]), color = "teal", weight = log10(ship15[i])) %>% 
    
    addCircleMarkers(data = ASEAN2015, lat=olat15, lng=olong15, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2015, lat=dlat15[i], lng=dlong15[i], radius=1, label = ~paste(dname15[i], "<br>Shipments:", ship15[i]) %>% lapply(htmltools::HTML), labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m15 


# saves the map widget as a html file
saveWidget(m15, file="CargoIS_Data/Map_Plots/malaysia_exports_all.html") 


##################################################################################################################################################################


#Initiate Map object 

m15 = leaflet(data = ASEAN2015) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 71:80) { 
  
  m15 = m15 %>% 
    
    addPolylines(data = ASEAN2015, lat =c(olat15[i],dlat15[i]), lng =c(olong15[i],dlong15[i]), color = "brown", weight = log10(ship15[i])) %>% 
    
    addCircleMarkers(data = ASEAN2015, lat=olat15, lng=olong15, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2015, lat=dlat15[i], lng=dlong15[i], radius=1, label = ~paste(dname15[i], "<br>Shipments:", ship15[i]) %>% lapply(htmltools::HTML), labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m15 


# saves the map widget as a html file
saveWidget(m15, file="CargoIS_Data/Map_Plots/indonesia_exports_all.html") 

m15 = leaflet(data = ASEAN2015) %>% addTiles() 


###################################################################################################################################################################

#Initiate Map object 

m15 = leaflet(data = ASEAN2015) %>% addTiles() 

#Loop to add polyline and circle marker layers 

for (i in 81:90) { 
  
  m15 = m15 %>% 
    
    addPolylines(data = ASEAN2015, lat =c(olat15[i],dlat15[i]), lng =c(olong15[i],dlong15[i]), color = "black", weight = log10(ship15[i])) %>% 
    
    addCircleMarkers(data = ASEAN2015, lat=olat15, lng=olong15, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2015, lat=dlat15[i], lng=dlong15[i], radius=1, label = ~paste(dname15[i], "<br>Shipments:", ship15[i]) %>% lapply(htmltools::HTML), labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m15 


# saves the map widget as a html file
saveWidget(m15, file="CargoIS_Data/Map_Plots/cambodia_exports_all.html") 


##################################################################################################################################################################


#Initiate Map object 

m15 = leaflet(data = ASEAN2015) %>% addTiles() 

#Loop to add polyline and circle marker layers 

for (i in 91:100) { 
  
  m15 = m15 %>% 
    
    addPolylines(data = ASEAN2015, lat =c(olat15[i],dlat15[i]), lng =c(olong15[i],dlong15[i]), color = "purple", weight = log10(ship15[i])) %>% 
    
    addCircleMarkers(data = ASEAN2015, lat=olat15, lng=olong15, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2015, lat=dlat15[i], lng=dlong15[i], radius=1, label = ~paste(dname15[i], "<br>Shipments:", ship15[i]) %>% lapply(htmltools::HTML), labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m15 


# saves the map widget as a html file
saveWidget(m15, file="CargoIS_Data/Map_Plots/myanmar_exports_all.html") 


##################################################################################################################################################################


## 2016 Stuff

# initiating variables for 2016 column names 

olat16 = ASEAN2016$origin_latitude 

dlat16 = ASEAN2016$destination_latitude 

olong16 = ASEAN2016$origin_longitude 

dlong16 = ASEAN2016$destination_longitude 

ship16 = ASEAN2016$`Total Shipments` 

dname16 = ASEAN2016$`Destination Country Name` 

wgt16 = ASEAN2016$`Total Weight` 



#Initiate Map object 

m16 = leaflet(data = ASEAN2016) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 1:10) { 
  
  m16 = m16 %>% 
    
    addPolylines(data = ASEAN2016, lat =c(olat16[i],dlat16[i]), lng =c(olong16[i],dlong16[i]), color = "red", weight = log10(ship16[i])) %>% 
    
    addCircleMarkers(data = ASEAN2016, lat=olat16, lng=olong16, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2016, lat=dlat16[i], lng=dlong16[i], radius=1, label = ~dname16[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m16 

saveWidget(m16, file="CargoIS_Data/Map_Plots/2016/singapore_exports_2016.html")

#######################################################################################################################################################################

#Initiate Map object 

m16 = leaflet(data = ASEAN2016) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 11:20) { 
  
  m16 = m16 %>% 
    
    addPolylines(data = ASEAN2016, lat =c(olat16[i],dlat16[i]), lng =c(olong16[i],dlong16[i]), color = "orange", weight = log10(ship16[i])) %>% 
    
    addCircleMarkers(data = ASEAN2016, lat=olat16, lng=olong16, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2016, lat=dlat16[i], lng=dlong16[i], radius=1, label = ~dname16[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m16 

saveWidget(m16, file="CargoIS_Data/Map_Plots/2016/brunei_exports_2016.html")

#######################################################################################################################################################################

#Initiate Map object 

m16 = leaflet(data = ASEAN2016) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 21:30) { 
  
  m16 = m16 %>% 
    
    addPolylines(data = ASEAN2016, lat =c(olat16[i],dlat16[i]), lng =c(olong16[i],dlong16[i]), color = "violet", weight = log10(ship16[i])) %>% 
    
    addCircleMarkers(data = ASEAN2016, lat=olat16, lng=olong16, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2016, lat=dlat16[i], lng=dlong16[i], radius=1, label = ~dname16[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m16 

saveWidget(m16, file="CargoIS_Data/Map_Plots/2016/vietnam_exports_2016.html")

#######################################################################################################################################################################

#Initiate Map object 

m16 = leaflet(data = ASEAN2016) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 31:40) { 
  
  m16 = m16 %>% 
    
    addPolylines(data = ASEAN2016, lat =c(olat16[i],dlat16[i]), lng =c(olong16[i],dlong16[i]), color = "navy", weight = log10(ship16[i])) %>% 
    
    addCircleMarkers(data = ASEAN2016, lat=olat16, lng=olong16, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2016, lat=dlat16[i], lng=dlong16[i], radius=1, label = ~dname16[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m16 

saveWidget(m16, file="CargoIS_Data/Map_Plots/2016/laos_exports_2016.html")

#######################################################################################################################################################################

#Initiate Map object 

m16 = leaflet(data = ASEAN2016) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 41:50) { 
  
  m16 = m16 %>% 
    
    addPolylines(data = ASEAN2016, lat =c(olat16[i],dlat16[i]), lng =c(olong16[i],dlong16[i]), color = "blue", weight = log10(ship16[i])) %>% 
    
    addCircleMarkers(data = ASEAN2016, lat=olat16, lng=olong16, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2016, lat=dlat16[i], lng=dlong16[i], radius=1, label = ~dname16[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m16 

saveWidget(m16, file="CargoIS_Data/Map_Plots/2016/thailand_exports_2016.html")

#######################################################################################################################################################################

#Initiate Map object 

m16 = leaflet(data = ASEAN2016) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 51:60) { 
  
  m16 = m16 %>% 
    
    addPolylines(data = ASEAN2016, lat =c(olat16[i],dlat16[i]), lng =c(olong16[i],dlong16[i]), color = "green", weight = log10(ship16[i])) %>% 
    
    addCircleMarkers(data = ASEAN2016, lat=olat16, lng=olong16, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2016, lat=dlat16[i], lng=dlong16[i], radius=1, label = ~dname16[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m16 

saveWidget(m16, file="CargoIS_Data/Map_Plots/2016/philippines_exports_2016.html")

#######################################################################################################################################################################

#Initiate Map object 

m16 = leaflet(data = ASEAN2016) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 61:70) { 
  
  m16 = m16 %>% 
    
    addPolylines(data = ASEAN2016, lat =c(olat16[i],dlat16[i]), lng =c(olong16[i],dlong16[i]), color = "teal", weight = log10(ship16[i])) %>% 
    
    addCircleMarkers(data = ASEAN2016, lat=olat16, lng=olong16, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2016, lat=dlat16[i], lng=dlong16[i], radius=1, label = ~dname16[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m16 

saveWidget(m16, file="CargoIS_Data/Map_Plots/2016/malaysia_exports_2016.html")

#######################################################################################################################################################################

#Initiate Map object 

m16 = leaflet(data = ASEAN2016) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 71:80) { 
  
  m16 = m16 %>% 
    
    addPolylines(data = ASEAN2016, lat =c(olat16[i],dlat16[i]), lng =c(olong16[i],dlong16[i]), color = "brown", weight = log10(ship16[i])) %>% 
    
    addCircleMarkers(data = ASEAN2016, lat=olat16, lng=olong16, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2016, lat=dlat16[i], lng=dlong16[i], radius=1, label = ~dname16[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m16 

saveWidget(m16, file="CargoIS_Data/Map_Plots/2016/indonesia_exports_2016.html")

#######################################################################################################################################################################

#Initiate Map object 

m16 = leaflet(data = ASEAN2016) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 81:90) { 
  
  m16 = m16 %>% 
    
    addPolylines(data = ASEAN2016, lat =c(olat16[i],dlat16[i]), lng =c(olong16[i],dlong16[i]), color = "black", weight = log10(ship16[i])) %>% 
    
    addCircleMarkers(data = ASEAN2016, lat=olat16, lng=olong16, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2016, lat=dlat16[i], lng=dlong16[i], radius=1, label = ~dname16[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m16 

saveWidget(m16, file="CargoIS_Data/Map_Plots/2016/cambodia_exports_2016.html")

#######################################################################################################################################################################

#Initiate Map object 

m16 = leaflet(data = ASEAN2016) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 91:100) { 
  
  m16 = m16 %>% 
    
    addPolylines(data = ASEAN2016, lat =c(olat16[i],dlat16[i]), lng =c(olong16[i],dlong16[i]), color = "purple", weight = log10(ship16[i])) %>% 
    
    addCircleMarkers(data = ASEAN2016, lat=olat16, lng=olong16, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2016, lat=dlat16[i], lng=dlong16[i], radius=1, label = ~dname16[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m16 

saveWidget(m16, file="CargoIS_Data/Map_Plots/2016/myanmar_exports_2016.html")

#######################################################################################################################################################################


## 2017 Stuff

# initiating variables for 2017 column names 

olat17 = ASEAN2017$origin_latitude 

dlat17 = ASEAN2017$destination_latitude 

olong17 = ASEAN2017$origin_longitude 

dlong17 = ASEAN2017$destination_longitude 

ship17 = ASEAN2017$`Total Shipments` 

dname17 = ASEAN2017$`Destination Country Name` 

wgt17 = ASEAN2017$`Total Weight` 



#Initiate Map object 

m17 = leaflet(data = ASEAN2017) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 1:10) { 
  
  m17 = m17 %>% 
    
    addPolylines(data = ASEAN2017, lat =c(olat17[i],dlat17[i]), lng =c(olong17[i],dlong17[i]), color = "red", weight = log10(ship17[i])) %>% 
    
    addCircleMarkers(data = ASEAN2017, lat=olat17, lng=olong17, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2017, lat=dlat17[i], lng=dlong17[i], radius=1, label = ~dname17[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m17

saveWidget(m17, file="CargoIS_Data/Map_Plots/2017/singapore_exports_2017.html")

##################################################################################################################################################################################

#Initiate Map object 

m17 = leaflet(data = ASEAN2017) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 11:20) { 
  
  m17 = m17 %>% 
    
    addPolylines(data = ASEAN2017, lat =c(olat17[i],dlat17[i]), lng =c(olong17[i],dlong17[i]), color = "orange", weight = log10(ship17[i])) %>% 
    
    addCircleMarkers(data = ASEAN2017, lat=olat17, lng=olong17, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2017, lat=dlat17[i], lng=dlong17[i], radius=1, label = ~dname17[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m17

saveWidget(m17, file="CargoIS_Data/Map_Plots/2017/brunei_exports_2017.html")

##################################################################################################################################################################################

#Initiate Map object 

m17 = leaflet(data = ASEAN2017) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 21:30) { 
  
  m17 = m17 %>% 
    
    addPolylines(data = ASEAN2017, lat =c(olat17[i],dlat17[i]), lng =c(olong17[i],dlong17[i]), color = "violet", weight = log10(ship17[i])) %>% 
    
    addCircleMarkers(data = ASEAN2017, lat=olat17, lng=olong17, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2017, lat=dlat17[i], lng=dlong17[i], radius=1, label = ~dname17[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m17

saveWidget(m17, file="CargoIS_Data/Map_Plots/2017/vietnam_exports_2017.html")

##################################################################################################################################################################################

#Initiate Map object 

m17 = leaflet(data = ASEAN2017) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 31:40) { 
  
  m17 = m17 %>% 
    
    addPolylines(data = ASEAN2017, lat =c(olat17[i],dlat17[i]), lng =c(olong17[i],dlong17[i]), color = "navy", weight = log10(ship17[i])) %>% 
    
    addCircleMarkers(data = ASEAN2017, lat=olat17, lng=olong17, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2017, lat=dlat17[i], lng=dlong17[i], radius=1, label = ~dname17[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m17

saveWidget(m17, file="CargoIS_Data/Map_Plots/2017/laos_exports_2017.html")

##################################################################################################################################################################################

#Initiate Map object 

m17 = leaflet(data = ASEAN2017) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 41:50) { 
  
  m17 = m17 %>% 
    
    addPolylines(data = ASEAN2017, lat =c(olat17[i],dlat17[i]), lng =c(olong17[i],dlong17[i]), color = "blue", weight = log10(ship17[i])) %>% 
    
    addCircleMarkers(data = ASEAN2017, lat=olat17, lng=olong17, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2017, lat=dlat17[i], lng=dlong17[i], radius=1, label = ~dname17[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m17

saveWidget(m17, file="CargoIS_Data/Map_Plots/2017/thailand_exports_2017.html")

##################################################################################################################################################################################

#Initiate Map object 

m17 = leaflet(data = ASEAN2017) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 51:60) { 
  
  m17 = m17 %>% 
    
    addPolylines(data = ASEAN2017, lat =c(olat17[i],dlat17[i]), lng =c(olong17[i],dlong17[i]), color = "green", weight = log10(ship17[i])) %>% 
    
    addCircleMarkers(data = ASEAN2017, lat=olat17, lng=olong17, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2017, lat=dlat17[i], lng=dlong17[i], radius=1, label = ~dname17[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m17

saveWidget(m17, file="CargoIS_Data/Map_Plots/2017/philippines_exports_2017.html")

##################################################################################################################################################################################

#Initiate Map object 

m17 = leaflet(data = ASEAN2017) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 61:70) { 
  
  m17 = m17 %>% 
    
    addPolylines(data = ASEAN2017, lat =c(olat17[i],dlat17[i]), lng =c(olong17[i],dlong17[i]), color = "teal", weight = log10(ship17[i])) %>% 
    
    addCircleMarkers(data = ASEAN2017, lat=olat17, lng=olong17, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2017, lat=dlat17[i], lng=dlong17[i], radius=1, label = ~dname17[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m17

saveWidget(m17, file="CargoIS_Data/Map_Plots/2017/malaysia_exports_2017.html")

##################################################################################################################################################################################

#Initiate Map object 

m17 = leaflet(data = ASEAN2017) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 71:80) { 
  
  m17 = m17 %>% 
    
    addPolylines(data = ASEAN2017, lat =c(olat17[i],dlat17[i]), lng =c(olong17[i],dlong17[i]), color = "brown", weight = log10(ship17[i])) %>% 
    
    addCircleMarkers(data = ASEAN2017, lat=olat17, lng=olong17, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2017, lat=dlat17[i], lng=dlong17[i], radius=1, label = ~dname17[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m17

saveWidget(m17, file="CargoIS_Data/Map_Plots/2017/indonesia_exports_2017.html")

##################################################################################################################################################################################

#Initiate Map object 

m17 = leaflet(data = ASEAN2017) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 81:90) { 
  
  m17 = m17 %>% 
    
    addPolylines(data = ASEAN2017, lat =c(olat17[i],dlat17[i]), lng =c(olong17[i],dlong17[i]), color = "black", weight = log10(ship17[i])) %>% 
    
    addCircleMarkers(data = ASEAN2017, lat=olat17, lng=olong17, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2017, lat=dlat17[i], lng=dlong17[i], radius=1, label = ~dname17[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m17

saveWidget(m17, file="CargoIS_Data/Map_Plots/2017/cambodia_exports_2017.html")

##################################################################################################################################################################################

#Initiate Map object 

m17 = leaflet(data = ASEAN2017) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 91:100) { 
  
  m17 = m17 %>% 
    
    addPolylines(data = ASEAN2017, lat =c(olat17[i],dlat17[i]), lng =c(olong17[i],dlong17[i]), color = "purple", weight = log10(ship17[i])) %>% 
    
    addCircleMarkers(data = ASEAN2017, lat=olat17, lng=olong17, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2017, lat=dlat17[i], lng=dlong17[i], radius=1, label = ~dname17[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m17

saveWidget(m17, file="CargoIS_Data/Map_Plots/2017/myanmar_exports_2017.html")

##################################################################################################################################################################################



## 2018 Stuff

# initiating variables for 2018 column names 

olat18 = ASEAN2018$origin_latitude 

dlat18 = ASEAN2018$destination_latitude 

olong18 = ASEAN2018$origin_longitude 

dlong18 = ASEAN2018$destination_longitude 

ship18 = ASEAN2018$`Total Shipments` 

dname18 = ASEAN2018$`Destination Country Name` 

wgt18 = ASEAN2018$`Total Weight` 



#Initiate Map object 

m18 = leaflet(data = ASEAN2018) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 1:10) { 
  
  m18 = m18 %>% 
    
    addPolylines(data = ASEAN2018, lat =c(olat18[i],dlat18[i]), lng =c(olong18[i],dlong18[i]), color = "red", weight = log10(ship18[i])) %>% 
    
    addCircleMarkers(data = ASEAN2018, lat=olat18, lng=olong18, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2018, lat=dlat18[i], lng=dlong18[i], radius=1, label = ~dname18[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m18 

saveWidget(m18, file="CargoIS_Data/Map_Plots/2018/singapore_exports_2018.html")

################################################################################################################################################################################

#Initiate Map object 

m18 = leaflet(data = ASEAN2018) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 11:20) { 
  
  m18 = m18 %>% 
    
    addPolylines(data = ASEAN2018, lat =c(olat18[i],dlat18[i]), lng =c(olong18[i],dlong18[i]), color = "orange", weight = log10(ship18[i])) %>% 
    
    addCircleMarkers(data = ASEAN2018, lat=olat18, lng=olong18, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2018, lat=dlat18[i], lng=dlong18[i], radius=1, label = ~dname18[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m18 

saveWidget(m18, file="CargoIS_Data/Map_Plots/2018/brunei_exports_2018.html")

################################################################################################################################################################################

#Initiate Map object 

m18 = leaflet(data = ASEAN2018) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 21:30) { 
  
  m18 = m18 %>% 
    
    addPolylines(data = ASEAN2018, lat =c(olat18[i],dlat18[i]), lng =c(olong18[i],dlong18[i]), color = "violet", weight = log10(ship18[i])) %>% 
    
    addCircleMarkers(data = ASEAN2018, lat=olat18, lng=olong18, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2018, lat=dlat18[i], lng=dlong18[i], radius=1, label = ~dname18[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m18 

saveWidget(m18, file="CargoIS_Data/Map_Plots/2018/vietnam_exports_2018.html")

################################################################################################################################################################################

#Initiate Map object 

m18 = leaflet(data = ASEAN2018) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 31:40) { 
  
  m18 = m18 %>% 
    
    addPolylines(data = ASEAN2018, lat =c(olat18[i],dlat18[i]), lng =c(olong18[i],dlong18[i]), color = "navy", weight = log10(ship18[i])) %>% 
    
    addCircleMarkers(data = ASEAN2018, lat=olat18, lng=olong18, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2018, lat=dlat18[i], lng=dlong18[i], radius=1, label = ~dname18[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m18 

saveWidget(m18, file="CargoIS_Data/Map_Plots/2018/laos_exports_2018.html")

################################################################################################################################################################################

#Initiate Map object 

m18 = leaflet(data = ASEAN2018) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 41:50) { 
  
  m18 = m18 %>% 
    
    addPolylines(data = ASEAN2018, lat =c(olat18[i],dlat18[i]), lng =c(olong18[i],dlong18[i]), color = "blue", weight = log10(ship18[i])) %>% 
    
    addCircleMarkers(data = ASEAN2018, lat=olat18, lng=olong18, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2018, lat=dlat18[i], lng=dlong18[i], radius=1, label = ~dname18[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m18 

saveWidget(m18, file="CargoIS_Data/Map_Plots/2018/thailand_exports_2018.html")

################################################################################################################################################################################

#Initiate Map object 

m18 = leaflet(data = ASEAN2018) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 51:60) { 
  
  m18 = m18 %>% 
    
    addPolylines(data = ASEAN2018, lat =c(olat18[i],dlat18[i]), lng =c(olong18[i],dlong18[i]), color = "green", weight = log10(ship18[i])) %>% 
    
    addCircleMarkers(data = ASEAN2018, lat=olat18, lng=olong18, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2018, lat=dlat18[i], lng=dlong18[i], radius=1, label = ~dname18[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m18 

saveWidget(m18, file="CargoIS_Data/Map_Plots/2018/philippines_exports_2018.html")

################################################################################################################################################################################

#Initiate Map object 

m18 = leaflet(data = ASEAN2018) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 61:70) { 
  
  m18 = m18 %>% 
    
    addPolylines(data = ASEAN2018, lat =c(olat18[i],dlat18[i]), lng =c(olong18[i],dlong18[i]), color = "teal", weight = log10(ship18[i])) %>% 
    
    addCircleMarkers(data = ASEAN2018, lat=olat18, lng=olong18, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2018, lat=dlat18[i], lng=dlong18[i], radius=1, label = ~dname18[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m18 

saveWidget(m18, file="CargoIS_Data/Map_Plots/2018/malaysia_exports_2018.html")

################################################################################################################################################################################

#Initiate Map object 

m18 = leaflet(data = ASEAN2018) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 71:80) { 
  
  m18 = m18 %>% 
    
    addPolylines(data = ASEAN2018, lat =c(olat18[i],dlat18[i]), lng =c(olong18[i],dlong18[i]), color = "brown", weight = log10(ship18[i])) %>% 
    
    addCircleMarkers(data = ASEAN2018, lat=olat18, lng=olong18, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2018, lat=dlat18[i], lng=dlong18[i], radius=1, label = ~dname18[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m18 

saveWidget(m18, file="CargoIS_Data/Map_Plots/2018/indonesia_exports_2018.html")

################################################################################################################################################################################

#Initiate Map object 

m18 = leaflet(data = ASEAN2018) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 81:90) { 
  
  m18 = m18 %>% 
    
    addPolylines(data = ASEAN2018, lat =c(olat18[i],dlat18[i]), lng =c(olong18[i],dlong18[i]), color = "black", weight = log10(ship18[i])) %>% 
    
    addCircleMarkers(data = ASEAN2018, lat=olat18, lng=olong18, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2018, lat=dlat18[i], lng=dlong18[i], radius=1, label = ~dname18[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m18 

saveWidget(m18, file="CargoIS_Data/Map_Plots/2018/cambodia_exports_2018.html")

################################################################################################################################################################################

#Initiate Map object 

m18 = leaflet(data = ASEAN2018) %>% addTiles() 


#Loop to add polyline and circle marker layers 

for (i in 91:100) { 
  
  m18 = m18 %>% 
    
    addPolylines(data = ASEAN2018, lat =c(olat18[i],dlat18[i]), lng =c(olong18[i],dlong18[i]), color = "purple", weight = log10(ship18[i])) %>% 
    
    addCircleMarkers(data = ASEAN2018, lat=olat18, lng=olong18, radius=1, color="red") %>% 
    
    addCircleMarkers(data = ASEAN2018, lat=dlat18[i], lng=dlong18[i], radius=1, label = ~dname18[i], labelOptions = labelOptions(noHide = TRUE, textOnly = FALSE)) 
  
} 

m18 

saveWidget(m18, file="CargoIS_Data/Map_Plots/2018/myanmar_exports_2018.html")

################################################################################################################################################################################





