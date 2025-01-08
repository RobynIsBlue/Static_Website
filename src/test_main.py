import unittest

from main import *

class TestHTMLNode(unittest.TestCase):
    def test_extract_title(self):
        sup = extract_title("src/hehe_testing.txt")
        self.assertEqual(sup, "Title")
    
    def test_generate_page(self):
        generate_page("content/index.md", "template.html", "public/index.html")
    
    def test_generate_page_recursive(self):
        generate_pages_recursive("content", "template.html", "public")
        