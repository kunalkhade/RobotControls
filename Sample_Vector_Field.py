import matplotlib.pyplot as plt
import numpy as np
sin = np.sin
cos = np.cos

# http://stackoverflow.com/questions/6370742/#6372413
xmax = 4.0
xmin = -xmax
D = 20
ymax = 4.0
ymin = -ymax
x = np.linspace(xmin, xmax, D)
y = np.linspace(ymin, ymax, D)
X, Y = np.meshgrid(x, y)
# plots the vector field for Y'=Y**3-3*Y-X
deg = np.arctan(Y ** 3 - 3 * Y - X)
widths = np.linspace(0, 2, X.size)
plt.quiver(X, Y, cos(deg), sin(deg), linewidths=widths)
plt.show()
