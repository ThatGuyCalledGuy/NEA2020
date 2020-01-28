#Polar Coordinates
import numpy as np
import matplotlib.pyplot as plt

#x = rcosth
#y = rsinth

#ax.grid(which="major",linestyle="-",color="black")
#ax.minorticks_on()
#ax.grid(which="minor",linestyle=":",color="black")

n = 2001

f = 4

ax = plt.subplot(111)#,projection='polar')

r = lambda theta: 15*np.cos(sum([(theta/x) for x in range(1,1000)]))
#r = lambda theta: np.cos(3*theta)

theta = np.arange(0,128*np.pi,0.005)

xs = (r(theta))  * np.cos(theta)
ys = (r(theta))  * np.sin(theta)
#f = lambda x: (x**3) * np.log(x)

#xs = [x/100 for x in range(1000)]
#ys = [f(x/100) for x in range(1000)]



ax.set_aspect(1)
#ax.axhline(y=0, color="k")
#ax.axvline(x=0, color="k")
#ax.axis([-1.5,1.5,-1.5,1.5])
#ax.grid(which="major",linestyle="-",color="blue")
#ax.minorticks_on()
#ax.grid(which="minor",linestyle=":",color="black")



ax.plot(xs,ys)

#if cartesian
#plt.axis([-1.25,1.25,-1.25,1.25])
#plt.axis([-5,5,-5,5])

#if projection = polar
#ax.set_rmax(2)
#ax.set_rticks([0.5,1,1.5,2])

plt.show()