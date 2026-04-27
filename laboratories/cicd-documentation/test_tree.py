import unittest
from tree import Tree
from node import Node

class TestTreeFind(unittest.TestCase):
    
    def setUp(self):
    
        self.tree = Tree()
        self.tree.add(3)
        self.tree.add(4)
        self.tree.add(0)
        self.tree.add(8)
        self.tree.add(2)

    def test_find_non_existing_node(self):
        """vedem daca functia returneaza None pentru valori care nu exista."""
        gasit = self.tree.find(10)
        self.assertIsNone(gasit, "Valoarea 10 nu exista, functia trebuia sa returneze None.")

    def test_find_in_empty_tree(self):
        """ cautare in arbore nou, gol"""
        empty_tree = Tree()
        gasit = empty_tree.find(3)
        self.assertIsNone(gasit, "Cautarea intr-un arbore gol returneaza None.")

if __name__ == '__main__':
    unittest.main()