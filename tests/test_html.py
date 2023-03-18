from unittest import TestCase

from lxml import html

from articles.html import create_paragraphs, tokenize_html


class CreateParagraphsTests(TestCase):
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


class TokenizeHtmlTests(TestCase):
    def test_tokenize_html(self):
        html_text = """
<html>
  <head>
    <title>title text</title>
  </head>
  <body>
    body text
    <h1>a header</h1>
    some more text
  </body>
</html>
"""
        html_document = html.document_fromstring(html_text)

        tokens = tokenize_html(html_document)

        expected_result = [
            "<html>",
            "<head>",
            "<title>",
            "title",
            "text",
            "</title>",
            "</head>",
            "<body>",
            "body",
            "text",
            "<h1>",
            "a",
            "header",
            "</h1>",
            "some",
            "more",
            "text",
            "</body>",
            "</html>",
        ]

        self.assertListEqual(tokens, expected_result)
