#! usr/bin/env/python

import numpy as np

from threading import Thread

class Ising_Lattice(object):
    """
        Ising model lattice class object. Takes keyword arguments:

        temperature = Float, the temperature of the lattice.
        size        = Tuple, the size of the lattice (n,m).
        mode        = String, can be "r" for random mode, "l" or "h".
        animate     = Boolean, whether or not to animate the simulation.
    """

    def __init__(self, **kwargs):
        self.temp = kwargs.get("temperature")
        self.size = kwargs.get("size")
        self.mode = kwargs.get("mode")
        self.anim = kwargs.get("animate")
        self.build()

    def build(self):
        """
            Creates a new class attribute of type ndarray and fills it with spin
            values, depending on the user specified mode.
        """
        if self.mode == "r":
            self.lattice = np.random.choice(a=[-1,1], size=self.size)
        if self.mode == "h":
            self.lattice = np.ones(self.size, dtype=int)
        if self.mode == "l":
            self.lattice = - np.ones(self.size, dtype=int)

    def bc(self, indices):
        """
            Determines if a pair of indices falls outside the boundary of the
            lattice and if so, applies a periodic (toroidal) boundary condition
            to return new indices.
        """
        return((indices[0]%self.size[0], indices[1]%self.size[1]))

    def delta_energy(self, indices):
        """
            Calculates and returns the change in energy from flipping a given
            of a given lattice site (n,m) due to spin interaction with its
            neighbors. Change in energy given by:

            E = - S_n,m * (S_n+1,m + Sn-1,m + S_n,m-1, + S_n,m+1)

            Four other lattice points enter this expression.
            # TODO: Verify this calculation!
        """
        n, m = indices
        # TODO: Make line wrapping PEP8 compliant, here.
        delta_energy = 2 * self.lattice[n,m] * (
                    self.lattice[self.bc((n-1, m))]
                    + self.lattice[self.bc((n+1,m))]
                    + self.lattice[self.bc((n, m-1))]
                    + self.lattice[self.bc((n, m+1))]
                    )
        return(delta_energy)

    def attempt_flip(self):
        """
            Randomly chooses a site on the lattice and tries to flip it.
            # TODO: Make line wrapping PEP8 compliant, here.
            # TODO: Move kawasaki/glauber differentiation into the delta_energy
            method.
        """
        if self.dyn == "glauber":
            indices = (np.random.randint(0, self.size[0]),
                        np.random.randint(0, self.size[1])
                        )
            if self.delta_energy(indices) <= 0.0:
                self.lattice[indices] *= -1
            elif np.random.rand() < np.exp(-self.delta_energy(indices) / self.temp):
                self.lattice[indices] *= -1

        elif self.dyn == "kawasaki":
            indices_i = (np.random.randint(0, self.size[0]),
                        np.random.randint(0, self.size[1])
                        )
            indices_j = (np.random.randint(0, self.size[0]),
                        np.random.randint(0, self.size[1])
                        )

            if self.lattice[indices_i] == -self.lattice[indices_j]:
                self.lattice[indices_j] *= -1
                i_energy = self.delta_energy(indices_i)
                self.lattice[indices_j] *= -1
                self.lattice[indices_i] *= -1
                j_energy = self.delta_energy(indices_j)

                delta_energy = i_energy + j_energy

                if delta_energy <= 0.0:
                    self.lattice[indices_j] *= 1
                elif np.random.rand() < np.exp(- delta_energy / self.temp):
                    self.lattice[indices_j] *= 1
                else:
                    self.lattice[indices_i] *= -1

    def magnetization(self):
        return(np.sum(self.lattice))

    def run(self, **kwargs):
        """
            Sets up a figure, image, and FuncAnimation instance, then runs the
            simulation to the specified maximum number of iterations.
            # TODO: Utilise the Boolean animate attribute here, and implement
            datafile output.
            # TODO: Make the number of Metropolis trials more understandable.
            (Currently number of attempted flips is more than those specified by
            the user by a factor of 10^3 due to the way animate() method works.)
        """

        self.dyn = kwargs.get("dynamic")
        simulation = Thread(target=self.attempt_flip)
        simulation.start()
