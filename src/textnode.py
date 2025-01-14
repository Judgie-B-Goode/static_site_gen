from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
	TEXT = "text"
	NORMAL = "normal"
	BOLD = "bold"
	ITALIC = "italic"
	CODE = "code"
	LINKS = "links"
	IMAGES = "images"
	

class TextNode():
	def __init__(self, text, text_type, url="None"):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, target):
		if self.__repr__() == target.__repr__():
			return True

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

	def text_node_to_html_node(self, text_node):
		if self.text_type == TextType.NORMAL:
			return LeafNode(None, self.text, props=None)
		if self.text_type == TextType.BOLD:
			return LeafNode("b", self.text, props=None)
		if self.text_type == TextType.ITALIC:
			return LeafNode("i", self.text, props=None)
		if self.text_type == TextType.CODE:
			return LeafNode("code", self.text, props=None)
		if self.text_type == TextType.LINKS:
			return LeafNode("a", self.text, props="href=")
		if self.text_type == TextType.IMAGES:
			return LeafNode("img", "", props={"src":text_node.url,"alt" : text_node.text})
		raise Exception("Invalid Type")