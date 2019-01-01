from readability.exceptions import ReadabilityException


class Result:
    def __init__(self, score, grade_level):
        self.score = score
        self.grade_level = grade_level

    def __str__(self):
        return "score: {}, grade_level: '{}'". \
            format(self.score, self.grade_level)


class ColemanLiau:
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
        scalar = s.num_words / 100
        letters_per_100_words = s.num_letters / scalar
        sentences_per_100_words = s.num_sentences / scalar
        return 0.0588 * letters_per_100_words - \
            0.296 * sentences_per_100_words - 15.8

    def _grade_level(self, score):
        return str(round(score))
