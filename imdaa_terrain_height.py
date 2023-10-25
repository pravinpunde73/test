#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from matplotlib import pyplot as plt
from wrf import getvar,ALL_TIMES
from netCDF4 import Dataset
import cartopy.crs as ccrs
import netCDF4 as nc
from netCDF4 import Dataset
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import pandas as pd
import cartopy as cart
import cartopy.crs as crs
from cartopy.feature import NaturalEarthFeature
import cartopy.feature as cfeature
import cartopy.crs as ccrs
import cartopy.mpl.ticker as cticker
from cartopy.util import add_cyclic_point
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature
import xarray as xr
# from sklearn.linear_model import LinearRegression
import numpy as np
# import metpy.calc as mpc
import matplotlib.pylab as plt
from matplotlib.patches import Polygon
# from metpy.units import units
# import metpy
from wrf import (to_np, getvar,interplevel, smooth2d, get_cartopy, cartopy_xlim,
                 cartopy_ylim, latlon_coords,ALL_TIMES)
from matplotlib.dates import MonthLocator, DateFormatter
import cmocean
import cartopy as cart
import cartopy.feature as cfeature
import cartopy.crs as ccrs
import cartopy.mpl.ticker as cticker
from cartopy.util import add_cyclic_point
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature
from matplotlib import rc,rcParams
import metpy
import metpy.calc as mpc


# In[14]:


plt.rcParams.update({'font.size': 7})
plt.rcParams['font.family'] = 'serif'
plt.rcParams['figure.dpi'] = 200
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"


# In[3]:


ds_01 = xr.open_dataset("/home/PDTC/PDTCCAIPEEX/caipeex_common/Pravin/IMDAA_Terrain_0101216.nc")


# In[19]:


ds_01.MTERH_sfc.shape


# In[43]:


rc('font', weight='bold')
fig, ax = plt.subplots(1,1, figsize=(11, 2), facecolor='w', edgecolor='k',subplot_kw=dict(projection=ccrs.PlateCarree()))
fig.subplots_adjust(hspace = .1, wspace=.05)



# fig.suptitle('Total precipitation on 03082019 00-18UTC ',fontsize=8,weight='bold',y=1.1)
# plot=[]
label='Solapur'
plot1=ax.contourf(ds_01.longitude[30:700], ds_01.latitude[5:490],ds_01.MTERH_sfc[1,5:490,30:700],30,cmap='terrain')
# ax.scatter(75.85,17.73,marker="*",label='solapur',s = 20,color ="k")
ax.plot([70, 70, 82, 82, 70],[28, 38, 38, 28, 28] ,
         color='black', linewidth=1,
         transform=ccrs.PlateCarree(), #remove this line to get straight lines
         )
# ax.set_title('THOM_AERO',fontsize=7,weight='bold')
ax.coastlines()
# plt.colorbar(plot0,ax=ax)
ax.set_ylabel('Latitude',fontsize=7)
ax.set_xlabel('Longitude',fontsize=7)
plt.colorbar(plot1)


# In[17]:


ds_01.longitude.shape


# In[18]:


ds_01.latitude.shape


# In[ ]:




