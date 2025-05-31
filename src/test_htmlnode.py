################
# Unit Tests
################

import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node1.__str__(), node2.__str__())

    def test_ne(self):
        node1 = HTMLNode()
        node2 = HTMLNode("<p>")
        self.assertNotEqual(node1.__str__(), node2.__str__())

    def test_props_to_html(self):
        props = ''
        props_dict = {
                "href": "http://example.com",
                "class": "my-class"
                }
        for prop in props_dict:
            props += f' {prop}="{props_dict[prop]}"'

        node = HTMLNode("<p>", "", "", props_dict)
        self.assertEqual(props, node.props_to_html())

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


    def test_leaf_to_html_href(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_with_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchild(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node1 = LeafNode("b", "grandchild 1")
        grandchild_node2 = LeafNode("i", "grandchild 2")
        child_node = ParentNode("span", [grandchild_node1, grandchild_node2])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild 1</b><i>grandchild 2</i></span></div>",
        )

    def test_to_html_DINK(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

if __name__ == '__main__':
    unittest.main()
