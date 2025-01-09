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
        return (self.tag, self.value, self.children, self.props)
    
        