#Kunal Khade
#Department of Electrical Engineering
#South Dakota School of Mines and Technology
#Date - November 5, 2019 5:30PM
#Robot Control System Lab-4
#Professor - Dr.Hoover

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

plt.axhline(0, linewidth=0.5, color='black')
plt.axvline(0, linewidth=0.5, color='black')

samples = int(60/4)
y1 = np.linspace(-2.0, 8.0, samples)
y2 = np.linspace(-2.0, 2.0, samples)

Y1, Y2 = np.meshgrid(y1, y2)

t = 0
u, v = np.zeros(Y1.shape), np.zeros(Y2.shape)
Row, Col = Y1.shape

g = -9.8
l = 5.0
m = 1.0
k = 0.5  #Constants

def f(Y, t):
    y1, y2 = Y

   # return [(y2),((g/l)*np.sin(y1)-((k/m)*(y2)))] #equation for inverted pendulum

   
for i in range(Row):
    for j in range(Col):
        x = Y1[i, j]
        y = Y2[i, j]
        yprime = f([x, y], t)
        u[i,j] = yprime[0]
        v[i,j] = yprime[1]
        


plt.xlabel('Y1')
plt.ylabel('Y2')
plt.title('Phase Plot of Y1 and Y2')
plt.xlim([-2, 8])
plt.ylim([-4, 4])

widths = np.linspace(0, 0.5, Y1.size)
plt.quiver(Y1, Y2, u, v, linewidths=widths, color='r', )

plt.show()
