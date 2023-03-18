from typing import List


def _tokenize_html_recursive(element, tokens):
    if element.tag:
        tokens.append("<" + element.tag + ">")

    if element.text:
        for term in element.text.strip().split():
            tokens.append(term)

    for child in element.getchildren():
        tokens = _tokenize_html_recursive(child, tokens)

    if element.tag:
        tokens.append("</" + element.tag + ">")

    if element.tail:
        for term in element.tail.strip().split():
            tokens.append(term)

    return tokens


def create_paragraphs(tokens: List[str]) -> List[str]:
    """Merge the document tokens into paragraphs

    :param tokens: the list with the document tokens
    :return: returns a list with the paragraphs
    """
    paragraphs = []
    cleaned_tokens = []

    for term in tokens:
        if term in [
            "<h1>",
            "<h2>",
            "<h3>",
            "<h4>",
            "<h5>",
            "</h1>",
            "</h2>",
            "</h3>",
            "</h4>",
            "</h5>",
            "<ul>",
            "</ul>",
            "<ol>",
            "</ol>",
            "<li>",
            "</li>",
            "<p>",
            "</p>" "<div>",
            "</div>",
        ]:
            if cleaned_tokens:
                if cleaned_tokens[-1] == " ":
                    cleaned_tokens = cleaned_tokens[:-1]
                paragraphs.append("".join(cleaned_tokens))
                cleaned_tokens = []
        elif not term.startswith("<") and not term.endswith(">"):
            cleaned_tokens.extend([term, " "])

    if cleaned_tokens:
        if cleaned_tokens[-1] == " ":
            cleaned_tokens = cleaned_tokens[:-1]
        paragraphs.append("".join(cleaned_tokens))

    return paragraphs


def tokenize_html(html_document) -> List[str]:
    """Create a list that contains the tags and terms of the document.

    :param html_document: the html document to tokenize
    :returns: return a list with the document tokens
    """
    tokens = _tokenize_html_recursive(html_document, [])

    return tokens
