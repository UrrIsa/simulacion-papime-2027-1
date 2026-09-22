# 1c : Basic operations
#--------------------------------------------------------

import os
import pandas as pd
import numpy as np

# Retrieves the working directory, to know where I will save the file
os.getcwd()
#os.chdir("/Users/tu_usuario/Desktop") # An example. The 'os.chdir' is used to change the current working directory
os.chdir("/home/urrisaac/Profesional/GIT/")

Flights_ex = pd.read_csv("1c flights.csv")

# 1. Data frames
Flights_ex.info() # Structures the data frame. - NOTE: several numbers are read as characters
type(Flights_ex)
print(Flights_ex["id_ciss"])
print(Flights_ex["id_ciss"].dtype)
print(Flights_ex["aircraft_category"].dtype)
print(Flights_ex["actual_block_time"].dtype)

# Some columns are classified as text while they should be time-data!

Flights_ex["scheduled_datetime"] = pd.to_datetime(Flights_ex["scheduled_datetime"] )
Flights_ex["actual_block_time"] = pd.to_datetime(Flights_ex["actual_block_time"] )
Flights_ex["actual_landing_time"] = pd.to_datetime(Flights_ex["actual_landing_time"] )
Flights_ex["actual_take_off_time"] = pd.to_datetime(Flights_ex["actual_take_off_time"] )

Flights_ex["actual_take_off_time"] - Flights_ex["actual_block_time"]


# 2. How to select rows by condition?

# A. All 737 aircraft
Flights_ex["aircraft_iata_main"].unique()
#print(Flights_ex["aircraft_iata_main"].unique())
TOTAL_737 = Flights_ex[Flights_ex["aircraft_iata_main"] == "737"]
TOTAL_787 = Flights_ex[Flights_ex["aircraft_iata_main"] == "787"]
TOTAL_220 = Flights_ex[Flights_ex["aircraft_iata_main"] == "220"]
TOTAL_737787 = Flights_ex[(Flights_ex["aircraft_iata_main"] == "737") | (Flights_ex["aircraft_iata_main"] == "787")]
TOTAL_737787 = Flights_ex[Flights_ex["aircraft_iata_main"].isin(["737","787"])]

# Delete all flights that do no have the actual block time registered
Flights_ex = Flights_ex[Flights_ex["actual_block_time"].notna()].copy()
#print(Flights_ex)
# Flights_ex = Flights_ex.loc[Flights_ex["actual_block_time"].notna(), Flights_ex.columns[[0,6,7,8]]]   #Select some columns


# Separate arrivals and departures
Flights_ex_A = Flights_ex[Flights_ex["flight_direction"] == "A"].reset_index(drop=True)
Flights_ex_D = Flights_ex[Flights_ex["flight_direction"] == "D"].reset_index(drop=True)

# Other ways to do the same :
Flights_ex_D = Flights_ex[Flights_ex["flight_direction"].isin(["D"])]
Flights_ex_D = Flights_ex.loc[Flights_ex["flight_direction"] == "D"]

# Redefine the file, but without all records with flight_direction "D"
Flights_ex_A = Flights_ex[~(Flights_ex["flight_direction"] == "D")]



#Select only usefull columns: departing flights do not have landing time, arriving flights do not have take off times
Flight_ex_A = Flights_ex_A.iloc[:,[0,3,4,5,6,7,8]]
Flight_ex_D = Flights_ex_D.iloc[:,[0,3,4,5,6,7,9]]
# In pandas, indices start at 0




