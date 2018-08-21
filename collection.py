class Collection(dict):
    """."""
    def __init__(self, *arg, **kw):
        """Constructor."""
        super(Collection, self).__init__(*arg, **kw)
        self.type = "<class 'Collection'>"
        self.names = []# list
        for each in iter(self):
            self.names.append(each)
    def __str__(self):
        """String representation."""
        list = []

        for key in self.keys():
            list.append(
                "'{0}': {1}".format(key, type(self[key]))
            )

        joined = "\n".join(list)
        lines = "\n--- Collection:\n" + joined + "\n---"

        return lines
    def add(self, obj):
        """Appending a new position in the colletion."""
        for k, v in obj.items():
            self[k] = v
            self.names.append(k)
    def remove(self, key):
        """Removing a specific position from the colletion."""
        for i, name in enumerate(self.names):
            if name == key:
                del self[key]
                del self.names[i]
