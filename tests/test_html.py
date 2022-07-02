from unittest import TestCase, main

from article_extraction.html import create_paragraphs, create_text


class FormatHtmlTokensTests(TestCase):
    def test_create_paragraphs(self):
        tokens = [
            "<p>",
            "this",
            "is",
            "a",
            "test",
            "</p>",
            "<a>",
            "link",
            "</a>",
            "text",
            "<h1>",
            "header",
            "</h1>",
        ]

        expected_result = ["this is a test link text", "header"]

        result = create_paragraphs(tokens)

        self.assertListEqual(result, expected_result)

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
