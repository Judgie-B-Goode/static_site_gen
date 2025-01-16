import unittest

from blockparse import markdown_to_blocks, block_to_blocktype

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


    def test_paragraph(self):
        self.assertEqual(
            "paragraph",
            block_to_blocktype("this is some text")
        )

        self.assertEqual(
            "paragraph",
            block_to_blocktype("""* I have a cat and a (dog)
* I have a cat and a (dog)
                               I have a fish""")
        )

        self.assertEqual(
            "paragraph",
            block_to_blocktype("""1. I have a cat and a (dog)
2. I have a cat and a (dog)
I have a fish""")
        )

    def test_heading(self):
        self.assertEqual(
            "heading",
            block_to_blocktype("# this is a heading")
        )
        self.assertEqual(
            "heading",
            block_to_blocktype("## this is also a heading")
        )

    def test_code(self):
        self.assertEqual(
            "code",
            block_to_blocktype("```this is code```")
        )

    def test_quote(self):
        self.assertEqual(
            "quote",
            block_to_blocktype(">this is a quote")
        )

    def test_olist(self):
        self.assertEqual(
            "ordered_list",
            block_to_blocktype("""1. I have a cat and a (dog)
2. I have a cat and a (dog)
3. I have a fish""")
        )

    def test_ulist(self):
        self.assertEqual(
            "unordered_list",
            block_to_blocktype("""* I have a cat and a (dog)
* I have a cat and a (dog)
* I have a fish""")
        )


if __name__ == "__main__":
    unittest.main()