from . utils import(
    PATH,
    validateDict,
    createTiledMap,
    loadJSON,
    perPixelAlpha
    )
from . tileset import Tileset
import pygame as pg

class Map(pg.Surface):
    """A Map object generated from a tiled-map."""
    # default values
    default = {
        "name": "NoName",
        "width": 50,
        "height": 50,
        "tilewidth": 10,
        "tileheight": 10,
        "tilesets": {},
        "layers": {}
    }
    def __init__(self, config={}):
        """Constructor."""
        self.config = validateDict(config, self.default)# dict
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
        self.blocks = []# list
        for each in self.layers:
            # adding blockable positions from each layer
            self.blocks += self.layers[each]["blocks"]

            # draw each layer to surface
            self.blit(self.layers[each]["image"], (0, 0))
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
        """Return a dict of layers. Each layer is an own dict with several
        attributes."""
        layers = {}

        for each in self.config["layers"]:
            tmap = createTiledMap(each, self.tiles)

            # exception for layer 'shadows'
            if each["name"] == "shadows":
                tmap["image"] = perPixelAlpha(tmap["image"], 50)

            # updating layers
            layers.update({each["name"]: tmap})

        return layers
    def getTiles(self):# list
        """Get tile objects from every appended tileset and return them in one
        single list."""
        tiles = []

        for k, v in self.tilesets.items():
            for tile in v.tiles:
                tiles.append(tile)

        return tiles
