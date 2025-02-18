import sys
import os

src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(src_dir)

import unittest

from src.textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    text_node_to_html_node,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", "bold")
        self.assertIsNone(node.url)

    def test_url_not_eq_none(self):
        node = TextNode("This is a text node", "bold",'https://www.boot.dev')
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", "bold",'https://www.boot.dev')
        node2 = TextNode("This is a text node", "bold", 'https://www.boot.dev/dev1')
        self.assertNotEqual(node, node2)
    
    def test_text_not_eq(self):
        node = TextNode("This is a text node", "bold",'https://www.boot.dev')
        node2 = TextNode("This is not a text node", "bold", 'https://www.boot.dev')
        self.assertNotEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", text_type_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", text_type_image, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.google.com", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", text_type_bold)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()