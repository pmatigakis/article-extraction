import textwrap


def create_text(paragraphs):
    paragraphs = [
        textwrap.fill(paragraph, width=80) for paragraph in paragraphs
    ]

    return "\n\n".join(paragraphs)
