# 1a : Installation of useful packages for database analysis
#------------------------------------------------------------

# In python, packages/librarys are install in the Terminal (not within the script)
# using pip (the equivalent of `install.packages()` in R) :
#
# pip install package_name

# This file explain how to install and use the packages,
# but the general way to use them is : 
#   import package_name as package_nickname
# 
# Where `package_nickname` is the name used to refer it within the 
# code so you don't have to type its full name. It is recommended to
# use a short name.



# The equivalents of readxl (read Excel files), WriteXLS (write Excel files)
# and dplyr (data frame manipulation) are included in pandas.
#

# It is installed as follows : 
#   pip install pandas openpyxl
#
# and we use it like this : 
import pandas as pd


# However, to read an write Excel files, we use different pandas methods.
#
# 1. To read, we use read_excel : 
# df = pd.read_excel("file.xlsx")       The equivalence of `read_excell()`

# 2. To write, we use to_excel : 
# df.to_excel("output_file.xlsx", index = False)        Where `df` is the data frame to convert

# 3. The features of dplyr are organized into functions
# In the left are the R functions, and on the right are the Python equivalence
# select() -> df[['col1', 'col2']]
# filter() -> df[df['col1'] > 5]
# mutate() -> df['new_col'] = df['col1'] * 2
# arrange() -> df.sort_values('col1')
# group_by() + summarise() -> df.groupby('col1').agg(...)


# Paquetes avanzados
# 4. The equivalent of grDevices (colors to RGB) : 
#   pip install matplotlib
import matplotlib.colors as mcolors

# 5. The equivalent of maps and mapdata (maps apps) : 
#   pip install geopandas folium
import geopandas as gpd
import folium

# 6. The equivalent of ggplot2 (graphics) :
#   pip install plotnine    (muy parecido a ggplot2)
from plotnine import ggplot, aes, geom_point

# 7. The equivalent of shiny (interactive web apps)
#   pip install streamlit
import streamlit as st

# If you want to install all the packages in one line you can do : 
#   pip install pandas openpyxl matplotlib geopandas folium plotnine streamlit
