# -*- coding: utf-8 -*-


from context import alchemist
import unittest


class TestAlchemist(unittest.TestCase):
    """A set of tests for the Alchemist code generation package."""
    def setUp(self):
        self._filename = "input.txt"

    def test_transmute(self):
        al = alchemist.Alchemist(self._filename)
        al.transmute()


if __name__ == "__main__":
    unittest.main()
