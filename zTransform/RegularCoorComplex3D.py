from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import cmath
import scipy.special as spl

#rectangular coordinate
#f = lambda z: abs(mpmath.loggamma(z))
#f = lambda z: arg2(mpmath.exp(z))
#f = lambda z: abs(mpmath.besselj(3,z))
#f = lambda z: (abs(z)==1 and ((cmath.phase(z)>-1.5 and cmath.phase(z)<1.5) and 1 or 0) or 0)
f = lambda z: abs(spl.ndtr(z))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = np.arange(-2, 2, 0.03125)
Y = np.arange(-2, 2, 0.03125)
X, Y = np.meshgrid(X, Y)
xn, yn = X.shape
W = X*0
for xk in range(xn):
    for yk in range(yn):
        try:
            z = complex(X[xk,yk],Y[xk,yk])
            w = float(f(z))
            if w != w:
                raise ValueError
            W[xk,yk] = w
        except (ValueError, TypeError, ZeroDivisionError):
            # can handle special values here
            pass

# can comment out one of these
ax.plot_surface(X, Y, W, rstride=1, cstride=1, cmap=cm.jet)
#ax.plot_wireframe(X, Y, W, rstride=5, cstride=5)

plt.show()

