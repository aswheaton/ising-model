from Ising_Lattice import Ising_Lattice
from Animation import Animation
import matplotlib.pyplot as plt

simulation = Ising_Lattice(temperature=1.5, size=(100,100), mode="r", animate=True)
simulation.run(dynamic="kawasaki")
animation = Animation(simulation=simulation, max_iter=10000)
animation.run()
