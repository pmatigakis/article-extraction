class TermTypeScores:
    """Container for the term scores"""

    def __init__(self, word_score: float = 1.0, tag_score: float = -2.0):
        """Create a new TermTypeScores object

        :param word_score: the score for words
        :param tag_score: the score for html tags
        """
        self.word_score = word_score
        self.tag_score = tag_score

    def score(self, term: str) -> float:
        """Calculate the score for the given term

        :param term: the term for which we want to calculate the score
        :return: returns the calculated score
        """
        if term.startswith("<") and term.endswith(">"):
            return self.tag_score
        else:
            return self.word_score
