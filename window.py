# dependencies
from .utils import (
    IMG,
    systemResolution,
    createBackground,
    getEvents,
    getPressedKeys,
    getDisplay,
    windowIcon,
    windowTitle,
    draw,
    validateDict
    )
import sys, time
import pygame as pg

class Window:
    """pygame's window module in a box."""
    # default values
    default = {
        "size": (320, 240),
        "caption": "project",
        "fps": 60,
        "gamespeed": 1,
        "background": IMG["windowbg"],
        # "background": (25, 25, 35)
        "backgroundrepeat": "xy",
        "resizable": False,
        "zoom": 1,
        }
    def __init__(self, config={}):
        """Constructor."""
        # pygame module init
        pg.init()

        self.config = validateDict(config, self.default)# dict
        self.resizable = self.config["resizable"]# bool
        self.display = getDisplay(# pygame surface
            self.config["size"],
            resizable=self.resizable
            )
        self.rect = self.display.get_rect()# pygame rect
        self.background = self.config["background"]# str / tuple / pygame.surface
        self.backgroundrepeat = self.config["backgroundrepeat"]# str
        self.bg = createBackground(# pygame.surface
            self.background,
            self.rect,
            self.backgroundrepeat)
        self.clock = pg.time.Clock()# pygame.clock
        self.fps = self.config["fps"]# int
        self.gamespeed = self.config["gamespeed"]# int / float
        self.zoom = self.config["zoom"]# int

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
            resizable=self.resizable
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

            # scaling the game screen
            if event.type is pg.MOUSEBUTTONDOWN and event.button == 4:
                # self.zoom += 1
                pass
            if event.type is pg.MOUSEBUTTONDOWN and event.button == 5:
                # self.zoom -= 1
                pass
            if self.zoom < 1:
                # self.zoom = 1
                pass

            # resizing the window
            if event.type is pg.VIDEORESIZE:
                self.resize(event.size)

            # going fullscreen
            # // TODO get fullscreening to work
            if event.type is pg.KEYDOWN and event.key == pg.K_F12:
                self.resize(systemResolution())

        return events
    def getKeys(self):# tuple
        """Quick method to get pressed keys instantly."""
        return getPressedKeys()
