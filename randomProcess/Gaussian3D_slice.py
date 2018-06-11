import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

def get_XStatic_XYZ_Points(xPosition, surface):
    lineY = np.arange(-limit, limit, .02)
    lineX = np.full(lineY.shape, xPosition)
    z = surface(lineX, lineY)
    return lineX, lineY, z


def cross_Section(xPosition, surface, ax, color='C6'):
    lineX, lineY, z = get_XStatic_XYZ_Points(xPosition, surface)

    poly3DSize = np.size(lineX)
    poly3d = np.zeros((poly3DSize, 4, 3))
    for itr in np.arange(poly3DSize-1):
        poly3d[itr,:,:] = [[lineX[itr],   lineY[itr],   0        ],
                           [lineX[itr+1], lineY[itr+1], 0        ],
                           [lineX[itr+1], lineY[itr+1], z[itr+1] ],
                           [lineX[itr],   lineY[itr],   z[itr]   ]]
    ax.add_collection3d(Poly3DCollection(poly3d, facecolors=color, linewidths=1, alpha=.3))
    ax.add_collection3d(Line3DCollection(poly3d, colors=color, linewidths=.2))

limit = 2

fig = plt.figure(figsize=(10, 4), dpi=120)
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
ax1.set_xlim(-limit, limit)
ax1.set_ylim(-limit, limit)
ax1.set_zlim(0, .2)
ax2.set_xlim(-limit, limit)
ax2.set_ylim(-limit, limit)
ax2.set_zlim(0, .2)

ax1.xaxis.set_ticks([-1, 0, 1])
ax1.yaxis.set_ticks([-1, 0, 1])
ax1.zaxis.set_ticks([])
ax2.xaxis.set_ticks([-1, 0, 1])
ax2.yaxis.set_ticks([-1, 0, 1])
ax2.zaxis.set_ticks([])

sigmaX = 1
sigmaY = 1
expectX = 0
expectY = 0
rho = .3
c = 1.0/(2*np.pi*sigmaX*sigmaY*np.sqrt(1-rho**2))
q = lambda u, v: 1.0/2*np.pi*(1-rho**2)*(v**2-2*rho*u*v+u**2)
pdfGaussian = lambda x, y: c*np.exp(-q(1.0*(x-expectX)/sigmaX, 1.0*(y-expectY)/sigmaY))

x = np.arange(-limit, limit, .02)
y = np.arange(-limit, limit, .02)
X, Y = np.meshgrid(x, y)
ZPDF = pdfGaussian(X, Y)

internal = .4
for x_Pos in np.arange(-limit+internal, limit, internal):
    lineX, lineY, lineZ = get_XStatic_XYZ_Points(x_Pos, pdfGaussian)
    ax1.plot3D(lineX, lineY, np.full(lineX.shape, 0), color='k')
    ax1.plot3D(lineX, lineY, lineZ, color='r')
ax1.plot_surface(X, Y, ZPDF, cmap=cm.BrBG, alpha=.7)

i = 0
for x_Pos in np.arange(-limit+internal, limit, internal):
    #lineX, lineY, lineZ = get_XStatic_XYZ_Points(x_Pos, pdfGaussian)
    #ax2.plot3D(lineX, lineY, lineZ, color='r')
    cross_Section(x_Pos, pdfGaussian, ax2, 'C'+str(i))
    i += 1

fig.text(.27, .03, r"$f_{X,Y}(x,y)$")
fig.text(.63, .03, r"$f_{X,Y}(x=0, y),\ f_{X,Y}(x=\pm 0.4, y),\cdot\cdot\cdot$")
plt.annotate(r'$f_{X,Y}(x=0,y)$', xytext=(.68, .8), xy=(.73, .62), bbox=dict(boxstyle='round,pad=.5', fc='C4', alpha=.5), xycoords='figure fraction', arrowprops=dict(arrowstyle='->'))
plt.annotate(r'$f_{Y|X}(y|x=0)$', xytext=(.85, .8), xy=(.77, .81), bbox=dict(boxstyle='round,pad=.5', fc='C4', alpha=.5), xycoords='figure fraction', arrowprops=dict(arrowstyle='<-'))
fig.text(.77, .82, "normalize")

fig.savefig("Gaussian3D_slice.png", format='png')
plt.show()
