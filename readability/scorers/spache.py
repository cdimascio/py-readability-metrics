from readability.exceptions import ReadabilityException


class Result:
    def __init__(self, score, grade_level):
        self.score = score
        self.grade_level = grade_level

    def __str__(self):
        return "score: {}, grade_level: '{}'". \
            format(self.score, self.grade_level)


class Spache:
    def __init__(self, stats):
        self._stats = stats
        if stats.num_words < 100:
            raise ReadabilityException('100 words required.')

    def score(self):
        score = self._score()
        return Result(
            score=score,
            grade_level=self._grade_level(score))

    def _score(self):
        stats = self._stats
        avg_sentence_len = stats.num_words / stats.num_sentences
        percent_difficult_words = \
            stats.num_spache_complex / stats.num_words * 100

        return (0.141 * avg_sentence_len) + (0.086 * percent_difficult_words) + 0.839

    def _grade_level(self, score):
        return str(round(score))
