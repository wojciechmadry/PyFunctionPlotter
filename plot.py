import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

def graph(Function, a, b, step, tol=10**-5):
    """
    Draw plot
    """
    Vectors = Function.function_value(a, b, step, tol)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.plot(Vectors["x"], Vectors["y"])

def save_as(Filename):
    """
    Save plot to file
    """
    plt.gcf().savefig(Filename)


def draw_x_line(linestyle='--', color='black'):
    """
    Draw line in x = 0
    """
    plt.axline((-1, 0), (1, 0), linestyle=linestyle, color=color)

def draw_y_line(linestyle='--', color='black'):
    """
    Draw line in y = 0
    """
    plt.axline((0, 1), (0, -1), linestyle=linestyle, color=color)

def reset():
    """
    Clear plot
    """
    plt.close()
    plt.figure()

def draw_point(xy, marker = 'o', text = None, fillstyle='full'):
    """
    Mark the point
    """
    if xy == None or len(xy) != 2:
        raise Exception(" len(xy) != 2 or xy == None ")
    plt.plot(xy[0], xy[1], marker, fillstyle=fillstyle)
    if text != None:
        plt.annotate(text, (xy[0], xy[1]))

def draw_scatter(xy, s, facecolors, edgecolors):
    """
    Mark the point(slower)
    """
    plt.scatter(xy[0], xy[1], s=s, facecolors=facecolors, edgecolors=edgecolors)

def draw_rectangle(x, y, width, height):
    """
    Draw rectangle
    """
    plt.plot((x, x+width), (y, y), 'r')
    plt.plot((x, x+width), (y+height, y+height), 'r')
    plt.plot((x, x), (y, y+height), 'r')
    plt.plot((x+width, x+width),(y, y+height), 'r')
