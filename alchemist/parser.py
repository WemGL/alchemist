class Parser:
    def __init__(self, kwargs={}):
        self._properties = kwargs

    def get_properties(self):
        return self._properties

    def get_property(self, key):
        return self._properties.get(key, None)

    def set_property(self, key, value):
        self._properties[key] = value

    @property
    def file(self):
        return self._properties.get("file", None)

    @file.setter
    def file(self, file):
        self._properties["file"] = file

    @file.deleter
    def file(self):
        del self._properties["file"]

    def get_comment_pattern(self, line):
        pass

    def get_class_pattern(self, line):
        pass

    def get_field_pattern(self, line):
        pass

    def get_end_pattern(self, line):
        pass


