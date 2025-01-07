import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        control = " href=\"https://www.google.com\" target=\"_blank\""
        compare = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(control, compare.props_to_html())
    

    # def test_props2(self):
    #     compare = HTMLNode(None, None, None, None)
    #     with self.assertRaises(TypeError):
    #         compare.props_to_html()


    def test_props3(self):
        control = " href=\"https://www.pepe.com\" target=\"hi!!\""
        compare = HTMLNode("pepe", "textst", [], {"href": "https://www.pepe.com", "target": "hi!!",})
        self.assertEqual(control, compare.props_to_html())
    

    def test_to_html(self):
        control = "<p>This is a paragraph of text.</p>"
        compare = LeafNode("p", "This is a paragraph of text.", None)
        self.assertEqual(control, compare.to_html())
    

    def test_to_html_with_props(self):
        control = "<a href=\"https://www.google.com\" title=\"Example\">Click me!</a>"
        compare = LeafNode("a", "Click me!", {"href": "https://www.google.com", "title": "Example"})
        self.assertEqual(control, compare.to_html())


    def test_to_html_sin_value(self):
        teste = LeafNode("a", None, {"href": "https://www.google.com", "title": "Example"})
        with self.assertRaises(ValueError):
            teste.to_html()


    def test_to_html_sin_tag(self):
        teste = LeafNode(None, "Click me!", {"href": "https://www.google.com", "title": "Example"})
        control = "Click me!"
        self.assertEqual(control, teste.to_html())


    def test_parent_to_html_normal(self):
        control = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
        self.assertEqual(control, node.to_html())


    def test_parent_to_html_nested_parent_womp(self):
        control = "<p>Normal text<p><b>Bold text</b>Normal text</p><i>italic text</i></p>"
        node = ParentNode(
        "p",
        [
            LeafNode(None, "Normal text"),
            ParentNode(
                        "p",
                        [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                ],
            ),
            LeafNode("i", "italic text"),
        ],
        )
        self.assertEqual(control, node.to_html())


    def test_parent_to_html_with_props(self):
        control = "<p hehe=\"haha\" glorp=\"glep\"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        {"hehe": "haha", "glorp": "glep"}
        )
        self.assertEqual(control, node.to_html())

    def test_parent_to_html_nested_parent(self):
        control = "<p>Normal text<p><b hehe=\"haha\" glorp=\"glep\">Bold text</b>Normal text</p><i>italic text</i></p>"
        node = ParentNode(
        "p",
        [
            LeafNode(None, "Normal text"),
            ParentNode(
                        "p",
                        [
                    LeafNode("b", "Bold text", {"hehe": "haha", "glorp": "glep"}),
                    LeafNode(None, "Normal text"),
                ],
            ),
            LeafNode("i", "italic text"),
        ],
        )
        self.assertEqual(control, node.to_html())

    def test_text_node_to_html_node_aight(self):
        control = "hehehe"
        compare = TextNode("hehehe", TextType.NORMAL, {"href": "https://dork.com"})
        self.assertEqual(control, text_node_to_html_node(compare))

    def test_text_node_to_html_node_bruh(self):
        control = "<b>hehehe</b>"
        compare = TextNode("hehehe", TextType.BOLD, {"href": "https://dork.com"})
        self.assertEqual(control, text_node_to_html_node(compare))

    def test_text_node_to_html_no(self):
        control = "<i>hehehe</i>"
        compare = TextNode("hehehe", TextType.ITALIC, {"href": "https://dork.com"})
        self.assertEqual(control, text_node_to_html_node(compare))

    def test_text_node_to_html_node_lol(self):
        control = "<code>hehehe</code>"
        compare = TextNode("hehehe", TextType.CODE, {"href": "https://dork.com"})
        self.assertEqual(control, text_node_to_html_node(compare))

    def test_text_node_to_html_node_wo(self):
        control = "<a href=\"https://dork.com\">hehehe</a>"
        compare = TextNode("hehehe", TextType.LINKS, {"href": "https://dork.com"})
        self.assertEqual(control, text_node_to_html_node(compare))

    def test_text_node_to_html_node_haha(self):
        control = "<img src=\"https://dork.com\" alt=\"this is a pee\"></img>"
        compare = TextNode("hehehe", TextType.IMAGES, {"src": "https://dork.com", "alt": "this is a pee"})
        self.assertEqual(control, text_node_to_html_node(compare))

    def test_text_node_to_html_node_hehe(self):
        TextNode("hehehe", "hehe", {"href": "https://dork.com"})
        with self.assertRaises(Exception):
            text_node_to_html_node()