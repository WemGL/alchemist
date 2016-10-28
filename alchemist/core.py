# -*- coding: utf-8 -*-

import alchemist


class Alchemist:
    def __init__(self, file=None):
        self._file = file

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, file):
        self._file = file

    @file.deleter
    def file(self):
        del self._file

    def transmute(self, language):
        if language == "Java":
            parser = alchemist.JavaParser({'file': self.file})
            parser.parse()


def main():
    alchemist = Alchemist()


if __name__ == '__main__':
    main()
