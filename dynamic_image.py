"""
=================
An animated image
=================

Animation of an image.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def updatefig(*args):
    global x, y
    x += np.pi / 15.
    y += np.pi / 20.
    im.set_array(f(x, y))
    return im,

def f(x, y):
    return np.sin(x) + np.cos(y)

x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)

fig = plt.figure()
im = plt.imshow(f(x, y), animated=True)

ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
plt.show()
