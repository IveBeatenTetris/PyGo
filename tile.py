import pygame as pg

class Tile(pg.sprite.Sprite):
    """."""
    def __init__(self, config={}):
        """Constructor."""
        self.config = config
        pg.sprite.Sprite.__init__(self)
        self.image = config["image"]
        self.id = config["id"] + 1
    def __repr__(self):# str
        """String representation."""
        return "<Tile({0})>".format(self.id)
