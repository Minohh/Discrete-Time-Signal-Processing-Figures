import numpy as np
import matplotlib.pyplot as plt

def axesCross(ax):
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.yaxis.set_ticks([])
    ax.set_xlim(-5, 5)
    ax.set_ylim(-.1, 2.2)
    ax.xaxis.set_ticks([-4, -2, 0, 2, 4])
    ax.xaxis.set_ticklabels([r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$"])

def periodization(f, T, times, ax=None):
    limit = np.floor(T*times/2)
    x = np.arange(-limit, limit, .02)
    sumY = 0
    for n in np.arange(times):
        y1 = f(x-T*n)
        sumY = sumY + y1
        if ax is not None:
            ax.plot(x, y1, color='C0', linestyle=':')
            ax.fill_between(x, 0, y1, facecolor='#999999', alpha=.5)

        if n != 0:
            y2 = f(x+T*n)
            sumY = sumY + y2
            if ax is not None:
                ax.plot(x, y2, color='C0', linestyle=':')
                ax.fill_between(x, 0, y2, facecolor='#999999', alpha=.5)
    return x, sumY


# the tick 2 is pi
f = lambda x: np.where(np.abs(x)<2, .5*np.sqrt(4-x**2), 0)
f2 = lambda x:f(.5*x)
lowpass = lambda x: np.where(np.abs(x)<1, 1, 0)
highpass = lambda x: np.where(np.abs(x)<1, 0, np.where(np.abs(x)<2, 1, 0))

fig = plt.figure(figsize=(9,12), dpi=120)
(ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8), (ax9, ax10), (ax11, ax12) = fig.subplots(6, 2)

x, y = periodization(f, 4, 10)
lx, ly = periodization(lowpass, 4, 10)
hx, hy = periodization(highpass, 4, 10)

axesCross(ax1)
ax1.plot(x, y)
ax1.fill_between(x, 0, y, color='C0', alpha=.3)
ax1.plot(lx, ly, color='r')
ax1.annotate(r"$X(e^{j\omega})$", xy=(0, 0), xytext=(-5, 2), color='C0')
ax1.annotate(r"$lowpass\ filter\ H_0(e^{j\omega})$", xy=(0, 0), xytext=(-3, 2), color='r')

axesCross(ax2)
ax2.plot(x, y)
ax2.fill_between(x, 0, y, color='C0', alpha=.3)
ax2.plot(hx, hy, color='r')
ax2.annotate(r"$X(e^{j\omega})$", xy=(0, 0), xytext=(-5, 2), color='C0')
ax2.annotate(r"$highpass\ filter\ H_1(e^{j\omega})$", xy=(0, 0), xytext=(-3, 2), color='r')

axesCross(ax3)
ax3.plot(x, y*ly)
ax3.fill_between(x, 0, y*ly, color='C0', alpha=.3)
ax3.annotate(r"$low\ band=X(e^{j\omega})H_0(e^{j\omega})$", xy=(0, 0), xytext=(-5, 2), color='C0')

axesCross(ax4)
ax4.plot(x, y*hy)
ax4.fill_between(x, 0, y*hy, color='C0', alpha=.3)
ax4.annotate(r"$high\ band=X(e^{j\omega})H_1(e^{j\omega})$", xy=(0, 0), xytext=(-5, 2), color='C0')

axesCross(ax5)
x51 = x*2
y51 = .5*ly*y
x52 = (x+4/2)*2
ax5.plot(x51, y51)
ax5.plot(x52, y51)
ax5.fill_between(x51, 0, y51, color='C0', alpha=.3)
ax5.fill_between(x52, 0, y51, color='C1', alpha=.3)
ax5.annotate(r"$V_0(e^{j\omega}) = compress\ low\ band\ with\ 2$", xy=(0, 0), xytext=(-5, 2), color='C0')

axesCross(ax6)
x61 = x*2
y61 = .5*hy*y
x62 = (x+4/2)*2
ax6.plot(x61, y61)
ax6.plot(x62, y61)
ax6.fill_between(x61, 0, y61, color='C0', alpha=.3)
ax6.fill_between(x62, 0, y61, color='C1', alpha=.3)
ax6.annotate(r"$V_1(e^{j\omega})=compress\ high\ band\ with\ 2$", xy=(0, 0), xytext=(-5, 2), color='C0')

axesCross(ax7)
x71 = x
y71 = .5*ly*y
x72 = x+4/2
ax7.plot(x71, y71)
ax7.plot(x72, y71)
ax7.fill_between(x71, 0, y71, color='C0', alpha=.3)
ax7.fill_between(x72, 0, y71, color='C1', alpha=.3)
ax7.annotate(r"$V_0(e^{2j\omega}) = expand\ V_0(e^{j\omega})\ with\ 2$", xy=(0, 0), xytext=(-5, 2), color='C0')

axesCross(ax8)
x81 = x
y81 = .5*hy*y
x82 = x+4/2
ax8.plot(x81, y81)
ax8.plot(x82, y81)
ax8.fill_between(x81, 0, y81, color='C0', alpha=.3)
ax8.fill_between(x82, 0, y81, color='C1', alpha=.3)
ax8.annotate(r"$V_1(e^{2j\omega}) = expand\ V_1(e^{j\omega})\ with\ 2$", xy=(0, 0), xytext=(-5, 2), color='C0')

axesCross(ax9)
x91 = x
y91 = .5*ly*y
x92 = x+4/2
ax9.plot(x91, y91)
ax9.plot(x92, y91)
ax9.plot(lx, 2*ly, color='r')
ax9.fill_between(x91, 0, y91, color='C0', alpha=.3)
ax9.fill_between(x92, 0, y91, color='C1', alpha=.3)
ax9.annotate(r"$lowpass\ filter\ G_0(e^{j\omega})$", xy=(0, 0), xytext=(-5, 2), color='r')

axesCross(ax10)
x101 = x
y101 = .5*hy*y
x102 = x+4/2
ax10.plot(x101, y101)
ax10.plot(x102, y101)
ax10.plot(hx, 2*hy, color='r')
ax10.fill_between(x101, 0, y101, color='C0', alpha=.3)
ax10.fill_between(x102, 0, y101, color='C1', alpha=.3)
ax10.annotate(r"$highpass\ filter\ G_1(e^{j\omega})$", xy=(0, 0), xytext=(-5, 2), color='r')

axesCross(ax11)
ax11.plot(x, y*ly)
ax11.fill_between(x, 0, y*ly, color='C0', alpha=.3)
ax11.annotate(r"$Y_0(e^{j\omega}) = V_0(e^{2j\omega})G_0(e^{j\omega})$", xy=(0, 0), xytext=(-5, 2), color='C0')

axesCross(ax12)
ax12.plot(x, y*hy)
ax12.fill_between(x, 0, y*hy, color='C0', alpha=.3)
ax12.annotate(r"$Y_1(e^{j\omega}) = V_1(e^{2j\omega})G_1(e^{j\omega})$", xy=(0, 0), xytext=(-5, 2), color='C0')

plt.show()
fig.savefig("DualSpectrum.png", format='png')
