from typing import List


def _tokenize_html_recursive(element, tokens):
    for child in element.getchildren():
        if child.tag:
            tokens.append("<" + child.tag + ">")

        if child.text:
            for term in child.text.strip().split():
                tokens.append(term)

        tokens = _tokenize_html_recursive(child, tokens)

        if child.tag:
            tokens.append("</" + child.tag + ">")

        if child.tail:
            for term in child.tail.strip().split():
                tokens.append(term)

    return tokens


def create_paragraphs(tokens: List[str]) -> List[str]:
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
    """Create a list that contains the tags and terms of the document."""
    tokens = []

    if html_document.tag:
        tokens.append("<" + html_document.tag + ">")

    if html_document.text:
        for term in html_document.text.strip().split():
            tokens.append(term)

    tokens = _tokenize_html_recursive(html_document, tokens)

    if html_document.tag:
        tokens.append("</" + html_document.tag + ">")

    return tokens
