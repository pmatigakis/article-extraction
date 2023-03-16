class TermTypeScores:
    def __init__(self, word_score=1.0, tag_score=-2.0):
        self.word_score = word_score
        self.tag_score = tag_score

    def score(self, term: str) -> float:
        if term.startswith("<") and term.endswith(">"):
            return self.tag_score
        else:
            return self.word_score
