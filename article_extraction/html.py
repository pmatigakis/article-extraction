import textwrap


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


def create_text(paragraphs):
    paragraphs = [
        textwrap.fill(paragraph, width=80) for paragraph in paragraphs
    ]

    return "\n\n".join(paragraphs)
