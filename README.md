# Article extraction library.

article-extraction is a package that can be used to extract the article content
from an HTML page.

# Installation

Use poetry to install the library from GitHub.

```bash
poetry add "git+https://github.com/pmatigakis/article-extraction.git"
```

# Usage

Extract the content of an article using article-extraction.

```python
from urllib.request import urlopen

from articles.mss.extractors import MSSArticleExtractor

document = urlopen("https://www.bbc.com/sport/formula1/64983451").read()
article_extractor = MSSArticleExtractor()
article = article_extractor.extract_article(document)
print(article)
```
