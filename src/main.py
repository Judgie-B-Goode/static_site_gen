from textnode import TextNode, TextType

def main():
    dum1 = "This is a text node"
    dum2 = TextType.NORMAL
    text_node = TextNode(dum1, dum2)
    print(text_node.__repr__())



main()
