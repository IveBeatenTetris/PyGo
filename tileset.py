# dependencies
from .utils import (
    PATH,
    validateDict,
    getFrames,
    draw
    )
from .tile import Tile
import pygame as pg

class Tileset:
    """Holds all tiles as single objects in a list."""
    # default values
    default = {
        "name": "NoTileset",
        "image": "notileset.png",
        "tilewidth": 16,
        "tileheight": 16,
        "tilecount": 0,
        "tileproperties": {}
        }
    def __init__(self, config={}):
        """Constructor."""
        self.config = validateDict(config, self.default)# dict
        self.name = self.config["name"]# str
        if self.config["image"] == "notileset.png":
            path = PATH["sysimg"]
        else:
            path = "{0}\\{1}".format(PATH["tilesets"], self.name)
        self.path = path# str
        self.imagepath = self.path + "\\" + self.config["image"]# str
        self.image = pg.image.load(self.imagepath)# pygame.surface
        self.tilesize = (# tuple
            self.config["tilewidth"],
            self.config["tileheight"]
            )
        self.tiles = self.__createTiles()# list
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
            # this is food for a new tile object
            config = {
                "image": each,
                "id": i,
                }

            # additional properties
            if "tileproperties" in self.config:
                props = self.config["tileproperties"]
                if str(i) in props:

                    # block passable?
                    try:
                        config["block"] = props[str(i)]["block"]
                    except KeyError:
                        pass
                    # block visibility
                    try:
                        config["visible"] = props[str(i)]["visible"]
                    except KeyError:
                        pass

            # appending to the resulting list
            tilelist.append(Tile(config))

        return tilelist
