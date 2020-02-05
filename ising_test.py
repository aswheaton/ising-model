import numpy as np
from Ising_Lattice import Ising_Lattice
import time

temperatures = np.arange(1.0,3.1,0.1)

tic = time.clock()

for temp in temperatures:

    simulation = Ising_Lattice(temperature=temp, size=(50,50), mode="r")

    simulation.run(dynamic="kawasaki", animate=False, max_iter=10000)

toc = time.clock()
print("Executed script in "+str(toc-tic)+" seconds.")
