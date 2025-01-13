import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props1(self):
        tester = HTMLNode(tag="<a>",value="Some Stuff")
        print(tester.props_to_html()) 

    def test_props2(self):
        tester = HTMLNode(tag="<a>",value="Some Stuff", props= {"href": "https://www.google.com", 
        "target": "_blank"})
        print(tester.props_to_html())

    def test_props3(self):
        tester = HTMLNode(tag="<a>",value="Some Stuff", props= {"href": "https://www.google.com", 
        "target": "_blank", "height" : 500, "width" : 500})
        print(tester.props_to_html())

    def test_leaf1(self):
        leaftest = LeafNode(tag = "a", value = "POOP", props={"butt":"junk"})
        print(leaftest.to_html())

    def test_leaf3(self):
        leaftest = LeafNode(None, value = "POOP", props={"butt":"junk"})
        print(leaftest.to_html())

    def test_to_html_with_children(self):
            child_node = LeafNode("span", "child")
            parent_node = ParentNode("div", [child_node])
            self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
        
if __name__ == "__main__":
    unittest.main()