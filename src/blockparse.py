import re

def markdown_to_blocks(markdown):
    second_run = []
    first_run = markdown.split("\n\n")
    for item in first_run:
        if item != "":
            second_run.append(item.strip())
    return second_run


def block_to_blocktype(block):
    heading = ("#","##","###","####","#####","######")
    if block.startswith(heading):
        return "heading"
    if block.startswith("```") and re.findall(r"```(.*?)```", block) != []:
        return "code"
    if block.startswith(">"):
        return "quote"
    if block.startswith("* ") or block.startswith("- "):
        start_char = block[0:1]
        for unordered_list_check in block.split("\n"):
            if not unordered_list_check.startswith(start_char):
                return "paragraph"
        return "unordered_list"
    if block.startswith("1. "):
        x = 1
        for ordered_list_check in block.split("\n"):
            if not ordered_list_check.startswith(f"{x}. "):
                return "paragraph"
            x += 1
        return "ordered_list"
    return("paragraph")

