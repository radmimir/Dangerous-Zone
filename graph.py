import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy

def makeData ():
    x = numpy.arange (-10, 10, 0.1)
    y = numpy.arange (-10, 10, 0.1)
    xgrid, ygrid = numpy.meshgrid(x, y)
    zgrid = numpy.sin (xgrid) * numpy.sin (ygrid) / (xgrid * ygrid)
    return xgrid, ygrid, zgrid

x, y, z = makeData()

fig = pylab.figure()
axes = Axes3D(fig)

axes.plot_surface(x, y, z)

pylab.show()
def find_dx(mass,min,max):
    nmin=32555
    dx = (max-min)/20.0
    x=min
    n=0
    x1=min
    x2=x1+dx
    for i in 0,mass.size:
        if mass[i]<x2 and mass[i]>=x1:
            n=n+1
            if n>5:
                x1=x1+dx
                x2 = x2+dx
                n=0
        else :
            x1=x1+dx
            x2 = x2+dx
            if n<nmin:
                nmin=n
            if n<3:
                dx=dx*1.5
                i=0
                x1=min
                x2=x1+dx
                nmin=32555
            n=0



