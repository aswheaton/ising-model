#! usr/bin/env/python

import numpy as np
import os
import matplotlib.pyplot as plt

def mean(data):
    return(np.mean(data))

def heat_capacity(data, temp):
    return(np.var(data) / 2500.0 / temp**2)

def susceptibility(data, temp):
    return(np.var(magnets) / 2500.0 / temp)

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
                    susceptibilities_errors.append(bootstrap_error(magnets, susceptibility, temp))

    fig, axes = plt.subplots(2,2)
    fig.suptitle(dynamic+" dynamics")
    axes[0,0].plot(temperatures,mean_energies)
    axes[0,1].plot(temperatures,mean_magnetizations)
    axes[1,0].errorbar(temperatures,heat_capacities,yerr=heat_capacities_errors)
    axes[1,1].errorbar(temperatures,susceptibilities, yerr=susceptibilities_errors)
    axes[0,0].set(ylabel="mean energy")
    axes[0,1].set(ylabel="mean magnetization")
    axes[1,0].set(ylabel="heat capacity")
    axes[1,1].set(ylabel="susceptibility")
    axes[1,0].set(xlabel="temperature")
    axes[1,1].set(xlabel="temperature")
    plt.show()
