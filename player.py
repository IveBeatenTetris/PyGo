import pygame as pg
from .utils import getFrames
from .config import PATH

class Player(pg.sprite.Sprite):
    """Representing a playable character."""
    def __init__(self, config={}):
        """Constructor."""
        pg.sprite.Sprite.__init__(self)
        self.config = config# dict
        self.name = config["name"]# str
        self.path = "{0}\\{1}".format(PATH["identities"], self.name)# str
        self.imagepath = self.path + "\\" + config["image"]
        self.rawimage = pg.image.load(self.imagepath)# pygame surface
        self.framesize = config["framesize"]# tuple
        self.frames = getFrames(self.rawimage, self.framesize)# list
        self.image = self.frames[0]# pygame surface
