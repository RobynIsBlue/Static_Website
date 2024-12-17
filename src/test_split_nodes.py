import unittest

from split_nodes import *

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        control = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL),
            ]
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(control, new_nodes)

    def test_split_nodes_delimiter_silly(self):
        control = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.BOLD),
            TextNode(" word", TextType.NORMAL),
            ]
        node = TextNode("This is text with a **code block** word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(control, new_nodes)

    def test_split_nodes_delimiter_silly(self):
        control = [
            TextNode("This is text with a dog!", TextType.NORMAL)
            ]
        node = TextNode("This is text with a dog!", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "", TextType.BOLD)
        self.assertEqual(control, new_nodes)
        
    def test_split_nodes_delimiter_silly(self):
        node = TextNode("This is text with a **code block** word", TextType.NORMAL)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", "WOKLOS")
        
    def test_extract_markdown_images(self):
        control = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        text = extract_markdown_images(text)
        print(control)
        print(text)