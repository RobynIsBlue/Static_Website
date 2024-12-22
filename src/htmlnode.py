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
        if not isinstance(self.props, dict):
            raise TypeError("Self.Props not a dict")
        keys = self.props.keys()
        all = []
        for key in keys:
            print(key, self.props, self.props[key])
            all.append(f" {key}=\"{self.props[key]}\"")
        return "".join(all)
        
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
        htmlized = ""
        if self.props != None:
            htmlized = self.props_to_html()
        return f"<{self.tag}{htmlized}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        htmlized = ""
        if self.tag == None:
            raise ValueError("Object has no tag")
        if self.children == None:
            raise ValueError("Object has no children (get some bitches)")
        child_list = []
        if self.props != None:
            htmlized = self.props_to_html()
        for child in self.children:
            child_list.append(child.to_html())
        joined_child_list = "".join(child_list)
        return f"<{self.tag}{htmlized}>{joined_child_list}</{self.tag}>"


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
            return LeafNode("a", text_node.text, text_node.url).to_html()
        case TextType.IMAGES:
            return LeafNode("img", "", text_node.url).to_html()
        case _:
            raise Exception("Invalid Text Type")