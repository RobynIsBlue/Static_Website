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
        split_old_node_text = old_node.text.split(delimiter)
        returned_list.append(TextNode(split_old_node_text[0], TextType.NORMAL))
        for block_index in range(1, len(split_old_node_text), 2):
            returned_list.append(TextNode(split_old_node_text[block_index], text_type))
            if block_index <= len(split_old_node_text):
                returned_list.append(TextNode(split_old_node_text[block_index + 1], text_type.NORMAL))

    return returned_list
        
def extract_markdown_images(text):
    matches = re.findall(r"\!\[.*?\]\(.*?\)", text)
    return matches
