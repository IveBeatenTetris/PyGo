import pygame as pg
import os

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
    "windowbg": pg.image.load(PATH["sysimg"] + "\\bg01.png")
}
