import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue
        if old_node.text.count(delimiter) < 2:
            raise Exception("Not enough delimiter characters")
        split_nodes = []
        node_chunks = old_node.text.split(delimiter)
        for chunk in range(len(node_chunks)):
            if node_chunks[chunk] == "":
                continue
            if chunk % 2 == 0:
                split_nodes.append(TextNode(node_chunks[chunk],TextType.TEXT))
            else:
                split_nodes.append(TextNode(node_chunks[chunk], text_type))
        new_nodes.extend(split_nodes)    
    return new_nodes
        
def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)