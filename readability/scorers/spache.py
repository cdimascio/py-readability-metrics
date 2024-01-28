from readability.scorers.base_scorer import ReadabilityScorer



class Spache(ReadabilityScorer):
    def __init__(self, stats, min_words=100):
        super().__init__(stats, min_words)
        self.scorer_name = "Spache"

    def _raw_score(self):
        stats = self._stats
        avg_sentence_len = stats.num_words / stats.num_sentences
        percent_difficult_words = \
            stats.num_spache_complex / stats.num_words * 100

        return (0.141 * avg_sentence_len) + (0.086 * percent_difficult_words) + 0.839

    def _grade_level(self):
        return str(round(self.raw_score))
