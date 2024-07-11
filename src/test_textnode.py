import unittest

from textnode import TextNode


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


if __name__ == "__main__":
    unittest.main()