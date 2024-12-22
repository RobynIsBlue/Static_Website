from enum import Enum

def markdown_to_blocks(markdown):
    markdown.split("\n")
    returned = []
    for marked in markdown:
        if marked != "\n":
            returned.append(marked)
    return returned



class MarkDownType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6

def block_to_block_type(text):
    if text.text[0] == "#":
        #HEADING
        pass
    if text[0:2] == "```":
        # CODE
        pass
    if text[0] == ">":
        # QUOTE
        pass
    if text[0:1] == "* " or text[0:1] == "- ":
        #UNORDERED_LIST
        pass
    hehe = 1
    text.split("\n")
    for line in text:
        if line[0:2] != f"{hehe}. ":
            #PARAGRAPH
            pass
    #ORDERED_LIST
    pass

