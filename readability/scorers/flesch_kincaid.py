from readability.scorers.base_scorer import ReadabilityScorer


class FleschKincaid(ReadabilityScorer):
    def __init__(self, stats, min_words=100):
        super().__init__(stats, min_words)
        self.scorer_name = "Flesh-Kincaid"

    def _raw_score(self):
        stats = self._stats
        return (0.38 * stats.avg_words_per_sentence +
                11.8 * stats.avg_syllables_per_word) - 15.59

    def _grade_level(self):
        return str(round(self._score))
