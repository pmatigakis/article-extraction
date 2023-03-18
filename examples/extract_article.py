from argparse import ArgumentParser
from urllib.request import urlopen

from articles.mss.extractors import MSSArticleExtractor

parser = ArgumentParser()
parser.add_argument("output")
parser.add_argument("url")
args = parser.parse_args()

document = urlopen(args.url).read()

article_extractor = MSSArticleExtractor()
article = article_extractor.extract_article(document)

with open(args.output, "w") as f:
    f.write(article)
