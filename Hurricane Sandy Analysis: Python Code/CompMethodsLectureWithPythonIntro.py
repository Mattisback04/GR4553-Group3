a=2
b='Hello'
c=3.59

print(a+c)

ab='cat'
ba=ab
print(b)
d=1e-4

print((float(a)))
a=float(a)
a=int(a)

print(int(c))
c=round(c,1)

e=314159e-5
print('The value of e is %0.4f.'%e)

f=7
print('The value of f is %d.' % f)

ba
print("The word enclosed in ba is %s."%ba)

hotdog='hot'+'dog'
print(hotdog)

print(hotdog[1])
print(hotdog[0:6])
print(hotdog[0:6])

#Creating Lists

g= [1,1.5, 'two']
print(g[1])

listnum= [-3, -1, 1, 3, 5, 7, 9, 11, 13, 15, 17]
max(listnum)
min(listnum)
sum(listnum)

#Open and Read file
inputfile= open('US_prcp.dat', 'r')
firstline=inputfile.readline()
print(firstline)

secondline=inputfile.readline()
print(secondline)

#read data in file all at once
inputfile.seek(0)
alldata=inputfile.readlines()

#always close files after opening in labs!!
inputfile.close()

#Open a file for writing
wfile=open("somefile.txt",'w')
print('My lucky number is %d.' % 4, file=wfile)
print("The value of pi to two decimal places is %0.2f." % 3.14159, file=wfile)
print("I am %d feet %d inches tall and have %s colored hair." % (5,9,'dark-brown'), file=wfile)
wfile.close()

print(wfile)

#if statements:
var1 = 100
if var1: 
    print('Expression is true')
    print(var1)

var2 = 0
if var2:
    print("Exression is true")
    print(var2)
else: 
    print('Expression is false')
    print(var2)
    
var3 = 250
if var3 >= 200:
    print('1 - Expression is true')
    print(var3)
elif var3 ==150:
    print('2 - Expression is true')
    print(var3)
elif var3 == 100:
    print('3 - Expression is true')
    print(var3)
elif var3 < 100:
    print('4 - Expression is false')
    print(var3)
else:
    print('5 - Expression is false')
    print(var3)
    
    
num1=7
num2 = 5
sum_num=num1+num2
if sum_num >= 100:
    print('The sum is greater or equal to 100.')
elif sum_num <= 25:
    print('The sum is less than or equal to 25.')
else:
    print('The sum is between 25 and 99.')

#loops
data = [4,9.0,-8,'cat','mouse']

for d in data:
    print(d)
    
for d in range(0,len(data),2):
    print(data[d])

fruits=['banana','apple', 'orange']  
for index in range(len(fruits)):
    print('Current fruit is: %s' % fruits[index])
    
    
for i in range(0,10):
    print('This is index i= %d' % i)
    for j in range(0,10):
        print('This is index j= %d' % j)
        
name="Matthew"
grade=89.75
print('My name is %s, and I got a %.2f on my test!' %(name, grade))

hours=range(1,24+1)

for h in hours:
    print(h)
else:
    print('Day complete')
    

    
studyHours = 0

ready=False

while ready == False:
    studyHours = studyHours + 1 
    print(studyHours)
    if studyHours==5:
        ready=True
else:
    print('Mollee is ready for her interview! She prepared for %d hours.' % (studyHours))
   # print(studyHours)
   
number = 16
#checj if number is even
if number % 2 == 0:
    print('%d is an even number.' % number)
    
AutumnAge= 25
MichaelAge=23

if AutumnAge == MichaelAge:
    print('We are the same age')
#elif AutumnAge > MichaelAge: 
#    print('Autumn is older.')
elif abs(AutumnAge - MichaelAge) <= 5:
    print('They are around the same age.')
else:
    print('We are different ages')
    
    
AutumnAge = 27
MichealAge =23

if AutumnAge == MichaelAge:
    print('We are the same age')
elif (AutumnAge != MichaelAge) and (abs(AutumnAge - MichaelAge) <= 5):
    print('Yay')
    
hours = [7,8,9,10,11]
myHours=[False, True, False, True, True]
Molhours=[True, True, True, False, False]
JoHours= [False, True, True, True, False]

#when can we all meet at the same time

for i in range(0,len(hours)):
    if myHours[i] and Molhours[i] and JoHours[i]:
        print('We are all available at %d AM' %hours[i]) 
    else:
        print('We are not all avialable at the same time since one of us is unavailable at %d AM' % (hours[i]))
        


#list and arrays
emptyList=[]
fruits=['oranges','grapes','apples']
print(fruits[2])
print(fruits[-1])
#appending
fruits.append('bananas')
print(fruits[:])

#looping through lists
for i in range(len(fruits)):
    print(fruits[i])

#Slicing
myList=[0,1,2,3,4,5,6,7,8,9]
print(myList[0:-1])
print(myList[0:])
myList.append(10)
print(myList)

#arrays
#but first install numpy!!

import numpy as np
a = np.array([1,2,3,4,5],dtype = np.float64)
print(a[3])

onearr=np.ones((2,3), dtype = np.float16)
zeroarr=np.zeros((2,3), dtype= np.int64)

a =np.arange(0,11,2)
print(a)

b =np.arange(10,-3, -3)
print(b)

a=np.linspace(0,10,101)
print(a)

import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a[0,1])
print(a[1,1])
print(a[0,:])
print(a[:,0])
print(a[-1,-2])

#flatten array from 2D to 1D
print(a.flatten())

b=a.flatten()
b2D=np.reshape(b,(2,3))
print(b2D)

bday=np.array([[22,26,10,25,24],[2,9,20,5,1]])
bday_sort_row=np.sort(bday,0)
print(bday_sort_row)
bday_sort_col=np.sort(bday,1)
print(bday_sort_col)

print(a*2)
print(a-3+3*1.5)

c=np.array([[6,5,4],[3,2,1]])
print(a+c)

print(a[0,:]+c[1,:])
print(a[0,:]**c[1,:])

#Throwing all examples together
Clist=[]
Flist=[50,60,70,80,90]

for n in range(len(Flist)):
    Ctemp=(5/9)*(int(Flist[n])-32)
    Clist.append(Ctemp)

print("The temperature of the 3rd element in Celsius is %.1f degC." %Clist[2])
        
[m,n]=np.shape(a)
print(m,n)

col=0
barray=np.zeros([m,n],'d')
for i in range(m):
    for j in range(n):
        #print(a[i,j])
        print('col: %d' %col)
        barray[i,j]=b[col]
        print(b[col])
        print(barray[i,j])
        col =col+1 
      
import numpy as np
rng = np.random.default_rng(seed=42)
rlist=rng.uniform(low=20.0,high=35.0,size=9)
rarray = np.ones([3,3],dtype=float)
[row,col]=np.shape(rarray)

mike=0
for i in range(row):
    for j in range(col):
        rarray[i,j]=rlist[mike]
        mike = mike +1

print(np.average(rarray))
print(np.std(rarray))
print(np.max(rarray))
print(np.average(rarray[:,0]))

ravg=np.ones(3,dtype=float)
rstd=np.ones(3, dtype=float)
for i in range(col):
    ravg[i]=np.average(rarray[:,i])
    rstd[i]=np.std(rarray[:,i])
print(rstd)
print(ravg)
print(np.min(rstd))
print(np.argmin(rstd))

ravg=np.ones(3,dtype=float)
rstd=np.ones(3, dtype=float)
for i in range(row):
    ravg[i]=np.average(rarray[i,:])
    rstd[i]=np.std(rarray[i,:])
print(rstd)
print(ravg)
print(np.min(rstd))
print(np.argmin(rstd))
print(np.argmax(rstd))
print(np.max(rstd))

# USING PYGRIB
import pygrib
import numpy as np

grbGFS= pygrib.open('gfs.t12z.pgrb2.0p25.anl')
print(grbGFS.messages)

#Gives total amount of messages in this GRIB file
msg_num = grbGFS.messages

#loop through and print all messages to see what you have
for msg in grbGFS:
    print(msg)

#Two different methods to looks at a particular message
print(grbGFS[573])
print(grbGFS.message(573))

#helps display where message marker is located
print(grbGFS.tell())

#moves message marker to top of messages
grbGFS.seek(0)
print(grbGFS.tell())

#search for messages of a specific variable
grbGFS.select(name='Geopotential height')

#pull message and set to variable
gh500msg=grbGFS[332]

#pull data for particular message
gh500=gh500msg.values

#pull lat and long now
[lats, lons] = gh500msg.latlons()

[rows, cols] = gh500.shape

#find lat and lon of starkville
latSTK=33.45
lonSTK=-88.82 + 360

distMin=999. 
iMin = None
jMin = None

for i in range(rows):
    for j in range(cols):
        dist=np.hypot(latSTK - lats[i,j], lonSTK - lons[i,j])
        if dist < distMin:
            distMin=dist
            iMin, jMin =i, j
distMin

#pull 500mb GH at STK
gh500STK=gh500[iMin, jMin]
print(gh500STK)

import netCDF4
f=netCDF4.Dataset('dropsonde.nc')

#print all varibles in file
print(f.variables)

#print just the variable winds here
print(f.variables.keys())

#gives file info
print(f)

#print metadata of specific variable
print(f.variables['gpsalt'])

#print actual data
print(f.variables['gpsalt'][:])
gpsalt= f.variables['gpsalt'][:]

#get rid of the mask in the data
f.set_auto_mask(False)
gpsalt= f.variables['gpsalt'][:] #re run this!

gpsaltunits=f.variables['gpsalt'].units
gpsaltmiss=f.variables['gpsalt'].missing_value
gpsaltsize=gpsalt.size

pres = f.variables['pres'][:]
presunits=f.variables['pres'].units
pressize=pres.size

#create dictionary
GR4553 = {"name":["Ashton", "Noelle", "Taylor", "Jacob", "Matthew", "Malachi", "Emily", "Gabe", "Dawson"], "netid": ["mac1384", "nwd40", "teh287", "jtk290", "mwl140", "mkm779", "emr397", "gas253","des383"], "level":['s','s','s','s','s','j','s','j','s']}

#creating a list!
print(GR4553.keys())
print(list(GR4553.keys()))
key_list= (list(GR4553.keys()))

print(GR4553.values())
values_list= (list(GR4553.values()))
print(values_list[0])

import pandas as pd
data = pd.read_csv('Kumpula-June-2016-w-metadata.txt')

#skip them rows of 'unimportant' text
data = pd.read_csv('Kumpula-June-2016-w-metadata.txt', skiprows=8)

print(data)
data.tail(10)

#information about data
[rows,cols]=data.shape
print(data.columns.values)
print(data.index)
print(data.dtypes)

#selection of data
selection = data[['YEARMODA','TEMP']]
print(selection)

data['TEMP']
data['TEMP'].mean()
data.mean()
data.describe()

%matplotlib
data[["TEMP", "MAX", "MIN"]].plot()

#%%
import matplotlib.pyplot as plt
from numpy import *

x =arange(0, 10, 0.1)
y = sin(x)
simple_plot = plt.plot(x,y)
plt.show()

simple_plot = plt.plot(x,y)
x_label = plt.xlabel('horizontal axis')
y_label = plt.ylabel('vertical axis')
ttl = plt.title("Sine Function")
ax = plt.axis([-2,12, -1.5, 1.5])
grd = plt.grid(True)
txt= plt.text(0,1.3, "We have this random text feature")
ann = plt. annotate('a point on a curve', xy = (4.7, -1), xytext = (3, -1.3), arrowprops = dict(arrowstyle = '->'))
plt.show()

a = cos(x)
b = sin(x)
c = exp(x/10)
d = exp(-x/10)
a1 = plt.plot(x, a, "b-", label = 'cosine')
b1 = plt.plot(x, b, 'r--', label = 'sine')
c1 = plt.plot(x, c, 'g->', label = 'exponential of a positive')
d1 = plt.plot(x, d, 'y-', linewidth = 5, label = 'exponential of a negative')
lx = plt.xlabel('x-axis')
ly = plt.ylabel('y-axis')
leg = plt.legend(loc='upper left')

fg = plt.figure(figsize=(10,8))

plt.show()
#%% Subplots
import matplotlib.pyplot as plt
from numpy import *

fg = plt.figure(figsize=(10,8))
adj = plt.subplots_adjust(hspace=0.4, wspace= 0.4)

# Subplot 1
sp = plt.subplot(2,2,1)
x = linspace(0,10,101)
y = exp(x)
ll = plt.semilogy(x, y)
lx = plt.xlabel('x-axis')
ly = plt.ylabel('y-axis')
tl = plt.title('y=exp(x)')

# Subplot 2
sp = plt.subplot(2,2,2)
y = x**-1.67
ll = plt.loglog(x, y, color = 'm', linewidth=2)
lx = plt.xlabel('x-axis')
ly = plt.ylabel('y-axis')
tl = plt.title('y=x$^{5/3}$')

# Subplot 3
sp = plt.subplot(2,2,3)
x = arange(1001)
y = mod(x,2.87)
hist = plt.hist(y, color= 'r', rwidth=0.8)
lx = plt.xlabel('y')
ly = plt.ylabel('num(y)')
tl = plt.title('y = mod(arange(1001),2.87)')

# Subplot 4
sp = plt.subplot(2,2,4)
ll = plt.hist(y, bins=25, density=True, cumulative=True, orientation='horizontal')
lx = plt.xlabel('density')
ly = plt.ylabel('y')
tl = plt.title('horizontal histogram')

plt.show()

#%%
# numpy arrays and 2D plots

x=linspace(0,10,51)
y =linspace(0,8,41)
(X,Y)=meshgrid(x,y)
a = exp(-((X-2.5)**2 + (Y-4)**2)/4) - exp(-((X-7.5)**2 + (Y-4)**2)/4)
c = plt.contour(x,y,a)
l = plt.clabel(c)
plt.show()

c = plt.contourf(x,y,a, linspace(-1,1,11))
b = plt.colorbar(c, orientation = 'vertical')
m = plt.jet()
lx = plt.xlabel('x')
ly = plt.ylabel('y')
ax = plt.axis([0,10,0,8])
plt.show

#%% Making Vecor Arrows (AKA a wind field)

fig=plt.figure(figsize=(10,8))
x=linspace(0,10,11)
y =linspace(0,15,16)

(X,Y)=meshgrid(x,y)
u = 5*X
v = 5*Y
q = plt.quiver(X,Y,u,v,angles='xy',scale=1000,color='r')
p = plt.quiverkey(q,X.min(),Y.min(),50,"50 m/s",coordinates='data',color='r')
lx = plt.xlabel('x')
ly = plt.ylabel('y')
plt.show()

#%%

s =plt.scatter(x,x)
plt.show()
plt.savefig('figname.png')

#%%

import cartopy
import cartopy.feature as cf
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

fig = plt.figure()
proj = ccrs.PlateCarree()

ax = plt.axes(projection=proj)
ax.coastlines()

#using Lambert Conformal projection for the US
fig = plt.figure()
projL= ccrs.LambertConformal(central_longitude=-96.0, central_latitude=30.0, standard_parallels=(30.0,30.0))
ax=plt.axes(projection = projL)
ax.set_extent([-123.,-70.,20.,50.])

#with features
ax.add_feature(cf.BORDERS)
ax.add_feature(cf.LAKES)
ax.add_feature(cf.LAND)
ax.add_feature(cf.STATES)
ax.add_feature(cf.OCEAN)
ax.add_feature(cf.COASTLINE)

plt.show()

#%%
import cartopy
import cartopy.feature as cf
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
#with options
fig = plt.figure()
projL= ccrs.LambertConformal(central_longitude=-96.0, central_latitude=30.0, standard_parallels=(30.0,30.0))
ax=plt.axes(projection = projL)
ax.set_extent([-123.,-70.,20.,50.])

#with features

ax.add_feature(cf.LAKES, color = 'dodgerblue')
ax.add_feature(cf.LAND, color = 'lightgray')
ax.add_feature(cf.STATES, color = 'lightgray')
ax.add_feature(cf.OCEAN, color = 'dodgerblue')
ax.add_feature(cf.COASTLINE, color = 'black')
ax.add_feature(cf.BORDERS, color = 'black')
ax.gridlines(crs=projL)

ax.draw_labels(True, linewidth = 1, color = 'black', alpha = 0.5, linestyle = '--')
#%% adding data to Map Projections
import pygrib
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

plt.figure(figsize=(10, 5))

grbGFS = pygrib.open('gfs_4_20121031_0000_000.grb2')
for msg in grbGFS:
    print(msg)
tempmsg = grbGFS[211]

temp_k = tempmsg.values
lats, lons = tempmsg.latlons()
temp_c = temp_k - 273

contour_levels = np.arange(-60, 55, 5)

map_proj = ccrs.PlateCarree()
data_crs = ccrs.PlateCarree() 

ax = plt.axes(projection=map_proj)

ax.coastlines(resolution='50m', color='black', linewidth=1)
ax.add_feature(cfeature.BORDERS, linestyle=':')

c_f = ax.contourf(lons, lats, temp_c, 
                  levels=contour_levels, 
                  cmap='coolwarm', 
                  transform=data_crs)

gl = ax.gridlines(draw_labels=True, alpha=0.5, linestyle='--')

plt.colorbar(c_f, orientation='horizontal', pad=0.1, aspect=50, label='Global Surface Temperature (C)')
plt.title('GFS Surface Temperature Analysis (Global Plate Carree)')

plt.show()

#%%
import pygrib
import matplotlib.pyplot as plt
import cartopy.feature as cf
import cartopy.crs as ccrs
import numpy as np
import cartopy

grbGFS= pygrib.open('gfs.t12z.pgrb2.0p25.anl')

temp850 = grbGFS[438]
temp = temp850.values

rh850 = grbGFS[439]
rh = rh850.values

[lats, lons] = temp850.latlons()

plt.figure(figsize=(8, 8))

proj = ccrs.LambertConformal(central_longitude=-96.0, central_latitude=40.0, standard_parallels=(40.0,40.0))
ax = plt.axes(projection = proj)

ax.set_extent([-125.0, -70.0, 20.0, 60.0], crs=ccrs.PlateCarree())

ax.add_feature(cf.LAND, color = 'wheat', alpha = 0.5)
ax.add_feature(cf.OCEAN)
ax.add_feature(cf.LAKES)
ax.add_feature(cf.STATES, edgecolor = 'gray')
ax.add_feature(cf.BORDERS, edgecolor = 'black', linestyle = '-')
ax.add_feature(cf.COASTLINE, edgecolor = 'black')

gl=ax.gridlines(crs= ccrs.PlateCarree(), draw_labels = True, linewidth = 2, color = 'white', alpha = 0.5, linestyle = '--')

plt.contourf(lons, lats, rh, np.arange(80,100,5), cmap=plt.cm.YlGn, transform = ccrs.PlateCarree())
cbar = plt.colorbar(location = 'bottom')
cbar.set_label('percent')
plt.contour(lons, lats, temp-273, np.arange(np.min(temp-273), np.max(temp-273),4), linewidths=2, cmap=plt.cm.jet, transform=ccrs.PlateCarree())

plt.title('850mb Temperature (C)/ 850mb RH %')

plt.show()

#%% 2 variables with wind barbs

import pygrib
import matplotlib.pyplot as plt
import cartopy.feature as cf
import cartopy.crs as ccrs
import numpy as np
import cartopy

grbGFS= pygrib.open('gfs.t12z.pgrb2.0p25.anl')

temp850 = grbGFS[438]
temp = temp850.values

#850mb winds
grbGFS.select(name='U component of wind')
uwind850 = grbGFS[443]
uwind= uwind850.values

grbGFS.select(name='V component of wind')
vwind850 = grbGFS[444]
vwind= vwind850.values

#set up cartopy map
[lats, lons] = temp850.latlons()

plt.figure(figsize=(8, 8))

proj = ccrs.LambertConformal(central_longitude=-96.0, central_latitude=40.0, standard_parallels=(40.0,40.0))
ax = plt.axes(projection = proj)

ax.set_extent([-125.0, -70.0, 20.0, 60.0], crs=ccrs.PlateCarree())

ax.add_feature(cf.LAND, color = 'wheat', alpha = 0.5)
ax.add_feature(cf.OCEAN)
ax.add_feature(cf.LAKES)
ax.add_feature(cf.STATES, edgecolor = 'gray')
ax.add_feature(cf.BORDERS, edgecolor = 'black', linestyle = '-')
ax.add_feature(cf.COASTLINE, edgecolor = 'black')

gl=ax.gridlines(crs= ccrs.PlateCarree(), draw_labels = True, linewidth = 2, color = 'white', alpha = 0.5, linestyle = '--')
gl.top_labels= False
gl.left_labels = False

#plot GFS data onto cartopy map 
bounds = [0,5,10,20,30,40,50,60]

wmag = np.sqrt(uwind**2 + vwind**2) * 1.94

plt.contourf(lons, lats, wmag, bounds, cmap = 'hot_r', transform=ccrs.PlateCarree())
cbar = plt.colorbar(location = 'bottom')
cbar.set_label('knots')

t = plt.contour(lons, lats, temp -273, np.arange(np.min(temp-273), np.max(temp-273), 4), cmap = 'jet', transform= ccrs.PlateCarree())
plt.clabel(t)

plt.barbs(lons[::12, ::12], lats[::12, ::12], uwind[::12, ::12], vwind[::12, ::12], transform=ccrs.PlateCarree())

plt.title('850mb Wind Magnitude (kts) / 850mb Temperature (C) / 850mb Isotachs (kts)')

plt.show()
#%%
import metpy.calc as mpcalc
import numpy as np
from metpy.units import units
import metpy as mp

np.random.seed(19990503)

u=np.random.randint(0,15,10) * units('m/s')
v=np.random.randint(0,15,10) * units('m/s')

direction = mpcalc.wind_direction(u,v)

speed = mpcalc.wind_speed(u,v)
print(speed.to('mph'))
print(direction)
#%%%

from datetime import datetime
from metpy.units import units
from siphon.simplewebservice.wyoming import WyomingUpperAir
import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays
import numpy as np

date = datetime(2020,4,12,21)
station = 'LIX'

#make data request here
df=WyomingUpperAir.request_data(date,station)

print(df.columns)

#save variables and units
print(df['pw']*0.0394)
print(df.units)


p_units=(df.units['pressure'])
pressure = df['pressure'].values*units(p_units)
print(pressure)

data = pandas_dataframe_to_unit_arrays(df)

p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 35)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio= None, pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(date), loc='right');

#%%

from datetime import datetime
from metpy.units import units
from siphon.simplewebservice.wyoming import WyomingUpperAir
import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import pandas_dataframe_to_unit_arrays
import numpy as np
import metpy.calc as mpcalc 

date = datetime(2020,4,12,21)
station = 'LIX'

#make data request here
df=WyomingUpperAir.request_data(date,station)

print(df.columns)

#save variables and units
print(df['pw']*0.0394)
print(df.units)


p_units=(df.units['pressure'])
pressure = df['pressure'].values*units(p_units)
print(pressure)

data = pandas_dataframe_to_unit_arrays(df)

p = data['pressure']
T = data['temperature']
Td = data['dewpoint']
u = data['u_wind']
v = data['v_wind']

fig = plt.figure(figsize=(9, 11))

# Initiate the skew-T plot type from MetPy class loaded earlier
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p[::3], u[::3], v[::3], y_clip_radius=0.03)

# Set some appropriate axes limits for x and y
skew.ax.set_xlim(-30, 35)
skew.ax.set_ylim(1020, 100)

# Add the relevant special lines to plot throughout the figure
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K,
                       alpha=0.25, color='orangered')
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K,
                         alpha=0.25, color='tab:green')
skew.plot_mixing_lines(mixing_ratio= None, pressure=np.arange(1000, 99, -20) * units.hPa,
                       linestyle='dotted', color='tab:blue')

# ====================================================================
# NEW: Convective Parameters (CAPE, LCL, LFC, EL)
# ====================================================================

# 1. Calculate the thermodynamic levels (using surface conditions)
lcl_pressure, lcl_temperature = mpcalc.lcl(p[0], T[0], Td[0])
lfc_pressure, lfc_temperature = mpcalc.lfc(p, T, Td)
el_pressure, el_temperature = mpcalc.el(p, T, Td)

# 2. Calculate Surface-Based CAPE and CIN
cape, cin = mpcalc.surface_based_cape_cin(p, T, Td)

# 3. Calculate and plot the parcel profile (needed to shade CAPE)
parcel_prof = mpcalc.parcel_profile(p, T[0], Td[0]).to('degC')
skew.plot(p, parcel_prof, 'k', linewidth=2, label='SB Parcel')

# 4. Shade the CAPE and CIN areas
skew.shade_cape(p, T, parcel_prof)
skew.shade_cin(p, T, parcel_prof, Td)

# 5. Draw horizontal dashed lines for LCL, LFC, and EL
skew.ax.axhline(lcl_pressure, color='dodgerblue', linestyle='--', label=f'LCL: {lcl_pressure.m:.0f} hPa')
skew.ax.axhline(lfc_pressure, color='crimson', linestyle='--', label=f'LFC: {lfc_pressure.m:.0f} hPa')
skew.ax.axhline(el_pressure, color='purple', linestyle='--', label=f'EL: {el_pressure.m:.0f} hPa')

# 6. Add text box for CAPE and print a legend
skew.ax.text(0.02, 0.98, f"SBCAPE: {cape.m:.0f} J/kg", transform=skew.ax.transAxes, 
             verticalalignment='top', fontsize=11, 
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
skew.ax.legend(loc='upper right')

# ====================================================================

# Add some descriptive titles
plt.title('{} Sounding'.format(station), loc='left')
plt.title('Valid Time: {}'.format(date), loc='right')

plt.show() 


#%%

#NEXRAD Level 2 File

import cartopy.crs as ccrs
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
from metpy.calc import azimuth_range_to_lat_lon
from metpy.cbook import get_test_data
from metpy.io import Level2File
#from metpy.plots import add_metpy_logo, add_timestamp,
from metpy.plots import USCOUNTIES
from metpy.units import units

###########################################
# Open the file
f = Level2File('KEWX20131031_120325_V06')
print(f.sweeps[0][0])

###########################################
# Pull data out of the file
sweep = 0
# First item in ray is header, which has azimuth angle
az = np.array([ray[0].az_angle for ray in f.sweeps[sweep]])

###########################################
# We need to take the single azimuth (nominally a mid-point) we get in the data and
# convert it to be the azimuth of the boundary between rays of data, taking care to handle
# where the azimuth crosses from 0 to 360.
diff = np.diff(az)
crossed = diff < -180
diff[crossed] += 360.
avg_spacing = diff.mean()

# Convert mid-point to edge
az = (az[:-1] + az[1:]) / 2
az[crossed] += 180.

# Concatenate with overall start and end of data we calculate using the average spacing
az = np.concatenate(([az[0] - avg_spacing], az, [az[-1] + avg_spacing]))
az = units.Quantity(az, 'degrees')

###########################################
# Calculate ranges for the gates from the metadata
# 5th item is a dict mapping a var name (byte string) to a tuple
# of (header, data array)
ref_hdr = f.sweeps[sweep][0][4][b'REF'][0]
ref_range = (np.arange(ref_hdr.num_gates + 1) - 0.5) * ref_hdr.gate_width + ref_hdr.first_gate
ref_range = units.Quantity(ref_range, 'kilometers')
ref = np.array([ray[4][b'REF'][1] for ray in f.sweeps[sweep]])

rho_hdr = f.sweeps[sweep][0][4][b'RHO'][0]
rho_range = (np.arange(rho_hdr.num_gates + 1) - 0.5) * rho_hdr.gate_width + rho_hdr.first_gate
rho_range = units.Quantity(rho_range, 'kilometers')
rho = np.array([ray[4][b'RHO'][1] for ray in f.sweeps[sweep]])

# Extract central longitude and latitude from file
cent_lon = f.sweeps[0][0][1].lon
cent_lat = f.sweeps[0][0][1].lat

###########################################
#spec=gridspec.GridSpec(1, 2)
spec = gridspec.GridSpec(1, 1)
#fig = plt.figure(figsize=(15, 8))
fig = plt.figure(figsize=(8,8))

for var_data, var_range, ax_rect in zip((ref, rho), (ref_range, rho_range), spec):
    # Turn into an array, then mask
    data = np.ma.array(var_data)
    data[np.isnan(data)] = np.ma.masked
    
    # Convert az,range to x,y
    xlocs, ylocs = azimuth_range_to_lat_lon(az, var_range, cent_lon, cent_lat)
    
    # Plot the data
    crs = ccrs.LambertConformal(central_longitude=cent_lon, central_latitude=cent_lat)
    ax = fig.add_subplot(ax_rect, projection=crs)
    ax.add_feature(USCOUNTIES, linewidth=0.5)
    pcm = ax.pcolormesh(xlocs, ylocs, data, cmap='gist_ncar', transform=ccrs.PlateCarree())
    ax.set_extent([cent_lon - 3, cent_lon + 3, cent_lat - 3, cent_lat + 3])
    ax.set_aspect('equal', 'datalim')
    
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,linewidth=2, color='grey', alpha=0.5, linestyle='--')
    plt.title("KEWX - AUSTIN/S ANT, TX Radar 12:03 PM CDT Oct. 31")
    #add_timestamp(ax, f.dt, y=0.02, high_contrast=True)

plt.colorbar(pcm, location = 'bottom')

plt.show()
#%%
import cartopy.crs as ccrs
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import s3fs
from metpy.calc import azimuth_range_to_lat_lon
from metpy.io import Level2File
from metpy.plots import USCOUNTIES
from metpy.units import units

###########################################
# 1. Connect to the AWS NEXRAD Archive
###########################################
# Create an anonymous connection to AWS S3
fs = s3fs.S3FileSystem(anon=True)

# Point to KDGX (Jackson, MS) for March 25, 2023 (UTC)
bucket_path = 'unidata-nexrad-level2/2023/03/25/KDGX/'
files = fs.ls(bucket_path)
print(f"Found {len(files)} radar scans for this day.")

# Find scans from roughly 01:00 UTC (right as it hit Rolling Fork)
target_files = [f for f in files if 'KDGX20230325_010' in f]
target_file = target_files[0] if target_files else files[-1]
print(f"Opening file: {target_file}")

###########################################
# 2. Open the file directly from AWS into MetPy
###########################################
with fs.open(target_file, 'rb') as fobj:
    f = Level2File(fobj)

###########################################
# 3. Pull Reflectivity Data out of the file
###########################################
sweep = 0
az = np.array([ray[0].az_angle for ray in f.sweeps[sweep]])

# Handle where the azimuth crosses from 0 to 360
diff = np.diff(az)
crossed = diff < -180
diff[crossed] += 360.
avg_spacing = diff.mean()

# Convert mid-point to edge
az = (az[:-1] + az[1:]) / 2
az[crossed] += 180.
az = np.concatenate(([az[0] - avg_spacing], az, [az[-1] + avg_spacing]))
az = units.Quantity(az, 'degrees')

# Calculate ranges for the gates
ref_hdr = f.sweeps[sweep][0][4][b'REF'][0]
ref_range = (np.arange(ref_hdr.num_gates + 1) - 0.5) * ref_hdr.gate_width + ref_hdr.first_gate
ref_range = units.Quantity(ref_range, 'kilometers')
ref = np.array([ray[4][b'REF'][1] for ray in f.sweeps[sweep]])

# Extract central longitude and latitude from file
cent_lon = f.sweeps[0][0][1].lon
cent_lat = f.sweeps[0][0][1].lat

###########################################
# 4. Plot the Data
###########################################
spec = gridspec.GridSpec(1, 1)
fig = plt.figure(figsize=(10, 10))

# Turn into an array, then mask NaNs
data = np.ma.array(ref)
data[np.isnan(data)] = np.ma.masked

# Convert az/range to x/y coordinates
xlocs, ylocs = azimuth_range_to_lat_lon(az, ref_range, cent_lon, cent_lat)

# Plotting parameters
crs = ccrs.LambertConformal(central_longitude=cent_lon, central_latitude=cent_lat)
ax = fig.add_subplot(spec[0], projection=crs)
ax.add_feature(USCOUNTIES, linewidth=0.5)

# Plot the mesh
ax.pcolormesh(xlocs, ylocs, data, cmap='Spectral_r', transform=ccrs.PlateCarree())

# Zoom in slightly to the northwest of Jackson, MS to frame Rolling Fork
ax.set_extent([cent_lon - 1.5, cent_lon + 0.5, cent_lat - 0.5, cent_lat + 1.5])
ax.set_aspect('equal', 'datalim')

# Add gridlines and title
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=2, color='grey', alpha=0.5, linestyle='--')
plt.title(f"KDGX Radar (Jackson, MS) - Rolling Fork Tornado - {f.dt:%Y-%m-%d %H:%M} UTC")

plt.show()

#%%
import pygrib
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# 1. Open the GRIB file
grbs = pygrib.open('gfs_4_20121029_0000_003.grb2')

# 2. Extract Data (Using name selection is safer than hardcoded indices)
# Mean Sea Level Pressure (Often preferred over raw surface pressure for synoptic maps)
MLSPMSG = grbs[207]
[lats, lons] = MLSPMSG.latlons()
sfcP_mb = MLSPMSG.values / 100.0 

uMSG = grbs[298]
vMSG = grbs[299]

u_knots = uMSG.values * 1.94384
v_knots = vMSG.values * 1.94384


# 3. Setup Figure and Projection
fig = plt.figure(figsize=(10, 8))

# Center the projection on the new specific bounds (70W, 41N is roughly the center)
proj = ccrs.LambertConformal(central_longitude=-70.0, central_latitude=41.0)
ax = plt.axes(projection=proj)

# Set the exact extent requested: 80W to 60W, 35N to 47N
ax.set_extent([-80, -60, 35, 47], crs=ccrs.PlateCarree())

# 4. Add Map Features
ax.add_feature(cfeature.LAND, facecolor='wheat')
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
ax.add_feature(cfeature.LAKES, facecolor='lightblue')
ax.add_feature(cfeature.STATES, edgecolor='grey')
ax.add_feature(cfeature.BORDERS, edgecolor='grey')
ax.coastlines(resolution='50m', color='black', linewidth=1)

# Format gridlines to match the smaller map area
gl = ax.gridlines(draw_labels=True, color='white', linestyle='--', 
                  xlocs=np.arange(-80, -55, 5), ylocs=np.arange(30, 50, 5))
gl.top_labels = False
gl.right_labels = False

# 5. Plot Surface Pressure Contours
# Standard surface pressure maps use 4mb intervals
p_min = np.floor(np.min(sfcP_mb))
p_max = np.ceil(np.max(sfcP_mb))
p_levels = np.arange(p_min, p_max, 4) 

p_contours = ax.contour(lons, lats, sfcP_mb, levels=p_levels, 
                        colors='black', linewidths=2, transform=ccrs.PlateCarree())

# Adding inline labels so you can read the pressure values
ax.clabel(p_contours, inline=True, fontsize=10, fmt='%1.0f') 

# 6. Plot Wind Barbs
# Thinning by 40 is too sparse for this zoomed-in map. 
# A step of 3 or 4 is much better for this regional view.
step = 4 
lat_thin = lats[::step, ::step]
lon_thin = lons[::step, ::step]
u_thin = u_knots[::step, ::step]
v_thin = v_knots[::step, ::step]

ax.barbs(lon_thin, lat_thin, u_thin, v_thin, length=5, transform=ccrs.PlateCarree())
import warnings
warnings.filterwarnings("ignore")
# 7. Title and Show
plt.title('Surface Pressure (mb) and 10m Wind Barbs (knots)')

plt.show()
#%%
#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import sounderpy as spy


okx_oct29_12z_sounding = spy.get_obs_data('OKX', '2012', '10', '29', '12')
spy.build_sounding(okx_oct29_12z_sounding)
okx_oct30_0z_sounding = spy.get_obs_data('OKX', '2012', '10', '30', '0')
spy.build_sounding(okx_oct30_0z_sounding, special_parcels=False)
okx_oct30_12z_sounding = spy.get_obs_data('OKX', '2012', '10', '30', '12')
spy.build_sounding(okx_oct30_12z_sounding)

#%%

import pandas as pd
import matplotlib.pyplot as plt

# Original data was manually filtered down to only have the needed columns as everything else was listed as NAN
sandy_buoy_data = pd.read_csv('buoy_data.csv')

# Combines the Date and time into one column and converts it to datatime
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
ax1.set_ylim(940, 1015)

# Temperature
# (sets the water temp and temp to the right y-axis and to share the right side y-axis that shares the same x-axis)
ax2 = ax1.twinx()
ax2.plot(sandy_buoy_data.index, sandy_buoy_data["Temp"], color="tab:red", label="Air Temp")
ax2.plot(sandy_buoy_data.index, sandy_buoy_data["Water Temp"], color="tab:green", label="Water Temp")
ax2.set_ylabel("Temperature (°C)")

# Legend
# (combines the axes so the meteogram shares the axes)
handles, labels = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles + handles2, labels + labels2)

plt.title("Atlantic City, NJ: Buoy Station ACYN4 Meteogram")
plt.show()



