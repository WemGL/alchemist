from alchemist import Parser
import re


class JavaParser(Parser):
    def __init__(self, kwargs):
        self._file_extension = "Java"
        self._current_match = None
        self._fields = []
        self._classname = ""
        Parser.__init__(self, kwargs)

    def parse(self):
        fh = open(self.file)
        comments = []
        for line in fh:
            if self.matched_class_pattern(line):
                self.parse_class_match(comments)
            elif self.matched_comment_pattern(line):
                self.parse_comment_match(comments)
            elif self.matched_field_pattern(line):
                self.parse_field_match(comments)
            elif self.matched_end_pattern(line):
                self.write_constructor()
                self.parse_end_match()

        self.file.close()
        fh.close()

    def parse_end_match(self):
        print("}", file=self.file)

    def parse_field_match(self, comments):
        if len(comments) > 0:
            joined_comments = "\n".join(comments)
            print(joined_comments, file=self.file)
            comments.clear()
        type = self._current_match.group(2)
        identifier = self._current_match.group(1)
        field = dict()
        field[type] = identifier
        self._fields.append(field)
        print("    {} {};".format(type, identifier), file=self.file)

    def parse_comment_match(self, comments):
        comments.append(self._current_match.group(0))

    def parse_class_match(self, comments):
        self._classname = self._current_match.group(1)
        filename = "{}.{}".format(self._classname, self._file_extension.lower())
        self.file = open(filename, "w")
        if len(comments) > 0:
            joined_comments = "\n".join(comments)
            print(joined_comments, file=self.file)
            comments.clear()
        print("public class {} {{".format(self._classname), file=self.file)

    def matched_comment_pattern(self, line):
        self._current_match = re.compile("^[/]{2}\s.*$").search(line)
        return self._current_match is not None

    def matched_class_pattern(self, line):
        self._current_match = re.compile("^C\s(([A-Z](?=[a-z])[a-z]+)+)$").search(line)
        return self._current_match is not None

    def matched_field_pattern(self, line):
        self._current_match = re.compile("^F\s(\\b(?:[a-z]+)(?=[A-Z]+)(?:[A-Za-z]+)|[a-z]+\\b)\s*((?:[A-Z]?[a-z]+("
                   "?:[[]])?))$").search(line)
        return self._current_match is not None

    def matched_end_pattern(self, line):
        self._current_match = re.compile("^E$").search(line)
        return self._current_match is not None

    def write_constructor(self):
        match_found = len(self._current_match.group(0)) > 0
        if not match_found:
            return

        self.write_newline()

        fields = ", ".join(self.format_type_and_identifier())
        print("    public {}({}) {{".format(self._classname, fields), file=self.file)

        for identifier in self.get_identifiers():
            self.write_initialization_for(identifier[0])

        print("    }", file=self.file)

    def get_identifiers(self):
        return map(lambda type_with_identifiers: list(type_with_identifiers.values()), self._fields)

    def format_type_and_identifier(self):
        return map(
            lambda type_with_identifiers: "{} {}".format(list(type_with_identifiers.keys())[0],
                                                         list(type_with_identifiers.values())[0]),
            self._fields)

    def write_initialization_for(self, identifier):
        print("        this.{} = {};".format(identifier, identifier), file=self.file)

    def write_newline(self):
        print("", file=self.file, end="\n")


