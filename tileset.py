import pygame as pg
from .config import PATH
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

        rows = int(self.image.get_rect().height / self.tilesize[1])
        lines = int(self.image.get_rect().width / self.tilesize[0])
        rect = pg.Rect((0, 0), self.tilesize)

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
