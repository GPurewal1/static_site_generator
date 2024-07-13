import sys
import os

src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(src_dir)

import unittest

from src.parentnode import ParentNode
from src.leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_initialization_with_valid_value(self):
        node = ParentNode("p",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"), LeafNode(None, "Normal text"),])
        self.assertEqual(node.value, '')
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.props, {})

    def test_to_html(self):
        node = ParentNode("p",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"), LeafNode(None, "Normal text"),])
        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_initialization_without_value(self):
        with self.assertRaises(ValueError) as context:
            node = ParentNode("",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"), LeafNode(None, "Normal text"),])
            node.to_html()
        self.assertTrue("Tag must be provided" in str(context.exception))
        with self.assertRaises(ValueError) as context:
            node = ParentNode("p",[])
            node.to_html()
        self.assertTrue("Children must be provided" in str(context.exception))
        with self.assertRaises(ValueError) as context:
            node = ParentNode(None,[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"), LeafNode(None, "Normal text"),])
            node.to_html()
        self.assertTrue("Tag must be provided" in str(context.exception))       
        with self.assertRaises(ValueError) as context:
            node = ParentNode("p",None)
            node.to_html()
        self.assertTrue("Children must be provided" in str(context.exception))

    def test_nested_parent_node(self):
        inner_node = ParentNode("div", [LeafNode(None, "Inner text")])
        outer_node = ParentNode("p", [inner_node, LeafNode(None, "Outer text")])
        self.assertEqual(outer_node.to_html(), "<p><div>Inner text</div>Outer text</p>")

if __name__ == "__main__":
    unittest.main()