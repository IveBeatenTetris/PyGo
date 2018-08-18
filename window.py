# dependencies
from .utils import (
    PATH,
    IMG,
    createBackground,
    getEvents,
    getPressedKeys,
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
import sys, time
# default values
default = {
    "size": (320, 240),
    "caption": "project",
    "fps": 60,
    "gamespeed": 1,
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
        # pygame module init
        pg.init()

        self.config = validateDict(config, default)# dict
        self.resizable = self.config["resizable"]# bool
        self.display = getDisplay(# pygame surface
            self.config["size"],
            resizable = self.resizable
            )
        self.rect = self.display.get_rect()# pygame rect
        self.background = self.config["background"]# str / tuple / pygame.surface
        self.backgroundrepeat = self.config["backgroundrepeat"]# str
        self.bg = createBackground(self.background, self.rect, self.backgroundrepeat)# pygame.surface
        self.clock = pg.time.Clock()# pygame.clock
        self.fps = self.config["fps"]# int
        self.gamespeed = self.config["gamespeed"]# int / float

        # window caption and icon
        pg.display.set_caption(self.config["caption"])
        windowIcon(IMG["windowicon"])

        # drawing background to display
        draw(self.bg, self.display)
    def update(self):
        """Update stuff at app's loop-end."""
        pg.display.update()
        self.clock.tick(self.fps)

        # set the global gameplay speed. also reduces fps and cpu
        if self.gamespeed == 1:
            pass
        elif self.gamespeed < 1:
            counter = str(self.gamespeed)[2]
            counter = 10 - int(counter)

            # literally make the window wait
            time.sleep(counter / 1000)

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
        self.bg = createBackground(self.background, self.rect, self.backgroundrepeat)
    def getEvents(self):# pygame.event
        """Get pygame events."""
        events = getEvents()

        for event in events:
            # quit application
            if event.type is pg.QUIT or (event.type is pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            # resizing the window
            if event.type is pg.VIDEORESIZE:
                self.resize(event.size)

        return events
    def getKeys(self):# tuple
        return getPressedKeys()
