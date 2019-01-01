import math
from readability.exceptions import ReadabilityException


class Result:
    def __init__(self, score, grade_levels, ages):
        self.score = score
        self.grade_levels = grade_levels
        self.ages = ages

    def __str__(self):
        return "score: {}, grade_levels: {}, ages: {}". \
            format(self.score, self.grade_levels, self.ages)


class ARI:
    def __init__(self, stats):
        self._stats = stats
        if stats.num_words < 100:
            raise ReadabilityException('100 words required.')

    def score(self):
        score = self._score()
        return Result(
            score=score,
            grade_levels=self._grade_levels(score),
            ages=self._ages(score))

    def _score(self):
        s = self._stats
        letters_per_word = s.num_letters / s.num_words
        words_per_sent = s.num_words / s.num_sentences
        return 4.71 * letters_per_word + 0.5 * words_per_sent - 21.43

    def _grade_levels(self, score):
        score = math.ceil(score)
        if score <= 1:
            return ['K']
        elif score <= 2:
            return ['1', '2']
        elif score <= 3:
            return ['3']
        elif score <= 4:
            return ['4']
        elif score <= 5:
            return ['5']
        elif score <= 6:
            return ['6']
        elif score <= 7:
            return ['7']
        elif score <= 8:
            return ['8']
        elif score <= 9:
            return ['9']
        elif score <= 10:
            return ['10']
        elif score <= 11:
            return ['11']
        elif score <= 12:
            return ['12']
        elif score <= 13:
            return ['college']
        else:
            return ['college_graduate']

    def _ages(self, score):
        score = math.ceil(score)
        if score <= 1:
            return [5, 6]
        elif score <= 2:
            return [6, 7]
        elif score <= 3:
            return [7, 9]
        elif score <= 4:
            return [9, 10]
        elif score <= 5:
            return [10, 11]
        elif score <= 6:
            return [11, 12]
        elif score <= 7:
            return [12, 13]
        elif score <= 8:
            return [13, 14]
        elif score <= 9:
            return [14, 15]
        elif score <= 10:
            return [15, 16]
        elif score <= 11:
            return [16, 17]
        elif score <= 12:
            return [17, 18]
        elif score <= 13:
            return [18, 24]
        else:
            return [24, 100]
