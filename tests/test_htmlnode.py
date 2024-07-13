import sys
import os

src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(src_dir)

import unittest

from src.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_empty_dict(self):
        node = HTMLNode('h1','heading')
        self.assertEqual(node.props,{})

    def test_children_none(self):
        node = HTMLNode('h1','heading')
        self.assertIsNone(node.children)

    def test_props_not_eq(self):
        node = HTMLNode('h1','heading',None,{"href": "https://www.google.com", "target": "_blank",})
        node2 = HTMLNode('h1','heading',None,{"href": "https://www.google.com",})
        self.assertNotEqual(node, node2)

    def test_tag_not_eq(self):
        node = HTMLNode('h1','heading',None,{"href": "https://www.google.com", "target": "_blank",})
        node2 = HTMLNode('p','heading',None,{"href": "https://www.google.com", "target": "_blank",})
        self.assertNotEqual(node.tag, node2.tag)
    
    def test_value_not_eq(self):
        node = HTMLNode('h1','heading',None,{"href": "https://www.google.com", "target": "_blank",})
        node2 = HTMLNode('h1','title',None,{"href": "https://www.google.com", "target": "_blank",})
        self.assertNotEqual(node.value, node2.value)


if __name__ == "__main__":
    unittest.main()