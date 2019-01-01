from readability.exceptions import ReadabilityException


class Result:
    def __init__(self, score, grade_level):
        self.score = score
        self.grade_level = grade_level

    def __str__(self):
        return "score: {}, grade_level: '{}'". \
            format(self.score, self.grade_level)


class GunningFog:
    def __init__(self, stats):
        self._stats = stats
        if stats.num_words < 100:
            raise ReadabilityException('100 words required.')

    def score(self):
        score = self._score()
        return Result(
            score=score,
            grade_level=self._grade_level(score)
        )

    def _score(self):
        s = self._stats
        word_per_sent = s.num_words / s.num_sentences
        poly_syllables_per_word = s.num_gunning_complex / s.num_words
        return 0.4 * (word_per_sent + 100 * poly_syllables_per_word)

    def _grade_level(self, score):
        rounded = round(score)
        if rounded < 6:
            return 'na'
        elif rounded >= 6 and rounded <= 12:
            return str(rounded)
        elif rounded >= 13 and rounded <= 16:
            return 'college'
        else:
            return 'college_graduate'
