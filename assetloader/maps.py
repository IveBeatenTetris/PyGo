# import stuff
import pygame as pg
from .utils import *
from .tilesets import Tileset, PATH_TILESETS
import os
# declaring working path
PATH_MAPS = os.getcwd() + "\\assets\\maps"
# class object
class Map:
    """A Map object holds information about it's tilesets and has a separate
    list for all Tile object combined."""
    def __init__(self, config={}):
        """Constructor."""
        self.config = config# dict
        self.name = config["name"]# str
        self.tilesets = self.__createTilesets()# list
        self.tilesize = (config["tilewidth"], config["tileheight"])# tuple
        self.tiles = self.__createTileList()
        self.size = (config["width"], config["height"])# tuple
        self.layers = self.__createLayers()# list
        self.preview = self.__createPreview()# pygame surface
    def __str__(self):
        """String representation."""
        name = self.config["name"]
        size = (str(self.size[0]), str(self.size[1]))

        return "<Map('" + name + "' " + size[0] + "x" + size[1] + ")>"
    def __createTilesets(self):
        """Create a list of tileset objects from the config and return it."""
        tilesets = []

        for each in self.config["tilesets"]:
            path = os.path.abspath(
                PATH_TILESETS + each["source"].split("tilesets")[-1]
                )
            config = loadJSON(path)
            tilesets.append(Tileset(config))

        return tilesets# list
    def __createTileList(self):
        """Combine all Tile objects from each Tileset and return them in a
        list."""
        tiles = []

        for each in self.tilesets:
            for tile in each.tiles:
                tiles.append(tile)


        return tiles# list
    def __createLayers(self):# list
        """Create a list of pygame-surface layers and return it."""
        width = self.size[0] * self.tilesize[0]
        height = self.size[1] * self.tilesize[1]
        layers = []

        for each in self.config["layers"]:
            width = each["width"] * self.tilesize[0]
            height = each["height"] * self.tilesize[1]
            layer = pg.Surface((width, height), pg.SRCALPHA, 32)

            # drawing tiles on each layer
            i = 0
            for row in range(each["height"]):
                y = row * self.tilesize[1]
                for line in range(each["width"]):
                    x = line * self.tilesize[0]
                    # clean tile
                    if each["data"][i] == 0:
                        pass
                    else:
                        layer.blit(self.tiles[each["data"][i] - 1].image, (x, y))
                    i = i + 1

            layers.append(layer)

        return layers
    def __createPreview(self):# pygame surface
        """Create a preview of the rendered map by drawing every layer on a
        pygame surface."""
        width = self.size[0] * self.tilesize[0]
        height = self.size[1] * self.tilesize[1]
        preview = pg.Surface((width, height))

        for layer in self.layers:
            preview.blit(layer, (0, 0))
        #preview.blit(self.layers[0], (0, 0))
        #preview.blit(self.layers[1], (0, 0))

        return preview

def load(name):
    """Load a Map object and return it."""
    path = PATH_MAPS + "\\" + name

    for each in os.walk(path):
        for each in each[2]:
            if each.split(".")[1] == "json":
                js = loadJSON(path + "\\" + each)
                js.update({"name": name})

    return Map(js)
