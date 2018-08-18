from . utils import (
    PATH,
    validateDict
    )
import pygame as pg

class Tile(pg.sprite.Sprite):
    """Cut out sprite from an image (tileset). It also holds extra information
    about being blockable etc."""
    # default values
    default = {
        "image": "notile.png",
        "id": 0,
        "block": False,
        "visible": True
    }
    def __init__(self, config={}):
        """Constructor."""
        self.config = validateDict(config, self.default)# dict
        pg.sprite.Sprite.__init__(self)
        self.visible = self.config["visible"]# bool
        if type(self.config["image"]) is str:
            if self.config["image"] == "notile.png":
                self.image = pg.image.load("{0}\\{1}".format(# pygame.surface
                        PATH["sysimg"],
                        self.config["image"]
                    )
                )
        else:
            self.image = self.config["image"]# pygame.surface
        if self.visible is False:
            self.image = pg.Surface(self.image.get_rect().size, pg.SRCALPHA)# pygame.surface
        self.id = self.config["id"] + 1# int
        self.block = self.config["block"]# bool

    def __repr__(self):# str
        """String representation."""
        return "<Tile({0})>".format(self.id)
