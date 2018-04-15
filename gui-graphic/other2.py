from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax  = Axes3D(fig)
x = rand(20)
y = rand(20)
ax.plot(x, y, x+y, '.')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
show()
