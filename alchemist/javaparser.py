from alchemist import Parser
import re


class JavaParser(Parser):
    def __init__(self, kwargs):
        self._file_extension = "Java"
        Parser.__init__(self, kwargs)

    def parse(self):
        fh = open(self.file)
        comments = []
        for line in fh:
            line = line.strip("\n")
            match = self.get_class_pattern(line)
            if match:
                classname = match.group(1)
                filename = "{}.{}".format(classname, self._file_extension.lower())
                self.file = open(filename, "w")
                if len(comments) > 0:
                    joined_comments = "\n".join(comments)
                    print(joined_comments, file=self.file)
                    comments.clear()

                print("public class {} {{".format(classname), file=self.file)
                continue

            match = self.get_comment_pattern(line)
            if match:
                comments.append(match.group(0))
                continue

            match = self.get_field_pattern(line)
            if match:
                if len(comments) > 0:
                    joined_comments = "\n".join(comments)
                    print(joined_comments, file=self.file)
                    comments.clear()

                print("    {} {};".format(match.group(2), match.group(1)), file=self.file)
                continue

            match = self.get_end_pattern(line)
            if match:
                print("}", file=self.file)

        self.file.close()
        fh.close()

    def get_comment_pattern(self, line):
        return re.compile("^[/]{2}\s.*$").search(line)

    def get_class_pattern(self, line):
        return re.compile("^C\s(([A-Z](?=[a-z])[a-z]+)+)$").search(line)

    def get_field_pattern(self, line):
        return re.compile("^F\s(\\b(?:[a-z]+)(?=[A-Z]+)(?:[A-Za-z]+)|[a-z]+\\b)\s*((?:[A-Z]?[a-z]+("
                   "?:[[]])?))$").search(line)

    def get_end_pattern(self, line):
        return re.compile("^E$").search(line)


