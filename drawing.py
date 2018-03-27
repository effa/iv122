from math import sqrt, pi, sin, cos, atan, radians, degrees
import numpy as np
import matplotlib.pyplot as plt


def show_image(im, axis=False, grid=False, flipy=False, size=6):
    """Display PIL.Image in jupyter notebook using matplotlib.

    Note that new new jupyter notebooks can display PIL.Images themselves. This
    function can be still useful for debugging (using axis and grid options).
    """
    plt.figure(figsize=[size,size])
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

    def line(self, start, end, linewidth=1.0):
        plt.plot([start[0], end[0]], [start[1], end[1]], 'k-', linewidth=linewidth)
        return self

    def lines(self, lines):
        for line in lines:
            self.line(*line)
        return self

    def point(self, point, color='k'):
        plt.plot([point[0]], [point[1]], color + 'o')
        return self

    def points(self, points, color='k'):
        for point in points:
            self.point(point, color=color)
        return self

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

    def forward(self, distance, linewidth=1.0):
        nx = self.x + cos(self.angle) * distance
        ny = self.y + sin(self.angle) * distance
        if self.is_pendown:
            self.lines.append(([self.x, self.y], [nx, ny], linewidth))
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

    def show(self, size=5, axis=False, im=None):
        im = im or VectorImage(size=size, axis=axis)
        for start, end, linewidth in self.lines:
            im.line(start, end, linewidth=linewidth)
