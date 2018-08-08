import json
import pygame as pg

# console
def prettyPrint(data, sort=False, tabs=4):
    """Pretty print dict."""
    if data.__class__ is dict:
        print(json.dumps(data, sort_keys=sort, indent=tabs))
    else:
        print("Nothing to pretty-print.")
# files & directories
def loadJSON(path):# dict
    """Load and convert a JSON file."""
    with open(path) as text:
        content = "".join(text.readlines())
        js = json.loads(content)
        js.update({"name": path.split("\\")[-2]})
        js.update({"filepath": path})

    return js
# dictionary operations
def validateDict(config={}, defaults={}):# dict
    """Validate a dictionary by given defaults. Params must be dict."""
    validated = {}

    for each in defaults:
        try:
            validated[each] = config[each]
        except KeyError:
            validated[each] = defaults[each]

    return validated
# pygame
def createIcon(path):
    """Create an icon for the window from a png file."""
    icon = pg.image.load(path)
    icon = pg.transform.scale(icon , (32 , 32))
    pg.display.set_icon(icon)
def draw(object, destination, position=(0, 0)):# pygame surface
    """Drawing a single or multiple objects to the destination surface. Then
    return it."""
    if type(position) is pg.Rect:
        position = position.topleft

    if type(object) is tuple:
        destination.fill(object, destination.get_rect())
    elif object.__class__.__bases__[0] is pg.Surface or type(object) is pg.Surface:
        destination.blit(object, position)
    elif object.__class__.__bases__[0] is pg.sprite.Sprite:
        destination.blit(object.image, position)
    elif object.__class__ is pg.sprite.Group:
        for sprite in object:
            destination.blit(sprite.image, sprite.rect.topleft)

    return destination
def drawBorder(rect, config):# pygame surface
    """Drawing a border to a surface and return it."""
    size, line, color = config
    surface = pg.Surface(rect.size, pg.SRCALPHA)

    pg.draw.lines(
        surface,
        color,
        False,
        [
            (0, 0),
            (0, rect.height - 1),
            (rect.width - 1, rect.height - 1),
            (rect.width - 1, 0),
            (0, 0)
        ],
        size
    )

    return surface
def perPixelAlpha(image , opacity=255):# pygame surface
    """Convert per pixel alpha from image."""
    image.convert_alpha()
    alpha_img = pg.Surface(image.get_rect().size , pg.SRCALPHA)
    alpha_img.fill((255 , 255 , 255 , opacity))
    image.blit(alpha_img , (0 , 0) , special_flags = pg.BLEND_RGBA_MULT)

    return image
def getFrames(image, framesize):# list
    """return a list of frames clipped from an image."""
    frames = []

    rows = int(image.get_rect().height / framesize[1])
    cells = int(image.get_rect().width / framesize[0])
    rect = pg.Rect((0, 0), framesize)

    # running each frame
    for row in range(rows):
        y = row * framesize[1]
        rect.top = y
        for cell in range(cells):
            x = cell * framesize[0]
            rect.left = x

            image.set_clip(rect)
            clip = image.subsurface(image.get_clip())

            frames.append(clip)

    return frames
def scale(surface, factor):
    """."""
    width = surface.get_rect().width * factor
    height = surface.get_rect().height * factor

    scaled = pg.transform.scale(surface, (width, height))

    return scaled
def repeatX(image, parent, pos=(0, 0)):# pygame surface
    """Return a surface with x-line repeated image blitting."""
    child = image.get_rect()
    surface = pg.Surface(parent.size, pg.SRCALPHA)
    for each in range(int(parent.width / child.width) + child.width):
        surface.blit(image, (each * child.width, pos[0]))

    return surface
def repeatY(image, parent, pos=(0, 0)):# pygame surface
    """Return a surface with y-line repeated image blitting."""
    child = image.get_rect()
    surface = pg.Surface(parent.size, pg.SRCALPHA)
    for each in range(int(parent.height / child.height) + child.height):
        surface.blit(image, (pos[1], each * child.height))

    return surface
def repeatXY(image, parent, bg_position=(0, 0)):# pygame surface
    """Return a surface with x and y-line repeated image blitting."""
    child = image.get_rect()
    surface = pg.Surface(parent.size, pg.SRCALPHA)
    for j in range(int(parent.width / child.width) + child.width):
        for i in range(int(parent.height / child.height) + child.height):
            surface.blit(image, (j * child.width, i * child.width))

    return surface
