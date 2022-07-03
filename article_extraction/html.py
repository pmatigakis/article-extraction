def create_paragraphs(tokens):
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


def tokenize_html(html_document):
    """Create a list that contains the tags and terms of the document."""

    def tokenize_html_recurcive(element, tokens=None):
        tokens = tokens or []

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
