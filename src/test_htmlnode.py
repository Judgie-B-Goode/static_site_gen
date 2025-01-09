import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode



def test_props1():
    tester = HTMLNode(tag="<a>",value="Some Stuff")
    print(tester.props_to_html()) 

def test_props2():
    tester = HTMLNode(tag="<a>",value="Some Stuff", props= {"href": "https://www.google.com", 
    "target": "_blank"})
    print(tester.props_to_html())

def test_props3():
    tester = HTMLNode(tag="<a>",value="Some Stuff", props= {"href": "https://www.google.com", 
    "target": "_blank", "height" : 500, "width" : 500})
    print(tester.props_to_html())

def test_leaf1():
    leaftest = LeafNode(tag = "a", value = "POOP", props={"butt":"junk"})
    print(leaftest.to_html())

def test_leaf2():
    leaftest = LeafNode(tag = "a", props={"butt":"junk"})
    print(leaftest.to_html())

def test_leaf3():
    leaftest = LeafNode(value = "POOP", props={"butt":"junk"})
    print(leaftest.to_html())