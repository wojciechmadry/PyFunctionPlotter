import numpy as np
import plot
def MonteCarlo(Function, a, b, n, draw):
    """
    Calculate and draw(optionally) monte carlo integral.
    Draw circles.
    """
    if n <= 0:
        raise Exception("n <= 0")
    if a >= b:
        raise Exception("a >= b")
    def where(f, x, y):
        fx = f(x)
        if 0 < y <= fx or  0 > y > fx:
            if fx > 0:
                return 1
            return 2
        return 0
    gt0 = 0
    lt0 = 0
    ydown = min(0, Function.find_minimum(a, b)[1])
    yup = max(0, Function.find_maximum(a, b)[1])
    RX = a + np.random.uniform(size=n) * ( b - a )
    RY = ydown + np.random.uniform(size=n) * (yup-ydown)
    for (rx, ry) in zip(RX, RY):
        isFit =  where(Function.function_at, rx, ry)
        if isFit >= 1:
            if draw:
                plot.draw_point((rx, ry),marker="or", fillstyle='none')
            if isFit == 1:
                gt0 += 1
            else:
                lt0 += 1
        elif draw:
            plot.draw_point((rx, ry),marker='ob', fillstyle='none')
    return ((b - a)*(gt0-lt0)*(yup-ydown))/n
