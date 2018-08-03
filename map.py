import pygame as pg
from .config import PATH
from .utils import loadJSON, perPixelAlpha
from .tileset import Tileset

class Map(pg.Surface):
    """."""
    def __init__(self, config={}):
        """Constructor."""
        self.config = config# dict
        self.name = config["name"]# str
        self.size = (config["width"], config["height"])# tuple
        self.tilesize = (config["tilewidth"], config["tileheight"])# tuple
        self.tilesets = self.__createTilesets()# dict
        self.tiles = self.getTiles()# list
        self.layers = self.__createLayers()# dict

        pg.Surface.__init__(
            self, (
                self.size[0] * self.tilesize[0],
                self.size[1] * self.tilesize[1]
            )
        )
        self.rect = self.get_rect()

        # blit each surface to a layer
        for each in self.layers:
            self.blit(self.layers[each], (0, 0))
    def __repr__(self):# str
        """String representation."""
        return "<Map" + str(self.size) + ">"
    def __createTilesets(self):# dict
        """Create a dict of tileset-objects from the config and return it."""
        tilesets = {}

        for cfg in self.config["tilesets"]:
            split = cfg["source"].split("/")
            name = split[-2]
            file = split[-1]
            path = PATH["tilesets"] + "\\" + name + "\\" + file
            config = loadJSON(path)
            tilesets.update({name: Tileset(config)})

        return tilesets
    def __createLayers(self):# dict
        """."""
        layers = {}

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
                    if each["data"][i] != 0:
                        layer.blit(self.tiles[each["data"][i] - 1].image, (x, y))
                    i = i + 1

            # exception for layer 'shadows'
            if each["name"] == "shadows":
                layer = perPixelAlpha(layer, 50)

            layers.update({each["name"]: layer})

        return layers
    def getTiles(self):# list
        """Get tile objects from every appended tileset and return them in one
        single list."""
        tiles = []

        for k, v in self.tilesets.items():
            for tile in v.tiles:
                tiles.append(tile)

        return tiles
