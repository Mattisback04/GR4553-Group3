#500mb Geopotential Height and Relative Humidity
import pygrib
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

grbs = pygrib.open('gfs_4_20121029_0600_027.grb2')
#for msg in grbs:
#        print(msg)

hgtMSG = grbs[103]
hgt = hgtMSG.values/10.0 
[lats, lons] = hgtMSG.latlons()

tempMSG= grbs[104]
temp = tempMSG.values - 273 

rhMSG = grbs[105]
rh = rhMSG.values

domain = (lons >= 270) & (lons <= 305) & (lats >= 20) & (lats <= 55)

rows = np.where(np.any(domain, axis=1))[0]
cols = np.where(np.any(domain, axis=0))[0]

row1 = rows.min()
row2 = rows.max() + 1
col1 = cols.min()
col2 = cols.max() + 1

lats = lats[row1:row2, col1:col2]
lons = lons[row1:row2, col1:col2]
hgt = hgt[row1:row2, col1:col2]
temp = temp[row1:row2, col1:col2]
rh = rh[row1:row2, col1:col2]

lons = lons - 360


fig = plt.figure(figsize=(8, 8))

proj = ccrs.LambertConformal(central_longitude=-90.0, central_latitude=35.0)
ax = plt.axes(projection=proj)
ax.set_extent([-90, -65, 30, 50], crs=ccrs.PlateCarree())

ax.add_feature(cfeature.LAND, facecolor='wheat')
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
ax.add_feature(cfeature.LAKES, facecolor='lightblue')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')

# Gridlines 

glx = ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=['bottom'], x_inline=False,y_inline=False,rotate_labels=True,color='white', linestyle='--', xlocs=np.arange(-90, -65, 5),ylocs=[]) 
gly = ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=['right'], x_inline=False,y_inline=False,color='white', linestyle='--', xlocs=[],ylocs=np.arange(30, 50, 4)) 
glx.xpadding=10
glx.xlabel_style={'rotation':385}
 
rhFILL = ax.contourf(lons, lats, rh, levels=[70, 80, 90, 100], cmap='Greens', transform=ccrs.PlateCarree())

hgtLEVELS = np.arange(520, 585, 5)

hgtCONTOURS = ax.contour(lons, lats, hgt, levels=hgtLEVELS, colors='black', linewidths=2, transform=ccrs.PlateCarree())

ax.clabel(hgtCONTOURS, levels=hgtLEVELS, inline=True, fontsize=10, fmt='%d')

tempMIN = np.min(temp)
tempMAX = np.max(temp)
tempLEVELS = np.arange(tempMIN, tempMAX, 3)

#tempCONTOURS = ax.contour(lons, lats, temp, levels=tempLEVELS, cmap='cool_r', linestyles='dotted', transform=ccrs.PlateCarree())
#cbar = plt.colorbar(tempCONTOURS, orientation='horizontal')
cbar = plt.colorbar(rhFILL, orientation='horizontal')
cbar.set_label('Relative Humidity (%)')
cbar.ax.xaxis.set_label_position('top')

plt.title('500mb Heights (dm) / Humidity (%)')

plt.show()