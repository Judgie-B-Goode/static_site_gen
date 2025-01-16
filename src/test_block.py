import unittest

from blockparse import markdown_to_blocks

class TestBlockParse(unittest.TestCase):
    def test_block_parse_1(self):
        test_case = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        result = markdown_to_blocks(test_case)

        self.assertListEqual(
            [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item""",
            
            ],
            result,
        )

    def test_block_parse_2(self):
        test_case = """# This is a heading



This is a paragraph of text. It has some **bold** and *italic* words inside of it.




* This is the first list item in a list block
* This is a list item
* This is another list item"""
        result = markdown_to_blocks(test_case)

        self.assertListEqual(
            [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item""",
            
            ],
            result,
        )


    def test_block_parse_3(self):
        test_case = """# This is a heading






This is a paragraph of text. It has some **bold** and *italic* words inside of it.






* This is the first list item in a list block
* This is a list item
* This is another list item"""
        result = markdown_to_blocks(test_case)

        self.assertListEqual(
            [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item""",
            
            ],
            result,
        )





if __name__ == "__main__":
    unittest.main()