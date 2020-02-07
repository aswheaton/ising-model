import sys
import numpy as np
import time

from Ising_Lattice import Ising_Lattice

dynamic = sys.argv[1]
temp = float(sys.argv[2])
mode = sys.argv[3]
n = int(sys.argv[4])
m = int(sys.argv[5])



tic = time.clock()

temperatures = np.arange(1.0,3.1,0.1)

try:

    if sys.argv[6] == "animate":
        simulation = Ising_Lattice(temperature=temp, size=(n,m), mode=mode)
        simulation.run(dynamic=dynamic, animate=True, max_iter=10000)

except IndexError:
    
    if dynamic == "glauber":
        for temp in temperatures:
            simulation = Ising_Lattice(temperature=temp, size=(n,m), mode=mode)
            simulation.run(dynamic=dynamic, animate=False, max_iter=10000)

    if dynamic == "kawasaki":
        simulation = Ising_Lattice(temperature=temp, size=(n,m), mode=mode)
        for temp in temperatures:
            simulation.temp = temp
            simulation.run(dynamic=dynamic, animate=False, max_iter=10000)

toc = time.clock()
print("Executed script in "+str(toc-tic)+" seconds.")
