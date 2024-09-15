from readability.scorers.base_scorer import ReadabilityScorer


class GunningFog(ReadabilityScorer):
    def __init__(self, stats, min_words=100):
        super().__init__(stats, min_words)
        self.scorer_name = "Gunning Fog"

    def _raw_score(self):
        s = self._stats
        word_per_sent = s.num_words / s.num_sentences
        poly_syllables_per_word = s.num_gunning_complex / s.num_words
        return 0.4 * (word_per_sent + 100 * poly_syllables_per_word)

    def _grade_level(self):
        rounded = round(self._score)
        if rounded < 6:
            return 'na'
        elif 6 <= rounded <= 12:
            return str(rounded)
        elif 13 <= rounded <= 16:
            return 'college'
        else:
            return 'college_graduate'
