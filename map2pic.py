"""
Read a raster file a numpy array with GDAL
IMG format files downloaded from The National Map
http://nationalmap.gov
Author: Kelsey Jordahl, Enthought, Vatlark
Scipy 2013 geospatial tutorial
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from osgeo import gdal

# GDAL does not use python exceptions by default
gdal.UseExceptions()

cwd = os.path.dirname(__file__)

img_n = os.path.join(os.path.split(cwd)[0],'ned19_n27x25_w082x50_fl_sarasota_2007', 'ned19_n27x25_w082x50_fl_sarasota_2007.img')
geo = gdal.Open(img_n)
drv = geo.GetDriver()
print drv.GetMetadataItem('DMD_LONGNAME')
topo = geo.ReadAsArray()
# i, j = np.where(topo>0)
# topo = topo[min(i):max(i)+1, min(j):max(j)+1]
# topo[topo==0] = np.nan
topo[topo<-1000] = 0
topo = topo[3000:5500,:3000]
print np.amin(topo)
print np.amax(topo)
print np.median(topo)
print topo.shape
#topo = topo[::2,::2]

print topo.shape


fig = plt.figure(frameon=False)
plt.imshow(topo, cmap=cm.gray)
plt.axis('off')
cbar = plt.colorbar(shrink=0.75)
cbar.set_label('meters')
plt.savefig('output.png', dpi=300, bbox_inches='tight')
plt.show()
