#! usr/bin/env/python

import numpy as np
import os
import matplotlib.pyplot as plt

def mean(data):
    return(np.mean(data))

def heat_capacity(data, temp):
    return(np.var(data) / 2500 / temp)

def susceptibility(data, temp):
    return(np.var(magnets) / 2500 / temp**2)

def bootstrap_error(full_data, statistic, temp):
    statistics = []
    for sample_round in range(100):
        sample = []
        for i in range(len(full_data)):
            sample.append(full_data[np.random.randint(0,len(full_data))])
        statistics.append(statistic(sample, temp))
    return(np.var(statistics)**0.5)

temperatures = np.arange(1.0,3.1,0.1)

for dynamic in ["glauber","kawasaki"]:
    heat_capacities = []
    susceptibilities = []
    mean_energies = []
    mean_magnetizations = []
    heat_capacities_errors = []
    susceptibilities_errors = []
    for temp in temperatures:
        for root, dir, files in os.walk("dat/"):
            for filename in files:
                if str(temp) in filename and dynamic in filename:
                    data = np.loadtxt(root+filename,delimiter=", ")
                    energies, magnets = np.array(data[:,0]), np.array(data[:,1])
                    mean_energies.append(mean(energies))
                    mean_magnetizations.append(mean(magnets))
                    heat_capacities.append(heat_capacity(energies, temp))
                    heat_capacities_errors.append(bootstrap_error(energies, heat_capacity, temp))
                    susceptibilities.append(susceptibility(magnets, temp))
                    susceptibilities_errors.append(bootstrap_error(magnets, susceptibility,temp))


    plt.plot(temperatures,mean_energies)
    plt.xlabel("temperature")
    plt.ylabel("mean energy")
    plt.show()
    plt.plot(temperatures,mean_magnetizations)
    plt.xlabel("temperature")
    plt.ylabel("mean magnetization")
    plt.show()
    plt.errorbar(temperatures,heat_capacities,yerr=heat_capacities_errors)
    plt.xlabel("temperature")
    plt.ylabel("heat capacity")
    plt.show()
    plt.plot(temperatures,susceptibilities, yerr=susceptibilities_errors)
    plt.xlabel("temperature")
    plt.ylabel("susceptibility")
    plt.show()
