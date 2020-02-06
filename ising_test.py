import sys
import numpy as np
import time

from Ising_Lattice import Ising_Lattice

temperatures = np.arange(1.0,3.1,0.1)

# tic = time.clock()

for temp in temperatures:

    simulation = Ising_Lattice(temperature=temp, size=(50,50), mode=sys.argv[2])
    simulation.run(dynamic=sys.argv[1], animate=False, max_iter=10000)

# toc = time.clock()
# print("Executed script in "+str(toc-tic)+" seconds.")
