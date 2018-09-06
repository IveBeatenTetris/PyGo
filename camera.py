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
    """
    The camera is used for correctly draw everything on the window screen.
    You should use the camera as position agrument to draw a map, layer or just
    everything that's static and not really moving.
    The 'getRectOf' method acts exactly the same way except it's for everything
    thats non-static and CAN move like player, npcs and so on.
    """
    # default values
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
        pg.Rect.__init__(self, self.config["position"], self.config["size"])
        self.tracking = self.config["track"]# none / entity
        self.zoomfactor = self.config["zoomfactor"]# int
    def __str__(self):
        """String representation."""
        return "<Camera({0}, {1}, {2}, {3})>".format(
            self.left,
            self.top,
            self.width,
            self.height,
            )
    def update(self):
        """Update the camera with each tick."""
        if self.tracking:
            self.left = -(self.tracking.rect.center[0] - int(self.width / 2))
            self.top = -(self.tracking.rect.center[1] - int(self.height / 2))
    def getRectOf(self, entity):
        """
        Recalculate the position of the given entity on the map and return it
        in a pygame.rect, so one can use that rect to finally draw the entity
        in right place on the map.
        """
        return pg.Rect(
            entity.rect.left + self.left,
            entity.rect.top + self.top,
            entity.rect.width,
            entity.rect.height
            )
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
