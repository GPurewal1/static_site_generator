class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props or {}

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        return_str = ''
        for key,value in self.props.items():
            return_str += f' {key}="{value}"'
        return return_str
    
    def __repr__(self):
        return f"<HTMLNode tag='{self.tag}', value='{self.value}', children={self.children}, props={self.props}>"


class LeafNode(HTMLNode):
    def __init__(self,tag=None, value='', props=None):
        super().__init__(tag=tag, value=value, props=props)
        self.children = []
        
        if value is None or value == '':
            raise ValueError("LeafNode must have a value")
        
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        if self.tag is None:
            return self.value
        
        props_str = self.props_to_html()
        return f'<{self.tag}{props_str}>{self.value}</{self.tag}>'