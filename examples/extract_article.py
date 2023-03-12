from argparse import ArgumentParser

from article_extraction.mss import MSSArticleExtractor

parser = ArgumentParser()
parser.add_argument("output")
parser.add_argument("url")
args = parser.parse_args()

article_extractor = MSSArticleExtractor()

article = article_extractor.extract_article_from_url(args.url)

with open(args.output, "w") as f:
    f.write(article)
