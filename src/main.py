from textnode import TextNode
from textnode import TextType

def main():
    dum1 = "This is a text node"
    dum2 = TextType.Normal_Text
    text_node = TextNode(dum1, dum2)
    print(text_node.__repr__())



main()
