import unittest

from markdowns import *

class TestMarkdown(unittest.TestCase):

    def test_markdown_to_blocks(self):
        control = ["Block 1", "Block 2", "Block 4", "Block 3!!!"]
        teste = "Block 1\n\nBlock 2\nBlock 4   \n\n\n  Block 3!!!"
        test = markdown_to_blocks(teste, "\n")
        self.assertEqual(control, test)

    def test_markdown_to_blocks_heading(self):
        control = "Heading"
        teste = "#### hey"
        test = block_to_block_type(teste)
        self.assertEqual(control, test)
    
    def test_markdown_to_blocks_quote(self):
        control = "Quote"
        teste = ">hey"
        test = block_to_block_type(teste)
        self.assertEqual(control, test)

    def test_markdown_to_blocks_unordered_list(self):
        control = "Unordered List"
        teste = "- hey!!\n- sup\n- looool\n* lmao\n* teehee"
        test = block_to_block_type(teste)
        self.assertEqual(control, test)

    def test_markdown_to_blocks_ordered_list(self):
        control = "Paragraph"
        teste = "1. hey\n2. what's up\n3. \n3. lol"
        test = block_to_block_type(teste)
        self.assertEqual(control, test)
        
    def test_markdown_to_blocks_ordered_list2(self):
        control = "Ordered List"
        teste = "1. hey\n2. what's up\n3. \n4. lol"
        test = block_to_block_type(teste)
        self.assertEqual(control, test)
    
    def test_markdown_to_blocks_paragraph(self):
        control = "Paragraph"
        teste = "``!!hey"
        test = block_to_block_type(teste)
        self.assertEqual(control, test)

    def test_markdown_to_blocks_code(self):
        control = "Code"
        teste = "```hey```"
        test = block_to_block_type(teste)
        self.assertEqual(control, test)

    def test_markdown_to_html_node_1(self):
        test = "hi"
        control = ParentNode("div", [LeafNode("p", test)])
        self.assertEqual(control, markdown_to_html_node(test))

    def test_markdown_to_html_node_2(self):
        control = ParentNode("div", [
             LeafNode("h1", "Title"),
             LeafNode("p", "This is a paragraph."),
             ParentNode("ul", [
                 LeafNode("li", "Item 1"),
                 LeafNode("li", "Item 2")
             ])
         ])   
        test = "# Title\nThis is a paragraph.\n\n- Item 1\n- Item 2"
        self.assertEqual(control, markdown_to_html_node(test))
    
    def test_markdown_to_html_node_3(self):
        control = ParentNode("div", [
             LeafNode("h1", "Title"),
             LeafNode("p", "This is a paragraph."),
         ])   
        test = "# Title\nThis is a paragraph."
        self.assertEqual(control, markdown_to_html_node(test))

    def test_markdown_to_html_node_4(self):
        control = ParentNode("div", [
             ParentNode("ul", [
                 LeafNode("li", "Item 1"),
                 LeafNode("li", "Item 2")
             ])
         ])   
        test = "- Item 1\n- Item 2"
        self.assertEqual(control, markdown_to_html_node(test))

# import unittest

# from markdowns import *

# class TestMarkdown(unittest.TestCase):

#     def test_markdown_to_blocks(self):
#         control = ["Block 1", "Block 2", "Block 4", "Block 3!!!"]
#         teste = "Block 1\n\nBlock 2\nBlock 4   \n\n\n  Block 3!!!"
#         test = markdown_to_blocks(teste, "\n")
#         self.assertEqual(control, test)

#     def test_markdown_to_blocks_heading(self):
#         control = "Heading"
#         teste = "#### hey"
#         test = block_to_block_type(teste)
#         self.assertEqual(control, test)
    
#     def test_markdown_to_blocks_quote(self):
#         control = "Quote"
#         teste = ">hey"
#         test = block_to_block_type(teste)
#         self.assertEqual(control, test)

#     def test_markdown_to_blocks_unordered_list(self):
#         control = "Unordered List"
#         teste = "- hey!!\n- sup\n- looool\n* lmao\n* teehee"
#         test = block_to_block_type(teste)
#         self.assertEqual(control, test)

#     def test_markdown_to_blocks_ordered_list(self):
#         control = "Paragraph"
#         teste = "1. hey\n2. what's up\n3. \n3. lol"
#         test = block_to_block_type(teste)
#         self.assertEqual(control, test)
        
#     def test_markdown_to_blocks_ordered_list2(self):
#         control = "Ordered List"
#         teste = "1. hey\n2. what's up\n3. \n4. lol"
#         test = block_to_block_type(teste)
#         self.assertEqual(control, test)
    
#     def test_markdown_to_blocks_paragraph(self):
#         control = "Paragraph"
#         teste = "``!!hey"
#         test = block_to_block_type(teste)
#         self.assertEqual(control, test)

#     def test_markdown_to_blocks_code(self):
#         control = "Code"
#         teste = "```hey```"
#         test = block_to_block_type(teste)
#         self.assertEqual(control, test)

#     def test_markdown_to_html_node_1(self):
#         test = "hi"
#         control = HTMLNode("div", None, [HTMLNode("p", test)])
#         self.assertEqual(control, markdown_to_html_node(test))

#     def test_markdown_to_html_node_2(self):
#         control = HTMLNode("div", None, [
#              HTMLNode("h1", "Title"),
#              HTMLNode("p", "This is a paragraph."),
#              HTMLNode("ul", None, [
#                  HTMLNode("li", "Item 1"),
#                  HTMLNode("li", "Item 2")
#              ])
#          ])   
#         test = "# Title\nThis is a paragraph.\n\n- Item 1\n- Item 2"
#         self.assertEqual(control, markdown_to_html_node(test))
    
#     def test_markdown_to_html_node_3(self):
#         control = HTMLNode("div", None, [
#              HTMLNode("h1", "Title"),
#              HTMLNode("p", "This is a paragraph."),
#          ])   
#         test = "# Title\nThis is a paragraph."
#         self.assertEqual(control, markdown_to_html_node(test))

#     def test_markdown_to_html_node_4(self):
#         control = HTMLNode("div", None, [
#              HTMLNode("ul", None, [
#                  HTMLNode("li", "Item 1"),
#                  HTMLNode("li", "Item 2")
#              ])
#          ])   
#         test = "- Item 1\n- Item 2"
#         self.assertEqual(control, markdown_to_html_node(test))