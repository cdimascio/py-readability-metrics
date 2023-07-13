from readability.exceptions import ReadabilityException


class Result:
    def __init__(self, score, ease):
        self.score = score
        self.ease = ease

    def __str__(self):
        return "score: {}, ease: '{}'". \
            format(self.score, self.ease)


class Lix:
    def __init__(self, stats):
        self._stats = stats
        if stats.num_words < 100:
            raise ReadabilityException('100 words required.')

    def score(self):
        score = self._score()
        return Result(
            score=score,
            ease=self._ease(score))

    def _score(self):
        stats = self._stats
        words_per_sent = stats.num_words / stats.num_sentences
        percentage_long_words = stats.num_long_words / stats.num_words * 100
        return words_per_sent + percentage_long_words

    def _ease(self, score):
        if score > 60:
            return 'very_difficult'
        elif score > 50 and score <= 60:
            return 'difficult'
        elif score > 40 and score <= 50:
            return 'medium difficulty'
        elif score > 30 and score <= 40:
            return 'easy reading'
        else:
            return 'very easy'
