from Ising_Lattice import Ising_Lattice

simulation = Ising_Lattice(temperature=1.5, size=(50,50), mode="r")

simulation.run(dynamic="kawasaki", animate=False, max_iter=10000)
