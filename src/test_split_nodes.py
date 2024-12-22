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

    def test_split_nowdes_delimiter_silly(self):
        control = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.BOLD),
            TextNode(" word", TextType.NORMAL),
            ]
        node = TextNode("This is text with a **code block** word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(control, new_nodes)

    def test_split_nodevs_delimiter_silly(self):
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
        
    def tesat_extract_markdown_image12s(self):
        control = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        text = extract_markdown_images(text)
        self.assertEqual(control, text)
    
    def test_extract_marskdown_images(self):
        control = []
        text = "This is text with a "
        text = extract_markdown_images(text)
        self.assertEqual(control, text)
    
    def test_extract_markddown_image1s(self):
        control = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"), ("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg), ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        text = extract_markdown_images(text)
        self.assertEqual(control, text)

    def test_extract_markddown_images(self):
        control = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(control, extract_markdown_links(text))

    def test_split_nodes_image(self):
        control =  [
        TextNode("This is text with a link ", TextType.NORMAL),
        TextNode("to boot dev", TextType.IMAGES, "https://www.boot.dev"),
        TextNode(" and ", TextType.NORMAL),
        TextNode("to youtube", TextType.IMAGES, "https://www.youtube.com/@bootdotdev"),
        TextNode(" teehee", TextType.NORMAL),
        ]
        compare = split_nodes_image(TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev) teehee", TextType.IMAGES))
        self.assertEqual(control, compare)

    def test_split_two_consec_images(self):
        control =  [
        TextNode("This is text with a link ", TextType.NORMAL),
        TextNode("to boot dev", TextType.IMAGES, "https://www.boot.dev"),
        TextNode("to youtube", TextType.IMAGES, "https://www.youtube.com/@bootdotdev"),
        TextNode(" teehee", TextType.NORMAL),
        ]
        compare = split_nodes_image(TextNode("This is text with a link ![to boot dev](https://www.boot.dev)![to youtube](https://www.youtube.com/@bootdotdev) teehee", TextType.IMAGES))
        self.assertEqual(control, compare)
    
    def test_split_nodes_links(self):
        control =  [
        TextNode("This is text with a link ", TextType.NORMAL),
        TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
        TextNode(" and ", TextType.NORMAL),
        TextNode("to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev"),
        ]
        compare = split_nodes_links(TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL))
        self.assertEqual(control, compare)
    
    def test_text_to_textnodes(self):
        control = [
        TextNode("This is ", TextType.NORMAL),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.NORMAL),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.NORMAL),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.NORMAL),
        TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.NORMAL),
        TextNode("link", TextType.LINKS, "https://boot.dev"),
        ]
        test = text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertEqual(control, test)

    def test_text_to_textnodes_hehe(self):
        control = [
        TextNode("This is", TextType.NORMAL),
        ]
        test = text_to_textnodes("This is")
        self.assertEqual(control, test)