################
# HTML node
################

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented")

    def props_to_html(self):
        html_props = ""
        if self.props != None:
            for prop in self.props:
                html_props += f' {prop}="{self.props[prop]}"'
        return html_props

    def __str__(self):
        return f"<{self.tag} {self.props}>{self.value}{self.children}</{self.tag}>"

    def __repr__(self):
        return str(self)

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("leaf node must have a value")
        if self.tag == None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.children == None:
            raise ValueError("parent node must have children")
        if self.tag == None:
            raise ValueError("parent node must have a tag")
        return f"<{self.tag}{self.props_to_html()}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"

