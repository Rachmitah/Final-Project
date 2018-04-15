import numpy as np
import matplotlib.pyplot as plt

nrows, ncols = 1000, 1000
z = 500 * np.random.random(nrows * ncols).reshape((nrows, ncols))

plt.imshow(z, interpolation='nearest')
plt.colorbar()
plt.show()
