from urllib.request import urlopen

from lxml import html
from lxml.html.clean import Cleaner

from article_extraction.html import create_paragraphs, tokenize_html
from article_extraction.text import create_text


class TermTypeScores(object):
    def __init__(self, word_score=1.0, tag_score=-2.0):
        self.word_score = word_score
        self.tag_score = tag_score

    def score(self, term):
        if term.startswith("<") and term.endswith(">"):
            return self.tag_score
        else:
            return self.word_score


class MSSArticleExtractor(object):
    """Extract the page article using the Maximum Subsequence algorithm."""

    def __init__(self, scoring=None):
        if not scoring:
            self.scoring = TermTypeScores()
        else:
            self.scoring = scoring

    def _find_maximum_subsequence(self, scores):
        """Find the subsequence with the highest score."""
        start = 0
        pos = 0
        sm = 0
        maxSS = [-100000000]

        for i in range(len(scores)):
            sm += scores[i]

            if sm > sum(maxSS):
                maxSS = [scores[o] for o in range(start, i + 1)]
                pos = start
            if sm < 0:
                start = i + 1
                sm = 0

        return pos, len(maxSS)

    def _extract_maximum_subsequence(self, tokens, scores):
        """Return the term sequence with the highest score."""
        start, length = self._find_maximum_subsequence(scores)

        terms = tokens[start : start + length]  # noqa: E203

        return terms

    def extract_article_from_url(self, url):
        """Extract the article from the page at the url."""
        url = url.strip()
        if not url.startswith("http://") and not url.startswith("https://"):
            raise ValueError("only http and https schemes are allowed")

        filehandle = urlopen(url)
        content = filehandle.read()
        content = content.decode("utf-8")

        return self.extract_article(content)

    def extract_article(self, document):
        """Extract the article from the page contents."""
        cleaner = Cleaner(style=True)
        html_document = cleaner.clean_html(html.document_fromstring(document))
        tokens = tokenize_html(html_document)
        scores = [self.scoring.score(term) for term in tokens]
        terms = self._extract_maximum_subsequence(tokens, scores)
        terms = create_paragraphs(terms)
        contents = create_text(terms)

        return contents
