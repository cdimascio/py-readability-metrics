from readability.scorers.base_scorer import ReadabilityScorer




class ColemanLiau(ReadabilityScorer):
    def __init__(self, stats, min_words=100):
        super().__init__(stats, min_words)
        self.scorer_name = 'Coleman-Liau'

    def _raw_score(self):
        s = self._stats
        scalar = s.num_words / 100
        letters_per_100_words = s.num_letters / scalar
        sentences_per_100_words = s.num_sentences / scalar
        return 0.0588 * letters_per_100_words - \
            0.296 * sentences_per_100_words - 15.8

    def _grade_level(self):
        return str(round(self.raw_score))
