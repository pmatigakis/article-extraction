import re
from lxml import html

from article_extraction.html import format_html_tokens, create_text

def tokenize_html(html_document):
    def tokenize_html_recurcive(element, tokens=[]):
        for child in element.getchildren():
            if child.tag:
                tokens.append("<" + child.tag + ">")

            if child.text:
                for term in child.text.strip().split():
                    tokens.append(term)

            tokens = tokenize_html_recurcive(child, tokens)

            if child.tag:
                tokens.append("</" + child.tag + ">")

            if child.tail:
                for term in child.tail.strip().split():
                    tokens.append(term)

        return tokens

    tokens = []

    if html_document.tag:
        tokens.append("<" + html_document.tag + ">")

    if html_document.text:
        for term in html_document.text.strip().split():
            tokens.append(term)

    tokens = tokenize_html_recurcive(html_document, tokens)

    if html_document.tag:
        tokens.append("</" + html_document.tag + ">")

    return tokens

class TermTypeScores(object):
    def __init__(self, word_score=1, tag_score=-4):
        self.word_score = word_score
        self.tag_score = tag_score

    def score(self, term):
        if term.startswith("<") and term.endswith(">"):
            return self.tag_score
        else:
            return self.word_score

class MSSArticleExtractor(object):
    def __init__(self, scoring):
        self.scoring = scoring

    def _extract_maximum_subsequence(self, tokens, scores):
        start = 0
        sm = 0
        maxSS = [-100000000]
        txt = []

        for i in range(len(tokens)):
            sm += scores[i]

            if sm > sum(maxSS):
                maxSS = [scores[o] for o in range(start, i+1)]
                txt = [tokens[o] for o in range(start, i+1)]
            if sm < 0:
                start = i + 1
                sm = 0

        return txt

    def extract_article(self, document):
        html_document = html.document_fromstring(document)

        tokens = tokenize_html(html_document)

        scores = [self.scoring.score(term) for term in tokens]

        terms = self._extract_maximum_subsequence(tokens, scores)

        terms = format_html_tokens(terms)

        terms = [re.sub(r"\n ", "\n", term, flags=re.UNICODE)
                 for term in terms]

#        contents =  re.sub(r"\n ", "\n", u' '.join(terms), flags=re.UNICODE)
        contents = create_text(terms)

        return contents
