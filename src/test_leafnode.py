import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_initialization_with_valid_value(self):
        node = LeafNode(tag="p", value="This is a paragraph.")
        self.assertEqual(node.value, "This is a paragraph.")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.props, {})
        self.assertEqual(node.children, []) # No children allowed

    def test_initialization_without_value(self):
        with self.assertRaises(ValueError):
            LeafNode(tag="p", value='')
        with self.assertRaises(ValueError):
            LeafNode(tag="p", value=None)

    def test_html_rendering_with_tag(self):
        node = LeafNode(tag="p", value="This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")
    
    def test_html_rendering_without_tag(self):
        node = LeafNode(value="Just some text.")
        self.assertEqual(node.to_html(), "Just some text.")
    
    def test_html_rendering_with_props(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')


if __name__ == "__main__":
    unittest.main()