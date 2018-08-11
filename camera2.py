import pygame as pg
from .utils import validateDict
from .player import Player
# default values
default = {
    #"size": (1200, 650),
    "size": (640, 480),
    "position": (0, 0),
    "border": [1, "solid", (255, 255, 255)],
    "scale": 2,
    "track": None
}

class Camera2(pg.Surface):
    """."""
    def __init__(self, config={}):
        """Constructor."""
        self.config = validateDict(config, default)# dict
        pg.Surface.__init__(self, self.config["size"], pg.SRCALPHA)# pygame Surface
        self.rect = self.get_rect()# pygame rect

        self.tracking = self.config["track"]# none/object
    def capture(self, object, position=(0, 0)):
        """."""
        if type(object) is list:
            for obj in object:
                if type(obj) is Player:
                    pass
