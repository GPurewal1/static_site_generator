from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode


def main():
    text_node = TextNode('This is a text node', 'bold', "https://www.google.com")
    html_node = HTMLNode('h1','heading',None,{"href": "https://www.google.com", "target": "_blank",})
    leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    parent_node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )

    print(parent_node.to_html())

main()