
import matplotlib.pyplot as plt
import numpy as np

#def onpick(event):
#    object = event.artist
#    xdata = object.get_xdata()
#    ydata = object.get_ydata()
#    ind = event.ind
#    points = tuple(zip(xdata[ind], ydata[ind]))
#    print('onpick points:', points)

x = np.arange(0.0, 2.0, 0.01)
y = 1 + np.sin(2*np.pi*x)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('plt from docker with picker')
#ax.plot(x, y, '-o', picker=3)
ax.plot(x, y)

ax.set_xlabel('x')
ax.set_ylabel('1 + np.sin(2*np.pi*x)')
ax.grid(True)

#fig.canvas.mpl_connect('pick_event', onpick)

plt.savefig("y.png")
plt.show()

