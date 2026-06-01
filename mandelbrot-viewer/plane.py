#plane.py
from PIL import Image

class Viewport:
    def __init__(self, image, center, width):
        self.image = image
        self.center = center
        self.width = width
        return None

    @property
    def height(self):
        return self.scale * self.image.height

    @property
    def offset(self):
        return self.center + complex(-self.width, self.height) / 2

    @property
    def scale(self):
        return self.width / self.image.width

    def __iter__(self):
        for y in range(self.image.height):
            for x in range(self.image.width):
                yield Pixel(self, x, y)

class Pixel:
    def __init__(self, viewport, x, y):
        self.viewport = viewport
        self.x = x
        self.y = y
        return None

    @property
    def color(self):
        return self.viewport.image.getpixel((self.x, self.y))

    @color.setter
    def color(self, value):
        self.viewport.image.putpixel((self.x, self.y), value)

    def __complex__(self):
        return (
                complex(self.x, -self.y)
                * self.viewport.scale
                + self.viewport.offset
        )