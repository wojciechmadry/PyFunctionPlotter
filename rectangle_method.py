import plot

def rectangle_method(Function, a, b, width, draw):
    """
    Calculate recaangle method
    """
    try:
        area = 0
        height = 0
        a = int(a)
        b = int(b)
        if draw :
            for i in range(a, b-width, width):
                height = Function.at(i)
                if height != None:
                    area += abs(height*width)
                    if draw :
                        plot.draw_point((i, height), marker='-rx')
                        plot.draw_rectangle(i, 0, width, height)
            height = Function.at(b -width + b%width)
            if height != None:
                plot.draw_point((b -width + b%width, height), marker='-rx')
                plot.draw_rectangle(b-width + b%width, 0, width - b%width, height)
        else:
            for i in range(a, b-width, width):
                height = Function.at(i)
                if height != None:
                    area += abs(height*width)
            height = Function.at(b)
        area += abs(height *  (width - b%width))
        return area
    except:
        return None

