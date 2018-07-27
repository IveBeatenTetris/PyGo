# import stuff
import pygame as pg
from .utils import *
from .tiles import Tile
import os
# declaring working path
PATH_TILESETS = os.getcwd() + "\\assets\\tilesets"
# class object
class Tileset:
    """A tileset holds all tiles from an Image. It's NOT the actual tiled game
    map."""
    def __init__(self, config={}):
        """Constructor."""
        self.config = config# dict
        self.path = PATH_TILESETS + "\\" + config["name"]# str
        self.name = config["name"]# str
        self.tilesize = (config["tilewidth"], config["tileheight"])# tuple
        self.image = pg.image.load(self.path + "\\" + config["image"]).convert_alpha()
        self.tiles = self.__createTiles()
    def __str__(self):
        """String representation."""
        name = self.config["name"]

        return "<Tileset('" + name + "')>"
    def __repr__(self):
        """String replacement."""
        name = self.config["name"]

        return "<Tileset('" + name + "')>"
    def __createTiles(self):
        """Return a list of all tiles in the given tileset image."""
        rows = int(self.image.get_rect().height / self.tilesize[1])
        lines = int(self.image.get_rect().width / self.tilesize[0])
        rect = pg.Rect((0, 0), self.tilesize)
        tilelist = []

        i = 0
        for row in range(rows):
            y = row * self.tilesize[1]
            rect.top = y
            for line in range(lines):
                x = line * self.tilesize[0]
                rect.left = x

                self.image.set_clip(rect)
                clip = self.image.subsurface(self.image.get_clip())
                config = {
                    "image": clip,
                    "id": i
                    }
                tilelist.append(Tile(config))
                i = i + 1

        return tilelist

def load(name):
    """Load a Map object and return it."""
    path = PATH_TILESETS + "\\" + name

    for each in os.walk(path):
        for each in each[2]:
            if each.split(".")[1] == "json":
                js = loadJSON(path + "\\" + each)

    return Tileset(js)
