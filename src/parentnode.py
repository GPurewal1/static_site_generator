from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=[], props={}):
        super().__init__(tag=tag, children=children, props=props)
        self.value = ''

        if self.tag is None or self.tag == '':
            raise ValueError("Tag must be provided")
        
        if self.children is None or self.children == []:
            raise ValueError("Children must be provided")
        
    def to_html(self):
        if self.tag is None or self.tag == '':
            raise ValueError("Tag must be provided")
        
        if self.children is None or self.children == []:
            raise ValueError("Children must be provided")
        
        props_str = self.props_to_html()
        children_str = ''

        for child in self.children:
            children_str += child.to_html()

        return f'<{self.tag}{props_str}>{children_str}</{self.tag}>'