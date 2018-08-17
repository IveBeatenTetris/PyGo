from . utils import (
    PATH,
    validateDict,
    draw,
    getFrames,
    drawBorder,
    getPressedKeys,
    wait
    )
from . animation import Animation
import pygame as pg

# default values
default = {
    "name": "Player1",
    "image": "noimage.png",
    "framesize": [50, 50],
    #"border": None,
    "border": [1, "solid", [255, 0, 0]],
    "animationspeed": 25,
    "collisionbox": None
    }

class Player(pg.sprite.Sprite):
    """Representing a playable character."""
    def __init__(self, config={}):
        """Constructor."""
        pg.sprite.Sprite.__init__(self)
        self.config = validateDict(config, default)# dict
        self.name = self.config["name"]# str

        # no image exception
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
        self.moving = False# bool
        self.border = self.config["border"]# none / list / tuple
        self.animationspeed = self.config["animationspeed"]# int
        self.animations = {# dict
            "walkdown": Animation({
                "frames": self.frames,
                "sequence": [4, 5, 6, 7],
                "duration": self.animationspeed
                }),
            "walkleft": Animation({
                "frames": self.frames,
                "sequence": [8, 9, 10, 11],
                "duration": self.animationspeed
                }),
            "walkup": Animation({
                "frames": self.frames,
                "sequence": [12, 13, 14, 15],
                "duration": self.animationspeed
                }),
            "walkright": Animation({
                "frames": self.frames,
                "sequence": [16, 17, 18, 19],
                "duration": self.animationspeed
                })
            }
        if self.config["collisionbox"]:
            self.collisionbox = pg.Rect(self.config["collisionbox"])# pygame.rect
        else:
            self.collisionbox = self.rect# pygame.rect
            self.config["collisionbox"] = pg.Rect(self.collisionbox)# pygame.rect
    def __repr__(self):# str
        """String representation."""
        return "<Player({0})".format(str(self.rect.topleft))
    # //TODO get this collision shit together
    def __moveSingleAxis(self, pos, blocks):
        """Dirty method to check for collisions and moving the player to the
        right position."""
        self.rect.x += pos[0]
        self.rect.y += pos[1]
        self.collisionbox.topleft = (
            self.rect.left + self.config["collisionbox"][0],
            self.rect.top + self.config["collisionbox"][1]
            )

        for block in blocks:
            # if self.rect.colliderect(block):
            #     if pos[0] > 0:
            #         self.rect.right = block.left
            #     if pos[0] < 0:
            #         self.rect.left = block.right
            #     if pos[1] > 0:
            #         self.rect.bottom = block.top
            #     if pos[1] < 0:
            #         self.rect.top = block.bottom
            if self.collisionbox.colliderect(block):
                rect = pg.Rect(self.config["collisionbox"])

                if pos[0] > 0:
                    self.rect.right = block.left + (self.rect.width - rect.right)
                if pos[0] < 0:
                    self.rect.left = block.right - rect.left
                if pos[1] > 0:
                    self.rect.bottom = block.top + (self.rect.height - rect.bottom)
                if pos[1] < 0:
                    self.rect.top = block.bottom - rect.top
    def move(self, blocks=[]):
        """Moving the player to given coordinates."""
        keys = getPressedKeys()
        self.moving = False

        # moving the payer sprite
        if keys[pg.K_a]:
            self.__moveSingleAxis((-self.speed, 0), blocks)
            self.facing = "left"
            self.moving = True
        if keys[pg.K_d]:
            self.__moveSingleAxis((self.speed, 0), blocks)
            self.facing = "right"
            self.moving = True
        if keys[pg.K_w]:
            self.__moveSingleAxis((0, -self.speed), blocks)
            self.facing = "up"
            self.moving = True
        if keys[pg.K_s]:
            self.__moveSingleAxis((0, self.speed), blocks)
            self.facing = "down"
            self.moving = True

        # walking cycle
        if self.moving:
            if self.facing == "down":
                name = "walkdown"
            elif self.facing == "left":
                name = "walkleft"
            elif self.facing == "up":
                name = "walkup"
            elif self.facing == "right":
                name = "walkright"

            self.image = self.animations[name].image
            self.animations[name].update()

        # idle facing direction
        else:
            if self.facing == "down":
                self.image = self.frames[0]
            elif self.facing == "left":
                self.image = self.frames[1]
            elif self.facing == "up":
                self.image = self.frames[2]
            elif self.facing == "right":
                self.image = self.frames[3]

        # drawing a border around the player
        if self.border:
            draw(
                drawBorder(self.rect, self.border),
                self.image,
                (0, 0)
                )
            draw(
                drawBorder(
                        self.collisionbox,
                        [1, "solid", [0, 0, 255]]
                    ),
                    self.image,
                    pg.Rect(self.config["collisionbox"]).topleft
                )
