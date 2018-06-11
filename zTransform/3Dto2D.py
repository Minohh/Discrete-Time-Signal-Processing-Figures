import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

omega = np.arange(-np.pi,np.pi,np.pi/100)
r = 1
x = r*np.cos(omega)
y = r*np.sin(omega)
z = np.where(abs(omega)<1.5,1,0)
ax.plot(x,y,z, color='b')

plt.show()
