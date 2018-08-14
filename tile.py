from .utils import (
    PATH,
    validateDict
    )
import pygame as pg

default = {
    "image": "notile.png",
    "id": 0,
    "block": False
    }

class Tile(pg.sprite.Sprite):
    """Cut out sprite from an image (tileset). It also holds extra information
    about being blockable etc."""
    def __init__(self, config={}):
        """Constructor."""
        #self.config = validateDict(config, default)
        self.config = validateDict(config, default)# dict
        pg.sprite.Sprite.__init__(self)
        if type(self.config["image"]) is str:
            if self.config["image"] == "notile.png":
                self.image = pg.image.load("{0}\\{1}".format(# pygame.surface
                        PATH["sysimg"],
                        self.config["image"]
                    )
                )
        else:
            self.image = self.config["image"]# pygame.surface
        self.id = self.config["id"] + 1# int
    def __repr__(self):# str
        """String representation."""
        return "<Tile({0})>".format(self.id)
