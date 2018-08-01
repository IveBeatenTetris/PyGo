import json
import pygame as pg

def loadJSON(path):
    """Load and convert a JSON file."""
    with open(path) as text:
        content = "".join(text.readlines())
        js = json.loads(content)
        js.update({"name": path.split("\\")[-2]})
        js.update({"filepath": path})

    return js
def perPixelAlpha(image , opacity=255):# pygame surface
    """Convert per pixel alpha from image."""
    image.convert_alpha()
    alpha_img = pg.Surface(image.get_rect().size , pg.SRCALPHA)
    alpha_img.fill((255 , 255 , 255 , opacity))
    image.blit(alpha_img , (0 , 0) , special_flags = pg.BLEND_RGBA_MULT)

    return image
