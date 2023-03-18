from os import path
from unittest import TestCase

from articles.mss.extractors import MSSArticleExtractor


class MSSArticleExtractorTests(TestCase):
    def test_extract_article(self):
        with open(
            path.join(
                path.dirname(__file__),
                "..",
                "data",
                "pages",
                "simple-page.html",
            )
        ) as f:
            document = f.read()

        article_extractor = MSSArticleExtractor()
        content = article_extractor.extract_article(document)

        self.assertEqual(
            content,
            """This is a simple page

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum iaculis neque sagittis elit condimentum blandit. Pellentesque eros orci, porta quis tristique sit amet, fringilla id nunc. Nunc efficitur bibendum tincidunt. Donec condimentum nunc eu posuere bibendum. Nullam blandit justo massa, quis faucibus mauris pretium et. Fusce nec odio non ante consequat hendrerit vel at elit. Pellentesque mollis mattis arcu, ut interdum magna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nullam finibus orci at est vestibulum, a interdum mi pulvinar.

Duis venenatis dignissim imperdiet. Pellentesque vel dui sed urna pretium porttitor a id mi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec non nunc mi. Duis et viverra tortor, efficitur rhoncus arcu. Integer a lacus vel turpis sagittis accumsan. Duis ornare pulvinar ultricies. Praesent accumsan faucibus vestibulum.""",  # noqa
        )
