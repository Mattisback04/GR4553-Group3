#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import geopandas as gpd
import seaborn as sns
import matplotlib.pyplot as plt
from cartopy import crs as ccrs
import cartopy.feature as cfeature
import numpy as np
import os
import sounderpy as spy
import metpy
import pyart
import siphon
import pygrib
import metpy.calc as mpcalc
from metpy.units import units


# In[2]:


okx_oct29_12z_sounding = spy.get_obs_data('OKX', '2012', '10', '29', '12')
spy.build_sounding(okx_oct29_12z_sounding)
okx_oct30_0z_sounding = spy.get_obs_data('OKX', '2012', '10', '30', '0')
spy.build_sounding(okx_oct30_0z_sounding, special_parcels=False)
okx_oct30_12z_sounding = spy.get_obs_data('OKX', '2012', '10', '30', '12')
spy.build_sounding(okx_oct30_12z_sounding)


# In[2]:


os.chdir(os.path.expanduser('~'))
os.chdir('CompMethods')
os.chdir('Sandy')
os.getcwd()


# In[3]:


sandy_buoy_data = pd.read_csv('buoy_data.csv')

sandy_buoy_data.columns = sandy_buoy_data.columns.str.strip()
sandy_buoy_data["Datetime"] = pd.to_datetime(sandy_buoy_data["Date"] + " " + sandy_buoy_data["Time"])
sandy_buoy_data = sandy_buoy_data.sort_values("Datetime").set_index("Datetime")

sandy_buoy_data["Pressure"] = pd.to_numeric(sandy_buoy_data["Pressure"], errors="coerce")
sandy_buoy_data["Temp"] = pd.to_numeric(sandy_buoy_data["Temp"], errors="coerce")
sandy_buoy_data["Water Temp"] = pd.to_numeric(sandy_buoy_data["Water Temp"], errors="coerce")

fig, ax1 = plt.subplots(figsize=(12, 5))

# Pressure
ax1.plot(sandy_buoy_data.index, sandy_buoy_data["Pressure"], color="tab:blue", label="Pressure")
ax1.set_ylabel("Pressure (hPa)", color="tab:blue")
ax1.tick_params(axis="y", labelcolor="tab:blue")
ax1.grid(True)

# Temperature
ax2 = ax1.twinx()
ax2.plot(sandy_buoy_data.index, sandy_buoy_data["Temp"], color="tab:red", label="Air Temp")
ax2.plot(sandy_buoy_data.index, sandy_buoy_data["Water Temp"], color="tab:green", label="Water Temp")
ax2.set_ylabel("Temperature (°C)")

# Legend
handles, labels = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles + handles2, labels + labels2)

plt.title("Buoy Meteogram")
plt.show()


# In[ ]:




