#! usr/bin/env/python

import numpy as np
import os
import matplotlib.pyplot as plt

temperatures = np.arange(1.0,3.1,0.1)
specific_heats = []
susceptibilities = []

for dynamic in ["glauber"]:
    for temp in temperatures:
        for root, dir, files in os.walk("dat/"):
            for filename in files:
                if str(temp) in filename and dynamic in filename:
                    data = np.loadtxt(root+filename,delimiter=", ")
                    energies, magnets = np.array(data[:,0]), np.array(data[:,1])
                    specific_heats.append(np.var(energies) / 2500 / temp)
                    susceptibilities.append(np.var(magnets) / 2500 / temp**2)

plt.plot(temperatures,specific_heats)
plt.show()

plt.plot(temperatures,susceptibilities)
plt.show()
