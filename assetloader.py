from . utils import (
    PATH,
    loadAssets,
    loadJSON
    )
from . collection import Collection
import os

class AssetLoader:
    """Load assets in json format and append them to the assetloader."""
    def __init__(self, path=None):
        """Constructor."""
        if path:
            self.path = path# str
        else:
            self.path = PATH["assets"]# str
        self.images = self.get("images")# collection
        self.identities = self.get("identities")# collection
        self.tilesets = self.get("tilesets")# collection
        self.maps = self.get("maps")# collection
    def __repr__(self):# str
        """String representation."""
        return "<AssetLoader>"
    def get(self, assetname):# dict
        """Load a json config from the given asset's name path."""
        collection = Collection()
        assets = loadAssets(self.path + "\\" + assetname)

        for asset in assets:
            collection.add({asset["name"]: asset})

        return collection
