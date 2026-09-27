# 1d : use of pandas and visualization
#--------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the files we prepared earlier
Flights_ex_A = pd.read_csv("Flights_ex_A.csv")

print(Flights_ex_A["scheduled_datetime"].dtype)  # pandas read it as text

# Some columns are classified as text, while they should be time-data
Flights_ex_A["scheduled_datetime"] = pd.to_datetime(Flights_ex_A["scheduled_datetime"])

Flights_ex_A["actual_block_time"] = pd.to_datetime(Flights_ex_A["actual_block_time"])

Flights_ex_A["actual_landing_time"] = pd.to_datetime(Flights_ex_A["actual_landing_time"])

Flights_ex_A["taxi_in"] = pd.to_numeric(Flights_ex_A["taxi_in"], errors="coerce")


# Group taxi times by aircraft category
taxi_times = (
    Flights_ex_A.groupby("aircraft_category")
    .agg(taxi_in_avg=("taxi_in", "mean"), counts=("taxi_in", "size"))
    .reset_index()
    .sort_values("aircraft_category")
)

# Group taxi times by hour
Flights_ex_A["hour"] = Flights_ex_A["scheduled_datetime"].dt.hour
taxi_times_2 = (
    Flights_ex_A.groupby("hour")
    .agg(taxi_in_av=("taxi_in", "mean"), counts=("taxi_in", "size"))
    .reset_index()
    .sort_values("hour")
)


# Divide by aircraft category
print(Flights_ex_A["aircraft_category"].unique())

Taxi_in_2 = Flights_ex_A[Flights_ex_A["aircraft_category"] == 2]
print(Taxi_in_2)

Taxi_in_3 = Flights_ex_A[Flights_ex_A["aircraft_category"] == 3]
print(Taxi_in_3)

Taxi_in_4 = Flights_ex_A[Flights_ex_A["aircraft_category"] == 4]
print(Taxi_in_4)

# Taxi_in_5 = Flights_ex_A[Flights_ex_A["aircraft_category"] == 5]   # no flights with aircraft category 5

Taxi_in_6 = Flights_ex_A[Flights_ex_A["aircraft_category"] == 6]
print(Taxi_in_6)

Taxi_in_7 = Flights_ex_A[Flights_ex_A["aircraft_category"] == 7]
print(Taxi_in_7)

Taxi_in_8 = Flights_ex_A[Flights_ex_A["aircraft_category"] == 8]
print(Taxi_in_8)

Taxi_in_9 = Flights_ex_A[Flights_ex_A["aircraft_category"] == 9]
print(Taxi_in_9)


# Histograms of taxi in times
# NOTE : if you want to use your own function to make the histogram, so you don't have yo write the same thing over an over again, check out Appendix 1 (line 146)

plt.figure(figsize=(10,14)) # the equivalence of 'par(mfrow=c(4,2))' 
bins = np.arange(0,90,5) #equivalence of seq(0,85,5)


# Taxi-in Cat 2
plt.subplot(4,2,1)
plt.hist(Taxi_in_2["taxi_in"].dropna().astype(float), bins=bins, range=(0,85))
plt.xlim(0,85)
plt.title("Taxi-in Cat 2")
plt.xlabel("Time(min)")
plt.axvline(x=5, color="red")
plt.axvline(x=20, color="red")

# Taxi-in Cat 3
plt.subplot(4,2,2)
plt.hist(Taxi_in_3["taxi_in"].dropna().astype(float), bins=bins, range=(0,85))
plt.xlim(0,85)
plt.title("Taxi-in Cat 3")
plt.xlabel("Time(min)")
plt.axvline(x=5, color="red")
plt.axvline(x=20, color="red")

# Taxi-in Cat 4
plt.subplot(4,2,3)
plt.hist(Taxi_in_4["taxi_in"].dropna().astype(float), bins=bins, range=(0,85))
plt.xlim(0,85)
plt.title("Taxi-in Cat 4")
plt.xlabel("Time(min)")
plt.axvline(x=5, color="red")
plt.axvline(x=20, color="red")

# There are no category 5 flights.

# Taxi-in Cat 6
plt.subplot(4,2,5)
plt.hist(Taxi_in_6["taxi_in"].dropna().astype(float), bins=bins, range=(0,85))
plt.xlim(0,85)
plt.title("Taxi-in Cat 6")
plt.xlabel("Time(min)")
plt.axvline(x=5, color="red")
plt.axvline(x=20, color="red")

# Taxi-in Cat 7
plt.subplot(4,2,6)
plt.hist(Taxi_in_7["taxi_in"].dropna().astype(float), bins=bins, range=(0,85))
plt.xlim(0,85)
plt.title("Taxi-in Cat 7")
plt.xlabel("Time(min)")
plt.axvline(x=5, color="red")
plt.axvline(x=20, color="red")

# Taxi-in Cat 8
plt.subplot(4,2,7)
plt.hist(Taxi_in_8["taxi_in"].dropna().astype(float), bins=bins, range=(0,85))
plt.xlim(0,85)
plt.title("Taxi-in Cat 8")
plt.xlabel("Time(min)")
plt.axvline(x=5, color="red")
plt.axvline(x=20, color="red")

# Taxi-in Cat 9
plt.subplot(4,2,8)
plt.hist(Taxi_in_9["taxi_in"].dropna().astype(float), bins=bins, range=(0,85))
plt.xlim(0,85)
plt.title("Taxi-in Cat 9")
plt.xlabel("Time(min)")
plt.axvline(x=5, color="red")
plt.axvline(x=20, color="red")

plt.tight_layout()
plt.subplots_adjust(hspace=0.5, wspace=0.3)
plt.show()




# APPENDIX 1
fig, axes = plt.subplots(4,2, figsize=(10,14))
axes = axes.flatten()
bins = np.arange(0,90,5)

categorias = [
    (Taxi_in_2, "Taxi-in Cat 2"),
    (Taxi_in_3, "Taxi-in Cat 3"),
    (Taxi_in_4, "Taxi-in Cat 4"),
    (Taxi_in_6, "Taxi-in Cat 6"),
    (Taxi_in_7, "Taxi-in Cat 7"),
    (Taxi_in_8, "Taxi-in Cat 8"),
    (Taxi_in_9, "Taxi-in Cat 9")
]

for ax, (df_cat, titulo) in zip(axes, categorias) : 
    ax.hist(df_cat["taxi_in"].dropna().astype(float), bins=bins, range=(0,85))
    ax.set_xlim(0,85)
    ax.set_title(titulo)
    ax.set_xlabel("Time(min)")
    ax.axvline(x=5, color="red")
    ax.axvline(x=20, color="red")

# to hide the extra subplot (7 categories to 8 spaces)
for ax in axes[len(categorias):]:
    ax.axis("off")

#plt.tight_layout()
#plt.subplots_adjust(hspace=0.5, wspace=0.3)
#plt.show()
   
