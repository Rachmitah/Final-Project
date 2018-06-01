import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

# PANJANG   = 60
# LEBAR     = 40

def array6x4(zz):
    x = np.arange(0,6,1)
    y = np.arange(0,4,1)
    xs, ys = np.meshgrid(x, y)
    zs = xs**2 + ys**2
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(xs, ys, zz, rstride=1, cstride=1, cmap=cm.viridis)
    plt.show()

