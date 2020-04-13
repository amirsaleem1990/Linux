for (package in c(
	"DBI",
	"plyr",
	"ggplot2",
	"h2o",
	"IRkernel",
	"knitr",
	"lubridate",
	"MASS",
	"mice", 
	"polynom",
	"purrr",
	"ranger",
	"rpart",
	"RSQLite",
	"shiny",
	"rpart.plot",
	"xlsx", 
	"XML", 
	"funModeling",  
	"tidyverse",  
	"Hmisc", 
	"dplyr", 
	"tidyverse", 
	"caret",
	"swirl"
	)){
	install.packages(package)
	readline("Enter any key to install next package")
}

#library(swirl)
# install_from_swirl("R_Programming")
# install_course("Getting and Cleaning Data")
# install_course("Exploratory Data Analysis")
