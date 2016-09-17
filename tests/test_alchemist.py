# -*- coding: utf-8 -*-


from context import alchemist
import unittest
import os.path


class TestAlchemist(unittest.TestCase):
    """
    A set of tests for the Alchemist code generation package.
    """
    def setUp(self):
        self._alchemist = alchemist.Alchemist("input.txt")

    def test_transmute_creates_java_file(self):
        self._alchemist.transmute()
        self.assertTrue(os.path.isfile("./AddProduct.java"))

    def test_transmute_writes_comments_to_file(self):
        self._alchemist.transmute()
        fh = open("AddProduct.java", "r")
        lines = fh.readlines()
        self.assertTrue("// Add a product", lines[0].strip("\n"))
        self.assertTrue("// to the 'on-order' list", lines[1].strip("\n"))

    def test_transmute_writes_class_to_file(self):
        self._alchemist.transmute()
        fh = open("AddProduct.java", "r")
        lines = fh.readlines()
        self.assertTrue("public class AddProduct {", lines[2].strip("\n"))

    def tearDown(self):
        os.remove("./AddProduct.java")


if __name__ == "__main__":
    unittest.main()
