from .utils import loadJSON
from .config import PATH
import os

class AssetLoader:
    """Load assets in json format and append them to the assetloader."""
    def __init__(self):
        """Constructor."""
        self.identities = self.get("identities")# dict
        self.tilesets = self.get("tilesets")# dict
        self.maps = self.get("maps")# dict
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
    def get(self, assetname):# dict
        """Load a json config from the given assets' name path."""
        collection = {}

        assets = self.loadAssets(PATH[assetname])

        for asset in assets:
            collection.update({asset["name"]: asset})

        return collection
