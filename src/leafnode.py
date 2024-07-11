from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self,tag=None, value='', props=None):
        super().__init__(tag=tag, value=value, props=props)
        self.children = []
        
        if value is None:
            raise ValueError("LeafNode must have a value")
        
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        if self.tag is None:
            return self.value
        
        props_str = self.props_to_html()
        return f'<{self.tag}{props_str}>{self.value}</{self.tag}>'