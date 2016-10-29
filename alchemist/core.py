# -*- coding: utf-8 -*-

import alchemist
import argparse


class Alchemist:
    def __init__(self, language, file):
        self._language = language
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
        if self._language.lower() == "java":
            parser = alchemist.JavaParser({'file': self.file})
            parser.parse()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("language", help="The desired output language described by the file to be transmuted")
    parser.add_argument("file", help="The path to description file of the language that is being transmuted")
    args = parser.parse_args()
    alchemist = Alchemist(args.language, args.file)
    alchemist.transmute()


if __name__ == '__main__':
    main()
