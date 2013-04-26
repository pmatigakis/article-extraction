from unittest import TestCase, main

from article_extraction.mss import TermTypeScores

class TermTypeScoresTests(TestCase):
    def test_scoring(self):
        scoring = TermTypeScores(word_score=2, tag_score=-5)

        self.assertEqual(scoring.score("<a>"), -5)
        self.assertEqual(scoring.score("term"), 2)

if __name__ == "__main__":
    main()
