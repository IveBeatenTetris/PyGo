# import stuff
import pygame as pg
from .utils import *
import os
# declaring working path
PATH_TILES = os.getcwd() + "\\assets\\tiles"
class Tile(pg.sprite.Sprite):
    """Get control of every tile with names, materials, sizes and so on."""
    def __init__(self, config={}):
        """Constructor."""
        self.config = config
        pg.sprite.Sprite.__init__(self)
        self.image = config["image"]
        self.id = config["id"] + 1
    def __repr__(self):
        """String replacement."""
        return "<Tile(" + str(self.id) + ")>"

def load(name):
    """Load a Map object and return it."""
    path = PATH_TILES + "\\" + name

    for each in os.walk(path):
        for each in each[2]:
            if each.split(".")[1] == "json":
                js = loadJSON(path + "\\" + each)

    return Tile(js)
