from sys import argv
import codecs
from httplib2 import Http
from lxml.html.clean import clean_html

from article_extraction.mss import MSSArticleExtractor, TermTypeScores

if len(argv) != 3:
    print("You must specify a url and an output file")
    quit()

url = argv[1]
output = argv[2]

http = Http()
resp, contents = http.request(url)

contents = contents.decode("utf-8")

cleaned_contents = clean_html(contents)

scoring = TermTypeScores()
article_extractor = MSSArticleExtractor(scoring)

article = article_extractor.extract_article(cleaned_contents)

with codecs.open(output, "w", encoding="utf-8") as f:
    f.write(article)
