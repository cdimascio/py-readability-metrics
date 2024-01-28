from readability.scorers.base_scorer import ReadabilityScorer


class Flesch(ReadabilityScorer):
    def __init__(self, stats, min_words=100):
        super().__init__(stats, min_words)
        self.scorer_name = "Flesch"

    def _raw_score(self):
        stats = self._stats
        words_per_sent = stats.num_words / stats.num_sentences
        syllables_per_word = stats.num_syllables / stats.num_words
        return 206.835 - (1.015 * words_per_sent) - (84.6 * syllables_per_word)

    def _description(self):
        score = self.raw_score
        if score >= 90 and score <= 100:
            return 'very_easy'
        elif score >= 80 and score < 90:
            return 'easy'
        elif score >= 70 and score < 80:
            return 'fairly_easy'
        elif score >= 60 and score < 70:
            return 'standard'
        elif score >= 50 and score < 60:
            return 'fairly_difficult'
        elif score >= 30 and score < 50:
            return 'difficult'
        else:
            return 'very_confusing'

    def _grade_level(self):
        score = self.raw_score
        if score >= 90 and score <= 100:
            return ['5']
        elif score >= 80 and score < 90:
            return ['6']
        elif score >= 70 and score < 80:
            return ['7']
        elif score >= 60 and score < 70:
            return ['8', '9']
        elif score >= 50 and score < 60:
            return ['10', '11', '12']
        elif score >= 30 and score < 50:
            return ['college']
        else:
            return ['college_graduate']
