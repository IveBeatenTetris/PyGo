import pygame as pg
from .utils import PATH, getFrames, drawBorder
#from .config import PATH

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
        self.rect = self.image.get_rect()# pygame rect
        self.speed = 2# int
        # drawing a border around the player
        self.image.blit(drawBorder(self.rect, [1, "solid", (255, 0, 0)]), (0, 0))
    def __repr__(self):# str
        """String representation."""
        return "<Player({0})".format(str(self.rect.topleft))
    def move(self, pos):
        """Moving the player to given coordinates."""
        x, y = self.rect.topleft
        self.rect.topleft = (x + pos[0], y + pos[1])
