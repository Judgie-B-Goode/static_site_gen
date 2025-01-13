class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag  #HTML Tag
        self.value = value #Text inside the tag
        self.children = children #Children of this node
        self.props = props #Attributes of this tag

    def to_html(self):
        raise NotImplementedError("Not Implemented")
    
    def props_to_html(self):
        props_string = ""
        if self.props is None:
            return ""
        for prop in self.props:
            props_string += f' {prop}="{self.props[prop]}"'
        return props_string
    
    def __repr__(self):
        return f"{str(self.tag)} {str(self.value)} {str(self.children)}  {str(self.props)}"
    
        
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Missing Value")
        if self.tag is None:
            return str(self.value)
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        child_nodes = ""
        if self.tag is None:
            raise ValueError("Tag is required")
        if self.children is None:
            raise ValueError("Parents have children")
        for child in self.children:
            child_nodes += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{child_nodes}</{self.tag}>"
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"