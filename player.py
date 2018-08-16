from .utils import (
    PATH,
    validateDict,
    draw,
    getFrames,
    drawBorder,
    getPressedKeys
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
        self.facing = "down"# str
        # drawing a border around the player
        # draw(
        #     drawBorder(self.rect, [1, "solid", (255, 0, 0)]),
        #     self.image,
        #     (0, 0)
        #     )
    def __repr__(self):# str
        """String representation."""
        return "<Player({0})".format(str(self.rect.topleft))
    # //TODO get this collision shit together
    def __moveSingleAxis(self, pos, blocks):
        """Dirty method to check for collisions and moving the player to the
        right position."""
        self.rect.x += pos[0]
        self.rect.y += pos[1]

        for block in blocks:
            if self.rect.colliderect(block):
                if pos[0] > 0:
                    self.rect.right = block.left
                if pos[0] < 0:
                    self.rect.left = block.right
                if pos[1] > 0:
                    self.rect.bottom = block.top
                if pos[1] < 0:
                    self.rect.top = block.bottom
    def move(self, blocks=[]):
        """Moving the player to given coordinates."""
        keys = getPressedKeys()

        if keys[pg.K_a]:
            self.__moveSingleAxis((-self.speed, 0), blocks)
            self.facing = "left"
        if keys[pg.K_d]:
            self.__moveSingleAxis((self.speed, 0), blocks)
            self.facing = "right"
        if keys[pg.K_w]:
            self.__moveSingleAxis((0, -self.speed), blocks)
            self.facing = "up"
        if keys[pg.K_s]:
            self.__moveSingleAxis((0, self.speed), blocks)
            self.facing = "down"

        self.turn()
    def turn(self):
        """."""
        if self.facing == "down":
            self.image = self.frames[0]
        elif self.facing == "left":
            self.image = self.frames[1]
        elif self.facing == "up":
            self.image = self.frames[2]
        elif self.facing == "right":
            self.image = self.frames[3]
