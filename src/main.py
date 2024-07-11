from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode


def main():
    text_node = TextNode('This is a text node', 'bold', 'https://www.boot.dev')
    html_node = HTMLNode('h1','heading',None,{"href": "https://www.google.com", "target": "_blank",})
    leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(leaf_node.to_html())

main()