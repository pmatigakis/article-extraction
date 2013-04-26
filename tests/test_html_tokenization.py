from unittest import TestCase, main
from lxml import html

from article_extraction.mss import tokenize_html

class HtmlTokenizeTests(TestCase):
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

        expected_result = ["<html>", 
                             "<head>", 
                             "<title>", "title", "text", "</title>",
                             "</head>",
                           "<body>",
                             "body", "text",
                             "<h1>", "a", "header", "</h1>",
                             "some", "more", "text",
                           "</body>",
                           "</html>"]

        self.assertListEqual(tokens, expected_result)

if __name__ == "__main__":
    main()
