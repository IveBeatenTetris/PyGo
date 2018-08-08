import pygame as pg
from .utils import draw, validateDict, drawBorder
# default values
default = {
    #"size": (1200, 650),
    "size": (640, 480),
    "position": (0, 0),
    "border": [1, "solid", (255, 255, 255)],
    "scale": 1,
    "track": None
}

class Camera(pg.Surface):
    """."""
    def __init__(self, config={}):
        """Constructor."""
        self.config = validateDict(config, default)# dict
        self.size = self.config["size"]# tuple
        pg.Surface.__init__(self, self.size, pg.SRCALPHA, 32)# pygame Surface
        self.rect = self.get_rect()# pygame rect
        self.rect.topleft = self.config["position"]# tuple
        self.border = drawBorder(self.rect, self.config["border"])
    def capture(self, object, position=(0, 0)):
        """Drawing a surface to the Camera."""
        surf = pg.Surface(self.size, pg.SRCALPHA, 32)
        draw(object, surf)
        draw(surf, self, position)
        draw(self.border, self)
    def track(self, object):
        """Track a given object by centering the camera to it's position."""
        #object.rect
        self.rect.topleft = object.rect.topleft
