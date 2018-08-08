import pygame as pg
from .utils import draw, validateDict, drawBorder
from .player import Player
from .map import Map
# default values
default = {
    #"size": (1200, 650),
    "size": (640, 480),
    "position": (0, 0),
    "border": [1, "solid", (255, 255, 255)],
    "scale": 2,
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
        self.tracking = self.config["track"]
        #self.rect.topleft = self.config["position"]# tuple
        self.screen = pg.Surface(self.size, pg.SRCALPHA)# pygame surface
        self.border = drawBorder(self.rect, self.config["border"])
    def capture(self, object, position=(0, 0)):
        """Drawing a surface to the Camera."""
        if type(object) is Map:
            draw(object, self.screen, object.rect)
        if type(object) is Player:
            draw(object, self.screen, self.rect.center)

        draw(self.screen, self)
