import pygame as pg
from .utils import draw

class Camera(pg.Surface):
    """."""
    def __init__(self, config={}):
        """Constructor."""
        self.config = config# dict
        self.size = config["size"]# tuple
        pg.Surface.__init__(self, self.size, pg.SRCALPHA, 32)# pygame Surface
        self.drawBorder()
    def capture(self, object, position=(0, 0)):
        """Drawing a surface to the Camera."""
        draw(object, self, position)
        self.drawBorder()
    def drawBorder(self):
        """Drawing a border to visualize the cameras' space."""
        pg.draw.lines(
            self,
            (255, 0, 0),
            False,
            [
                (0, 0),
                (0, self.size[1] -1),
                (self.size[0] - 1, self.size[1] - 1),
                (self.size[0] - 1, 0),
                (0, 0)
            ],
            2
        )
