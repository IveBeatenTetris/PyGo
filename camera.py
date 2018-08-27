# dependencies
from .utils import (
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
    def move(self, pos=None):
        if pos:
            self.left += pos[0]
            self.top += pos[1]
        else:
            # look for tracked objects
            if self.track:
                # recalculate center if zoomed in
                if self.zoomfactor > 1:
                    self.center = [each * self.zoomfactor for each in self.track.rect.center]
                else:
                    self.center = self.track.rect.center
    def zoom(self, factor):
        """Change the zoomfactor of the camera rect. Doesn't change the camera
        size."""
        if self.zoomfactor + factor < 1:
            self.zoomfactor = 1
        elif self.zoomfactor + factor > 3:
            self.zoomfactor = 3
        else:
            self.zoomfactor = self.zoomfactor + factor
