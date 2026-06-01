#mandelbrot.py
from math import log

class MandelbrotSet:

    def __init__(self, max_iterations, escape_radius):
        self.max_iterations = max_iterations
        self.escape_radius = escape_radius
        return None

    def __contains__(self, c: complex) -> bool:
        return self.stability(c) == 1

    def stability(self, c: complex, smooth = False, clamp = True) -> float:
        value = self.escapecount(c, smooth) / self.max_iterations
        return max(0.0, min(value, 1.0)) if clamp else value

    def escapecount(self, c: complex, smooth=False):
        z = 0
        for iteration in range(self.max_iterations):
            z = z ** 2 + c
            if abs(z) > self.escape_radius:
                if smooth:
                    return iteration + 1 - log(log(abs(z))) / log(2)
                return iteration
        return self.max_iterations
