################
# Unit Tests
################

import unittest

from textnode import TextNode, TextType

class TextTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_ne(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_url(self):
        n1 = TextNode("text", TextType.CODE)
        n2 = TextNode("text", TextType.CODE, None)
        self.assertEqual(n1, n2)

    def test_None_vs_blank(self):
        n1 = TextNode("", TextType.CODE, "")
        n2 = TextNode("", TextType.CODE)
        self.assertNotEqual(n1, n2)

if __name__ == '__main__':
    unittest.main()
