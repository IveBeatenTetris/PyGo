from .utils import (
    PATH,
    validateDict,
    draw,
    getFrames,
    drawBorder
    )
import pygame as pg

default = {
    "name": "Player1",
    "image": "noimage.png",
    "framesize": [50, 50]
}

class Player(pg.sprite.Sprite):
    """Representing a playable character."""
    def __init__(self, config={}):
        """Constructor."""
        pg.sprite.Sprite.__init__(self)
        self.config = validateDict(config, default)# dict
        self.name = self.config["name"]# str
        if self.config["image"] == "noimage.png":
            self.path = PATH["sysimg"]# str
        else:
            self.path = "{0}\\{1}".format(PATH["identities"], self.name)# str
        self.imagepath = self.path + "\\" + self.config["image"]# str
        self.rawimage = pg.image.load(self.imagepath)# pygame.surface
        self.framesize = self.config["framesize"]# tuple
        self.frames = getFrames(self.rawimage, self.framesize)# list
        self.image = self.frames[0]# pygame.surface
        self.rect = self.image.get_rect()# pygame.rect
        self.speed = 2# int
        # drawing a border around the player
        draw(
            drawBorder(self.rect, [1, "solid", (255, 0, 0)]),
            self.image,
            (0, 0)
            )
    def __repr__(self):# str
        """String representation."""
        return "<Player({0})".format(str(self.rect.topleft))
    def move(self, pos):
        """Moving the player to given coordinates."""
        # if pos is a pygame key-pressed tuple
        if len(pos) > 2:
            x , y = (0 , 0)

            if pos[pg.K_a]:
                x = -self.speed
            if pos[pg.K_d]:
                x = self.speed
            if pos[pg.K_w]:
                y = -self.speed
            if pos[pg.K_s]:
                y = self.speed

            pos = (x, y)

        x, y = self.rect.topleft
        self.rect.topleft = (x + pos[0], y + pos[1])
