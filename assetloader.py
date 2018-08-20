from .utils import (
    PATH,
    loadAssets,
    loadJSON
    )
import os

class AssetLoader:
    """Load assets in json format and append them to the assetloader."""
    def __init__(self, path=None):
        """Constructor."""
        if path:
            self.path = path# str
        else:
            self.path = PATH["assets"]# str
        self.images = self.get("images")# dict
        self.identities = self.get("identities")# dict
        self.tilesets = self.get("tilesets")# dict
        self.maps = self.get("maps")# dict
    def __repr__(self):# str
        """String representation."""
        return "<AssetLoader>"
    def get(self, assetname):# dict
        """Load a json config from the given asset's name path."""
        collection = {}
        assets = loadAssets(self.path + "\\" + assetname)

        for asset in assets:
            collection.update({asset["name"]: asset})

        return collection
