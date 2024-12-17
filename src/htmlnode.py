from textnode import TextNode, TextType


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return f" href=\"\" target=\"\""
        return f" href=\"{self.props["href"]}\" target=\"{self.props["target"]}\""
    
    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode has no value")
        if self.tag == None:
            return self.value
        all = []
        if self.props != None:
            keys = self.props.keys()
            for key in keys:
                all.append(f" {key}=\"{self.props[key]}\"")
        all = "".join(all)
        return f"<{self.tag}{all}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Object has no tag")
        if self.children == None:
            raise ValueError("Object has no children (get some bitches)")
        child_list = []
        all = []
        if self.props != None:
            keys = self.props.keys()
            for key in keys:
                all.append(f" {key}=\"{self.props[key]}\"")
        for child in self.children:
            child_list.append(child.to_html())
        joined_keys = "".join(all)
        joined_child_list = "".join(child_list)
        return f"<{self.tag}{joined_keys}>{joined_child_list}</{self.tag}>"


def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case TextType.NORMAL:
            return LeafNode(None, text_node.text).to_html()
        case TextType.BOLD:
            return LeafNode("b", text_node.text).to_html()
        case TextType.ITALIC:
            return LeafNode("i", text_node.text).to_html()
        case TextType.CODE:
            return LeafNode("code", text_node.text).to_html()
        case TextType.LINKS:
            return LeafNode("a", text_node.text, {"href": text_node.url}).to_html()
        case TextType.IMAGES:
            return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text}).to_html()
        case _:
            raise Exception("Invalid Text Type")