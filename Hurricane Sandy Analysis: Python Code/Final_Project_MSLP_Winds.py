# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:06:29 2026

@author: noell
"""

import pygrib 
import numpy as np 
import matplotlib.pyplot as plt 
import cartopy.crs as ccrs 
import cartopy.feature as cfeature 

# Replace file name in '' with the file you want to use
grbs = pygrib.open('gfs_4_20121029_0600_027.grb2') 

# Surface Pressure Message 

# Commeted out print statement reads all messages in data file, not needed to run the main code
#for msg in grbs:
 #   print(msg)

sfcMSLPMSG = grbs[207]
#print(sfcMSLPMSG)

[lats, lons] = sfcMSLPMSG.latlons() 

# Converts pascals to millibars (hectoPascals)

sfcMSLP_array = sfcMSLPMSG.values/100

# Wind Messages 

uMSG = grbs[298] 
vMSG = grbs[299] 

uKNOT = uMSG.values * 1.94384 
vKNOT = vMSG.values * 1.94384 
windMAG=np.sqrt(uKNOT**2 + vKNOT**2)*1.1508

# Sets up the chart and its projection

fig = plt.figure(figsize=(8, 8)) 
proj = ccrs.LambertConformal(central_longitude=-90.0, central_latitude=35.0) 
ax = plt.axes(projection=proj) 

# Updated Extent: 80W to 60W and 35N to 47N 

ax.set_extent([-80, -60, 35, 46], crs=ccrs.PlateCarree()) 

# Map Features

ax.add_feature(cfeature.LAND, facecolor='wheat') 
ax.add_feature(cfeature.OCEAN, facecolor='lightblue') 
ax.add_feature(cfeature.LAKES, facecolor='lightblue') 
ax.add_feature(cfeature.STATES, edgecolor='grey') 
ax.add_feature(cfeature.BORDERS, edgecolor='grey') 

# Gridlines 

glx = ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=['bottom'], x_inline=False,y_inline=False,rotate_labels=True,color='white', linestyle='--', xlocs=np.arange(-140, -60, 5),ylocs=[]) 
gly = ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=['right'], x_inline=False,y_inline=False,color='white', linestyle='--', xlocs=[],ylocs=np.arange(20, 60, 4)) 
glx.xpadding=10
glx.xlabel_style={'rotation':385}

# Mean Sea Level Pressure Contours 

MIN = np.min(sfcMSLP_array) 
MAX = np.max(sfcMSLP_array) 
LEVELS = np.arange(MIN, MAX, 7) 

bounds=[39,45,61,67,73]

hgtCONTOURS = ax.contour(lons, lats, sfcMSLP_array, levels=LEVELS,colors='black', transform=ccrs.PlateCarree()) 
ax.clabel(hgtCONTOURS,inline=True,fontsize=8,fmt='%d')

# Wind Contour with Colorbar

plt.contourf(lons,lats,windMAG,levels=bounds,cmap=plt.cm.autumn_r,transform=ccrs.PlateCarree())
cbar=plt.colorbar(location='bottom')
cbar.set_label('MPH')


# Wind Barbs using exact array slicing 

plt.barbs(lons[::5,::5],lats[::5,::5],uKNOT[::5,::5],vKNOT[::5,::5],transform=ccrs.PlateCarree())


plt.title('Mean Sea Level Pressure & Winds') 

#replace savefig name after mslp_winds_ to refelct your filename
plt.savefig('mslp_winds_0600_027')

plt.show() 