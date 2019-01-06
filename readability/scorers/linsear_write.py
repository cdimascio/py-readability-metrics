from readability.exceptions import ReadabilityException


class Result:
    def __init__(self, score, grade_level):
        self.score = score
        self.grade_level = grade_level

    def __str__(self):
        return "score: {}, grade_level: '{}'". \
            format(self.score, self.grade_level)


class LinsearWrite:
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
        num_easy_words = s.num_words - s.num_poly_syllable_words
        num_hard_words = s.num_poly_syllable_words
        inter_score = (num_easy_words + (num_hard_words * 3)) / s.num_sentences
        if inter_score > 20:
            return inter_score / 2
        return (inter_score - 2) / 2

    def _grade_level(self, score):
        return str(round(score))
