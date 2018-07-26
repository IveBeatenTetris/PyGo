# import stuff
import pygame as pg
from .utils import *
import os
# declaring working path
asset_path = os.getcwd() + "\\assets\\maps"
# class object
class Map:
    """."""
    def __init__(self, config={}):
        """Constructor."""
        self.config = config# dict
        self.name = config["name"]# str
        self.tilesize = (config["tilewidth"], config["tileheight"])# tuple
        self.size = (config["width"], config["height"])# tuple
        self.layers = self.__createLayers()# list
    def __createLayers(self):# list
        """Create a list of pygame-surface layers and return it."""
        layers = []

        for each in self.config["layers"]:
            width = self.size[0] * self.tilesize[0]
            height = self.size[1] * self.tilesize[1]
            layer = pg.Surface((width, height))
            layers.append(layer)

        return layers
    def __str__(self):
        """String representation."""
        name = self.config["name"]
        size = (str(self.size[0]), str(self.size[1]))

        return "<Map(" + name + " " + size[0] + "x" + size[1] + ")>"

def load(name):
    """Load a Map object and return it."""
    path = asset_path + "\\" + name

    for each in os.walk(path):
        for each in each[2]:
            if each.split(".")[1] == "json":
                js = loadJSON(path + "\\" + each)
                js.update({"name": name})

    return Map(js)
