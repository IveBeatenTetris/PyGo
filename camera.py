"""
The camera module is used to calculate positions of everything thats going
on a map. Use this pygame.rect to draw everything in relative positions to the
tracked object's position.
"""
# dependencies
from .utils import validateDict
import pygame as pg
# classes
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
        """
        Change the zoomfactor of the camera rect. Doesn't change the camera
        size.
        """
        if self.zoomfactor + factor < 1:
            self.zoomfactor = 1
        elif self.zoomfactor + factor > 3:
            self.zoomfactor = 3
        else:
            self.zoomfactor = self.zoomfactor + factor
