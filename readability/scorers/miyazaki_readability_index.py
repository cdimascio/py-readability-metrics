from readability.exceptions import ReadabilityException


class Result:
    def __init__(self, score, grade_levels, ease):
        self.score = score
        self.ease = ease
        self.grade_levels = grade_levels

    def __str__(self):
        return "score: {}, ease: '{}', grade_levels: {}". \
            format(self.score, self.ease, self.grade_levels)



class MiyazakiReadabilityIndex:
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
        Calculates the Miyazaki English as a Foreign Language Readability Index by Greenfiel 1999
        It is parametrized for Japanes L2 speakers of English, who are students and read academic texts.
        Average score of 50, ranges between 100 and minus infinity

        Formula:    164.935 - 18.792 * word_length - 1.916 * sentence_length

        :param word_length: average word length in characters
        :param sentence_length: average sentence length in words
        :return: ML2RI
        """
        stats = self._stats
        return 164.935 - 18.792 * stats.num_letters - 1.916 * stats.num_words

    def _ease(self, score):
        if score >= 91 and score <= 100:
            return 'very_easy'
        elif score >= 81 and score <= 90:
            return 'easy'
        elif score >= 71 and score <= 80:
            return 'Fairly easy'
        elif score >= 61 and score <= 70:
            return 'standard'
        elif score >= 51 and score <= 60:
            return 'fairly difficult'
        elif score >= 31 and score <= 50:
            return 'difficult'
        elif score < 31:
            return 'very_difficult'

    def _grade_levels(self, score):
        if score >= 91 and score <= 100:
            return ['5']
        elif score >= 81 and score <= 90:
            return ['6']
        elif score >= 71 and score <= 80:
            return ['7']
        elif score >= 61 and score <= 70:
            return ['8', '9']
        elif score >= 51 and score <= 60:
            return ['10', '11', '12']
        elif score >= 31 and score <= 50:
            return ['post-school/college level']
        elif score < 31:
            return ['university graduate']