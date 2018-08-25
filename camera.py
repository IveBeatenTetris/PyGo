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

class Camera2(pg.Rect):
    """docstring for Camera2."""
    default = {
        "size": (640, 480),
        "position": (0, 0),
        "border": None,
        "scale": 1,
        "track": None
        }
    def __init__(self, config={}):
        """Constructor."""
        self.config = validateDict(config, self.default)# dict
        self.size = self.config["size"]# tuple
        self.topleft = self.config["position"]# tuple
        print(self)
class Camera(pg.Surface):
    """Surface object to render all captured objects on."""
    # default values
    default = {
        "size": (640, 480),
        "border": None,
        "scale": 1,
        "track": None
        }
    def __init__(self, config={}):
        """Constructor."""
        self.config = validateDict(config, self.default)# dict
        pg.Surface.__init__(self, self.config["size"], pg.SRCALPHA)# pygame.surface
        self.rect = self.get_rect()# pygame.rect
        self.scale = self.config["scale"]# int
        self.tracking = self.config["track"]# none / object
        self.border = self.config["border"]# none / list / tuple
    def move(self, pos, anch=None):
        """Moving the camera rect to a specified position."""
        if type(anch) is str:
            if anch == "center":
                self.rect.center = pos
        else:
            self.rect.topleft = pos
    def capture(self, object, position=(0, 0)):
        """."""
        surface = pg.Surface(self.rect.size, pg.SRCALPHA)
        # drawing process depending on what to track
        if type(object) is list:
            for obj in object:
                if type(obj) is Map:
                    # centering the player if it has the camera's focus set
                    if type(self.tracking) is Player:
                        draw(obj, surface, (
                            -self.rect.left,
                            -self.rect.top
                            ))
                if type(obj) is Player:
                    # centering the player if it has the camera's focus set
                    if type(self.tracking) is Player:
                        self.move(obj.rect.center, "center")
                        draw(obj, surface, "center")
                if type(obj) is pg.Surface:
                    draw(obj, surface, (
                        -self.rect.left,
                        -self.rect.top
                        ))

        # drawing a border to viszualize the size
        if self.border:
            draw(drawBorder(self.rect, self.config["border"]), surface)

        # final drawing step
        if self.scale > 1:
            surface = scale(surface, self.scale)

            if self.rect.width < surface.get_rect().width or self.rect.height < surface.get_rect().height:
                pg.Surface.__init__(self, surface.get_rect().size, pg.SRCALPHA)

            # draw scaled surface at the center. Keep centered view
            if type(self.tracking) is Player:
                draw(surface, self, "center")
            else:
                draw(surface, self)
        else:
            draw(surface, self)
