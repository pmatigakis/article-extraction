from lxml import html
from lxml.html.clean import clean_html
from lxml.html import tostring
from difflib import SequenceMatcher
import re
import codecs
from os.path import join

import numpy as np
from scipy.stats import scoreatpercentile

from article_extraction.mss import MSSArticleExtractor

DATASET_PATH = "/home/panagiotis/Documents/datasets/boilerplate/dataset"

def extract_annotated_text(filepath):
    def extract_text_rec(document, text=[]):
        for element in document.getchildren():
            if element.text and element.attrib.get("class", None) in ["x-nc-sel1", "x-nc-sel2", "x-nc-sel3"]:
                text.append(element.text)

            text = extract_text_rec(element, text)

            if element.tail and element.attrib.get("class", None) in ["x-nc-sel1", "x-nc-sel2", "x-nc-sel3"]:
                text.append(element.tail)

        return text

    with codecs.open(filepath, "r") as f:
        content = f.read()

    h = html.document_fromstring(content)

    text = extract_text_rec(h)

    return '\n'.join(text)

def calculate_scores(annotated_filepath, original_filepath):
    text = extract_annotated_text(annotated_filepath)

    expected_terms = re.findall(r"\w+", text.lower(), flags=re.UNICODE)

    article_extractor = MSSArticleExtractor()

    with open(original_filepath, "r") as f:
        contents = f.read()

    contents = html.document_fromstring(contents)

    contents = clean_html(contents)

    with codecs.open("cleaned_text.html", "w", encoding="utf-8") as f:
        f.write(tostring(contents))

    article = article_extractor.extract_article(tostring(contents))

    with codecs.open("text.html", "w", encoding="utf-8") as f:
        f.write(article)

    terms = re.findall(r"\w+", article.lower(), flags=re.UNICODE)    

    matcher = SequenceMatcher(None, expected_terms, terms)

    matches = matcher.get_matching_blocks()

    sretsrel = sum([match.size for match in matches])
    srel = len(expected_terms)

    if terms:
        precision = float(sretsrel) / float(len(terms))
    else:
        precision = 0.0

    if srel > 0:
        recall = float(sretsrel) / float(srel)
    else:
        recall = 0.0

    try:
        f1 = 2 * ((precision * recall) / (precision + recall))
    except:
        f1 = 0.0
    
    return (precision, recall, f1)

def main():
    uuids = []
    with open(join(DATASET_PATH, "url-mapping.txt"), "r") as f:
        for line in f:
            uuid, url = line.split()
            uuids.append(uuid[10:-1])

    precisions = []
    recalls = []
    f1s = []

    for uuid in uuids:
        annotated_filepath = join(DATASET_PATH, "annotated", uuid + ".html")
        original_filepath = join(DATASET_PATH, "original", uuid + ".html")

        precision, recall, f1 = calculate_scores(annotated_filepath, original_filepath)

        precisions.append(precision)
        recalls.append(recall)
        f1s.append(f1)

    precisions = np.array(precisions)
    recalls = np.array(recalls)
    f1s = np.array(f1s)

    print "Precision"
    print "Mean: %f" % np.mean(precisions)
    print "Variance: %f" % np.var(precisions)
    print "Standard deviation: %f" % np.std(precisions)
    print "Median: %f" % scoreatpercentile(precisions, 50)
    print "1st percentile: %f" % scoreatpercentile(precisions, 25)
    print "3rd percentile: %f" % scoreatpercentile(precisions, 75)
    print ""

    print "Recall"
    print "Mean: %f" % np.mean(recalls)
    print "Variance: %f" % np.var(recalls)
    print "Standard deviation: %f" % np.std(recalls)
    print "Median: %f" % scoreatpercentile(recalls, 50)
    print "1st percentile: %f" % scoreatpercentile(recalls, 25)
    print "3rd percentile: %f" % scoreatpercentile(recalls, 75)
    print ""

    print "F1"
    print "Mean: %f" % np.mean(f1s)
    print "Variance: %f" % np.var(f1s)
    print "Standard deviation: %f" % np.std(f1s)
    print "Median: %f" % scoreatpercentile(f1s, 50)
    print "1st percentile: %f" % scoreatpercentile(f1s, 25)
    print "3rd percentile: %f" % scoreatpercentile(f1s, 75)

if __name__ == "__main__":
    main()
