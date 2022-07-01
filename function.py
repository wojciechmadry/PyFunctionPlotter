import scipy
import scipy.optimize
import scipy.integrate
from math import *
import numpy as np

def fix_check_function(MyFunc):
    """
    Replace 
    ^ to **
    , to .
    X to x
    """
    MyFunc = MyFunc.replace("^", "**")
    MyFunc = MyFunc.replace(",", ".")
    MyFunc = MyFunc.replace("X", "x")

    return MyFunc



class Function:
    """
    Store function and operation
    """
    def __init__(self, Func):
        self.__func = fix_check_function(Func)
        self.__funcR = '-('+self.__func+')'
        self.__callable = eval('lambda x: ' + self.__func)

    def reverse_X(self):
        """
        axis OX reflection
        """
        [self.__func, self.__funcR] = [self.__funcR, self.__func]
        self.__callable = eval('lambda x: ' + self.__func)

    def reverse_Y(self):
        """
        axis OY reflection
        """
        func = self.__callable
        self.__callable = lambda x: func(-x)

    def function_at(self, x):
        """
        Return value of function in point x.
        """
        try:
            return self.__callable(x)
        except:
            return None

    def at(self, x):
        """
        Return value of function in point x. same as function_at
        """
        return self.function_at(x)

    def function_value(self, a, b, step, tol = 10**-5):
        """
        Return 2 vector of x and y from a to b with step
        a > b && step > 0
        """
        if a >= b or step <= 0:
            raise Exception("Bad arguments value")
        result_x = []
        result_y = []
        while a <= b + tol:
            result_x.append(a)
            result_y.append(self.function_at(a))
            a += step
        return {"x":result_x, "y":result_y}

    @property
    def function(self):
        return self.__func

    @function.setter
    def function(self, NewFunction):
        self.__func = fix_check_function(NewFunction)
        self.__funcR = '-('+self.__func+')'
        self.__callable = eval('lambda x: ' + self.__func)

        
    def find_minimum(self, a, b, tol = 10**-5):
        """
        Find minimum in function
        """
        if a >= b:
            raise Exception(" A >= B")
        Minimum_left =  scipy.optimize.minimize(self.function_at, a, bounds=((a, b),), tol=tol)["x"][0]
        Minimum_mid =  scipy.optimize.minimize(self.function_at, (a+b)/2, bounds=((a, b),), tol=tol)["x"][0]
        Minimum_right =  scipy.optimize.minimize(self.function_at, b, bounds=((a, b),), tol=tol)["x"][0]
        fMinimum = self.function_at(Minimum_left)
        Minimum = Minimum_left
        new_f = self.function_at(Minimum_mid)
        if new_f < fMinimum:
            fMinimum = new_f
            Minimum = Minimum_mid
        new_f = self.function_at(Minimum_right)
        if new_f < fMinimum:
            fMinimum = new_f
            Minimum = Minimum_right
        return (Minimum, fMinimum)

    def find_root(self, a, b, tol = 10**-5, brute_force = True):
        """
        Find function root
        """
        try:
            root_x = scipy.optimize.bisect(self.function_at, a, b, rtol=tol, xtol=tol)
            return (root_x, self.function_at(root_x))
        except:
            try:
                if abs(self.function_at(0)) < tol:
                    return (0, self.function_at(0))
            except:
                return None
            if brute_force:
                while a <= b:
                    try:
                        if abs(self.function_at(a)) < tol:
                            return (a, self.function_at(a))
                        a+=tol
                    except:
                        a+= tol
            return None

    def find_maximum(self, a, b, tol = 10**-5):
        """
        Find maximum in function
        """
        if a >= b:
            raise Exception(" A >= B")
        maxi_left = scipy.optimize.minimize(lambda x: -self.function_at(x), a, bounds=((a, b),), tol=tol)["x"][0]
        maxi_mid = scipy.optimize.minimize(lambda x: -self.function_at(x), (a+b)/2, bounds=((a, b),), tol=tol)["x"][0]
        maxi_right = scipy.optimize.minimize(lambda x: -self.function_at(x), b, bounds=((a, b),), tol=tol)["x"][0]
        maxi=maxi_left
        fmax = self.function_at(maxi)
        f_new = self.function_at(maxi_mid)
        if f_new > fmax:
            fmax = f_new
            maxi = maxi_mid
        f_new = self.function_at(maxi_right)
        if f_new > fmax:
            fmax = f_new
            maxi = maxi_right
        return (maxi, fmax)
    def integral(self, a, b):
        """
         Calculation of the integral.
        """
        try:
            return scipy.integrate.quad(self.function_at,a, b)[0]
        except:
            return None





