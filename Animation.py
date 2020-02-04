import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Animation(object):
    """
    Animation wrapper for an arbitrary simulation which takes place on a 2D
    lattice. Recieves a simulation object, assuming it has an attribute "lattice"
    which has type 2darray and which is plottable by pyplot.imshow(), and which
    is updated in a separate thread. Animates the lattice when the run() method
    is called, returns nothing. 
    """

    def __init__(self, **kwargs):

        self.simulation = kwargs.get("simulation")
        self.max_iter = kwargs.get("max_iter")

    def animate(self, *args):
        """
            Steps the simulation forward by attempting 1000 spin flips.
            Takes *args for call by animation.FuncAnimation instance.
            # TODO: Make make number of attempted spin flips configurable!
            # TODO: Determine the purpose of the trailing comma in return().
        """
        self.image.set_array(self.simulation.lattice)
        return(self.image,)

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

        self.figure = plt.figure()
        self.image = plt.imshow(self.simulation.lattice, animated=True)

        # TODO: Make line wrapping PEP8 compliant, here.
        self.animation = animation.FuncAnimation(self.figure, self.animate,
                                                frames=self.max_iter,
                                                repeat=False,
                                                interval=50, blit=True
                                                )
        plt.show()

    def exportAnimation(self, filename, dotsPerInch):
        """
            Exports the animation to a .gif file without compression. (Linux
            distributions with package "imagemagick" only. Files can be large!)
            # TODO: rename this for PEP8 compliance and add support for other
            image writing packages.
        """
        self.animation.save(filename, dpi=dotsPerInch, writer="imagemagick")
