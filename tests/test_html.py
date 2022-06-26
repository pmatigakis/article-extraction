from unittest import TestCase, main

from article_extraction.html import create_text, format_html_tokens


class FormatHtmlTokensTests(TestCase):
    def test_format_html_tokens(self):
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

        expected_result = [
            "this",
            "is",
            "a",
            "test",
            "\n",
            "\n",
            "link",
            "text",
            "\n",
            "header",
            "\n",
        ]

        result = format_html_tokens(tokens)

        self.assertListEqual(result, expected_result)

    def test_create_text(self):
        tokens = [
            "this",
            "is",
            "a",
            "test",
            "\n",
            "\n",
            "link",
            "text",
            "\n",
            "header",
            "\n",
            "\n",
        ]

        expected_result = """this is a test

link text
header

"""
        result = create_text(tokens)

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()
