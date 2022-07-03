import textwrap
from typing import List


def create_text(paragraphs: List[str]) -> str:
    paragraphs = [
        textwrap.fill(paragraph, width=80) for paragraph in paragraphs
    ]

    return "\n\n".join(paragraphs)
