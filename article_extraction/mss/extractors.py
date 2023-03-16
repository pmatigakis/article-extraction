from typing import List, Optional, Tuple

from lxml import html
from lxml.html.clean import Cleaner

from article_extraction.extractors import ArticleExtractor
from article_extraction.html import create_paragraphs, tokenize_html
from article_extraction.mss.scores import TermTypeScores


class MSSArticleExtractor(ArticleExtractor):
    """Extract the page article using the Maximum Subsequence algorithm."""

    def __init__(self, scoring: Optional[TermTypeScores] = None):
        self.scoring = scoring or TermTypeScores()

    def _find_maximum_subsequence(
        self, scores: List[float]
    ) -> Tuple[int, int]:
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

    def _extract_maximum_subsequence(
        self, tokens: List[str], scores: List[float]
    ) -> List[str]:
        """Return the term sequence with the highest score."""
        start, length = self._find_maximum_subsequence(scores)

        terms = tokens[start : start + length]  # noqa: E203

        return terms

    def extract_article(self, document: str) -> str:
        cleaner = Cleaner(style=True)
        html_document = cleaner.clean_html(html.document_fromstring(document))
        tokens = tokenize_html(html_document)
        scores = [self.scoring.score(term) for term in tokens]
        terms = self._extract_maximum_subsequence(tokens, scores)
        paragraphs = create_paragraphs(terms)

        return "\n\n".join(paragraphs)
