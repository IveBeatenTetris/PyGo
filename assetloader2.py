from .utils import loadJSON
import os

class AssetLoader:
    """."""
    def __init__(self):
        """Constructor."""
        self.root = os.getcwd() + "\\assets"# str
        self.dirs = self.getDirectories()
        self.maps = self.getMaps()
    def getDirectories(self):
        """Create a dict of the main directories in the assets root folder.
        Return the dict at the end."""
        dirs = {}

        for each in os.listdir(self.root):
            dirs.update({each: self.root + "\\" + each})

        return dirs
    def getMaps(self):
        """Walk through the maps-directory and load each json file as a dict.
        Then return a list with each json file."""
        maps = MapList()

        for dirs in os.walk(self.dirs["maps"]):
            for each in dirs[2]:
                if each.split(".")[1] == "json":
                    config = loadJSON(dirs[0] + "\\" + each)
                    config["name"] = dirs[0].split("\\")[-1]
                    config["filepath"] = dirs[0] + "\\" + each
                    maps.append(config)

        return maps

class MapList(list):
    """Extended list for indexing it's dict-contents."""
    def __init__(self):
        """Constructor."""
        list.__init__(self)
    def byName(self, name):
        """Get list entry by it's name."""
        entry = ""

        for each in self:
            if each["name"] == name:
                entry = each

        return entry
