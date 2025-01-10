class HTMLNode():
    def __init__(self, tag="None", value="None", children="None", props="None"):
        self.tag = tag  #HTML Tag
        self.value = value #Text inside the tag
        self.children = children #Children of this node
        self.props = props #Attributes of this tag

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_string = ""
        if self.props == "None":
            return self.props
        for key,value in self.props.items():
            props_string = props_string + str(key) + '=' + "\"" + str(value) + "\" "
        return props_string
    
    def __repr__(self):
        return f"{str(self.tag)} {str(self.value)} {str(self.children)}  {str(self.props)}"
    
        
class LeafNode(HTMLNode):
    def __init__(self, tag="None", value="None", props="None"):
        super().__init__()
        self.tag = tag  #HTML Tag
        self.value = value #Text inside the tag
        self.props = props #Attributes of this tag

    def to_html(self):
        local_props = ""
        if self.value == "None":
            raise ValueError("Missing Value")
        if self.tag == "None":
            return str(self.value)
        if self.props == "None":
            local_props = ""
            return f"<{self.tag}{local_props}>{self.value}</{self.tag}>"
        else:
            for key,value in self.props.items():
                local_props = local_props + str(key) + '=' + "\"" + str(value) + "\""
                return f"<{self.tag} {local_props}>{self.value}</{self.tag}>"
            


class ParentNode(HTMLNode):
    def __init__(self, tag="None", value="None", children="None", props="None"):
        super().__init__()
        self.tag = tag  #HTML Tag
        self.value = value #Text inside the tag
        self.children = children #Children of this node
        self.props = props #Attributes of this tag

    def child_node_digger(self, children):
        if len(children) == 0:
            return ""
        else:
            return str(children[0].to_html) + self.child_node_digger(children[1:])

    def to_html(self):
        child_nodes = ""
        if self.tag == "None":
            raise ValueError("Tag is required")
        if self.children == "None":
            raise ValueError("Parents have children")
        return self.child_node_digger(self.children)
