import pygame as pg

class Animation(pg.sprite.Sprite):
    """."""
    def __init__(self, frames, sequence, delay):
        """Constructor."""
        pg.sprite.Sprite.__init__(self)# pygame.sprite
        self.frames = frames[sequence[0] : sequence[-1] + 1]# list
        self.framecount = len(self.frames)# int
        self.pointer = 0# int
        self.image = self.frames[self.pointer]
        self.delay = delay# int
        self.timer = self.delay + 1# int
        self.timemod = int(self.timer / self.framecount)# int
    def update(self):
        """Updating the pointer's position. The active frame is always drawn to the
        animation surface."""
        for i in range(self.framecount):
            if self.timer == int((i + 1) * self.timemod):
                self.nextFrame()

        if self.timer == 0:
            self.timer = self.delay + 1
        else:
            self.timer = self.timer - 1
    def nextFrame(self):
        """Set the pointer to the next frame."""
        if self.pointer < self.framecount - 1:
            self.pointer += 1
        else:
            self.pointer = 0

        self.image = self.frames[self.pointer]
