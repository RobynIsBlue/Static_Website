from enum import Enum
from htmlnode import *

import re

class MarkDownType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6

def block_to_block_type(text):
    count = 0
    if re.match(r"^#{1,6} ", text):
        return "Heading"
    if re.match(r"^\`\`\`[\s\S]+\`\`\`", text):
        return "Code"
    if text.startswith("* ") or text.startswith("- "):
        return "Unordered List"
    if text.startswith(">"):
        return "Quote"
    #fix the count :')

    sext = text.split("\n")
    for line in sext:
        count += 1
        if not re.match(rf"^{count}. ", line):
            return "Paragraph"
    return "Ordered List"

def markdown_to_html_node(markdown, header_num="\n\n"):
    blocked_markdown = markdown_to_blocks(markdown, header_num)
    block_types = ["Paragraph", "Heading", "Code", "Unordered List", "Quote", "Ordered List"]
    tags = ["p", "h", "code", "ul", "blockquote", "ol"]
    blocks = []
    for black in blocked_markdown:
        child = None
        block_type = block_to_block_type(black)

        if block_type == "Heading":
            heading_split = black.split()
            tags[1] = f"h{len(heading_split[0])}"
            if "\n" in black:
                blocks.extend(markdown_to_html_node(black, "\n").children)
                continue
            block = strip_beginning(black)
            index = block_types.index(block_type)
            blocks.append(LeafNode(tags[index], block))
            continue

        if block_type == "Ordered List" or block_type == "Unordered List":
            child = text_to_children(black, "li")
            blocks.append(ParentNode("ul", child))
            continue

        block = strip_beginning(black)
        index = block_types.index(block_type)
        blocks.append(LeafNode(tags[index], block))
    return ParentNode("div", blocks)

def markdown_to_blocks(markdown, splitter):
    say = markdown.split(splitter)
    returned = []
    for marked in say:
        if marked != "":
            returned.append(marked.lstrip("\n").lstrip(" ").rstrip(" "))
    return returned

def text_to_children(text, delim):
    splat = text.split("\n")
    childs = []
    for splot in splat:
        block = strip_beginning(splot)
        childs.append(LeafNode(delim, block))
    return childs
    
def strip_beginning(markdown):
    hehe = markdown.split(" ")
    begs = ["*", "-", "#"]
    if hehe[0] in begs:
        return " ".join(hehe[1:])
    if re.match(r"#{1,6}", hehe[0]):
        return " ".join(hehe[1:])
    if markdown.startswith("```") and markdown.endswith("```"):
        hey = list(markdown)
        return "".join(hey[3:-4])

    return markdown