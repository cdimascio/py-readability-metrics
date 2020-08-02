from readability.exceptions import ReadabilityException


class Result:
    def __init__(self, score, grade_levels):
        self.score = score
        self.grade_levels = grade_levels

    def __str__(self):
        return "score: {}, grade_levels: {}". \
            format(self.score, self.grade_levels)


class DaleChall:
    def __init__(self, stats):
        self._stats = stats
        if stats.num_words < 100:
            raise ReadabilityException('100 words required.')

    def score(self):
        score = self._score()
        return Result(
            score=score,
            grade_levels=self._grade_levels(score))

    def _score(self):
        stats = self._stats
        words_per_sent = stats.num_words / stats.num_sentences
        percent_difficult_words = \
            stats.num_dale_chall_complex / stats.num_words * 100
        raw_score = 0.1579 * percent_difficult_words + 0.0496 * words_per_sent
        adjusted_score = raw_score + 3.6365 \
            if percent_difficult_words > 5 \
            else raw_score
        return adjusted_score

    def _grade_levels(self, score):
        if score <= 4.9:
            return ['1', '2', '3', '4']
        elif score >= 5 and score < 6:
            return ['5', '6']
        elif score >= 6 and score < 7:
            return ['7', '8']
        elif score >= 7 and score < 8:
            return ['9', '10']
        elif score >= 8 and score < 9:
            return ['11', '12']
        elif score >= 9 and score < 10:
            return ['college']
        else:
            return ['college_graduate']
