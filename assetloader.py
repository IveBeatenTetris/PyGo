from .utils import (
    PATH,
    loadAssets,
    getPublicProperties
    )
from .collection import Collection

class AssetLoader:
    """Load assets in json format and append them to the assetloader."""
    def __init__(self, path=None):
        """Constructor."""
        if path:
            self.path = path# str
        else:
            self.path = PATH["assets"]# str
        self.images = self.get("images")# collection
        self.entities = self.get("entities")# collection
        self.tilesets = self.get("tilesets")# collection
        self.maps = self.get("maps")# collection
        self.behaviors = self.get("behaviors")# collection
    def __str__(self):# str
        """String representation."""
        list = []

        for k, v in getPublicProperties(self).items():
            try:
                t = v.type
            except AttributeError:
                t = type(v)

            list.append("'{0}': {1}".format(k, t))

        joined = "\n".join(list)
        lines = "\n--- AssetLoader:\n" + joined + "\n---"

        return lines
    def get(self, assetname):# dict
        """Load a json config from the given asset's name path."""
        collection = Collection()
        assets = loadAssets(self.path + "\\" + assetname)

        for asset in assets:
            #collection.add({asset["name"]: asset})
            collection.add({asset["filename"].split(".")[0]: asset})

        return collection
