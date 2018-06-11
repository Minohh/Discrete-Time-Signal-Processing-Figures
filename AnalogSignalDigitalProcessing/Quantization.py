import matplotlib.pyplot as plt
import numpy as np
def rotate(point, midpoint, angle):
    difX = point[0] - midpoint[0]
    difY = point[1] - midpoint[1]
    rotatedDifX = difX*np.cos(angle) - difY*np.sin(angle)
    rotatedDifY = difY*np.cos(angle) + difX*np.sin(angle)
    
    rotatedPoint = (midpoint[0]+rotatedDifX, midpoint[1]+rotatedDifY)
    return rotatedPoint

def demention(text, midpoint, length, angle=0, color='k'):
    halfLength = 1.0*length/2
    xLeftEnd  = midpoint[0] - halfLength
    xRightEnd = midpoint[0] + halfLength
    yLeftEnd  = midpoint[1]
    yRightEnd = midpoint[1]

    t = ax.text(-1000, -1000, text)
    # get text box in pixel
    tbox = t.get_window_extent(renderer=fig.canvas.get_renderer())
    # convert box from pixel to coordinate
    dbox = tbox.transformed(ax.transData.inverted())
    textWidth  = dbox.x1-dbox.x0
    textHeight = dbox.y1-dbox.y0
    
    xText = midpoint[0] - textWidth/2
    yText = midpoint[1] - textHeight/3
    
    xLeftBegin  = midpoint[0] - textWidth/2
    xRightBegin = midpoint[0] + textWidth/2
    yLeftBegin  = midpoint[1]
    yRightBegin = midpoint[1]

    leftEdgeX1  = xLeftEnd
    leftEdgeX2  = xLeftEnd
    rightEdgeX1 = xRightEnd
    rightEdgeX2 = xRightEnd
    leftEdgeY1  = yLeftEnd - .5
    leftEdgeY2  = yLeftEnd + .5
    rightEdgeY1 = yLeftEnd - .5
    rightEdgeY2 = yLeftEnd + .5

    textPoint  = (xText, yText)
    leftBegin  = (xLeftBegin, yLeftBegin)
    rightBegin = (xRightBegin, yRightBegin)
    leftEnd    = (xLeftEnd, yLeftEnd)
    rightEnd   = (xRightEnd, yRightEnd)
    leftEdge1  = (leftEdgeX1, leftEdgeY1) 
    leftEdge2  = (leftEdgeX2, leftEdgeY2) 
    rightEdge1 = (rightEdgeX1, rightEdgeY1) 
    rightEdge2 = (rightEdgeX2, rightEdgeY2) 

    if(angle != 0):
        leftBegin  = rotate(leftBegin, midpoint, angle)
        rightBegin = rotate(rightBegin, midpoint, angle)
        leftEnd  = rotate(leftEnd, midpoint, angle)
        rightEnd = rotate(rightEnd, midpoint, angle)
        leftEdge1  = rotate(leftEdge1, midpoint, angle)
        leftEdge2  = rotate(leftEdge2, midpoint, angle)
        rightEdge1 = rotate(rightEdge1, midpoint, angle)
        rightEdge2 = rotate(rightEdge2, midpoint, angle)

    ax.text(xText, yText, text, color=color)
    ax.annotate("", xy=leftEnd, xytext=leftBegin, arrowprops=dict(arrowstyle='->', color=color))
    ax.annotate("", xy=rightEnd, xytext=rightBegin, arrowprops=dict(arrowstyle='->', color=color))
    ax.annotate("", xy=leftEdge1, xytext=leftEdge2, arrowprops=dict(arrowstyle='-', color=color))
    ax.annotate("", xy=rightEdge1, xytext=rightEdge2, arrowprops=dict(arrowstyle='-', color=color))

def axesCross(ax):
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.xaxis.set_ticks([-9, -7, -5, -3, -1, 1, 3, 5, 7, 9])
    ax.yaxis.set_ticks([-8, -6, -4, -2, 2, 4, 6, 8])
    ax.xaxis.set_ticklabels([r"$-\frac{9\Delta}{2}$", r"$-\frac{7\Delta}{2}$", r"$-\frac{5\Delta}{2}$",r"$-\frac{3\Delta}{2}$", r"$-\frac{\Delta}{2}$",\
                                r"$\frac{\Delta}{2}$", r"$\frac{3\Delta}{2}$", r"$\frac{5\Delta}{2}$", r"$\frac{7\Delta}{2}$", r"$\frac{9\Delta}{2}$"])
    ax.yaxis.set_ticklabels([r"$-4\Delta$", r"$-3\Delta$", r"$-2\Delta$", r"$-\Delta$", r"$\Delta$", r"$2\Delta$", r"$3\Delta$", r"$4\Delta$"])
    demention(r"$2X_m$", (-1, -9.5), 16, 0, color='C0')
    #demention("xx", (-1, -9.5), 16, np.pi/4)

fig = plt.figure(figsize=(5, 5), dpi=120)
ax = fig.subplots(1, 1)

T = 2
f = lambda x: np.where(x<-8, -8, np.where(x<6, np.floor((x+(T/2))/T)*T, 6))

x = np.arange(-9, 7, .02)
xlow = np.arange(-11, -9, .02)
xhigh = np.arange(7, 11, .02)
y = f(x)
ylow = f(xlow)
yhigh = f(xhigh)

axesCross(ax)
ax.plot(x, y)
ax.plot(xlow, ylow, color='C1')
ax.plot(xhigh, yhigh, color='C1')
ax.annotate(r"$x$", xy=(0, 0), xytext=(10, -1))
ax.annotate(r"$\hat{x}$", xy=(0, 0), xytext=(-1, 10))

fig.savefig("Quantization.png", format='png')
plt.show()
