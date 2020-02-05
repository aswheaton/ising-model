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
                    spec_heat, susc = np.var(data[99:,:],axis=0)
                    plt.plot(range(len(data[:,0])),data[:,0])
                    plt.show()
                    specific_heats.append(spec_heat)
                    susceptibilities.append(susc)

plt.plot(temperatures,specific_heats)
plt.show()

plt.plot(temperatures,susceptibilities)
plt.show()
