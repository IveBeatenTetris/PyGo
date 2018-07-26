import pygame as pg
import sys

default = {
    #"size": (1200, 650),
    "size": (320, 240),
    "caption": "project",
    "fps": 15,
    "scale": 1
}

class Window:
    """pygame's window module in a box."""
    def __init__(self):
        """Constructor."""
        pg.init()
        self.display = pg.display.set_mode(default["size"], pg.RESIZABLE)
        self.rect = self.display.get_rect()
        pg.display.set_caption(default["caption"])
        self.clock = pg.time.Clock()
        self.fps = default["fps"]
    def draw(self, object, position=(0, 0)):
        """Draw everything to the window's surface."""
        if object.__class__.__bases__[0] is pg.Surface or type(object) is pg.Surface:
            self.display.blit(object, position)
        elif object.__class__.__bases__[0] is pg.sprite.Sprite:
            self.display.blit(object.image, position)
        elif object.__class__ is pg.sprite.Group:
            for sprite in object:
                self.display.blit(sprite.image, sprite.rect.topleft)
    def resize(self, size):
        """Resize the window and update it's rect."""
        self.display = pg.display.set_mode(size, pg.RESIZABLE)
        self.rect = self.display.get_rect()
    def update(self):
        """Update stuff at app's loop-end."""
        pg.display.update()
        self.clock.tick(self.fps)
    def getEvents(self):# pygame.event
        """Get pygame events."""
        for event in pg.event.get():
            if event.type is pg.QUIT or (event.type is pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type is pg.VIDEORESIZE:
                self.resize(event.size)

        return pg.event.get()
