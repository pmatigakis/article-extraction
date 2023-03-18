from unittest import TestCase

from articles.mss.scores import TermTypeScores


class TermTypeScoresTests(TestCase):
    def test_scoring(self):
        scoring = TermTypeScores(word_score=2, tag_score=-5)

        self.assertEqual(scoring.score("<a>"), -5)
        self.assertEqual(scoring.score("term"), 2)
