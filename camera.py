# dependencies
from .utils import (
    systemResolution,
    validateDict,
    draw,
    drawBorder,
    scale
    )
from .player import Player
from .map import Map
import pygame as pg

class Camera(pg.Rect):
    """docstring for Camera2."""
    default = {
        "size": (640, 480),
        "position": (0, 0),
        "border": None,
        "track": None,
        "zoomfactor": 1
        }
    def __init__(self, config={}):
        """Constructor."""
        self.config = validateDict(config, self.default)# dict
        self.size = self.config["size"]# tuple
        self.topleft = self.config["position"]# tuple
        self.track = self.config["track"]# none / object (pygame.surface)
        self.zoomfactor = self.config["zoomfactor"]# int
    def zoom(self, factor):
        """Change the zoomfactor of the camera rect. Doesn't change the camera
        size."""
        if self.zoomfactor + factor < 1:
            self.zoomfactor = 1
        elif self.zoomfactor + factor > 3:
            self.zoomfactor = 3
        else:
            self.zoomfactor = self.zoomfactor + factor

        # zoomfactor 4 holds a system specific resolution for the camera
        #if self.zoomfactor == 3:
            #self.size = [each / 2 for each in systemResolution()]
