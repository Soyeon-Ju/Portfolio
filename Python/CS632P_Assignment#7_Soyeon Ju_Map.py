import matplotlib.pyplot as plt

import cartopy.crs as ccrs
import cartopy
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER



ax = plt.axes(projection=ccrs.Mercator(central_longitude=70))



ax.coastlines(resolution='50m')

# gl =ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,linewidth=1, color='blue', alpha=0.5, linestyle='--')
ax.set_extent([-10, 5, 35, 45])

ax.add_feature(cartopy.feature.OCEAN, facecolor=("#37ffff"))
ax.add_feature(cartopy.feature.LAND, facecolor=("#ff6633"))



plt.show()
plt.savefig("/Users/soyeonju/Desktop/Map.png",dpi = 200)


