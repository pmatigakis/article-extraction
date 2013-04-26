def format_html_tokens(tokens):
    cleaned_tokens = []

    for term in tokens:
        if term in ["</p>", "</div>"]:
            cleaned_tokens.append("\n")
            cleaned_tokens.append("\n")
        elif term in ["<h1>", "<h2>", "<h3>", "<h4>", "<h5>",
                      "</h1>", "</h2>", "</h3>", "</h4>", "</h5>",
                      "<ul>", "</ul>", "<ol>", "</ol>",
                      "<li>", "</li>"]:
            cleaned_tokens.append("\n")
        elif not term.startswith("<") and not term.endswith(">"):            
            cleaned_tokens.append(term)

    return cleaned_tokens

def create_text(tokens):
    lines = []

    line = []
    for term in tokens:
        if term == "\n":
            if line:
                lines.append(' '.join(line))
                line = []
            lines.append("\n")
        else:
            if len(' '.join(line)) < 70:
                line.append(term)
            else:
                line.append(term)
                lines.append(' '.join(line))
                lines.append("\n")
                line = []

    if line:
        lines.append(' '.join(line))
        
    return ''.join(lines)
