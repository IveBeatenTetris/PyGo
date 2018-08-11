import pygame as pg
from .utils import draw, validateDict, drawBorder, scale
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
        pg.Surface.__init__(self, self.size, pg.SRCALPHA)# pygame Surface
        self.rect = self.get_rect()# pygame rect
        self.tracking = self.config["track"]
        self.screen = pg.Surface(self.size, pg.SRCALPHA)# pygame surface
        self.screenrect = self.screen.get_rect()# pygame rect
        self.scaled = pg.Surface((
                self.rect.width * self.config["scale"],
                self.rect.height * self.config["scale"]
            ),
            pg.SRCALPHA
            )
        self.scaledrect = self.scaled.get_rect()# pygame rect
        self.border = drawBorder(self.rect, self.config["border"])
    def capture(self, object, position=(0, 0)):
        """Drawing a surface to the Camera."""
        if type(object) is list:
            for each in object:
                if type(each) is Map:
                    # resizing the camera's screen-surface
                    er = each.rect
                    sr = self.screenrect
                    if er.width > sr.width or er.height > sr.height:
                        self.screen = pg.Surface(er.size, pg.SRCALPHA)
                        #self.screenrect = self.screen.get_rect()
                    # drawing layers to the temp surface
                    draw(each, self.screen, each.rect.topleft)
                if type(each) is Player:
                    # centering the player
                    draw(each, self.screen, (
                        self.rect.center[0] - int(each.rect.width / 2),
                        self.rect.center[1] - int(each.rect.height / 2)
                    ))
        # drawing a border around the camera
        draw(self.border, self.screen, self.screenrect)

        if self.config["scale"] > 1:
            self.scaled = scale(self.screen, self.config["scale"])
            draw(self.scaled, self, self.rect)
        else:

            draw(self.screen, self)
