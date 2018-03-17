from math import sqrt, pi, sin, cos, atan, radians, degrees
import numpy as np
import matplotlib.pyplot as plt


def show_image(im, axis=False, grid=False, flipy=False):
    """Display PIL.Image in jupyter notebook using matplotlib.

    Note that new new jupyter notebooks can display PIL.Images themselves. This
    function can be still useful for debugging (using axis and grid options).
    """
    ax = plt.subplot()
    ax.grid(grid)
    if not axis:
        ax.axis('off')
    if flipy:
        plt.ylim(0, im.size[1]-1)
    plt.imshow(np.asarray(im))


class VectorImage:
    def __init__(self, size=5, axis=False):
        plt.figure(figsize=[size,size])
        if not axis:
            plt.axis('off')
        plt.axis('equal')

    def line(self, start, end):
        plt.plot([start[0], end[0]], [start[1], end[1]], 'k-')

    def save(self, name):
        """To save as SVG, simply use name ending with '.svg'
        """
        plt.savefig(name)


# TODO: return Turtle for better chaining e.g `turtle.forward(10).left(20)`
# (+ jupyter display to omit show)
# TODO: `forward(d, draw=False)` instead of using penup/pendown
class Turtle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0  # in radians
        self.is_pendown = True
        self.lines = []

    def forward(self, distance):
        nx = self.x + cos(self.angle) * distance
        ny = self.y + sin(self.angle) * distance
        if self.is_pendown:
            self.lines.append(([self.x, self.y], [nx, ny]))
        self.x = nx
        self.y = ny

    def back(self, distance):
        self.forward(-distance)

    def left(self, degrees):
        radians = degrees * pi/180
        self.angle += radians

    def right(self, degrees):
        self.left(-degrees)

    def penup(self):
        self.is_pendown = False

    def pendown(self):
        self.is_pendown = True

    def show(self, size=5, axis=False):
        im = VectorImage(size=size, axis=axis)
        for start, end in self.lines:
            im.line(start, end)
