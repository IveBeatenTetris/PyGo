# dependencies
from .utils import (
    PATH,
    IMG,
    createBackground,
    getEvents,
    getDisplay,
    windowIcon,
    windowTitle,
    draw,
    validateDict,
    masterClass,
    repeatX,
    repeatY,
    repeatXY,
    scale
    )
import pygame as pg
# default values
default = {
    "size": (320, 240),
    "caption": "project",
    "fps": 60,
    "background": IMG["windowbg"],
    #"background": PATH["sysimg"] + "\\bg01.png",
    #"background": (25, 25, 35)
    "backgroundrepeat": "xy",
    "resizable": False
}

class Window:
    """pygame's window module in a box."""
    def __init__(self, config={}):
        """Constructor."""
        self.config = validateDict(config, default)# dict
        # pygame module init
        pg.init()
        self.resizable = self.config["resizable"]# bool
        self.display = getDisplay(# pygame surface
            self.config["size"],
            resizable = self.resizable
            )
        self.rect = self.display.get_rect()# pygame rect
        self.backgroundrepeat = self.config["backgroundrepeat"]# str
        self.background = self.config["background"]# str / tuple / pygame.surface
        self.bg = createBackground(self.background, self.rect)# pygame.surface
        self.clock = pg.time.Clock()# pygame clock
        self.fps = self.config["fps"]# int
        # window caption and icon
        pg.display.set_caption(self.config["caption"])
        windowIcon(IMG["windowicon"])
        # drawing background to display
        draw(self.bg, self.display)
    def update(self):
        """Update stuff at app's loop-end."""
        pg.display.update()
        self.clock.tick(self.fps)
        # caption of frames per second
        windowTitle("Quack: {0}".format(int(self.clock.get_fps())))
        draw(self.bg, self.display)
    def draw(self, object, position=(0, 0)):
        """Draw everything to the window's surface."""
        draw(object, self.display, position)
    def resize(self, size):
        """Resize the window and update it's rect."""
        self.display = getDisplay(# pygame surface
            size,
            resizable = self.resizable
            )
        self.rect = self.display.get_rect()
        self.bg = createBackground(self.background, self.rect)
    def getEvents(self):# pygame.event
        """Get pygame events."""
        events = getEvents()
        # resizing the window
        if "windowresize" in events:
            self.resize(events["windowresize"])

        return events
