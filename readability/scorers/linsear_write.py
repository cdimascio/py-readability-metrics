from readability.scorers.base_scorer import ReadabilityScorer


class LinsearWrite(ReadabilityScorer):
    def __init__(self, stats, min_words=100):
        super().__init__(stats, min_words)
        self.scorer_name = "Linsear Write"

    def _raw_score(self):
        s = self._stats
        num_easy_words = s.num_words - s.num_poly_syllable_words
        num_hard_words = s.num_poly_syllable_words
        inter_score = (num_easy_words + (num_hard_words * 3)) / s.num_sentences
        if inter_score > 20:
            return inter_score / 2
        return (inter_score - 2) / 2

    def _grade_level(self):
        return str(round(self.raw_score))
