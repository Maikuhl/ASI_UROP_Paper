# function for checking and loading required packages
loadPkg <- function(pkgname){
  # require() is the same as library() but returns a logical.
  # character.only= TRUE means pkgname is the name of the package.
  isInstalled <- require(pkgname,character.only = TRUE) 
  # If the package has not been installed yet, then install and try again.
  if (!isInstalled) {install.packages(pkgname); library(pkgname,character.only=TRUE)} 
}

# We will need the following libraries 
loadPkg("DBI")
loadPkg("RSQLite")

# Open an SQLite connection using the filename shown
conn <- dbConnect(RSQLite::SQLite(),"CargoIS_Data/CargoIS_data.db")
# Close the connection.
dbDisconnect(conn)

sgexports <- read.csv("CargoIS_Data/export_to_singapore.csv")

colors <- c('black', 'red')[unclass(Indonesia)]

pairs(sgexports, )