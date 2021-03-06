from math import sqrt, pi, sin, cos, atan, radians, degrees
import numpy as np
import matplotlib.pyplot as plt


def show_image(im, axis=False, grid=False, flipy=False, size=6):
    """Display PIL.Image in jupyter notebook using matplotlib.

    Note that new jupyter notebooks can display PIL.Images themselves. This
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
        #plt.figure(figsize=[size,size])
        self.fig, self.ax = plt.subplots(figsize=(size, size))
        if not axis:
            self.ax.set_axis_off()  # plt.axis('off')
        self.ax.set_aspect('equal')  # plt.axis('equal')


    def line(self, start, end, color='k', **kwargs):
        self.ax.plot([start[0], end[0]], [start[1], end[1]], '-', color=color, **kwargs)
        return self

    def lines(self, lines, **kwargs):
        for line in lines:
            self.line(*line, **kwargs)
        return self

    def point(self, point, color='k', **kwargs):
        self.ax.plot([point[0]], [point[1]], color=color, marker='o', **kwargs)
        return self

    def points(self, points, color='k'):
        for point in points:
            self.ax.point(point, color=color)
        return self

    def clear(self):
        self.ax.clear()

    def save(self, name):
        """To save as SVG, simply use name ending with '.svg'
        """
        self.fig.savefig(name)  # plt.savefig(name)


# TODO: return Turtle for better chaining e.g `turtle.forward(10).left(20)`
# (+ jupyter display to omit show)
class Turtle:
    def __init__(self, angle=0):
        """Initial angle is in degrees.
        """
        self.x = 0
        self.y = 0
        self.angle = radians(angle)
        self.is_pendown = True
        self.lines = []

    @property
    def state(self):
        return (self.x, self.y, self.angle)

    @state.setter
    def state(self, xya):
        self.x, self.y, self.angle = xya

    def forward(self, distance, draw=True, color='k', linewidth=1.0):
        nx = self.x + cos(self.angle) * distance
        ny = self.y + sin(self.angle) * distance
        if self.is_pendown and draw:
            self.lines.append(([self.x, self.y], [nx, ny], color, linewidth))
        self.x = nx
        self.y = ny

    def back(self, distance, draw=True):
        self.forward(-distance, draw=draw)

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
        for start, end, color, linewidth in self.lines:
            im.line(start, end, color=color, linewidth=linewidth)
