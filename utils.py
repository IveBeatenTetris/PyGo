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
# pygame
def createIcon(path):
    """Create an icon for the window from a png file."""
    icon = pg.image.load(path)
    icon = pg.transform.scale(icon , (32 , 32))
    pg.display.set_icon(icon)
def draw(object, destination, position=(0, 0)):# pygame surface
    """Drawing a single or multiple objects to the destination surface. Then
    return it."""
    if object.__class__.__bases__[0] is pg.Surface or type(object) is pg.Surface:
        destination.blit(object, position)
    elif object.__class__.__bases__[0] is pg.sprite.Sprite:
        destination.blit(object.image, position)
    elif object.__class__ is pg.sprite.Group:
        for sprite in object:
            destination.blit(sprite.image, sprite.rect.topleft)

    return destination
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
