# -*- coding: utf-8 -*-


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

    def transmute(self):
        fh = open(self._file)
        for line in fh:
            print(line, end='')


def main():
    alchemist = Alchemist()


if __name__ == '__main__':
    main()
