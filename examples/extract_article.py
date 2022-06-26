import codecs
from sys import argv

from article_extraction.mss import MSSArticleExtractor

if len(argv) != 3:
    print("You must specify a url and an output file")
    quit()

url = argv[1]
output = argv[2]

article_extractor = MSSArticleExtractor()

article = article_extractor.extract_article_from_url(url)

with codecs.open(output, "w", encoding="utf-8") as f:
    f.write(article)
