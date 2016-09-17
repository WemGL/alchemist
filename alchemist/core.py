# -*- coding: utf-8 -*-

import re
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

    def transmute(self):
        extension_pattern = re.compile("^Java$")
        comment_pattern = re.compile("^[/]{2}\s.*$")
        class_pattern = re.compile("^C\s(([A-Z](?=[a-z])[a-z]+)+)$")
        field_pattern = re.compile("^F\s(\b(?:[a-z]+)(?=[A-Z]+)(?:[A-Za-z]+)|(?:[a-z]+)\b)\s*(("
                                   "?:["
                                   "A-Z]?["
                                   "a-z]+(:?:[\[]])?))$")
        end_pattern = re.compile("^E$")

        fh = open("input.txt")
        first_line = fh.readline()
        extension_match = extension_pattern.search(first_line)
        if extension_match:
            file_extension = extension_match.group(0)
        else:
            return

        parser = alchemist.JavaParser()
        comments = []
        for line in fh:
            match = class_pattern.search(line)
            if match:
                classname = match.group(1)
                filename = "{}.{}".format(classname, file_extension.lower())
                parser.file = open(filename, "w")
                joined_comments = "\n".join(comments)
                print(joined_comments, file=parser.file)

                print("public class {} {{".format(classname), file=parser.file)
                continue

            match = comment_pattern.search(line)
            if match:
                comments.append(match.group(0))
                continue


def main():
    alchemist = Alchemist()


if __name__ == '__main__':
    main()
