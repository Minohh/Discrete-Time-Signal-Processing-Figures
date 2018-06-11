from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import cmath
from scipy import special

#angle coordinate
#f = lambda z: (abs(z)==1 and ((cmath.phase(z)>-1.5 and cmath.phase(z)<1.5) and 1 or 0) or 0)
f = lambda z: abs(special.ndtr(z))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax = fig.gca(projection='3d')

r = np.arange(0, 2, 0.03125)
omega = np.arange(-np.pi, np.pi, np.pi/32)
R,Omega = np.meshgrid(r,omega)
xn,yn = R.shape
W = R*0
X = R*0
Y = R*0
for xk in range(xn):
    for yk in range(yn):
        try:
            z = R[xk,yk]*cmath.exp(Omega[xk,yk]*1j)
            X[xk,yk] = z.real
            Y[xk,yk] = z.imag
            w = float(f(z))
            if w!=w:
                raise ValueError
            W[xk,yk] = w
        except (ValueError, TypeError, ZeroDivisionError):
            pass
#    print xk, xn
print xn,yn

#custom draw surface
poly3d = np.zeros((xn*(yn-1), 4, 3))

for yk in range(yn-1):
    for xk in range(xn):
        itr = yk*xn+xk
        if xk==xn-1:
            poly3d[itr,:,:] = [[X[xk, yk]   , Y[xk, yk]   , W[xk, yk]  ],
                               [X[0, yk]    , Y[0, yk]    , W[0, yk]   ], 
                               [X[0, yk+1]  , Y[0, yk+1]  , W[0, yk+1] ], 
                               [X[xk, yk+1] , Y[xk, yk+1] , W[xk, yk+1]]]
        else:
            poly3d[itr,:,:] = [[X[xk, yk]     , Y[xk, yk]     , W[xk, yk]    ],
                               [X[xk+1, yk]   , Y[xk+1, yk]   , W[xk+1, yk]  ], 
                               [X[xk+1, yk+1] , Y[xk+1, yk+1] , W[xk+1, yk+1]], 
                               [X[xk, yk+1]   , Y[xk, yk+1]   , W[xk, yk+1]  ]]

plt.xlim(-2.1,2.1)
plt.ylim(-2.1,2.1)
ax.add_collection3d(Poly3DCollection(poly3d, facecolors='#77dd77', linewidths=1,alpha=.5))
ax.add_collection3d(Line3DCollection(poly3d, colors='k', linewidths=.2))


#ax.plot_surface(X, Y, W, rstride=1, cstride=1, cmap=cm.jet)
#ax.plot_wireframe(X, Y, W, rstride=5, cstride=5)
#ax.contourf(X, Y, W, zdir='z', offset=-1, cmap=cm.coolwarm)

plt.show()
