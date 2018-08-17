from . utils import (
    validateDict
    )
import pygame as pg

default = {
    "frames": [],
    "sequence": [],
    "duration": 100
}

class Animation(pg.sprite.Sprite):
    """An animated sprite class."""
    def __init__(self, config={}):
        """Constructor."""
        self.config = validateDict(config, default)# dict
        self.sequence = self.config["sequence"]# tuple / list
        self.duration = self.config["duration"]# int
        self.frames = self.config["frames"][# list
            self.sequence[0] : self.sequence[-1] + 1
            ]
        pg.sprite.Sprite.__init__(self)# pygame.sprite
        self.pointer = 0# int
        self.image = self.frames[self.pointer]# pygame.surface
        self.framecount = len(self.frames)# int
        self.timer = self.duration + 1# int
        self.timemod = int(self.timer / self.framecount)# int
    def update(self):
        """Updating the pointer's position. The active frame is always drawn to
        the animation image surface."""
        for i in range(self.framecount):
            if self.timer == int((i) * self.timemod):
                self.nextFrame()

        if self.timer == 0:
            self.timer = self.duration + 1
        else:
            self.timer = self.timer - 1
    def nextFrame(self):
        """Set the pointer to the next frame."""
        if self.pointer < self.framecount - 1:
            self.pointer += 1
        else:
            self.pointer = 0

        self.image = self.frames[self.pointer]
