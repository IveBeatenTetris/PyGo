from .utils import (
    PATH,
    IMG,
    windowIcon,
    draw,
    validateDict,
    repeatX,
    repeatY,
    repeatXY,
    scale
    )
#from .config import PATH, IMG
import pygame as pg
import sys
# default values
default = {
    #"size": (1200, 650),
    "size": (320, 240),
    "caption": "project",
    "fps": 60,
    #"background": (25, 25, 35)
    #"background": IMG["windowbg"],
    "background": PATH["sysimg"] + "\\bg01.png",
    "backgroundrepeat": "xy",
    "scale": 2
}

class Window:
    """pygame's window module in a box."""
    def __init__(self, config={}):
        """Constructor."""
        self.config = validateDict(config, default)# dict
        # pygame module init
        pg.init()

        self.display = pg.display.set_mode(self.config["size"], pg.RESIZABLE)# pygame surface
        windowIcon(IMG["windowicon"])
        self.rect = self.display.get_rect()# pygame rect
        self.scale = self.config["scale"]
        self.backgroundrepeat = self.config["backgroundrepeat"]
        self.background = self.createBackground(self.config["background"])# pygame surface
        self.clock = pg.time.Clock()# pygame clock
        self.fps = self.config["fps"]# int
        pg.display.set_caption(self.config["caption"])# str

        draw(self.background, self.display)
    def update(self):
        """Update stuff at app's loop-end."""
        pg.display.update()
        self.clock.tick(self.fps)
        # caption of frames per second
        pg.display.set_caption("Quack: {0}".format(int(self.clock.get_fps())))
        draw(self.background, self.display)
    def draw(self, object, position=(0, 0)):
        """Draw everything to the window's surface."""
        draw(object, self.display, position)
    def resize(self, size):
        """Resize the window and update it's rect."""
        self.display = pg.display.set_mode(size, pg.RESIZABLE)
        self.rect = self.display.get_rect()
        self.background = self.createBackground(self.config["background"])
    def getEvents(self):# pygame.event
        """Get pygame events."""
        for event in pg.event.get():
            if event.type is pg.QUIT or (event.type is pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type is pg.VIDEORESIZE:
                self.resize(event.size)

        return pg.event.get()
    def createBackground(self, object):# pygame surface
        """Create a background surface depending on what type was given."""
        if type(object) is tuple:
            surface = pg.Surface(self.rect.size)
            surface.fill(object)
        elif type(object) is str:
            object = pg.image.load(object)
        if object.__class__.__bases__[0] is pg.Surface or type(object) is pg.Surface:
            if self.backgroundrepeat == "x":
                surface = repeatX(object, self.rect)
            elif self.backgroundrepeat == "y":
                surface = repeatY(object, self.rect)
            elif self.backgroundrepeat == "xy":
                surface = repeatXY(object, self.rect)

        return surface
