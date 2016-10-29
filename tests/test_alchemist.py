# -*- coding: utf-8 -*-


from context import alchemist
import unittest
import os.path


class TestAlchemist(unittest.TestCase):
    """
    A set of tests for the Alchemist code generation package.
    """
    def setUp(self):
        self._alchemist = alchemist.Alchemist("Java", "input.txt")

    def test_transmute_creates_java_file(self):
        self._alchemist.transmute()
        self.assertTrue(os.path.isfile("./AddProduct.java"))

    def test_transmute_writes_comments_to_file(self):
        self._alchemist.transmute()
        fh = open("AddProduct.java", "r")
        lines = fh.readlines()
        self.assertEquals("// Add a product", lines[0].strip("\n"))
        self.assertEquals("// to the 'on-order' list", lines[1].strip("\n"))

    def test_transmute_writes_class_to_file(self):
        self._alchemist.transmute()
        fh = open("AddProduct.java", "r")
        lines = fh.readlines()
        self.assertEquals("public class AddProduct {", lines[2].strip("\n"))

    def test_transmute_writes_fields_to_output_file(self):
        self._alchemist.transmute()
        fh = open("AddProduct.java", "r")
        lines = fh.readlines()
        self.assertEquals("    int id;", lines[3].strip("\n"))
        self.assertEquals("    char[] name;", lines[4].strip("\n"))
        self.assertEquals("    String orderCode;", lines[5].strip("\n"))

    def test_transmute_writes_end_of_class_brace(self):
        self._alchemist.transmute()
        fh = open("AddProduct.java", "r")
        lines = fh.readlines()
        self.assertEquals("}", lines[37].strip("\n"))

    def test_transmute_writes_constructor_to_file(self):
        self._alchemist.transmute()
        fh = open("AddProduct.java", "r")
        lines = fh.readlines()
        self.assertEquals("    public AddProduct(int id, char[] name, String orderCode) {", lines[7].strip("\n"))
        self.assertEquals("        this.id = id;", lines[8].strip("\n"))
        self.assertEquals("        this.name = name;", lines[9].strip("\n"))
        self.assertEquals("        this.orderCode = orderCode;", lines[10].strip("\n"))
        self.assertEquals("    }", lines[11].strip("\n"))


    def test_transmute_writes_accessors_and_mutators(self):
        self._alchemist.transmute()
        fh = open("AddProduct.java", "r")
        lines = fh.readlines()
        self.assertEqual("    public int getId() {", lines[13].strip("\n"))
        self.assertEqual("        return id;", lines[14].strip("\n"))
        self.assertEqual("    }", lines[15].strip("\n"))

        self.assertEqual("    public void setId(int id) {", lines[17].strip("\n"))
        self.assertEqual("        this.id = id;", lines[18].strip("\n"))
        self.assertEqual("    }", lines[19].strip("\n"))

        self.assertEqual("    public char[] getName() {", lines[21].strip("\n"))
        self.assertEqual("        return name;", lines[22].strip("\n"))
        self.assertEqual("    }", lines[23].strip("\n"))

        self.assertEqual("    public void setName(char[] name) {", lines[25].strip("\n"))
        self.assertEqual("        this.name = name;", lines[26].strip("\n"))
        self.assertEqual("    }", lines[27].strip("\n"))

        self.assertEqual("    public String getOrderCode() {", lines[29].strip("\n"))
        self.assertEqual("        return orderCode;", lines[30].strip("\n"))
        self.assertEqual("    }", lines[31].strip("\n"))

        self.assertEqual("    public void setOrderCode(String orderCode) {", lines[33].strip("\n"))
        self.assertEqual("        this.orderCode = orderCode;", lines[34].strip("\n"))
        self.assertEqual("    }", lines[35].strip("\n"))


if __name__ == "__main__":
    unittest.main()
