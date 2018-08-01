from .utils import loadJSON
from .config import PATH
import os

class AssetLoader:
    """."""
    def __init__(self):
        """Constructor."""
        self.tilesets = self.getTilesets()# dict
        self.maps = self.getMaps()# dict
    def __repr__(self):# str
        """String representation."""
        return "<AssetLoader>"
    def loadAssets(self, path):# list
        """Walk the assets-directory and open each json file. Plus appending
        file name and file path to the json file."""
        list = []

        for dirs in os.walk(path):
            for each in dirs[2]:
                if each.split(".")[1] == "json":
                    config = loadJSON(dirs[0] + "\\" + each)
                    list.append(config)

        return list
    def getMaps(self):# dict
        """."""
        maps = {}

        assets = self.loadAssets(PATH["maps"])

        for asset in assets:
            maps.update({asset["name"]: asset})

        return maps
    def getTilesets(self):# dict
        """."""
        tilesets = {}

        assets = self.loadAssets(PATH["tilesets"])

        for asset in assets:
            tilesets.update({asset["name"]: asset})

        return tilesets
