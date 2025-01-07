from textnode import TextNode, TextType

import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    returned_list = []
    if delimiter == "" or delimiter == None:
        returned_list.extend(old_nodes)
        return returned_list

    if not isinstance(text_type, TextType):
        raise ValueError("Text type not valid")

    for old_node in old_nodes:
        if old_node.text_type == TextType.NORMAL:
            split_old_node_text = old_node.text.split(delimiter)
            returned_list.append(TextNode(split_old_node_text[0], TextType.NORMAL))
            for block_index in range(1, len(split_old_node_text), 2):
                returned_list.append(TextNode(split_old_node_text[block_index], text_type))
                if block_index <= len(split_old_node_text):
                    returned_list.append(TextNode(split_old_node_text[block_index + 1], text_type.NORMAL))
        else:
            returned_list.append(old_node)

    return returned_list

def list_split_nodes_delimiter(old_nodes, delimiter, text_type):
    returned_list = []
    for old_node in old_nodes:
        returned_list.append(split_nodes_delimiter(old_node, delimiter, text_type))


    return returned_list
        
def extract_markdown_images(text):
    matches = re.findall(r"\!\[([^]]*)\]\(([^)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[([^]]*)\]\(([^)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    split_nodes = []
    indexy = 0
    matches = extract_markdown_images(old_nodes.text)
    for match in matches:
        string_index = (old_nodes.text).find(match[0])
        url_index = (old_nodes.text).find(match[1])
        if indexy != string_index - 2:
            split_nodes.append(TextNode(old_nodes.text[indexy:string_index - 2], TextType.NORMAL))
        split_nodes.append(TextNode(old_nodes.text[string_index:string_index + len(match[0])], TextType.IMAGES, old_nodes.text[url_index:url_index + len(match[1])]))
        indexy = url_index + len(match[1]) + 1
    if indexy < len(old_nodes.text):
        split_nodes.append(TextNode(old_nodes.text[indexy:], TextType.NORMAL))
    return split_nodes

def split_nodes_links(old_nodes):
    if old_nodes.text_type == TextType.NORMAL:
        split_nodes = []
        indexy = 0
        matches = extract_markdown_links(old_nodes.text)
        for match in matches:
            string_index = (old_nodes.text).find(match[0])
            url_index = (old_nodes.text).find(match[1])
            if indexy != string_index - 1:
                split_nodes.append(TextNode(old_nodes.text[indexy:string_index - 1], TextType.NORMAL))
            split_nodes.append(TextNode(old_nodes.text[string_index:string_index + len(match[0])], TextType.LINKS, old_nodes.text[url_index:url_index + len(match[1])]))
            indexy = url_index + len(match[1]) + 1
        if indexy < len(old_nodes.text):
            split_nodes.append(TextNode(old_nodes.text[indexy:], TextType.NORMAL))
        return split_nodes
    else:
        return [old_nodes]

def text_to_textnodes(text):
    new_node = TextNode(text, TextType.NORMAL)
    linked = split_nodes_image(new_node)
    nodey = []
    if len(linked) == 1:
        nodey = [split_nodes_links(linked[0])]
    else:
        for linki in linked:
            nodey.append(split_nodes_links(linki))
    nodes = sum(nodey, [])
    return split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(nodes, "**", TextType.BOLD), "*", TextType.ITALIC), "`", TextType.CODE)




