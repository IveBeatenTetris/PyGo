import pygame as pg
# default values
# default = {
#
# }

class Image(pg.Surface):
    """A standart image object."""
    def __init__(self, config={}):
        """Constructor."""
        print(config)
