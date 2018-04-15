from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm    # NEU!

fig = figure()
ax1 = fig.add_subplot(1,2,1, projection='3d')
ax2 = fig.add_subplot(1,2,2, projection='3d')

x = frange(1,10,1)
X, Y = meshgrid(x,x)

ax1.plot_wireframe(X,Y,X+Y)
surf = ax2.plot_surface(X,Y,X+Y, cmap=cm.jet, cstride=1,rstride=1, linewidth=0)
fig.colorbar(surf)
show()
