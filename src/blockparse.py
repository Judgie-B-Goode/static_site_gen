def markdown_to_blocks(markdown):
    second_run = []
    first_run = markdown.split("\n\n")
    for item in first_run:
        if item != "":
            second_run.append(item.strip())
    return second_run


