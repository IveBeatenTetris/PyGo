from .utils import(
    PATH,
    validateDict,
    createTiledMap,
    loadJSON,
    perPixelAlpha
    )
from .tileset import Tileset
import pygame as pg

default = {
    "name": "NoName",
    "width": 50,
    "height": 50,
    "tilewidth": 10,
    "tileheight": 10,
    "tilesets": {},
    "layers": {}
}

class Map(pg.Surface):
    """A Map object generated from a tiled-map."""
    def __init__(self, config={}):
        """Constructor."""
        self.config = validateDict(config, default)# dict
        self.name = self.config["name"]# str
        self.size = (self.config["width"], self.config["height"])# tuple
        self.tilesize = (self.config["tilewidth"], self.config["tileheight"])# tuple
        self.tilesets = self.__createTilesets()# dict
        self.tiles = self.getTiles()# list
        self.layers = self.__createLayers()# dict
        pg.Surface.__init__(
                self, (
                    self.size[0] * self.tilesize[0],
                    self.size[1] * self.tilesize[1]
                )
            )
        self.rect = self.get_rect()# pygame.rect
        # blit each surface to a layer
        for each in self.layers:
            self.blit(self.layers[each], (0, 0))
    def __repr__(self):# str
        """String representation."""
        return "<Map('{0}', {1})>".format(self.name, str(self.size))
    def __createTilesets(self):# dict
        """Create a dict of tileset-configs and return it."""
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
            tmap = createTiledMap(each, self.tiles)
            # //TODO make layer a dict with several attributes
            layer = tmap["image"]
            blocks = tmap["blocks"]
            # exception for layer 'shadows'
            if each["name"] == "shadows":
                layer = perPixelAlpha(layer, 50)
            # updating layers
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
