# dependencies
import json, os, sys
import pygame as pg

# project and library pathes
PATH = {
    "go": os.path.dirname(__file__),
    "sysimg": os.path.dirname(__file__) + "\\images",
    "root": os.getcwd(),
    "assets" : os.getcwd() + "\\assets",
    "images" : os.getcwd() + "\\assets\\images",
    "maps": os.getcwd() + "\\assets\\maps",
    "tilesets": os.getcwd() + "\\assets\\tilesets",
    "identities": os.getcwd() + "\\assets\\identities"
}
IMG = {
    "noimage": pg.image.load(PATH["sysimg"] + "\\noimage.png"),
    "windowbg": pg.image.load(PATH["sysimg"] + "\\bg01.png"),
    "windowicon": pg.image.load(PATH["sysimg"] + "\\ente.png")
}
RESOLUTIONS = {
    "1920x1080": (1920, 1080)
}

# console
def prettyPrint(data, sort=False, tabs=4):
    """Pretty print dict."""
    if data.__class__ is dict:
        print(json.dumps(data, sort_keys=sort, indent=tabs))
    else:
        print("Nothing to pretty-print.")

# class and object functions
def getPublicProperties(obj):# dict
    """Return a dict of all handwritten class properties."""
    property_dict = {}

    for each in obj.__dict__:
        if each[:1] != "_":
            property_dict.update({each : obj.__dict__[each]})

    return property_dict
def masterClass(object , masterclass):# bool
    """Check if object's master class matches the given one."""
    if object.__class__.__bases__[0] is masterclass:
        bool = True
    else:
        bool = False

    return bool

# files & directories
def isPath(path):# bool
    """Return True if the given path exists."""
    if os.path.isfile(path) or os.path.exists(path):
        bool = True
    else:
        bool = False

    return bool
def loadAssets(path):# list
    """Walk the assets-directory and open each json file. Plus appending
    file name and file path to the json file."""
    list = []

    for dirs in os.walk(path):
        for each in dirs[2]:
            if each.split(".")[1] == "json":
                config = loadJSON(dirs[0] + "\\" + each)
                list.append(config)
            # if directory has an image
            elif each.split(".")[1] == "png":
                config = {
                    "name": each.split(".")[0],
                    "filename": each,
                    "type": "image",
                    "filepath": dirs[0]
                }
                list.append(config)

    return list
def loadJSON(path):# dict
    """Load and convert a JSON file."""
    with open(path) as text:
        content = "".join(text.readlines())
        js = json.loads(content)
        js.update({"name": path.split("\\")[-2]})
        js.update({"filepath": path})

    return js
def thisPath(path):# str
    """Return the path of the calling file's path."""
    return "\\".join(path.split("\\")[0:-1])

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

# pygame operations
def cut(surface, rect):# pygame.surface
    """
    Clip a part of the given surface and return it.
    'rect' can be <Tuple> of 4 or a pygame rect.
    Example: rect = (0, 0, 160, 120) // rect = pygame.Rect(0, 0, 160, 120).
    Usage: surf = cut(display, (0, 0, 32, 32)).
    """
    surface.set_clip(rect)
    clip = surface.subsurface(surface.get_clip())

    return clip
def createBackground(background, rect, bgrepeat=""):# pygame.surface
    """Create a background surface depending on what type was given."""
    surface = pg.Surface(rect.size)
    # background's class type doesn't matter
    if type(background) is tuple:
        surface = pg.Surface(rect.size)
        surface.fill(background)
    elif type(background) is str:
        object = pg.image.load(background).convert()

    if masterClass(background, pg.Surface) or type(background) is pg.Surface:
        if bgrepeat == "x":
            surface = repeatX(background, rect)
        elif bgrepeat == "y":
            surface = repeatY(background, rect)
        elif bgrepeat == "xy":
            surface = repeatXY(background, rect)
        else:
            surface = background

    return surface
def createTiledMap(config, tiles):# dict
    """
    Drawing tiles on a pygame surface and return it in a dict together with
    a list of wall rects.
    """
    tilesize = tiles[0].image.get_rect().size

    blocks = []
    surface = pg.Surface(
        (
            config["width"] * tilesize[0],
            config["height"] * tilesize[1]
        ),
        pg.SRCALPHA)

    i = 0
    for row in range(config["height"]):
        y = row * tilesize[1]
        for line in range(config["width"]):
            x = line * tilesize[0]

            # only draw tile if area isn't empty
            if config["data"][i] != 0:
                tile = tiles[config["data"][i] - 1]
                surface.blit(tile.image, (x, y))

                # add a block rect to blocklist if tile is not passable
                if tile.block:
                    blocks.append(pg.Rect((x, y), tile.image.get_rect().size))

            i += 1

    return {
        "image": surface,
        "blocks": blocks
        }
def getEvents():# pygame.events
    """Get pygame events."""
    return pg.event.get()
def getDisplay(size, **kwargs):# pygame.display.surface
    """Create a window display and return it. Customisation possible."""
    for key, value in kwargs.items():
        if key == "resizable":
            if value is True:
                display = pg.display.set_mode(size , pg.RESIZABLE)
            else:
                display = pg.display.set_mode(size)

    return display
def getPressedKeys():# pygame.event.keys
    """Get pygame.event's pressed-keys."""
    return pg.key.get_pressed()
def wait(amount):
    # t = pg.time.get_ticks()
    # getTicksLastFrame = t
    # # deltaTime in seconds.
    # deltaTime = (t - getTicksLastFrame) / 1000.0
    # print(deltaTime)
    ms = pg.time.Clock().tick(amount)
    #print(ms)
def windowIcon(path):
    """Create an icon for the window from a png file."""
    if type(path) is pg.Surface:
        icon = path
    elif type(path) is str:
        icon = pg.image.load(path)

    icon = pg.transform.scale(icon , (32 , 32))
    pg.display.set_icon(icon)
def windowTitle(title):
    """Set the window's caption."""
    pg.display.set_caption(title)
def draw(object, destination, position=(0, 0)):# pygame.surface
    """
    Drawing a single or multiple objects to the destination surface. Then
    return it.
    'position' can be tuple or pygame rect.
    Usage: draw(player, display, pygame.Rect(0, 0, 160, 120)).
    """
    if type(position) is str:
        # draw object in the center
        if position == "center":
            try:
                osize = object.get_rect().size
            except AttributeError:
                osize = object.image.get_rect().size
            dsize = destination.get_rect().size

            x = int(dsize[0] / 2) - int(osize[0] / 2)
            y = int(dsize[1] / 2) - int(osize[1] / 2)
            position = (x, y)

    # drawing depending on object's type
    if type(object) is tuple:
        destination.fill(object, destination.get_rect())
    elif object.__class__.__bases__[0] is pg.Surface or type(object) is pg.Surface:
        destination.blit(object, position)
    elif object.__class__.__bases__[0] is pg.sprite.Sprite:
        destination.blit(object.image, position)
    elif object.__class__ is pg.sprite.Group:
        for sprite in object:
            destination.blit(sprite.image, sprite.rect.topleft)

    # recursively drawing objects from a list
    elif type(object) is list:
        for each in object:
            draw(each, destination, position)

    return destination
def drawBorder(surface, rect, border):# pygame surface
    """
    Drawing a border to the given surface and return it.
    Syntax for border is (BorderSize<Int>, LineStyle<Str>, Color<Tuple>).
    Example: config = (1, 'solid', (255, 255, 255)).
    Usage: surf = drawBorder(display, (0, 0, 16, 16), (1, 'solid', (0 ,0, 0))).
    """
    size, line, color = border

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
def perPixelAlpha(image, opacity=255):# pygame.surface
    """
    Convert per pixel alpha from an image surface.
    'opacity' can be an int from 0~255 or a float from 0.01~1.0.
    Usage: surface = perPixelAlpha(surface, 0.5)
    """

    # generate an int if opacity is a float type
    if type(opacity) is float:
        if opacity < 1.0:
            opac = str(opacity).split(".")
            opacity = int(int(opac[1]) * 255 / 100)

    #image.convert_alpha()
    alpha_img = pg.Surface(image.get_rect().size, pg.SRCALPHA)
    alpha_img.fill((255 , 255 , 255 , opacity))
    image.blit(alpha_img , (0 , 0), special_flags = pg.BLEND_RGBA_MULT)

    return image
def getFrames(image, framesize):# list
    """
    Return a list of frames clipped from an image.
    'framesize' must be a tuple of 2.
    Usage: frames = getFrames(spritesheet, (16, 16)).
    """
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
    del(clip, rect)

    return frames
def scale(surface, factor):# pygame.surface
    """
    Scaling a surface by an int-factor.
    'factor' must be an integer.
    Usage: surf = scale(display, 2).
    """
    size = [each * factor for each in surface.get_rect().size]

    return pg.transform.scale(surface, size)
def repeatX(image, parent, pos=(0, 0)):# pygame.surface
    """Return a surface with x-line repeated image blitting."""
    child = image.get_rect()
    surface = pg.Surface(parent.size, pg.SRCALPHA)

    for each in range(int(parent.width / child.width) + 1):
        surface.blit(image, (each * child.width, pos[0]))

    return surface
def repeatY(image, parent, pos=(0, 0)):# pygame.surface
    """Return a surface with y-line repeated image blitting."""
    child = image.get_rect()
    surface = pg.Surface(parent.size, pg.SRCALPHA)

    for each in range(int(parent.height / child.height) + 1):
        surface.blit(image, (pos[1], each * child.height))

    return surface
def repeatXY(image, parent, bg_position=(0, 0)):# pygame.surface
    """Return a surface with x and y-line repeated image blitting."""
    child = image.get_rect()
    surface = pg.Surface(parent.size, pg.SRCALPHA)

    for j in range(int(parent.width / child.width) + 1):
        for i in range(int(parent.height / child.height) + 1):
            surface.blit(image, (j * child.width, i * child.width))

    return surface
