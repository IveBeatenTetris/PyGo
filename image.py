"""Slightly modified pygame.image object."""
# dependencies
from .utils import PATH, validateDict
import pygame as pg
# classes
class Image(pg.Surface):
    """A simple pygame.image surface with additional attributes."""
    # default values
    default = {
        "filepath": PATH["sysimg"],
        "filename": "noimage.png",
        }
    def __init__(self, config={}):
        """Constructor."""
        self.config = validateDict(config, self.default)# dict
        self.path = "{0}\\{1}".format(# str
            self.config["filepath"],
            self.config["filename"]
            )
        # # open image and draw it to surface
        image = pg.image.load(self.path)# pygame.surface
        pg.Surface.__init__(# pygame.surface
            self,
            image.get_rect().size,
            pg.SRCALPHA
            )
        self.rect = self.get_rect()# pygame.surface
        self.blit(image, self.rect)
