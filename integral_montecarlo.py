import random as rnd
import numpy as np
import plot
def MonteCarlo(Function, a, b, n, draw):
    """
    Calculate and draw(optionally) monte carlo integral.
    Draw circles.
    """
    if n <= 0:
        raise Exception("n <= 0")
    elif a >= b:
        raise Exception("a >= b")
    def where(f, x, y):
        fx = f(x)
        if ( y > 0 and y <= fx ) or (y < 0 and y > fx):
            return 1
        return 0
    included = 0
    ydown = min(0, Function.find_minimum(a, b)[1])
    yup = max(0, Function.find_maximum(a, b)[1])
    RX = a + np.random.uniform(size=n) * ( b - a )
    RY = ydown + np.random.uniform(size=n) * (yup-ydown)
    if draw:
        for i in range(len(RX)):
            if where( Function.function_at, RX[i], RY[i] ) == 1:
                plot.draw_point((RX[i], RY[i]),marker="or", fillstyle='none')
                included += 1
            else:
                plot.draw_point((RX[i], RY[i]),marker='ob', fillstyle='none')
    else:
        for i in range(len(RX)):
            included += where( Function.function_at, RX[i], RY[i])
    integral = (included/n)*((b-a)*(yup-ydown))
    return integral


