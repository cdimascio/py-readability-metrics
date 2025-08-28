from readability.exceptions import ReadabilityException


class Result:
    def __init__(self, score, grade_levels, ease):
        self.score = score
        self.ease = ease
        self.grade_levels = grade_levels

    def __str__(self):
        return "score: {}, ease: '{}', grade_levels: {}". \
            format(self.score, self.ease, self.grade_levels)



class LixLesbarkeitsIndex:
    def __init__(self, stats, min_words=100):
        self._stats = stats
        if stats.num_words < min_words:
            raise ReadabilityException('{} words required.'.format(min_words))

    def score(self):
        score = self._score()
        return Result(
            score=score,
            ease=self._ease(score),
            grade_levels=self._grade_levels(score)
        )

    def _score(self):
        """
        Calculates the Lix readability index
        :param avg_words_per_sentence: mean sentence length
        :param ratio_long_words: ratio of words with six or more characters
        :return: Lix index
        """
        stats = self._stats
        return stats.avg_words_per_sentence + stats.avg_num_six_letter_words

    def _ease(self, score):
        if score >= 4 and score <= 5:
            return 'very_easy'
        elif score >=6 and score <=7:
            return 'easy'
        elif score >=8 and score <=10:
            return 'average'
        elif score >=11 and score <=12:
            return 'difficult'
        else:
            return 'very_difficult'

    def _grade_levels(self, score):
        if score >= 4 and score <= 5:
            return [4, 5]
        elif score >=6 and score <=7:
            return [6, 7]
        elif score >=8 and score <=10:
            return [8, 9, 10]
        elif score >=11 and score <=12:
            return [11, 12]
        else:
            return ['college level and above']
