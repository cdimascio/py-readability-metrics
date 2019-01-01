from readability.exceptions import ReadabilityException


class Result:
    def __init__(self, score, grade_levels, ease):
        self.score = score
        self.ease = ease
        self.grade_levels = grade_levels

    def __str__(self):
        return "score: {}, ease: '{}', grade_levels: {}". \
            format(self.score, self.ease, self.grade_levels)


class Flesch:
    def __init__(self, stats):
        self._stats = stats
        if stats.num_words < 100:
            raise ReadabilityException('100 words required.')

    def score(self):
        score = self._score()
        return Result(
            score=score,
            ease=self._ease(score),
            grade_levels=self._grade_levels(score))

    def _score(self):
        stats = self._stats
        words_per_sent = stats.num_words / stats.num_sentences
        syllables_per_word = stats.num_syllables / stats.num_words
        return 206.835 - (1.015 * words_per_sent) - (84.6 * syllables_per_word)

    def _ease(self, score):
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

    def _grade_levels(self, score):
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
