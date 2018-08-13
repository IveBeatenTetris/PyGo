import pygame as pg
from .utils import (
    PATH,
    validateDict,
    getFrames
    )
from .tile import Tile

default = {
    "name": "NoName",
    "image": "notileset.png",
    "tilewidth": 16,
    "tileheight": 16
    }

class Tileset(pg.Surface):
    """Holds all tiles as single objects in a list. Also itself is a pygame
    surface for previewing purpose."""
    def __init__(self, config={}):
        """Constructor."""
        self.config = config# dict
        self.name = config["name"]# str
        if self.config["image"] == "noimage.png":
            self.path = PATH["sysimg"]# str
        else:
            self.path = "{0}\\{1}".format(PATH["tilesets"], self.name)# str
        self.imagepath = self.path + "\\" + self.config["image"]# str
        self.image = pg.image.load(self.imagepath)# pygame.surface
        pg.Surface.__init__(self, self.image.get_rect().size)

        self.tilesize = (config["tilewidth"], config["tileheight"])# tuple
        self.tiles = self.__createTiles()# list

        self.blit(self.image, (0, 0))
    def __repr__(self):# str
        """String representation."""
        return "<Tileset('{0}', tc={1})>".format(
            self.name,
            str(self.config["tilecount"])
            )
    def __createTiles(self):# list
        """Return a list of all tiles in the given tileset image."""
        tilelist = []

        for i, each in enumerate(getFrames(self.image, self.tilesize), 0):
            config = {
                "image": each,
                "id": i
                }
            tilelist.append(Tile(config))

        return tilelist
