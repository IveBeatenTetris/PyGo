import pygame as pg
from .utils import PATH, getFrames
#from .config import PATH
from .tile import Tile

class Tileset(pg.Surface):
    """."""
    def __init__(self, config={}):
        """Constructor."""
        self.config = config# dict
        self.name = config["name"]# str
        self.path = "{0}\\{1}\\{2}".format(
            PATH["tilesets"],
            self.name,
            config["image"]
            )
        self.image = pg.image.load(self.path)# pygame surface

        self.tilesize = (config["tilewidth"], config["tileheight"])# tuple
        self.tiles = self.__createTiles()# list

        pg.Surface.__init__(self, self.image.get_rect().size)
        self.blit(self.image, (0, 0))
    def __repr__(self):# str
        """String representation."""
        return (
            "<Tileset('" +
            self.name +
            "', " +
            "tc=" + str(self.config["tilecount"]) +
            ")>"
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
