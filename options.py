import manager as mg

class Option:
    """
    Plot options.
    """
    def __init__(self):
        self.man = mg.Manager() # Function manager
        self.xline = False # Draw axis x? = 0
        self.yline = False # Draw axos y? = 0
        self.step = 0.5 # Step (smaller = more accurate)
        self.fmin = False # Mark the minimum?
        self.fmax = False # Mark the maximum?
        self.froot = False # Mark the root?
        self.monte = False # Draw monte carlo method? (circles)
        self.rectangle = False # Draw rectangle method? (rectangles)
        self.n_monte = 10 # How much points to draw in monte carlo method.
        self.width_rect = 1 # Rectangle width to draw in rectangle method
        self.horiz = False # Reflect X?
        self.verti = False # Reflect Y?

        self.Min = None # Found minimum
        self.Max = None # Found maximum
        self.Root = None # Found root
        self.Integral = None # Integral value
        self.MonteIntegral = None # Monte Carlo Integral
        self.RectangleIntegral = None # Rectangle method integral

    def set_a(self, a):
        """
        Set new range a
        """
        self.man.a = a

    def set_b(self, b):
        """
        Set new range b
        """
        self.man.b = b

    def set_func(self, func):
        """
        Set new function
        """
        self.man.new_function(func)

    def clear(self):
        """
        Clear plot
        """
        self.man.clear()
        self.man.save_plot("plot.png")

    def plot(self, prgbar):
        """
        Draw plot with all picked options
        """
        def add():
            # 100/11 = 9
            prgbar.setValue(prgbar.value() + 9)

        add()#1
        if self.horiz:
            self.man.mirror_horizontal()
        if self.verti:
            self.man.mirror_vertical()
        add()#2
        if self.xline:
            self.man.draw_xLine()
        if self.yline:
            self.man.draw_yLine()
        add()#3
        self.Min = self.man.fMin(self.fmin)
        add()#4
        self.Max = self.man.fMax(self.fmax)
        add()#5
        self.Root = self.man.fRoot(self.froot)
        add()#6
        self.Integral = self.man.integral()
        add()#7
        self.MonteIntegral = self.man.MonteCarlo(self.n_monte, self.monte)
        add()#8
        self.RectangleIntegral = self.man.RectangleMethod(self.width_rect, self.rectangle)
        add()#9
        self.man.draw_plot(self.step)
        add()#10
        self.man.save_plot("plot.png")
        add()#11
        return {"min":self.Min, "max":self.Max, "root":self.Root, "integral":self.Integral, "monte":self.MonteIntegral, "rect":self.RectangleIntegral}
