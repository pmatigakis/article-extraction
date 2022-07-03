from unittest import TestCase, main

from article_extraction.text import create_text


class CreateTextTests(TestCase):
    def test_create_text(self):
        tokens = [
            "this is a test",
            "link text",
            "header",
        ]

        expected_result = """this is a test

link text

header"""
        result = create_text(tokens)

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()
