import math
import warnings

from readability.exceptions import ReadabilityException


class Result:
    def __init__(self, score, grade_level):
        self.score = score
        self.grade_level = grade_level

    def __str__(self):
        return "score: {}, grade_level: {}". \
            format(self.score, self.grade_level)


class Gsmog:
    def __init__(self, stats, ignore_length=False):
        """
        Bamberger adapted McLaughlin's original formula (Harry McLaughlin, 1969 https://ogg.osu.edu/media/documents/health_lit/WRRSMOG_Readability_Formula_G._Harry_McLaughlin__1969_.pdf)
        for German-speaking countries. The formula compares the number of multisyllabic words (three or more, see above) to the number of sentences in the entire text. Since the original formula refers to a
        sample of 30 sentences, the implementation in this class uses 30 sentences as a default if all_sentences is False.
        """
        if stats.num_sentences < 30:
            if not ignore_length:
                raise ReadabilityException(
                    'SMOG requires 30 sentences. {} found'
                    .format(stats.num_sentences))
            else:
                warnings.warn(
                    'SMOG requires 30 sentences. {} found'
                    .format(stats.num_sentences))


        self._stats = stats
            

    def score(self):
        score = self._score()
        grade_level = self._grade_level(score)
        return Result(
            score=score,
            grade_level=grade_level
        )

    def _score(self):

        num_sentences = self._stats.num_sentences
        num_complex_words = self._stats.num_poly_syllable_words # words with 3 or more syllables
        return math.sqrt(30 * num_complex_words / num_sentences) - 2

    def _grade_level(self, score):
        return str(round(score))

