import function 
import plot
import numpy as np

import integral_montecarlo as montecarlo
import rectangle_method


class Manager:
    """
    Function manager
    Range of a, b and approximation tol.
    base_color - Responsible for diferent color for diferent functions
    """
    base_color = ['b', 'g', 'r', 'c', 'm', 'y']
    base_id = 0
    def __init__(self, func="x^2", a=-10, b=10, tol=10**-5):
        self.__func = function.Function(func)
        self.__a = a
        self.__b = b
        self.__tol = tol
        self.__id = Manager.base_id
        Manager.base_id = (Manager.base_id+1)%len(Manager.base_color)
        
    @property
    def a(self):
        return self.__a
    @a.setter

    def a(self, new_value):
        self.__a = new_value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, new_value):
        self.__b = new_value

    @property
    def tol(self):
        return self.__tol

    @tol.setter
    def tol(self, new_value):
        if new_value > 0.1:
            self.__tol = 0.1
        else:
            self.__tol = new_value

    @property
    def function(self):
        return self.__func.function

    def new_function(self, NewFunction):
        """
        Update function and change mark color
        """
        self.__id = Manager.base_id
        Manager.base_id = (Manager.base_id+1)%len(Manager.base_color)
        self.__func.function = NewFunction

    def clear(self):
        """
        Reset plot
        """
        plot.reset()

    def draw_plot(self, step = 0.1):
        """
        Draw main plot
        """
        plot.graph(self.__func, self.__a, self.__b, step, self.__tol)

    def draw_xLine(self):
        """
        Draw x line (x = 0)
        """
        plot.draw_x_line()

    def draw_yLine(self):
        """
        Draw y line (y = 0)
        """
        plot.draw_y_line()

    def fMin(self, drawIt = False, text = None):
        """
        Find minimum
        return : (x, y)
        """
        marker = Manager.base_color[self.__id]+'o'
        minxy = self.__func.find_minimum(self.__a, self.__b, self.__tol)
        if drawIt:
            if text == None:
                plot.draw_point(minxy, marker, "Min")
            else:
                plot.draw_point(minxy, marker, text)
        return minxy

    def fRoot(self, drawIt = False, text = None):
        """
        Find root (x0)
        return : (x, y) or None
        """
        marker = Manager.base_color[self.__id]+'o'
        root = self.__func.find_root(self.__a, self.__b, self.__tol)
        if root != None and drawIt:
            if text == None:
                plot.draw_point(root, marker, "x0")
            else:
                plot.draw_point(root, marker, text)
        return root

    def fMax(self,  drawIt = False, text = None):
        """
        Find maximum
        return : (x, y)
        """
        marker = Manager.base_color[self.__id]+'o'
        maxxy = self.__func.find_maximum(self.__a, self.__b, self.__tol)
        if drawIt:
            if text == None:
                plot.draw_point(maxxy, marker, "Max")
            else:
                plot.draw_point(maxxy, marker, text)
        return maxxy

    def integral(self, a = None, b = None):
        """
        Calculation of the integral on the range: self.a self.b lub a, b
        """
        if ( a == b or a >= b ) and a != None:
            raise Exception("a == b or a >= b")
        elif a == None and b != None:
            raise Exception("If a is None, b must have too")
        elif b == None and a != None:
            raise Exception("If b is None, a must have too")
        elif b != None and a != None:
                return self.__func.integral(a, b)
        return self.__func.integral(self.__a, self.__b)

    def MonteCarlo(self, n, draw = True):
        """
        Return integral monte carlo (its calculate area under plot).
        Draw circle on plot
        """
        if n <= 0:
            raise Exception(" n <= 0")
        return montecarlo.MonteCarlo(self.__func, self.__a, self.__b, n, draw)
    
    def RectangleMethod(self, width, draw = True):
        """
        Return integral rectangle method (its calculate area under plot).
        Draw rectangle on plot
        """
        if width <= 0:
            raise Exception(" width <= 0")
        elif not isinstance(width, int):
            raise Exception(" Width is not a integer")

        return rectangle_method.rectangle_method(self.__func, self.__a, self.__b, width, draw)
    
    def save_plot(self, Filename):
        """
        Save plot to file
        """
        plot.save_as(Filename)
    
    def mirror_horizontal(self):
        """
        Horizontal reflection
        """
        self.__func.reverse_X()
    
    def mirror_vertical(self):
        """
        Vertical reflection
        """
        self.__func.reverse_Y()
