from PIL import Image
import matplotlib.cm
from mandelbrot import MandelbrotSet
from plane import Viewport


def paint(mandelbrotset, viewport, colormap, smooth):
    for pixel in viewport:
        stability = mandelbrotset.stability(complex(pixel), smooth)
        index = int(min(stability * len(colormap), len(colormap) - 1))
        pixel.color = colormap[index % len(colormap)]

def toInteger(colormap):
    return [
        tuple(int(channel * 255) for channel in color)
        for color in colormap
    ]

colormap = matplotlib.cm.get_cmap("magma").colors
newcolormap = toInteger(colormap)

mandelbrotset = MandelbrotSet(max_iterations = 100, escape_radius = 1000)#wait around 30s for it to load
image = Image.new(mode = "RGB", size = (2048, 2048))
viewport = Viewport(image, center = 0 + 0j, width = 3)
paint(mandelbrotset, viewport, newcolormap, smooth=True)
image.show()