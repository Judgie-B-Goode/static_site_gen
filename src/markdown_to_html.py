from blockparse import markdown_to_blocks, block_to_blocktype
from textnode import *
from htmlnode import ParentNode
from nodeparse import text_to_textnodes

#markdown_to_blocks splits the markdown to individual blocks based on two newlines
#block_to_blocktype identifies the type of each block
#block_to_html_node creates html node based on block type
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = [] #parent node will be a <div>
    for block in blocks:
        html_node = block_to_html_node(block)#generates node
        children.append(html_node)# creates list of child notes
    return ParentNode("div", children, None) # tag,children,props
    

def block_to_html_node(block):
    if block_to_blocktype(block) == "heading":
        return heading_html_node(block)
    if block_to_blocktype(block) == "code":
        return code_html_node(block)
    if block_to_blocktype(block) == "quote":
        return quote_html_node(block)
    if block_to_blocktype(block) == "paragraph":
        return paragraph_html_node(block)
    if block_to_blocktype(block) == "unordered_list":
        return ul_html_node(block)
    if block_to_blocktype(block) == "ordered_list":
        return ol_html_node(block)
    raise ValueError("Invalid block bype")

def heading_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def quote_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def paragraph_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def ul_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def ol_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = TextNode(text,TextType.NORMAL).text_node_to_html_node(text_node)
        children.append(html_node)
    return children