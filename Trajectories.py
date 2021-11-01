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

samples = 150                             #Sampling Rate Ts
y1 = np.linspace(-6.0, 6.0, samples)
y2 = np.linspace(-6.0, 6.0, samples)

Y1, Y2 = np.meshgrid(y1, y2)
t = 0
u, v = np.zeros(Y1.shape), np.zeros(Y2.shape)
Row, Col = Y1.shape

def f(Y, t):
    y1, y2 = Y
    return [(y2 - (y1* (y1*y1 + y2*y2 - 4))),(-y1-(y2 * (y1*y1 + y2*y2 - 4)))]  

for i in range(Row):
    for j in range(Col):
        x = Y1[i, j]
        y = Y2[i, j]
        yprime = f([x, y], t)
        u[i,j] = yprime[0]
        v[i,j] = yprime[1]

for k in [-5, 5, -2, 2]:                        #Points for Trajectories
    tspan = np.linspace(0, 5, 50)
    y0 = [2.0, k]                                  #Adjust the axis
    ys = odeint(f, y0, tspan)
   # plt.plot(ys[:,0], ys[:,1], 'b-')
    #plt.plot([ys[0,0]], [ys[0,1]], 'o') 
    #plt.plot([ys[-1,0]], [ys[-1,1]], 's')  

plt.xlabel('Y1')
plt.ylabel('Y2')
plt.title('Phase Plot trajectory of Y1 and Y2')
plt.xlim([-6, 6])
plt.ylim([-6, 6])
widths = np.linspace(0, 1, Y1.size)
plt.quiver(Y1, Y2, u, v, linewidths=widths, color='r')
plt.show() 
