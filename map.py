# dependencies
from .utils import(
    PATH,
    validateDict,
    createTiledMap,
    loadJSON,
    perPixelAlpha,
    draw
    )
from .tileset import Tileset
import pygame as pg

class Layer(pg.Surface):
    """A TiledLayer representation."""
    # default values
    default = {
        "blend": None
        }
    def __init__(self, config={}):
        """Constructor."""
        self.config = config# dict
        self.x = config["x"]# int
        self.y = config["y"]# int
        self.name = config["name"]# str
        self.data = config["data"]# list
        self.tiles = config["tiles"]# list
        self.blend = self.getBlendMode()# none / str / int
        self.width = config["width"] * config["tilesize"][0]# int
        self.height = config["height"] * config["tilesize"][1]# int
        self.blocks = []# list
        self.opacity = config["opacity"]# int
        self.visible = config["visible"]# bool

        pg.Surface.__init__(self, (self.width, self.height), pg.SRCALPHA)
        self.rect = self.get_rect()# pygame.rect
        self.rect.topleft = (self.x, self.y)# tuple

        # final build
        self._build()
    def __repr__(self):# str
        """String representation."""
        return "<Layer('{0}', {1})>".format(self.name, str(self.rect.size))
    def _build(self):
        """To keep __init__() clean."""
        tmap = createTiledMap(self.config, self.tiles)
        surface = tmap["image"]# pygame.surface
        self.blocks = tmap["blocks"]# list
        self._playerstart = tmap["playerstart"]# pygame.rect

        # render transparent layer if opacity is not 1.0 (standard)
        if self.opacity != 1:
            surface = perPixelAlpha(surface, self.opacity)

        # use blending mode if active
        if self.blend:
            if self.blend == "add":
                blend_mode = pg.BLEND_ADD
            elif self.blend == "sub":
                blend_mode = pg.BLEND_SUB
            elif self.blend == "multi":
                blend_mode = pg.BLEND_MULT

            draw(surface, surface, blendmode = blend_mode)

        # drawing map to layer surface
        draw(surface, self, self.rect)
    def getBlendMode(self):
        """Return the blend mode (str/int) for the current layer."""
        try:
            mode = self.config["properties"]["blend"]
        except KeyError:
            mode = self.default["blend"]

        return mode
class Map:
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
        self.rect = pg.Rect(
                (
                    0,
                    0
                ),
                (
                    self.size[0] * self.tilesize[0],
                    self.size[1] * self.tilesize[1]
                )
            )# pygame.rect
        self.blocks = self.getBlocks()# list
        self.playerstart = self.getPlayerStart()
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
            # tiled layer
            if each["type"] == "tilelayer":
                # updating layers
                each.update({
                    "tiles": self.tiles,
                    "tilesize": self.tilesize
                    })
                layer = Layer(each)
                layers.update({each["name"]: layer})

            # group layer
            elif each["type"] == "group":
                pass

        return layers
    def getBlocks(self):
        """Return a list with all blockable coordinates."""
        blocks = []

        for _, layer in self.layers.items():
            for block in layer.blocks:
                blocks.append(block)

        return blocks
    def getPlayerStart(self):
        """Return a pygame.rect if a layer has a player_start property."""
        ps = None

        for _, layer in self.layers.items():
            if layer._playerstart:
                ps = layer._playerstart

        return ps
    def getTiles(self):# list
        """Get tile objects from every appended tileset and return them in one
        single list."""
        tiles = []

        for k, v in self.tilesets.items():
            for tile in v.tiles:
                tiles.append(tile)

        return tiles
