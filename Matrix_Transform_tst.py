import numpy as np
import math
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1)
x_list = [x/1000000 for x in range(0,1000000)]
y_list = [1/math.sqrt(1-((x/1000000)**2)) for x in range(0,1000000)]
plt.plot(x_list,y_list)
plt.axis([0,1,0,8])
plt.grid(which="major",linestyle="-",color="blue")
plt.minorticks_on()
plt.grid(which="minor",linestyle=":",color="black")
plt.show()
